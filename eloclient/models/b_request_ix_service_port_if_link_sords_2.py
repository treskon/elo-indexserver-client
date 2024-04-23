from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.link_sord_info import LinkSordInfo
    from ..models.link_sord_z import LinkSordZ


T = TypeVar("T", bound="BRequestIXServicePortIFLinkSords2")


@_attrs_define
class BRequestIXServicePortIFLinkSords2:
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
        link_sord_z (Union[Unset, LinkSordZ]): This class encapsulates the constants of LinkSordC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        to_ids (Union[Unset, List[str]]):
        from_id (Union[Unset, str]):
        link_sord_info (Union[Unset, LinkSordInfo]): Additional parameters for function {@link
            IXServicePortIF#linkSords2}
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    link_sord_z: Union[Unset, "LinkSordZ"] = UNSET
    to_ids: Union[Unset, List[str]] = UNSET
    from_id: Union[Unset, str] = UNSET
    link_sord_info: Union[Unset, "LinkSordInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        link_sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_sord_z, Unset):
            link_sord_z = self.link_sord_z.to_dict()

        to_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.to_ids, Unset):
            to_ids = self.to_ids

        from_id = self.from_id

        link_sord_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_sord_info, Unset):
            link_sord_info = self.link_sord_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if link_sord_z is not UNSET:
            field_dict["linkSordZ"] = link_sord_z
        if to_ids is not UNSET:
            field_dict["toIds"] = to_ids
        if from_id is not UNSET:
            field_dict["fromId"] = from_id
        if link_sord_info is not UNSET:
            field_dict["linkSordInfo"] = link_sord_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.link_sord_info import LinkSordInfo
        from ..models.link_sord_z import LinkSordZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _link_sord_z = d.pop("linkSordZ", UNSET)
        link_sord_z: Union[Unset, LinkSordZ]
        if isinstance(_link_sord_z, Unset):
            link_sord_z = UNSET
        else:
            link_sord_z = LinkSordZ.from_dict(_link_sord_z)

        to_ids = cast(List[str], d.pop("toIds", UNSET))

        from_id = d.pop("fromId", UNSET)

        _link_sord_info = d.pop("linkSordInfo", UNSET)
        link_sord_info: Union[Unset, LinkSordInfo]
        if isinstance(_link_sord_info, Unset):
            link_sord_info = UNSET
        else:
            link_sord_info = LinkSordInfo.from_dict(_link_sord_info)

        b_request_ix_service_port_if_link_sords_2 = cls(
            ci=ci,
            link_sord_z=link_sord_z,
            to_ids=to_ids,
            from_id=from_id,
            link_sord_info=link_sord_info,
        )

        b_request_ix_service_port_if_link_sords_2.additional_properties = d
        return b_request_ix_service_port_if_link_sords_2

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
