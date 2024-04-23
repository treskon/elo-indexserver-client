from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFStartImport")


@_attrs_define
class BRequestIXServicePortIFStartImport:
    """
    Attributes:
        guid_method (Union[Unset, int]):
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
        filing_path (Union[Unset, str]):
        options (Union[Unset, str]):
    """

    guid_method: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    filing_path: Union[Unset, str] = UNSET
    options: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid_method = self.guid_method

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        filing_path = self.filing_path

        options = self.options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid_method is not UNSET:
            field_dict["guidMethod"] = guid_method
        if ci is not UNSET:
            field_dict["ci"] = ci
        if filing_path is not UNSET:
            field_dict["filingPath"] = filing_path
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        guid_method = d.pop("guidMethod", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        filing_path = d.pop("filingPath", UNSET)

        options = d.pop("options", UNSET)

        b_request_ix_service_port_if_start_import = cls(
            guid_method=guid_method,
            ci=ci,
            filing_path=filing_path,
            options=options,
        )

        b_request_ix_service_port_if_start_import.additional_properties = d
        return b_request_ix_service_port_if_start_import

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
