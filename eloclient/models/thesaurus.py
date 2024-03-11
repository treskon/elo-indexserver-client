from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Thesaurus")


@_attrs_define
class Thesaurus:
    """Internal class.

    Attributes:
        group_id (Union[Unset, int]): DB column: groupid
        prio (Union[Unset, int]): DB column: prio
        data (Union[Unset, str]): DB column: data
        compare (Union[Unset, str]): DB column: compare
        list_id (Union[Unset, int]): DB column: listid
    """

    group_id: Union[Unset, int] = UNSET
    prio: Union[Unset, int] = UNSET
    data: Union[Unset, str] = UNSET
    compare: Union[Unset, str] = UNSET
    list_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        prio = self.prio
        data = self.data
        compare = self.compare
        list_id = self.list_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if prio is not UNSET:
            field_dict["prio"] = prio
        if data is not UNSET:
            field_dict["data"] = data
        if compare is not UNSET:
            field_dict["compare"] = compare
        if list_id is not UNSET:
            field_dict["listId"] = list_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        prio = d.pop("prio", UNSET)

        data = d.pop("data", UNSET)

        compare = d.pop("compare", UNSET)

        list_id = d.pop("listId", UNSET)

        thesaurus = cls(
            group_id=group_id,
            prio=prio,
            data=data,
            compare=compare,
            list_id=list_id,
        )

        thesaurus.additional_properties = d
        return thesaurus

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
