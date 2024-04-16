from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="BRequestIXServicePortIFFindNextSords")


@_attrs_define
class BRequestIXServicePortIFFindNextSords:
    """
    Attributes:
        search_id (Union[Unset, str]):
        sord_z (Union[Unset, SordZ]): <p>
            This class encapsulates the constants of <code>SordC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        max_ (Union[Unset, int]):
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
        idx (Union[Unset, int]):
    """

    search_id: Union[Unset, str] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    idx: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_id = self.search_id

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        idx = self.idx

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if idx is not UNSET:
            field_dict["idx"] = idx

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        search_id = d.pop("searchId", UNSET)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        idx = d.pop("idx", UNSET)

        b_request_ix_service_port_if_find_next_sords = cls(
            search_id=search_id,
            sord_z=sord_z,
            max_=max_,
            ci=ci,
            idx=idx,
        )

        b_request_ix_service_port_if_find_next_sords.additional_properties = d
        return b_request_ix_service_port_if_find_next_sords

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
