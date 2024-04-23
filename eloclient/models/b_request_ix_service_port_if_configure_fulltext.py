from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.fulltext_config import FulltextConfig


T = TypeVar("T", bound="BRequestIXServicePortIFConfigureFulltext")


@_attrs_define
class BRequestIXServicePortIFConfigureFulltext:
    """
    Attributes:
        opts (Union[Unset, FulltextConfig]): This class provides information about the configuration of the fulltext
            database.
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
        user_id (Union[Unset, str]):
    """

    opts: Union[Unset, "FulltextConfig"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opts, Unset):
            opts = self.opts.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opts is not UNSET:
            field_dict["opts"] = opts
        if ci is not UNSET:
            field_dict["ci"] = ci
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.fulltext_config import FulltextConfig

        d = src_dict.copy()
        _opts = d.pop("opts", UNSET)
        opts: Union[Unset, FulltextConfig]
        if isinstance(_opts, Unset):
            opts = UNSET
        else:
            opts = FulltextConfig.from_dict(_opts)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        user_id = d.pop("userId", UNSET)

        b_request_ix_service_port_if_configure_fulltext = cls(
            opts=opts,
            ci=ci,
            user_id=user_id,
        )

        b_request_ix_service_port_if_configure_fulltext.additional_properties = d
        return b_request_ix_service_port_if_configure_fulltext

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
