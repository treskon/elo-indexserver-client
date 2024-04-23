from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindDirectC")


@_attrs_define
class FindDirectC:
    """Constants used in class FindDirect

    Attributes:
        field_guid (Union[Unset, str]): ELO iSearch field: GUID (Sord.
            guid)
        field_ext (Union[Unset, str]): ELO iSearch field: document file extension without leading dot (DocVersion.
            ext)
        field_doc_size (Union[Unset, str]): Document size
        field_desc (Union[Unset, str]): ELO iSearch field: descripton (memo text, Sord.
            desc)
        field_deldate_year (Union[Unset, str]): ELO iSearch field: Year of delete date, UTC (Sord.
            delDateIso)
        field_mask_name (Union[Unset, str]): ELO iSearch field: Keywording form name, (Sord.
            maskName)
        field_deldate_month (Union[Unset, str]): ELO iSearch field: Month of delete date, UTC (Sord.delDateIso), always
            2 characters, e.g.
            01
             for January.
        field_name (Union[Unset, str]): ELO iSearch field: short description (Sord.
            name)
        field_version_number (Union[Unset, str]): DocVersion.
            version
        field_xdate (Union[Unset, str]): ELO iSearch field: ISO formatted document date, UTC (Sord.
            xDateIso)
        field_tstamp (Union[Unset, str]): ELO iSearch field: last modified time stamp, UTC (Sord.
            tStamp)
        field_idate_year (Union[Unset, str]): ELO iSearch field: Year of archiving date, UTC (Sord.
            iDateIso)
        field_obj_key_date (Union[Unset, str]): Date Indexfields (dLINE)
        field_mask_id (Union[Unset, str]): ELO iSearch field: Keywording form ID, (Sord.
            mask)
        field_obj_key (Union[Unset, str]): ELO iSearch field: group name of index field (Sord.objKey[.].name,
            DocMask.line[.].
            key)
        field_owner (Union[Unset, str]): ELO iSearch field: owner name (Sord.
            ownerName)
        field_id (Union[Unset, str]): ELO iSearch field: ID (Sord.
            id)
        field_obj_key_tokenized (Union[Unset, str]): ELO iSearch field: group name of index field (Sord.objKey[.].name,
            DocMask.line[.].
            key) This
             field contains tokenized content (linguistic processing applied)
        field_deldate (Union[Unset, str]): ELO iSearch field: ISO formatted delete date, UTC (Sord.
            delDateIso)
        field_xdate_year (Union[Unset, str]): ELO iSearch field: Year of document date, UTC (Sord.
            xDateIso)
        field_xdate_month (Union[Unset, str]): ELO iSearch field: Month of document date, UTC (Sord.xDateIso), always 2
            characters, e.g.
            01
             for January.
        field_version_comment (Union[Unset, str]): DocVersion.
            comment
        field_type (Union[Unset, str]): ELO iSearch field: folder or document type (Sord.
            type)
        field_idate_month (Union[Unset, str]): ELO iSearch field: Month of archiving date, UTC (Sord.iDateIso), always 2
            characters, e.g.
            01
             for January.
        field_obj_key_numeric (Union[Unset, str]): Numeric Indexfields (nLINE)
        field_owner_id (Union[Unset, str]): ELO iSearch field: owner ID (Sord.
            ownerId)
        field_idate (Union[Unset, str]): ELO iSearch field: ISO formatted archiving date, UTC (Sord.
            iDateIso)
        field_version_owner (Union[Unset, str]): DocVersion.
            ownerId
    """

    field_guid: Union[Unset, str] = UNSET
    field_ext: Union[Unset, str] = UNSET
    field_doc_size: Union[Unset, str] = UNSET
    field_desc: Union[Unset, str] = UNSET
    field_deldate_year: Union[Unset, str] = UNSET
    field_mask_name: Union[Unset, str] = UNSET
    field_deldate_month: Union[Unset, str] = UNSET
    field_name: Union[Unset, str] = UNSET
    field_version_number: Union[Unset, str] = UNSET
    field_xdate: Union[Unset, str] = UNSET
    field_tstamp: Union[Unset, str] = UNSET
    field_idate_year: Union[Unset, str] = UNSET
    field_obj_key_date: Union[Unset, str] = UNSET
    field_mask_id: Union[Unset, str] = UNSET
    field_obj_key: Union[Unset, str] = UNSET
    field_owner: Union[Unset, str] = UNSET
    field_id: Union[Unset, str] = UNSET
    field_obj_key_tokenized: Union[Unset, str] = UNSET
    field_deldate: Union[Unset, str] = UNSET
    field_xdate_year: Union[Unset, str] = UNSET
    field_xdate_month: Union[Unset, str] = UNSET
    field_version_comment: Union[Unset, str] = UNSET
    field_type: Union[Unset, str] = UNSET
    field_idate_month: Union[Unset, str] = UNSET
    field_obj_key_numeric: Union[Unset, str] = UNSET
    field_owner_id: Union[Unset, str] = UNSET
    field_idate: Union[Unset, str] = UNSET
    field_version_owner: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_guid = self.field_guid

        field_ext = self.field_ext

        field_doc_size = self.field_doc_size

        field_desc = self.field_desc

        field_deldate_year = self.field_deldate_year

        field_mask_name = self.field_mask_name

        field_deldate_month = self.field_deldate_month

        field_name = self.field_name

        field_version_number = self.field_version_number

        field_xdate = self.field_xdate

        field_tstamp = self.field_tstamp

        field_idate_year = self.field_idate_year

        field_obj_key_date = self.field_obj_key_date

        field_mask_id = self.field_mask_id

        field_obj_key = self.field_obj_key

        field_owner = self.field_owner

        field_id = self.field_id

        field_obj_key_tokenized = self.field_obj_key_tokenized

        field_deldate = self.field_deldate

        field_xdate_year = self.field_xdate_year

        field_xdate_month = self.field_xdate_month

        field_version_comment = self.field_version_comment

        field_type = self.field_type

        field_idate_month = self.field_idate_month

        field_obj_key_numeric = self.field_obj_key_numeric

        field_owner_id = self.field_owner_id

        field_idate = self.field_idate

        field_version_owner = self.field_version_owner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_guid is not UNSET:
            field_dict["FIELD_GUID"] = field_guid
        if field_ext is not UNSET:
            field_dict["FIELD_EXT"] = field_ext
        if field_doc_size is not UNSET:
            field_dict["FIELD_DOC_SIZE"] = field_doc_size
        if field_desc is not UNSET:
            field_dict["FIELD_DESC"] = field_desc
        if field_deldate_year is not UNSET:
            field_dict["FIELD_DELDATE_YEAR"] = field_deldate_year
        if field_mask_name is not UNSET:
            field_dict["FIELD_MASK_NAME"] = field_mask_name
        if field_deldate_month is not UNSET:
            field_dict["FIELD_DELDATE_MONTH"] = field_deldate_month
        if field_name is not UNSET:
            field_dict["FIELD_NAME"] = field_name
        if field_version_number is not UNSET:
            field_dict["FIELD_VERSION_NUMBER"] = field_version_number
        if field_xdate is not UNSET:
            field_dict["FIELD_XDATE"] = field_xdate
        if field_tstamp is not UNSET:
            field_dict["FIELD_TSTAMP"] = field_tstamp
        if field_idate_year is not UNSET:
            field_dict["FIELD_IDATE_YEAR"] = field_idate_year
        if field_obj_key_date is not UNSET:
            field_dict["FIELD_OBJ_KEY_DATE"] = field_obj_key_date
        if field_mask_id is not UNSET:
            field_dict["FIELD_MASK_ID"] = field_mask_id
        if field_obj_key is not UNSET:
            field_dict["FIELD_OBJ_KEY"] = field_obj_key
        if field_owner is not UNSET:
            field_dict["FIELD_OWNER"] = field_owner
        if field_id is not UNSET:
            field_dict["FIELD_ID"] = field_id
        if field_obj_key_tokenized is not UNSET:
            field_dict["FIELD_OBJ_KEY_TOKENIZED"] = field_obj_key_tokenized
        if field_deldate is not UNSET:
            field_dict["FIELD_DELDATE"] = field_deldate
        if field_xdate_year is not UNSET:
            field_dict["FIELD_XDATE_YEAR"] = field_xdate_year
        if field_xdate_month is not UNSET:
            field_dict["FIELD_XDATE_MONTH"] = field_xdate_month
        if field_version_comment is not UNSET:
            field_dict["FIELD_VERSION_COMMENT"] = field_version_comment
        if field_type is not UNSET:
            field_dict["FIELD_TYPE"] = field_type
        if field_idate_month is not UNSET:
            field_dict["FIELD_IDATE_MONTH"] = field_idate_month
        if field_obj_key_numeric is not UNSET:
            field_dict["FIELD_OBJ_KEY_NUMERIC"] = field_obj_key_numeric
        if field_owner_id is not UNSET:
            field_dict["FIELD_OWNER_ID"] = field_owner_id
        if field_idate is not UNSET:
            field_dict["FIELD_IDATE"] = field_idate
        if field_version_owner is not UNSET:
            field_dict["FIELD_VERSION_OWNER"] = field_version_owner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_guid = d.pop("FIELD_GUID", UNSET)

        field_ext = d.pop("FIELD_EXT", UNSET)

        field_doc_size = d.pop("FIELD_DOC_SIZE", UNSET)

        field_desc = d.pop("FIELD_DESC", UNSET)

        field_deldate_year = d.pop("FIELD_DELDATE_YEAR", UNSET)

        field_mask_name = d.pop("FIELD_MASK_NAME", UNSET)

        field_deldate_month = d.pop("FIELD_DELDATE_MONTH", UNSET)

        field_name = d.pop("FIELD_NAME", UNSET)

        field_version_number = d.pop("FIELD_VERSION_NUMBER", UNSET)

        field_xdate = d.pop("FIELD_XDATE", UNSET)

        field_tstamp = d.pop("FIELD_TSTAMP", UNSET)

        field_idate_year = d.pop("FIELD_IDATE_YEAR", UNSET)

        field_obj_key_date = d.pop("FIELD_OBJ_KEY_DATE", UNSET)

        field_mask_id = d.pop("FIELD_MASK_ID", UNSET)

        field_obj_key = d.pop("FIELD_OBJ_KEY", UNSET)

        field_owner = d.pop("FIELD_OWNER", UNSET)

        field_id = d.pop("FIELD_ID", UNSET)

        field_obj_key_tokenized = d.pop("FIELD_OBJ_KEY_TOKENIZED", UNSET)

        field_deldate = d.pop("FIELD_DELDATE", UNSET)

        field_xdate_year = d.pop("FIELD_XDATE_YEAR", UNSET)

        field_xdate_month = d.pop("FIELD_XDATE_MONTH", UNSET)

        field_version_comment = d.pop("FIELD_VERSION_COMMENT", UNSET)

        field_type = d.pop("FIELD_TYPE", UNSET)

        field_idate_month = d.pop("FIELD_IDATE_MONTH", UNSET)

        field_obj_key_numeric = d.pop("FIELD_OBJ_KEY_NUMERIC", UNSET)

        field_owner_id = d.pop("FIELD_OWNER_ID", UNSET)

        field_idate = d.pop("FIELD_IDATE", UNSET)

        field_version_owner = d.pop("FIELD_VERSION_OWNER", UNSET)

        find_direct_c = cls(
            field_guid=field_guid,
            field_ext=field_ext,
            field_doc_size=field_doc_size,
            field_desc=field_desc,
            field_deldate_year=field_deldate_year,
            field_mask_name=field_mask_name,
            field_deldate_month=field_deldate_month,
            field_name=field_name,
            field_version_number=field_version_number,
            field_xdate=field_xdate,
            field_tstamp=field_tstamp,
            field_idate_year=field_idate_year,
            field_obj_key_date=field_obj_key_date,
            field_mask_id=field_mask_id,
            field_obj_key=field_obj_key,
            field_owner=field_owner,
            field_id=field_id,
            field_obj_key_tokenized=field_obj_key_tokenized,
            field_deldate=field_deldate,
            field_xdate_year=field_xdate_year,
            field_xdate_month=field_xdate_month,
            field_version_comment=field_version_comment,
            field_type=field_type,
            field_idate_month=field_idate_month,
            field_obj_key_numeric=field_obj_key_numeric,
            field_owner_id=field_owner_id,
            field_idate=field_idate,
            field_version_owner=field_version_owner,
        )

        find_direct_c.additional_properties = d
        return find_direct_c

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
