from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SordHistKeyC")


@_attrs_define
class SordHistKeyC:
    """
    Attributes:
        id_sord_name (Union[Unset, int]): Entry ID for Sord.name.
        id_sord_desc (Union[Unset, int]): Entry ID for Sord.desc.
        name_sord_name (Union[Unset, str]): Entry name for Sord.name.
        name_sord_deldate (Union[Unset, str]): Entry name for Sord.delDate.
        name_sord_acl (Union[Unset, str]): Entry ID for Sord.
            acl
        id_sord_xdate (Union[Unset, int]): Entry ID for Sord.xDate.
        name_sord_desc (Union[Unset, str]): Entry name for Sord.desc.
        id_sord_deldate (Union[Unset, int]): Entry ID for Sord.delDate.
        name_sord_xdate (Union[Unset, str]): Entry name for Sord.xDate.
        name_docmask_name (Union[Unset, str]): Entry mame for Sord.name.
        id_reserved_min (Union[Unset, int]): Entry IDs greater or equal of this value are used for Sord.name, Sord.xDate
            etc.
        id_docmask_name (Union[Unset, int]): Entry ID for Sord.mask.
        id_sord_acl (Union[Unset, int]): Entry ID for Sord.
            acl
    """

    id_sord_name: Union[Unset, int] = UNSET
    id_sord_desc: Union[Unset, int] = UNSET
    name_sord_name: Union[Unset, str] = UNSET
    name_sord_deldate: Union[Unset, str] = UNSET
    name_sord_acl: Union[Unset, str] = UNSET
    id_sord_xdate: Union[Unset, int] = UNSET
    name_sord_desc: Union[Unset, str] = UNSET
    id_sord_deldate: Union[Unset, int] = UNSET
    name_sord_xdate: Union[Unset, str] = UNSET
    name_docmask_name: Union[Unset, str] = UNSET
    id_reserved_min: Union[Unset, int] = UNSET
    id_docmask_name: Union[Unset, int] = UNSET
    id_sord_acl: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_sord_name = self.id_sord_name

        id_sord_desc = self.id_sord_desc

        name_sord_name = self.name_sord_name

        name_sord_deldate = self.name_sord_deldate

        name_sord_acl = self.name_sord_acl

        id_sord_xdate = self.id_sord_xdate

        name_sord_desc = self.name_sord_desc

        id_sord_deldate = self.id_sord_deldate

        name_sord_xdate = self.name_sord_xdate

        name_docmask_name = self.name_docmask_name

        id_reserved_min = self.id_reserved_min

        id_docmask_name = self.id_docmask_name

        id_sord_acl = self.id_sord_acl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id_sord_name is not UNSET:
            field_dict["ID_SORD_NAME"] = id_sord_name
        if id_sord_desc is not UNSET:
            field_dict["ID_SORD_DESC"] = id_sord_desc
        if name_sord_name is not UNSET:
            field_dict["NAME_SORD_NAME"] = name_sord_name
        if name_sord_deldate is not UNSET:
            field_dict["NAME_SORD_DELDATE"] = name_sord_deldate
        if name_sord_acl is not UNSET:
            field_dict["NAME_SORD_ACL"] = name_sord_acl
        if id_sord_xdate is not UNSET:
            field_dict["ID_SORD_XDATE"] = id_sord_xdate
        if name_sord_desc is not UNSET:
            field_dict["NAME_SORD_DESC"] = name_sord_desc
        if id_sord_deldate is not UNSET:
            field_dict["ID_SORD_DELDATE"] = id_sord_deldate
        if name_sord_xdate is not UNSET:
            field_dict["NAME_SORD_XDATE"] = name_sord_xdate
        if name_docmask_name is not UNSET:
            field_dict["NAME_DOCMASK_NAME"] = name_docmask_name
        if id_reserved_min is not UNSET:
            field_dict["ID_RESERVED_MIN"] = id_reserved_min
        if id_docmask_name is not UNSET:
            field_dict["ID_DOCMASK_NAME"] = id_docmask_name
        if id_sord_acl is not UNSET:
            field_dict["ID_SORD_ACL"] = id_sord_acl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_sord_name = d.pop("ID_SORD_NAME", UNSET)

        id_sord_desc = d.pop("ID_SORD_DESC", UNSET)

        name_sord_name = d.pop("NAME_SORD_NAME", UNSET)

        name_sord_deldate = d.pop("NAME_SORD_DELDATE", UNSET)

        name_sord_acl = d.pop("NAME_SORD_ACL", UNSET)

        id_sord_xdate = d.pop("ID_SORD_XDATE", UNSET)

        name_sord_desc = d.pop("NAME_SORD_DESC", UNSET)

        id_sord_deldate = d.pop("ID_SORD_DELDATE", UNSET)

        name_sord_xdate = d.pop("NAME_SORD_XDATE", UNSET)

        name_docmask_name = d.pop("NAME_DOCMASK_NAME", UNSET)

        id_reserved_min = d.pop("ID_RESERVED_MIN", UNSET)

        id_docmask_name = d.pop("ID_DOCMASK_NAME", UNSET)

        id_sord_acl = d.pop("ID_SORD_ACL", UNSET)

        sord_hist_key_c = cls(
            id_sord_name=id_sord_name,
            id_sord_desc=id_sord_desc,
            name_sord_name=name_sord_name,
            name_sord_deldate=name_sord_deldate,
            name_sord_acl=name_sord_acl,
            id_sord_xdate=id_sord_xdate,
            name_sord_desc=name_sord_desc,
            id_sord_deldate=id_sord_deldate,
            name_sord_xdate=name_sord_xdate,
            name_docmask_name=name_docmask_name,
            id_reserved_min=id_reserved_min,
            id_docmask_name=id_docmask_name,
            id_sord_acl=id_sord_acl,
        )

        sord_hist_key_c.additional_properties = d
        return sord_hist_key_c

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
