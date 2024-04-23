from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name import IdName


T = TypeVar("T", bound="ProcessReplSet")


@_attrs_define
class ProcessReplSet:
    """Replication sets to be added to/removed from an object.
    The replication set parameter must refer
     to existing objects that may contain empty lists. Null values are not allowed.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            add_repl_sets (Union[Unset, List['IdName']]):
            set_repl_sets (Union[Unset, List['IdName']]):
            and_repl_sets (Union[Unset, List['IdName']]):
            sub_repl_sets (Union[Unset, List['IdName']]):
    """

    add_repl_sets: Union[Unset, List["IdName"]] = UNSET
    set_repl_sets: Union[Unset, List["IdName"]] = UNSET
    and_repl_sets: Union[Unset, List["IdName"]] = UNSET
    sub_repl_sets: Union[Unset, List["IdName"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_repl_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.add_repl_sets, Unset):
            add_repl_sets = []
            for add_repl_sets_item_data in self.add_repl_sets:
                add_repl_sets_item = add_repl_sets_item_data.to_dict()
                add_repl_sets.append(add_repl_sets_item)

        set_repl_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.set_repl_sets, Unset):
            set_repl_sets = []
            for set_repl_sets_item_data in self.set_repl_sets:
                set_repl_sets_item = set_repl_sets_item_data.to_dict()
                set_repl_sets.append(set_repl_sets_item)

        and_repl_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.and_repl_sets, Unset):
            and_repl_sets = []
            for and_repl_sets_item_data in self.and_repl_sets:
                and_repl_sets_item = and_repl_sets_item_data.to_dict()
                and_repl_sets.append(and_repl_sets_item)

        sub_repl_sets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_repl_sets, Unset):
            sub_repl_sets = []
            for sub_repl_sets_item_data in self.sub_repl_sets:
                sub_repl_sets_item = sub_repl_sets_item_data.to_dict()
                sub_repl_sets.append(sub_repl_sets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_repl_sets is not UNSET:
            field_dict["addReplSets"] = add_repl_sets
        if set_repl_sets is not UNSET:
            field_dict["setReplSets"] = set_repl_sets
        if and_repl_sets is not UNSET:
            field_dict["andReplSets"] = and_repl_sets
        if sub_repl_sets is not UNSET:
            field_dict["subReplSets"] = sub_repl_sets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.id_name import IdName

        d = src_dict.copy()
        add_repl_sets = []
        _add_repl_sets = d.pop("addReplSets", UNSET)
        for add_repl_sets_item_data in _add_repl_sets or []:
            add_repl_sets_item = IdName.from_dict(add_repl_sets_item_data)

            add_repl_sets.append(add_repl_sets_item)

        set_repl_sets = []
        _set_repl_sets = d.pop("setReplSets", UNSET)
        for set_repl_sets_item_data in _set_repl_sets or []:
            set_repl_sets_item = IdName.from_dict(set_repl_sets_item_data)

            set_repl_sets.append(set_repl_sets_item)

        and_repl_sets = []
        _and_repl_sets = d.pop("andReplSets", UNSET)
        for and_repl_sets_item_data in _and_repl_sets or []:
            and_repl_sets_item = IdName.from_dict(and_repl_sets_item_data)

            and_repl_sets.append(and_repl_sets_item)

        sub_repl_sets = []
        _sub_repl_sets = d.pop("subReplSets", UNSET)
        for sub_repl_sets_item_data in _sub_repl_sets or []:
            sub_repl_sets_item = IdName.from_dict(sub_repl_sets_item_data)

            sub_repl_sets.append(sub_repl_sets_item)

        process_repl_set = cls(
            add_repl_sets=add_repl_sets,
            set_repl_sets=set_repl_sets,
            and_repl_sets=and_repl_sets,
            sub_repl_sets=sub_repl_sets,
        )

        process_repl_set.additional_properties = d
        return process_repl_set

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
