from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFTakeNodeC")


@_attrs_define
class WFTakeNodeC:
    """Constant class for controlling the taking over(passing to another user) of a workflow object.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            reset_department2 (Union[Unset, int]): WFNode.department2 is set when the node is taken over by another user.
            reset_in_use_date (Union[Unset, int]): WFNode.inUseDateIso is set when the node is taken over by another user.
            default (Union[Unset, int]): Standard action. Neither WFNode.department2 nor WFNode.inUseDateIso are returned.
    """

    reset_department2: Union[Unset, int] = UNSET
    reset_in_use_date: Union[Unset, int] = UNSET
    default: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reset_department2 = self.reset_department2

        reset_in_use_date = self.reset_in_use_date

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reset_department2 is not UNSET:
            field_dict["RESET_DEPARTMENT2"] = reset_department2
        if reset_in_use_date is not UNSET:
            field_dict["RESET_IN_USE_DATE"] = reset_in_use_date
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reset_department2 = d.pop("RESET_DEPARTMENT2", UNSET)

        reset_in_use_date = d.pop("RESET_IN_USE_DATE", UNSET)

        default = d.pop("DEFAULT", UNSET)

        wf_take_node_c = cls(
            reset_department2=reset_department2,
            reset_in_use_date=reset_in_use_date,
            default=default,
        )

        wf_take_node_c.additional_properties = d
        return wf_take_node_c

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
