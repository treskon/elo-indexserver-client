from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFNodeMatrixC")


@_attrs_define
class WFNodeMatrixC:
    """These constants describe the type of connection between two nodes.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            if_true (Union[Unset, int]): This connection is the TRUE connection following a decision node.
                This connection will be
                 utilised when the IF requirement is fulfilled.
            if_overtime (Union[Unset, int]): This connection is only for the case of overtime.
            always (Union[Unset, int]): Connection type for non-decision nodes.
                The connection will always be utilised to reach the
                 next node. No conditions have to be fulfilled.
            if_false (Union[Unset, int]): This connection is the FALSE connection following a decision node.
                This connection will be
                 utilised when the IF requirement is not fulfilled.
    """

    if_true: Union[Unset, int] = UNSET
    if_overtime: Union[Unset, int] = UNSET
    always: Union[Unset, int] = UNSET
    if_false: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_true = self.if_true

        if_overtime = self.if_overtime

        always = self.always

        if_false = self.if_false

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if if_true is not UNSET:
            field_dict["IF_TRUE"] = if_true
        if if_overtime is not UNSET:
            field_dict["IF_OVERTIME"] = if_overtime
        if always is not UNSET:
            field_dict["ALWAYS"] = always
        if if_false is not UNSET:
            field_dict["IF_FALSE"] = if_false

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_true = d.pop("IF_TRUE", UNSET)

        if_overtime = d.pop("IF_OVERTIME", UNSET)

        always = d.pop("ALWAYS", UNSET)

        if_false = d.pop("IF_FALSE", UNSET)

        wf_node_matrix_c = cls(
            if_true=if_true,
            if_overtime=if_overtime,
            always=always,
            if_false=if_false,
        )

        wf_node_matrix_c.additional_properties = d
        return wf_node_matrix_c

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
