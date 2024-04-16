from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.keyword_z import KeywordZ
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutKeywords")


@_attrs_define
class BRequestIXServicePortIFCheckoutKeywords:
    """
    Attributes:
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
        kwids (Union[Unset, List[str]]):
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        keyword_z (Union[Unset, KeywordZ]): This class encapsulates the constants of KeywordC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    kwids: Union[Unset, List[str]] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    keyword_z: Union[Unset, "KeywordZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        kwids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.kwids, Unset):
            kwids = self.kwids

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        keyword_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword_z, Unset):
            keyword_z = self.keyword_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if kwids is not UNSET:
            field_dict["kwids"] = kwids
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if keyword_z is not UNSET:
            field_dict["keywordZ"] = keyword_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.keyword_z import KeywordZ
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        kwids = cast(List[str], d.pop("kwids", UNSET))

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        _keyword_z = d.pop("keywordZ", UNSET)
        keyword_z: Union[Unset, KeywordZ]
        if isinstance(_keyword_z, Unset):
            keyword_z = UNSET
        else:
            keyword_z = KeywordZ.from_dict(_keyword_z)

        b_request_ix_service_port_if_checkout_keywords = cls(
            max_=max_,
            ci=ci,
            kwids=kwids,
            lock_z=lock_z,
            keyword_z=keyword_z,
        )

        b_request_ix_service_port_if_checkout_keywords.additional_properties = d
        return b_request_ix_service_port_if_checkout_keywords

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
