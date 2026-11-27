"""
Support for ELO keywording aspects (ELO 23 and newer).

Keywording forms (masks) with ``dataOrganisation = DATA_ORGANISATION_ASPECT`` don't store their index values as
ObjKeys but in aspect objects:

* An :class:`Aspect` defines a set of lines (technical key + type), e.g. an aspect "Address" with the lines
  "STREET", "CITY", "ZIP".
* A mask references aspects via aspect associations (``AspectAssoc``). An association has a name (e.g. "INVOICE_ADDRESS")
  and a cardinality (OPTIONAL, MANDATORY, OPTIONAL_MANY, MANDATORY_MANY). The same aspect can be associated multiple
  times under different names.
* A Sord stores the data in ``Sord.aspects``: association name -> list of aspect objects, where an aspect object is a
  map of line key -> value.

This module talks to the Indexserver with plain JSON instead of the generated models, as the generated models can't
deserialize the enums (e.g. ``Cardinality``) used by aspects.
"""
import logging
import re
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Optional, Union

import cachetools

from eloclient import Client
from eloservice.eloconstants import ElobitsetEditz
from eloservice.login_util import EloConnection

# AspectC.mbAll / AspectC.mbAllMembers
ASPECT_Z_MB_ALL = {"bset": "2251799813685247"}
# EditInfoC.mbAspectInfos
EDIT_INFO_MB_ASPECT_INFOS = "16384"
# EditInfoC.mbAll + SordC.mbAll, same as eloconstants (contain EditInfoC.mbAspectInfos and SordC.mbAspectObjects)
EDIT_INFO_Z_MB_ALL = {"bset": ElobitsetEditz.MB_ALL.value, "sordZ": {"bset": ElobitsetEditz.MB_ALL.value}}
# SordC.mbAspectObjects (same bit as SordC.mbObjKeys)
SORD_Z_MB_ASPECT_OBJECTS = {"bset": str(1 << 53)}
LOCK_Z_NO = {"bset": "0"}

# DocMaskC.DATA_ORGANISATION_*
DATA_ORGANISATION_OBJKEYS = 0
DATA_ORGANISATION_TABLE = 1
DATA_ORGANISATION_ASPECT = 2

# AspectLineC.TYPE_*
ASPECT_LINE_TYPE_TEXT = 3100
ASPECT_LINE_TYPE_USER = 3106
ASPECT_LINE_TYPE_INTEGER = 3113
ASPECT_LINE_TYPE_DOUBLE = 3116
ASPECT_LINE_TYPE_RELATION = 3118
ASPECT_LINE_TYPE_ISO_DATE_ONLY = 3130
ASPECT_LINE_TYPE_ISO_DATE_TIME = 3131
ASPECT_LINE_TYPE_STATUS = 3132
ASPECT_LINE_TYPE_TIME = 3133
ASPECT_LINE_TYPE_FIXED_POINT_NUMBER = 3134

# IndexValueC.TYPE_*
INDEX_VALUE_TYPE_INT = 1
INDEX_VALUE_TYPE_DOUBLE = 2
INDEX_VALUE_TYPE_STRING = 3
INDEX_VALUE_TYPE_ISO_DATE_ONLY = 4
INDEX_VALUE_TYPE_ISO_DATE_TIME = 5
INDEX_VALUE_TYPE_STATUS = 6
INDEX_VALUE_TYPE_RELATION = 7
INDEX_VALUE_TYPE_USER = 8
INDEX_VALUE_TYPE_TIME = 9
INDEX_VALUE_TYPE_FIXED_POINT_NUMBER = 10

ASPECT_LINE_TYPE_TO_INDEX_VALUE_TYPE = {
    ASPECT_LINE_TYPE_TEXT: INDEX_VALUE_TYPE_STRING,
    ASPECT_LINE_TYPE_USER: INDEX_VALUE_TYPE_USER,
    ASPECT_LINE_TYPE_INTEGER: INDEX_VALUE_TYPE_INT,
    ASPECT_LINE_TYPE_DOUBLE: INDEX_VALUE_TYPE_DOUBLE,
    ASPECT_LINE_TYPE_RELATION: INDEX_VALUE_TYPE_RELATION,
    ASPECT_LINE_TYPE_ISO_DATE_ONLY: INDEX_VALUE_TYPE_ISO_DATE_ONLY,
    ASPECT_LINE_TYPE_ISO_DATE_TIME: INDEX_VALUE_TYPE_ISO_DATE_TIME,
    ASPECT_LINE_TYPE_STATUS: INDEX_VALUE_TYPE_STATUS,
    ASPECT_LINE_TYPE_TIME: INDEX_VALUE_TYPE_TIME,
    ASPECT_LINE_TYPE_FIXED_POINT_NUMBER: INDEX_VALUE_TYPE_FIXED_POINT_NUMBER,
}

# Cardinality enum, in the order of its ordinal values
CARDINALITIES = ["OPTIONAL", "MANDATORY", "MANDATORY_MANY", "OPTIONAL_MANY"]
# IndexSearchOperator enum, in the order of its ordinal values
INDEX_SEARCH_OPERATORS = ["GREATER_THAN", "GREATER", "LOWER_THAN", "LOWER", "EQUALS", "LIKE", "ISNULL", "ISEMPTY"]

# formats of IndexValue.stringValue (verified on ELO 25): yyyyMMdd and yyyyMMddHHmmssSSS
ISO_DATE_ONLY_FORMAT = "%Y%m%d"


def format_iso_date_time(value: datetime) -> str:
    """Formats a datetime as ELO aspect ISO date time: yyyyMMddHHmmssSSS"""
    return value.strftime("%Y%m%d%H%M%S") + f"{value.microsecond // 1000:03d}"

ASPECT_SEARCH_KEY_SEPARATOR = "¶"


@dataclass
class AspectInfo:
    """Short info of an aspect, as returned by :func:`AspectUtil.get_aspects`"""
    id: int
    name: str
    guid: str = ""
    display_name: str = ""
    package_name: str = ""


@dataclass
class AspectLine:
    """A line (field) of an aspect"""
    key: str
    type: int
    display_name: str = ""

    @property
    def type_name(self) -> str:
        return _ASPECT_LINE_TYPE_NAMES.get(self.type, str(self.type))


@dataclass
class Aspect:
    """An aspect with its lines, as returned by :func:`AspectUtil.get_aspect`"""
    id: int
    name: str
    guid: str = ""
    display_name: str = ""
    package_name: str = ""
    lines: dict[str, AspectLine] = field(default_factory=dict)


@dataclass
class AspectAssoc:
    """The association of an aspect to a mask"""
    name: str
    aspect_id: int
    cardinality: str = ""
    display_name: str = ""

    @property
    def is_many(self) -> bool:
        return self.cardinality.endswith("_MANY")


_ASPECT_LINE_TYPE_NAMES = {
    ASPECT_LINE_TYPE_TEXT: "TYPE_TEXT",
    ASPECT_LINE_TYPE_USER: "TYPE_USER",
    ASPECT_LINE_TYPE_INTEGER: "TYPE_INTEGER",
    ASPECT_LINE_TYPE_DOUBLE: "TYPE_DOUBLE",
    ASPECT_LINE_TYPE_RELATION: "TYPE_RELATION",
    ASPECT_LINE_TYPE_ISO_DATE_ONLY: "TYPE_ISO_DATE_ONLY",
    ASPECT_LINE_TYPE_ISO_DATE_TIME: "TYPE_ISO_DATE_TIME",
    ASPECT_LINE_TYPE_STATUS: "TYPE_STATUS",
    ASPECT_LINE_TYPE_TIME: "TYPE_TIME",
    ASPECT_LINE_TYPE_FIXED_POINT_NUMBER: "TYPE_FIXED_POINT_NUMBER",
}


def _cardinality_name(value) -> str:
    if isinstance(value, int) and 0 <= value < len(CARDINALITIES):
        return CARDINALITIES[value]
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and value.get("name"):
        return value["name"]
    return ""


def _parse_iso(value: str, date_only: bool) -> Union[date, datetime, str]:
    if not value:
        return value
    if len(value) == 17 and value.isdigit():  # yyyyMMddHHmmssSSS
        parsed = datetime.strptime(value[:14], "%Y%m%d%H%M%S").replace(microsecond=int(value[14:]) * 1000)
        return parsed.date() if date_only else parsed
    formats = ["%Y%m%d", "%Y-%m-%d"] if date_only else []
    formats += ["%Y%m%d%H%M%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y%m%d%H%M", "%Y-%m-%dT%H:%M:%S.%f"]
    if not date_only:
        formats += ["%Y%m%d", "%Y-%m-%d"]
    for fmt in formats:
        try:
            parsed = datetime.strptime(value, fmt)
            return parsed.date() if date_only else parsed
        except ValueError:
            pass
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.date() if date_only else parsed
    except ValueError:
        logging.warning(f"Could not parse aspect date value '{value}', returning it as string")
        return value


def index_value_to_python(index_value: dict) -> Any:
    """
    Converts an IndexValue (JSON) of an aspect object to a python value:

    * INT -> int, DOUBLE -> float, FIXED_POINT_NUMBER -> Decimal
    * ISO_DATE_ONLY -> datetime.date, ISO_DATE_TIME -> datetime.datetime
    * STRING, STATUS, RELATION (Sord GUID), USER (user GUID), TIME -> str
    """
    if index_value is None:
        return None
    value_type = index_value.get("type")
    string_value = index_value.get("stringValue")
    if value_type == INDEX_VALUE_TYPE_INT:
        return index_value.get("intValue")
    if value_type == INDEX_VALUE_TYPE_DOUBLE:
        return index_value.get("doubleValue")
    if value_type == INDEX_VALUE_TYPE_FIXED_POINT_NUMBER:
        return Decimal(string_value) if string_value not in (None, "") else None
    if value_type == INDEX_VALUE_TYPE_ISO_DATE_ONLY:
        return _parse_iso(string_value, date_only=True)
    if value_type == INDEX_VALUE_TYPE_ISO_DATE_TIME:
        return _parse_iso(string_value, date_only=False)
    if string_value is not None:
        return string_value
    # unknown type: return whatever is set
    for key in ("intValue", "doubleValue"):
        if index_value.get(key) is not None:
            return index_value.get(key)
    return None


def python_to_index_value(value: Any, line_type: int) -> dict:
    """
    Converts a python value to an IndexValue (JSON) for an aspect line of the given type (AspectLineC.TYPE_*).
    Strings are passed through as they are (they must be in the format the Indexserver expects).
    """
    value_type = ASPECT_LINE_TYPE_TO_INDEX_VALUE_TYPE.get(line_type, INDEX_VALUE_TYPE_STRING)
    if value_type == INDEX_VALUE_TYPE_INT:
        return {"type": value_type, "intValue": int(value)}
    if value_type == INDEX_VALUE_TYPE_DOUBLE:
        return {"type": value_type, "doubleValue": float(value)}
    if value_type == INDEX_VALUE_TYPE_FIXED_POINT_NUMBER:
        return {"type": value_type, "stringValue": str(value)}
    if value_type == INDEX_VALUE_TYPE_ISO_DATE_ONLY:
        if isinstance(value, (date, datetime)):
            value = value.strftime(ISO_DATE_ONLY_FORMAT)
        return {"type": value_type, "stringValue": str(value)}
    if value_type == INDEX_VALUE_TYPE_ISO_DATE_TIME:
        if isinstance(value, datetime):
            value = format_iso_date_time(value)
        elif isinstance(value, date):
            value = format_iso_date_time(datetime(value.year, value.month, value.day))
        return {"type": value_type, "stringValue": str(value)}
    return {"type": value_type, "stringValue": str(value)}


def _search_condition(value: Any, operator: str = "EQUALS") -> dict:
    """Builds an IndexSearchValue (JSON) for a single python value"""
    if operator not in INDEX_SEARCH_OPERATORS:
        raise ValueError(f"Unknown operator '{operator}', must be one of {INDEX_SEARCH_OPERATORS}")
    if isinstance(value, bool):
        value = str(value)
    if isinstance(value, int):
        return {"intValue": {"operator": operator, "operand": value}}
    if isinstance(value, float):
        return {"doubleValue": {"operator": operator, "operand": value}}
    if isinstance(value, datetime):
        value = format_iso_date_time(value)
    elif isinstance(value, date):
        value = value.strftime(ISO_DATE_ONLY_FORMAT)
    return {"stringValue": {"operator": operator, "operand": "" if value is None else str(value)}}


def build_aspect_search(search_aspect_fields: dict) -> dict:
    """
    Builds the value for FindByIndex.aspects (JSON).

    :param search_aspect_fields: key -> search value. The key has the form
        ``"<association name>¶<aspect name, id or guid>¶<line key>"``, an empty part is a wildcard
        (e.g. ``"¶ADDRESS¶CITY"`` searches the line CITY of the aspect ADDRESS in all associations).
        Note: when combining several conditions, specify the association name, otherwise the Indexserver
        (ELO 25) finds nothing. Values:

        * a single value (str, int, float, Decimal, date, datetime): equals
        * a tuple ``(operator, value)``, operator is one of GREATER_THAN (>), GREATER (>=), LOWER_THAN (<),
          LOWER (<=), EQUALS, LIKE, ISNULL, ISEMPTY; e.g. ``("GREATER", 100)``
        * a list of the above: matches if any of them matches (or)
        * a dict: used as it is as FindByAspectValue
    """
    result = {}
    for key, value in search_aspect_fields.items():
        if key.count(ASPECT_SEARCH_KEY_SEPARATOR) != 2:
            raise ValueError(f"Invalid aspect search key '{key}', expected '<assoc>¶<aspect>¶<line>' "
                             f"(exactly two '{ASPECT_SEARCH_KEY_SEPARATOR}')")
        if isinstance(value, dict):
            result[key] = value
            continue
        values = value if isinstance(value, list) else [value]
        conditions = []
        for single in values:
            if isinstance(single, tuple) and len(single) == 2 and isinstance(single[0], str):
                conditions.append(_search_condition(single[1], single[0]))
            else:
                conditions.append(_search_condition(single))
        if len(conditions) == 1:
            result[key] = {"condition": conditions[0]}
        else:
            result[key] = {"disjunctConditions": conditions}
    return result


class AspectUtil:
    elo_connection: EloConnection
    elo_client: Client
    cache_aspect: Optional[cachetools.TTLCache] = None
    cache_mask_aspect_assocs: Optional[cachetools.TTLCache] = None

    def __init__(self, elo_client: Client, elo_connection: EloConnection,
                 cache_enable: bool = True, cache_ttl: int = 600, cache_maxsize: int = 128):
        self.elo_client = elo_client
        self.elo_connection = elo_connection
        if cache_enable:
            self.cache_aspect = cachetools.TTLCache(maxsize=cache_maxsize, ttl=cache_ttl)
            self.cache_mask_aspect_assocs = cachetools.TTLCache(maxsize=cache_maxsize, ttl=cache_ttl)

    def _call(self, method: str, body: dict):
        response = self.elo_client.get_httpx_client().post(f"/IXServicePortIF/{method}", json=body)
        if not 200 <= response.status_code < 300:
            raise ValueError(f"Error from ELO IX server: {response.status_code} - {response.text}")
        try:
            data = response.json()
        except ValueError:
            raise ValueError(f"Error from ELO IX server: unexpected response {response.text}")
        if data.get("exception"):
            # don't put the session ticket into error messages / logs
            exception = re.sub(r"\[TICKET:[^\]]*\]", "", str(data.get("exception")))
            raise ValueError(f"Error from ELO IX server ({method}): {exception}")
        return data.get("result")

    def get_aspects(self) -> list[AspectInfo]:
        """
        Returns all aspects of the repository
        """
        # createSord returns the requested EditInfo without saving anything (same workaround as for the mask names)
        result = self._call("createSord", {
            "parentId": "1", "maskId": "0", "editInfoZ": {"bset": EDIT_INFO_MB_ASPECT_INFOS, "sordZ": {"bset": "0"}}
        }) or {}
        return [AspectInfo(id=a.get("id"), name=a.get("name", ""), guid=a.get("guid", ""),
                           display_name=a.get("displayName", ""), package_name=a.get("packageName", ""))
                for a in (result.get("aspectInfos") or [])]

    def get_aspect(self, aspect_identifier: Union[str, int]) -> Aspect:
        """
        Returns an aspect with its lines
        :param aspect_identifier: id, guid or name of the aspect
        """
        cache_key = str(aspect_identifier)
        if self.cache_aspect is not None and cache_key in self.cache_aspect:
            return self.cache_aspect[cache_key]
        result = self._call("checkoutAspect", {"aspectId": cache_key, "aspectZ": ASPECT_Z_MB_ALL,
                                               "lockZ": LOCK_Z_NO})
        if not result:
            raise ValueError(f"Aspect '{aspect_identifier}' not found")
        lines = {}
        for key, line in (result.get("lines") or {}).items():
            line_key = line.get("key") or key
            lines[line_key] = AspectLine(key=line_key, type=line.get("type"), display_name=line.get("displayName", ""))
        aspect = Aspect(id=result.get("id"), name=result.get("name", ""), guid=result.get("guid", ""),
                        display_name=result.get("displayName", ""), package_name=result.get("packageName", ""),
                        lines=lines)
        if self.cache_aspect is not None:
            self.cache_aspect[cache_key] = aspect
        return aspect

    def get_mask_aspect_assocs(self, mask_identifier: Union[str, int]) -> dict[str, AspectAssoc]:
        """
        Returns the aspect associations of a mask (association name -> AspectAssoc). Empty if the mask is not
        based on aspects.
        :param mask_identifier: id, guid or name of the mask
        """
        cache_key = str(mask_identifier)
        if self.cache_mask_aspect_assocs is not None and cache_key in self.cache_mask_aspect_assocs:
            return self.cache_mask_aspect_assocs[cache_key]
        result = self._call("createSord", {"parentId": "1", "maskId": cache_key, "editInfoZ": EDIT_INFO_Z_MB_ALL})
        mask = (result or {}).get("mask") or {}
        assocs = self._parse_assocs(mask.get("aspectAssocs"))
        if self.cache_mask_aspect_assocs is not None:
            self.cache_mask_aspect_assocs[cache_key] = assocs
        return assocs

    @staticmethod
    def _parse_assocs(raw_assocs) -> dict[str, AspectAssoc]:
        assocs = {}
        for key, assoc in (raw_assocs or {}).items():
            name = assoc.get("name") or key
            assocs[name] = AspectAssoc(name=name, aspect_id=assoc.get("aspectId"),
                                       cardinality=_cardinality_name(assoc.get("cardinality")),
                                       display_name=assoc.get("displayName", ""))
        return assocs

    def _checkout_sord(self, sord_id: str) -> dict:
        result = self._call("checkoutSord", {"objId": str(sord_id), "editInfoZ": EDIT_INFO_Z_MB_ALL,
                                             "lockZ": LOCK_Z_NO})
        sord = (result or {}).get("sord")
        if not sord:
            raise ValueError(f"Sord with ID {sord_id} not found")
        return sord

    def get_aspect_fields(self, sord_id: str) -> dict[str, list[dict[str, Any]]]:
        """
        Returns the aspect data of a sord: association name -> list of aspect objects (line key -> value).
        The values are converted according to their type, see :func:`index_value_to_python`.
        """
        sord = self._checkout_sord(sord_id)
        return {
            assoc_name: [{line_key: index_value_to_python(index_value) for line_key, index_value in obj.items()}
                         for obj in (objects or [])]
            for assoc_name, objects in (sord.get("aspects") or {}).items()
        }

    def write_aspect_fields(self, sord_id: str, aspect_fields: dict[str, Union[dict, list[dict]]]):
        """
        Writes aspect data of a sord. For every given association, all its aspect objects are replaced by the given
        ones; associations which are not given stay as they are. An empty list removes all objects of an association.

        :param sord_id: The sordID of the sord in ELO
        :param aspect_fields: association name -> list of aspect objects (line key -> value). A single dict is
            treated as a list with one aspect object. Lines with value None are not written.
        """
        sord = self._checkout_sord(sord_id)
        assocs = self.get_mask_aspect_assocs(sord.get("mask"))
        if not assocs:
            raise ValueError(f"The mask '{sord.get('maskName')}' of sord {sord_id} has no aspect associations")
        aspects = dict(sord.get("aspects") or {})
        for assoc_name, objects in aspect_fields.items():
            assoc = assocs.get(assoc_name)
            if assoc is None:
                raise ValueError(f"Mask '{sord.get('maskName')}' has no aspect association '{assoc_name}', "
                                 f"available: {list(assocs)}")
            if isinstance(objects, dict):
                objects = [objects]
            if len(objects) > 1 and assoc.cardinality and not assoc.is_many:
                raise ValueError(f"Aspect association '{assoc_name}' has cardinality {assoc.cardinality} and only "
                                 f"allows one aspect object, got {len(objects)}")
            aspect = self.get_aspect(assoc.aspect_id)
            aspects[assoc_name] = [self._to_index_values(aspect, obj) for obj in objects]
        sord["aspects"] = aspects
        self._call("checkinSord", {"sord": sord, "sordZ": SORD_Z_MB_ASPECT_OBJECTS, "unlockZ": LOCK_Z_NO})

    @staticmethod
    def _to_index_values(aspect: Aspect, obj: dict) -> dict:
        result = {}
        for line_key, value in obj.items():
            line = aspect.lines.get(line_key)
            if line is None:
                raise ValueError(f"Aspect '{aspect.name}' has no line '{line_key}', available: {list(aspect.lines)}")
            if value is None:
                continue
            result[line_key] = python_to_index_value(value, line.type)
        return result
