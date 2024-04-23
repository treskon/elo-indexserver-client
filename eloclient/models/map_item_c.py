from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapItemC")


@_attrs_define
class MapItemC:
    """<p>Bit constants for members of MapItem</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_value (Union[Unset, int]): DB column: mapvalue
            ln_content_type (Union[Unset, int]): Column length: Content Type.
                DB column: mapcontenttype
            mb_id (Union[Unset, str]): DB column: mapid
            mb_key (Union[Unset, str]): DB column: mapkey
            mb_value (Union[Unset, str]): DB column: mapvalue
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_key (Union[Unset, int]): DB column: mapkey
            ln_blob_data (Union[Unset, int]): Column length: Blob data.
                DB column: mapblob
            mb_blob_data (Union[Unset, str]): Member bit: Blob data.
                DB column: mapblob
            mb_content_type (Union[Unset, str]): Member bit: Content Type.
                DB column: mapcontenttype
            ln_id (Union[Unset, int]): DB column: mapid
    """

    ln_value: Union[Unset, int] = UNSET
    ln_content_type: Union[Unset, int] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    mb_value: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    ln_blob_data: Union[Unset, int] = UNSET
    mb_blob_data: Union[Unset, str] = UNSET
    mb_content_type: Union[Unset, str] = UNSET
    ln_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_value = self.ln_value

        ln_content_type = self.ln_content_type

        mb_id = self.mb_id

        mb_key = self.mb_key

        mb_value = self.mb_value

        mb_all_members = self.mb_all_members

        ln_key = self.ln_key

        ln_blob_data = self.ln_blob_data

        mb_blob_data = self.mb_blob_data

        mb_content_type = self.mb_content_type

        ln_id = self.ln_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if ln_content_type is not UNSET:
            field_dict["lnContentType"] = ln_content_type
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if ln_blob_data is not UNSET:
            field_dict["lnBlobData"] = ln_blob_data
        if mb_blob_data is not UNSET:
            field_dict["mbBlobData"] = mb_blob_data
        if mb_content_type is not UNSET:
            field_dict["mbContentType"] = mb_content_type
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_value = d.pop("lnValue", UNSET)

        ln_content_type = d.pop("lnContentType", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        ln_blob_data = d.pop("lnBlobData", UNSET)

        mb_blob_data = d.pop("mbBlobData", UNSET)

        mb_content_type = d.pop("mbContentType", UNSET)

        ln_id = d.pop("lnId", UNSET)

        map_item_c = cls(
            ln_value=ln_value,
            ln_content_type=ln_content_type,
            mb_id=mb_id,
            mb_key=mb_key,
            mb_value=mb_value,
            mb_all_members=mb_all_members,
            ln_key=ln_key,
            ln_blob_data=ln_blob_data,
            mb_blob_data=mb_blob_data,
            mb_content_type=mb_content_type,
            ln_id=ln_id,
        )

        map_item_c.additional_properties = d
        return map_item_c

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
