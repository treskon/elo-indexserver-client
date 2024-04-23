from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SordHistKey")


@_attrs_define
class SordHistKey:
    """This class provides the version information for a keywording attribute that has been modified.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            hist_guid (Union[Unset, str]): GUID of the assigned SordHist object.
            key_no (Union[Unset, int]): ID of the attribute.
            key_data (Union[Unset, str]): Value of dat of the attribute.
            key_index (Union[Unset, int]): Index of the attribute within an array of attributes.
            key_name (Union[Unset, str]): Name of the attribute.
            key_id (Union[Unset, int]): External ID of the attribute, serves as an identifier for keyNames.
    """

    hist_guid: Union[Unset, str] = UNSET
    key_no: Union[Unset, int] = UNSET
    key_data: Union[Unset, str] = UNSET
    key_index: Union[Unset, int] = UNSET
    key_name: Union[Unset, str] = UNSET
    key_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hist_guid = self.hist_guid

        key_no = self.key_no

        key_data = self.key_data

        key_index = self.key_index

        key_name = self.key_name

        key_id = self.key_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hist_guid is not UNSET:
            field_dict["histGuid"] = hist_guid
        if key_no is not UNSET:
            field_dict["keyNo"] = key_no
        if key_data is not UNSET:
            field_dict["keyData"] = key_data
        if key_index is not UNSET:
            field_dict["keyIndex"] = key_index
        if key_name is not UNSET:
            field_dict["keyName"] = key_name
        if key_id is not UNSET:
            field_dict["keyId"] = key_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hist_guid = d.pop("histGuid", UNSET)

        key_no = d.pop("keyNo", UNSET)

        key_data = d.pop("keyData", UNSET)

        key_index = d.pop("keyIndex", UNSET)

        key_name = d.pop("keyName", UNSET)

        key_id = d.pop("keyId", UNSET)

        sord_hist_key = cls(
            hist_guid=hist_guid,
            key_no=key_no,
            key_data=key_data,
            key_index=key_index,
            key_name=key_name,
            key_id=key_id,
        )

        sord_hist_key.additional_properties = d
        return sord_hist_key

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
