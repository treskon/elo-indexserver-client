from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.package_export_info import PackageExportInfo


T = TypeVar("T", bound="BRequestPackageServiceExportPackageContent")


@_attrs_define
class BRequestPackageServiceExportPackageContent:
    """
    Attributes:
        export_info (Union[Unset, PackageExportInfo]): Describe export criteria for
            {@link PackageService#exportPackageContent(ClientInfo ci, PackageExportInfo exportInfo)}.
             EIX-1895
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
    """

    export_info: Union[Unset, "PackageExportInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        export_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.export_info, Unset):
            export_info = self.export_info.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_info is not UNSET:
            field_dict["exportInfo"] = export_info
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.package_export_info import PackageExportInfo

        d = src_dict.copy()
        _export_info = d.pop("exportInfo", UNSET)
        export_info: Union[Unset, PackageExportInfo]
        if isinstance(_export_info, Unset):
            export_info = UNSET
        else:
            export_info = PackageExportInfo.from_dict(_export_info)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_package_service_export_package_content = cls(
            export_info=export_info,
            ci=ci,
        )

        b_request_package_service_export_package_content.additional_properties = d
        return b_request_package_service_export_package_content

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
