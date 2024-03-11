from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MapHistItemC")


@_attrs_define
class MapHistItemC:
    """<p>
    Bit constants for members of MapHistItem
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_hist_guid (Union[Unset, str]): Member bit: Serialisation version ID DB column: maphistguid
            ln_hist_guid (Union[Unset, int]): Column length: Serialisation version ID DB column: maphistguid
            mb_key (Union[Unset, str]): DB column: mapkey
            ln_key (Union[Unset, int]): DB column: mapkey
            mb_value (Union[Unset, str]): DB column: mapvalue
            ln_value (Union[Unset, int]): DB column: mapvalue
            mb_content_type (Union[Unset, str]): DB column: mapcontenttype
            ln_content_type (Union[Unset, int]): DB column: mapcontenttype
            mb_blob_data (Union[Unset, str]): DB column: mapblob
            ln_blob_data (Union[Unset, int]): DB column: mapblob
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_hist_guid: Union[Unset, str] = UNSET
    ln_hist_guid: Union[Unset, int] = UNSET
    mb_key: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    mb_value: Union[Unset, str] = UNSET
    ln_value: Union[Unset, int] = UNSET
    mb_content_type: Union[Unset, str] = UNSET
    ln_content_type: Union[Unset, int] = UNSET
    mb_blob_data: Union[Unset, str] = UNSET
    ln_blob_data: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_hist_guid = self.mb_hist_guid
        ln_hist_guid = self.ln_hist_guid
        mb_key = self.mb_key
        ln_key = self.ln_key
        mb_value = self.mb_value
        ln_value = self.ln_value
        mb_content_type = self.mb_content_type
        ln_content_type = self.ln_content_type
        mb_blob_data = self.mb_blob_data
        ln_blob_data = self.ln_blob_data
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_hist_guid is not UNSET:
            field_dict["mbHistGuid"] = mb_hist_guid
        if ln_hist_guid is not UNSET:
            field_dict["lnHistGuid"] = ln_hist_guid
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if mb_value is not UNSET:
            field_dict["mbValue"] = mb_value
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if mb_content_type is not UNSET:
            field_dict["mbContentType"] = mb_content_type
        if ln_content_type is not UNSET:
            field_dict["lnContentType"] = ln_content_type
        if mb_blob_data is not UNSET:
            field_dict["mbBlobData"] = mb_blob_data
        if ln_blob_data is not UNSET:
            field_dict["lnBlobData"] = ln_blob_data
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_hist_guid = d.pop("mbHistGuid", UNSET)

        ln_hist_guid = d.pop("lnHistGuid", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        mb_value = d.pop("mbValue", UNSET)

        ln_value = d.pop("lnValue", UNSET)

        mb_content_type = d.pop("mbContentType", UNSET)

        ln_content_type = d.pop("lnContentType", UNSET)

        mb_blob_data = d.pop("mbBlobData", UNSET)

        ln_blob_data = d.pop("lnBlobData", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        map_hist_item_c = cls(
            mb_hist_guid=mb_hist_guid,
            ln_hist_guid=ln_hist_guid,
            mb_key=mb_key,
            ln_key=ln_key,
            mb_value=mb_value,
            ln_value=ln_value,
            mb_content_type=mb_content_type,
            ln_content_type=ln_content_type,
            mb_blob_data=mb_blob_data,
            ln_blob_data=ln_blob_data,
            mb_all_members=mb_all_members,
        )

        map_hist_item_c.additional_properties = d
        return map_hist_item_c

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
