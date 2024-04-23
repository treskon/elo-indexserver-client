from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFNodeAssoc")


@_attrs_define
class WFNodeAssoc:
    """<p>
    Represents a bridge (connection) in a workflow diagram
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            node_from (Union[Unset, int]): Start node (starting location)
            type (Union[Unset, int]): Type of bridge (connection).
                {@link WFNodeMatrixC#ALWAYS}, {@link WFNodeMatrixC#IF_TRUE},
                 {@link WFNodeMatrixC#IF_FALSE}.
            done (Union[Unset, bool]): Indicates whether the bridge has been passed through/over (used).
                For a condition node, this
                 member is true for both paths (TRUE and FALSE) if either has been passed. Thus it cannot be
                 used in a client application to find out, which path the workflow has taken.
            node_to (Union[Unset, int]): Destination (end) node
    """

    node_from: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    done: Union[Unset, bool] = UNSET
    node_to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_from = self.node_from

        type = self.type

        done = self.done

        node_to = self.node_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_from is not UNSET:
            field_dict["nodeFrom"] = node_from
        if type is not UNSET:
            field_dict["type"] = type
        if done is not UNSET:
            field_dict["done"] = done
        if node_to is not UNSET:
            field_dict["nodeTo"] = node_to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_from = d.pop("nodeFrom", UNSET)

        type = d.pop("type", UNSET)

        done = d.pop("done", UNSET)

        node_to = d.pop("nodeTo", UNSET)

        wf_node_assoc = cls(
            node_from=node_from,
            type=type,
            done=done,
            node_to=node_to,
        )

        wf_node_assoc.additional_properties = d
        return wf_node_assoc

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
