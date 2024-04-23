from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.link_sord_z import LinkSordZ


T = TypeVar("T", bound="BRequestIXServicePortIFUnlinkSords")


@_attrs_define
class BRequestIXServicePortIFUnlinkSords:
    """
    Attributes:
        link_z (Union[Unset, LinkSordZ]): This class encapsulates the constants of LinkSordC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
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
        to_ids (Union[Unset, List[str]]):
        from_id (Union[Unset, str]):
    """

    link_z: Union[Unset, "LinkSordZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    to_ids: Union[Unset, List[str]] = UNSET
    from_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_z, Unset):
            link_z = self.link_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        to_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.to_ids, Unset):
            to_ids = self.to_ids

        from_id = self.from_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_z is not UNSET:
            field_dict["linkZ"] = link_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if to_ids is not UNSET:
            field_dict["toIds"] = to_ids
        if from_id is not UNSET:
            field_dict["fromId"] = from_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.link_sord_z import LinkSordZ

        d = src_dict.copy()
        _link_z = d.pop("linkZ", UNSET)
        link_z: Union[Unset, LinkSordZ]
        if isinstance(_link_z, Unset):
            link_z = UNSET
        else:
            link_z = LinkSordZ.from_dict(_link_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        to_ids = cast(List[str], d.pop("toIds", UNSET))

        from_id = d.pop("fromId", UNSET)

        b_request_ix_service_port_if_unlink_sords = cls(
            link_z=link_z,
            ci=ci,
            to_ids=to_ids,
            from_id=from_id,
        )

        b_request_ix_service_port_if_unlink_sords.additional_properties = d
        return b_request_ix_service_port_if_unlink_sords

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
