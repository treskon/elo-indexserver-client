from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_list_of_map_to_index_value import MapToListOfMapToIndexValue
    from ..models.sord_hist_key import SordHistKey


T = TypeVar("T", bound="SordHist")


@_attrs_define
class SordHist:
    """Version history for the keywording from an object.
    A version history is created for a sord object
     when the keywording is changed for the first time (a newly created sord has no version history).
     Once created only one SordHist object exist for the sord object and is assigned to the sord
     object via the Sord.guid = SordHist.objGuid relationship. The keywording properties that were
     altered in the change process are saved in an array of SordHistKey objects.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            hist_guid (Union[Unset, str]): GUID of the SordHist object.
            time_stamp_utc (Union[Unset, str]): Timestamp of the change in the timezone of the client, in UTC form.
                The format is
                 JJJJ.MM.DD.hh.mm.ss
            work_station (Union[Unset, str]): The name of the computer from which the change was carried out.
                This is the parameter
                 clientComputer which is provided by the ix.login function.
            time_stamp_local (Union[Unset, str]): Timestamp of the change in the timezone of the client. The format is
                JJJJ.MM.DD.hh.mm.
                ss
            obj_guid (Union[Unset, str]): GUID of the sord object.
            user_no (Union[Unset, int]): The user who carried out the changes.
            hist_keys (Union[Unset, List['SordHistKey']]):
            aspect_objects (Union[Unset, MapToListOfMapToIndexValue]):
            hist_source (Union[Unset, int]): Identifies the application with which changes were made to the keywording.
            user_name (Union[Unset, str]): The name of the user who carried out the changes.
    """

    hist_guid: Union[Unset, str] = UNSET
    time_stamp_utc: Union[Unset, str] = UNSET
    work_station: Union[Unset, str] = UNSET
    time_stamp_local: Union[Unset, str] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    user_no: Union[Unset, int] = UNSET
    hist_keys: Union[Unset, List["SordHistKey"]] = UNSET
    aspect_objects: Union[Unset, "MapToListOfMapToIndexValue"] = UNSET
    hist_source: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hist_guid = self.hist_guid

        time_stamp_utc = self.time_stamp_utc

        work_station = self.work_station

        time_stamp_local = self.time_stamp_local

        obj_guid = self.obj_guid

        user_no = self.user_no

        hist_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hist_keys, Unset):
            hist_keys = []
            for hist_keys_item_data in self.hist_keys:
                hist_keys_item = hist_keys_item_data.to_dict()
                hist_keys.append(hist_keys_item)

        aspect_objects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_objects, Unset):
            aspect_objects = self.aspect_objects.to_dict()

        hist_source = self.hist_source

        user_name = self.user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hist_guid is not UNSET:
            field_dict["histGuid"] = hist_guid
        if time_stamp_utc is not UNSET:
            field_dict["timeStampUTC"] = time_stamp_utc
        if work_station is not UNSET:
            field_dict["workStation"] = work_station
        if time_stamp_local is not UNSET:
            field_dict["timeStampLocal"] = time_stamp_local
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if user_no is not UNSET:
            field_dict["userNo"] = user_no
        if hist_keys is not UNSET:
            field_dict["histKeys"] = hist_keys
        if aspect_objects is not UNSET:
            field_dict["aspectObjects"] = aspect_objects
        if hist_source is not UNSET:
            field_dict["histSource"] = hist_source
        if user_name is not UNSET:
            field_dict["userName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_list_of_map_to_index_value import MapToListOfMapToIndexValue
        from ..models.sord_hist_key import SordHistKey

        d = src_dict.copy()
        hist_guid = d.pop("histGuid", UNSET)

        time_stamp_utc = d.pop("timeStampUTC", UNSET)

        work_station = d.pop("workStation", UNSET)

        time_stamp_local = d.pop("timeStampLocal", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        user_no = d.pop("userNo", UNSET)

        hist_keys = []
        _hist_keys = d.pop("histKeys", UNSET)
        for hist_keys_item_data in _hist_keys or []:
            hist_keys_item = SordHistKey.from_dict(hist_keys_item_data)

            hist_keys.append(hist_keys_item)

        _aspect_objects = d.pop("aspectObjects", UNSET)
        aspect_objects: Union[Unset, MapToListOfMapToIndexValue]
        if isinstance(_aspect_objects, Unset):
            aspect_objects = UNSET
        else:
            aspect_objects = MapToListOfMapToIndexValue.from_dict(_aspect_objects)

        hist_source = d.pop("histSource", UNSET)

        user_name = d.pop("userName", UNSET)

        sord_hist = cls(
            hist_guid=hist_guid,
            time_stamp_utc=time_stamp_utc,
            work_station=work_station,
            time_stamp_local=time_stamp_local,
            obj_guid=obj_guid,
            user_no=user_no,
            hist_keys=hist_keys,
            aspect_objects=aspect_objects,
            hist_source=hist_source,
            user_name=user_name,
        )

        sord_hist.additional_properties = d
        return sord_hist

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
