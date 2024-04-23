from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFStartExport")


@_attrs_define
class BRequestIXServicePortIFStartExport:
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
        options (Union[Unset, str]):
        top_level_i_ds (Union[Unset, List[str]]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    options: Union[Unset, str] = UNSET
    top_level_i_ds: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        options = self.options

        top_level_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.top_level_i_ds, Unset):
            top_level_i_ds = self.top_level_i_ds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if options is not UNSET:
            field_dict["options"] = options
        if top_level_i_ds is not UNSET:
            field_dict["topLevelIDs"] = top_level_i_ds

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

        options = d.pop("options", UNSET)

        top_level_i_ds = cast(List[str], d.pop("topLevelIDs", UNSET))

        b_request_ix_service_port_if_start_export = cls(
            ci=ci,
            options=options,
            top_level_i_ds=top_level_i_ds,
        )

        b_request_ix_service_port_if_start_export.additional_properties = d
        return b_request_ix_service_port_if_start_export

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
