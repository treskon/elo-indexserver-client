from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFRefSord")


@_attrs_define
class BRequestIXServicePortIFRefSord:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        new_parent_id (Union[Unset, str]):
        obj_id (Union[Unset, str]):
        old_parent_id (Union[Unset, str]):
        man_sort_idx (Union[Unset, int]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    new_parent_id: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    old_parent_id: Union[Unset, str] = UNSET
    man_sort_idx: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        new_parent_id = self.new_parent_id

        obj_id = self.obj_id

        old_parent_id = self.old_parent_id

        man_sort_idx = self.man_sort_idx

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if new_parent_id is not UNSET:
            field_dict["newParentId"] = new_parent_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if old_parent_id is not UNSET:
            field_dict["oldParentId"] = old_parent_id
        if man_sort_idx is not UNSET:
            field_dict["manSortIdx"] = man_sort_idx

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        new_parent_id = d.pop("newParentId", UNSET)

        obj_id = d.pop("objId", UNSET)

        old_parent_id = d.pop("oldParentId", UNSET)

        man_sort_idx = d.pop("manSortIdx", UNSET)

        b_request_ix_service_port_if_ref_sord = cls(
            ci=ci,
            new_parent_id=new_parent_id,
            obj_id=obj_id,
            old_parent_id=old_parent_id,
            man_sort_idx=man_sort_idx,
        )

        b_request_ix_service_port_if_ref_sord.additional_properties = d
        return b_request_ix_service_port_if_ref_sord

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
