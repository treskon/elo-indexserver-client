from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.delete_config_info import DeleteConfigInfo


T = TypeVar("T", bound="BRequestConfigServiceDeleteConfiguration2")


@_attrs_define
class BRequestConfigServiceDeleteConfiguration2:
    """
    Attributes:
        delete_info (Union[Unset, DeleteConfigInfo]): Describe what to delete in
            {@link ConfigService#deleteConfiguration2(de.elo.ix.client.ClientInfo, DeleteConfigInfo)}.
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

    delete_info: Union[Unset, "DeleteConfigInfo"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delete_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.delete_info, Unset):
            delete_info = self.delete_info.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_info is not UNSET:
            field_dict["deleteInfo"] = delete_info
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.delete_config_info import DeleteConfigInfo

        d = src_dict.copy()
        _delete_info = d.pop("deleteInfo", UNSET)
        delete_info: Union[Unset, DeleteConfigInfo]
        if isinstance(_delete_info, Unset):
            delete_info = UNSET
        else:
            delete_info = DeleteConfigInfo.from_dict(_delete_info)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_config_service_delete_configuration_2 = cls(
            delete_info=delete_info,
            ci=ci,
        )

        b_request_config_service_delete_configuration_2.additional_properties = d
        return b_request_config_service_delete_configuration_2

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
