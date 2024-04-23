from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.client_info import ClientInfo
    from ..models.combine_acl_options import CombineAclOptions


T = TypeVar("T", bound="BRequestIXServicePortIFCombineAcl")


@_attrs_define
class BRequestIXServicePortIFCombineAcl:
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
        lhs (Union[Unset, List['AclItem']]):
        options (Union[Unset, CombineAclOptions]): This class specifies additional options for compareAcl.
        rhs (Union[Unset, List['AclItem']]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    lhs: Union[Unset, List["AclItem"]] = UNSET
    options: Union[Unset, "CombineAclOptions"] = UNSET
    rhs: Union[Unset, List["AclItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        lhs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lhs, Unset):
            lhs = []
            for lhs_item_data in self.lhs:
                lhs_item = lhs_item_data.to_dict()
                lhs.append(lhs_item)

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        rhs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rhs, Unset):
            rhs = []
            for rhs_item_data in self.rhs:
                rhs_item = rhs_item_data.to_dict()
                rhs.append(rhs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if lhs is not UNSET:
            field_dict["lhs"] = lhs
        if options is not UNSET:
            field_dict["options"] = options
        if rhs is not UNSET:
            field_dict["rhs"] = rhs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.client_info import ClientInfo
        from ..models.combine_acl_options import CombineAclOptions

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        lhs = []
        _lhs = d.pop("lhs", UNSET)
        for lhs_item_data in _lhs or []:
            lhs_item = AclItem.from_dict(lhs_item_data)

            lhs.append(lhs_item)

        _options = d.pop("options", UNSET)
        options: Union[Unset, CombineAclOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = CombineAclOptions.from_dict(_options)

        rhs = []
        _rhs = d.pop("rhs", UNSET)
        for rhs_item_data in _rhs or []:
            rhs_item = AclItem.from_dict(rhs_item_data)

            rhs.append(rhs_item)

        b_request_ix_service_port_if_combine_acl = cls(
            ci=ci,
            lhs=lhs,
            options=options,
            rhs=rhs,
        )

        b_request_ix_service_port_if_combine_acl.additional_properties = d
        return b_request_ix_service_port_if_combine_acl

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
