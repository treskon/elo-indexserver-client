from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString


T = TypeVar("T", bound="SessionInfo")


@_attrs_define
class SessionInfo:
    """<p>
    Provides details of the current session with the Index Server
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            client_computer (Union[Unset, str]): The client computer connected with the Index Server.
            user_id (Union[Unset, int]): The id of the user used for the connection.
            valid_seconds (Union[Unset, int]): The length of time the connection is valid for.
            ticket (Union[Unset, str]): The ticket of this session within the Index Server.
            user_name (Union[Unset, str]): The name of the user used for the connection.
            login_name (Union[Unset, str]): The name of the user who initialized the runAs connection
            best_before (Union[Unset, str]): The time stamp of the session best before date.
            app_name (Union[Unset, str]): The name of the client's application connected with the Index Server.
            app_version (Union[Unset, str]): The version of the client's application connected with the Index Server.
            app_type (Union[Unset, str]): The type of the client's application connected with the Index Server.
            run_as (Union[Unset, str]): Session is constrained to this account
            session_options (Union[Unset, MapToString]):
    """

    client_computer: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    valid_seconds: Union[Unset, int] = UNSET
    ticket: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    login_name: Union[Unset, str] = UNSET
    best_before: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    app_version: Union[Unset, str] = UNSET
    app_type: Union[Unset, str] = UNSET
    run_as: Union[Unset, str] = UNSET
    session_options: Union[Unset, "MapToString"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_computer = self.client_computer
        user_id = self.user_id
        valid_seconds = self.valid_seconds
        ticket = self.ticket
        user_name = self.user_name
        login_name = self.login_name
        best_before = self.best_before
        app_name = self.app_name
        app_version = self.app_version
        app_type = self.app_type
        run_as = self.run_as
        session_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_options, Unset):
            session_options = self.session_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_computer is not UNSET:
            field_dict["clientComputer"] = client_computer
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if valid_seconds is not UNSET:
            field_dict["validSeconds"] = valid_seconds
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if login_name is not UNSET:
            field_dict["loginName"] = login_name
        if best_before is not UNSET:
            field_dict["bestBefore"] = best_before
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if app_type is not UNSET:
            field_dict["appType"] = app_type
        if run_as is not UNSET:
            field_dict["runAs"] = run_as
        if session_options is not UNSET:
            field_dict["sessionOptions"] = session_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        client_computer = d.pop("clientComputer", UNSET)

        user_id = d.pop("userId", UNSET)

        valid_seconds = d.pop("validSeconds", UNSET)

        ticket = d.pop("ticket", UNSET)

        user_name = d.pop("userName", UNSET)

        login_name = d.pop("loginName", UNSET)

        best_before = d.pop("bestBefore", UNSET)

        app_name = d.pop("appName", UNSET)

        app_version = d.pop("appVersion", UNSET)

        app_type = d.pop("appType", UNSET)

        run_as = d.pop("runAs", UNSET)

        _session_options = d.pop("sessionOptions", UNSET)
        session_options: Union[Unset, MapToString]
        if isinstance(_session_options, Unset):
            session_options = UNSET
        else:
            session_options = MapToString.from_dict(_session_options)

        session_info = cls(
            client_computer=client_computer,
            user_id=user_id,
            valid_seconds=valid_seconds,
            ticket=ticket,
            user_name=user_name,
            login_name=login_name,
            best_before=best_before,
            app_name=app_name,
            app_version=app_version,
            app_type=app_type,
            run_as=run_as,
            session_options=session_options,
        )

        session_info.additional_properties = d
        return session_info

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
