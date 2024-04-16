from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginScriptOptionsC")


@_attrs_define
class LoginScriptOptionsC:
    """Constants for {@link LoginScriptOptions}.

    Attributes:
        client_name_integration (Union[Unset, str]): Integration client.
        client_name_limited_web_client_d (Union[Unset, str]): Web Client with limited access for special customer
            project.
        client_name_windows_client (Union[Unset, str]): Windows Client
        client_name_unknown (Union[Unset, str]): Constant for the name of unknown type.
        client_name_eloapp (Union[Unset, str]): Constant for the name ELO applications.
        client_name_dms_desktop (Union[Unset, str]): DMS Desktop
        client_name_mobile_client (Union[Unset, str]): Mobile client (Android, iOS)
        client_name_desktop_plus (Union[Unset, str]): Desktop Plus.
        client_name_partnerapp (Union[Unset, str]): Constant for the name of partner applications.
        client_name_task (Union[Unset, str]): Task client (a.k.a. Workflow Client).
        client_name_webclient (Union[Unset, str]): Constant for the name of the Web and Mobile Client.
        client_name_desktop_light (Union[Unset, str]): Desktop Plus.
        client_name_fullclient (Union[Unset, str]): Constant for the name of the Windows/Java Client.
        client_name_workflow_sap (Union[Unset, str]): Workflow Client für SAP ECM.
    """

    client_name_integration: Union[Unset, str] = UNSET
    client_name_limited_web_client_d: Union[Unset, str] = UNSET
    client_name_windows_client: Union[Unset, str] = UNSET
    client_name_unknown: Union[Unset, str] = UNSET
    client_name_eloapp: Union[Unset, str] = UNSET
    client_name_dms_desktop: Union[Unset, str] = UNSET
    client_name_mobile_client: Union[Unset, str] = UNSET
    client_name_desktop_plus: Union[Unset, str] = UNSET
    client_name_partnerapp: Union[Unset, str] = UNSET
    client_name_task: Union[Unset, str] = UNSET
    client_name_webclient: Union[Unset, str] = UNSET
    client_name_desktop_light: Union[Unset, str] = UNSET
    client_name_fullclient: Union[Unset, str] = UNSET
    client_name_workflow_sap: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_name_integration = self.client_name_integration

        client_name_limited_web_client_d = self.client_name_limited_web_client_d

        client_name_windows_client = self.client_name_windows_client

        client_name_unknown = self.client_name_unknown

        client_name_eloapp = self.client_name_eloapp

        client_name_dms_desktop = self.client_name_dms_desktop

        client_name_mobile_client = self.client_name_mobile_client

        client_name_desktop_plus = self.client_name_desktop_plus

        client_name_partnerapp = self.client_name_partnerapp

        client_name_task = self.client_name_task

        client_name_webclient = self.client_name_webclient

        client_name_desktop_light = self.client_name_desktop_light

        client_name_fullclient = self.client_name_fullclient

        client_name_workflow_sap = self.client_name_workflow_sap

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_name_integration is not UNSET:
            field_dict["CLIENT_NAME_INTEGRATION"] = client_name_integration
        if client_name_limited_web_client_d is not UNSET:
            field_dict["CLIENT_NAME_LIMITED_WEB_CLIENT_D"] = client_name_limited_web_client_d
        if client_name_windows_client is not UNSET:
            field_dict["CLIENT_NAME_WINDOWS_CLIENT"] = client_name_windows_client
        if client_name_unknown is not UNSET:
            field_dict["CLIENT_NAME_UNKNOWN"] = client_name_unknown
        if client_name_eloapp is not UNSET:
            field_dict["CLIENT_NAME_ELOAPP"] = client_name_eloapp
        if client_name_dms_desktop is not UNSET:
            field_dict["CLIENT_NAME_DMS_DESKTOP"] = client_name_dms_desktop
        if client_name_mobile_client is not UNSET:
            field_dict["CLIENT_NAME_MOBILE_CLIENT"] = client_name_mobile_client
        if client_name_desktop_plus is not UNSET:
            field_dict["CLIENT_NAME_DESKTOP_PLUS"] = client_name_desktop_plus
        if client_name_partnerapp is not UNSET:
            field_dict["CLIENT_NAME_PARTNERAPP"] = client_name_partnerapp
        if client_name_task is not UNSET:
            field_dict["CLIENT_NAME_TASK"] = client_name_task
        if client_name_webclient is not UNSET:
            field_dict["CLIENT_NAME_WEBCLIENT"] = client_name_webclient
        if client_name_desktop_light is not UNSET:
            field_dict["CLIENT_NAME_DESKTOP_LIGHT"] = client_name_desktop_light
        if client_name_fullclient is not UNSET:
            field_dict["CLIENT_NAME_FULLCLIENT"] = client_name_fullclient
        if client_name_workflow_sap is not UNSET:
            field_dict["CLIENT_NAME_WORKFLOW_SAP"] = client_name_workflow_sap

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_name_integration = d.pop("CLIENT_NAME_INTEGRATION", UNSET)

        client_name_limited_web_client_d = d.pop("CLIENT_NAME_LIMITED_WEB_CLIENT_D", UNSET)

        client_name_windows_client = d.pop("CLIENT_NAME_WINDOWS_CLIENT", UNSET)

        client_name_unknown = d.pop("CLIENT_NAME_UNKNOWN", UNSET)

        client_name_eloapp = d.pop("CLIENT_NAME_ELOAPP", UNSET)

        client_name_dms_desktop = d.pop("CLIENT_NAME_DMS_DESKTOP", UNSET)

        client_name_mobile_client = d.pop("CLIENT_NAME_MOBILE_CLIENT", UNSET)

        client_name_desktop_plus = d.pop("CLIENT_NAME_DESKTOP_PLUS", UNSET)

        client_name_partnerapp = d.pop("CLIENT_NAME_PARTNERAPP", UNSET)

        client_name_task = d.pop("CLIENT_NAME_TASK", UNSET)

        client_name_webclient = d.pop("CLIENT_NAME_WEBCLIENT", UNSET)

        client_name_desktop_light = d.pop("CLIENT_NAME_DESKTOP_LIGHT", UNSET)

        client_name_fullclient = d.pop("CLIENT_NAME_FULLCLIENT", UNSET)

        client_name_workflow_sap = d.pop("CLIENT_NAME_WORKFLOW_SAP", UNSET)

        login_script_options_c = cls(
            client_name_integration=client_name_integration,
            client_name_limited_web_client_d=client_name_limited_web_client_d,
            client_name_windows_client=client_name_windows_client,
            client_name_unknown=client_name_unknown,
            client_name_eloapp=client_name_eloapp,
            client_name_dms_desktop=client_name_dms_desktop,
            client_name_mobile_client=client_name_mobile_client,
            client_name_desktop_plus=client_name_desktop_plus,
            client_name_partnerapp=client_name_partnerapp,
            client_name_task=client_name_task,
            client_name_webclient=client_name_webclient,
            client_name_desktop_light=client_name_desktop_light,
            client_name_fullclient=client_name_fullclient,
            client_name_workflow_sap=client_name_workflow_sap,
        )

        login_script_options_c.additional_properties = d
        return login_script_options_c

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
