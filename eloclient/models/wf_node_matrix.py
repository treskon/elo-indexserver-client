from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_node_assoc import WFNodeAssoc


T = TypeVar("T", bound="WFNodeMatrix")


@_attrs_define
class WFNodeMatrix:
    """<p>
    Stores the relationship between workflow nodes
     </p>
     <p>
     Administers the bridges(connections) in a workflow diagram. These are objects of type
     WorkFlowNodeAssoc.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office
     </p>

        Attributes:
            assocs (Union[Unset, List['WFNodeAssoc']]):
    """

    assocs: Union[Unset, List["WFNodeAssoc"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assocs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.assocs, Unset):
            assocs = []
            for assocs_item_data in self.assocs:
                assocs_item = assocs_item_data.to_dict()
                assocs.append(assocs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assocs is not UNSET:
            field_dict["assocs"] = assocs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_node_assoc import WFNodeAssoc

        d = src_dict.copy()
        assocs = []
        _assocs = d.pop("assocs", UNSET)
        for assocs_item_data in _assocs or []:
            assocs_item = WFNodeAssoc.from_dict(assocs_item_data)

            assocs.append(assocs_item)

        wf_node_matrix = cls(
            assocs=assocs,
        )

        wf_node_matrix.additional_properties = d
        return wf_node_matrix

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
