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
            run_as (Union[Unset, str]): Session is constrained to this account
            session_options (Union[Unset, MapToString]):
            client_computer (Union[Unset, str]): The client computer connected with the Index Server.
            valid_seconds (Union[Unset, int]): The length of time the connection is valid for.
            app_version (Union[Unset, str]): The version of the client's application connected with the Index Server.
            ticket (Union[Unset, str]): The ticket of this session within the Index Server.
            best_before (Union[Unset, str]): The time stamp of the session best before date.
            app_name (Union[Unset, str]): The name of the client's application connected with the Index Server.
            app_type (Union[Unset, str]): The type of the client's application connected with the Index Server.
            login_name (Union[Unset, str]): The name of the user who initialized the runAs connection
            user_name (Union[Unset, str]): The name of the user used for the connection.
            user_id (Union[Unset, int]): The id of the user used for the connection.
    """

    run_as: Union[Unset, str] = UNSET
    session_options: Union[Unset, "MapToString"] = UNSET
    client_computer: Union[Unset, str] = UNSET
    valid_seconds: Union[Unset, int] = UNSET
    app_version: Union[Unset, str] = UNSET
    ticket: Union[Unset, str] = UNSET
    best_before: Union[Unset, str] = UNSET
    app_name: Union[Unset, str] = UNSET
    app_type: Union[Unset, str] = UNSET
    login_name: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_as = self.run_as

        session_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session_options, Unset):
            session_options = self.session_options.to_dict()

        client_computer = self.client_computer

        valid_seconds = self.valid_seconds

        app_version = self.app_version

        ticket = self.ticket

        best_before = self.best_before

        app_name = self.app_name

        app_type = self.app_type

        login_name = self.login_name

        user_name = self.user_name

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if run_as is not UNSET:
            field_dict["runAs"] = run_as
        if session_options is not UNSET:
            field_dict["sessionOptions"] = session_options
        if client_computer is not UNSET:
            field_dict["clientComputer"] = client_computer
        if valid_seconds is not UNSET:
            field_dict["validSeconds"] = valid_seconds
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if best_before is not UNSET:
            field_dict["bestBefore"] = best_before
        if app_name is not UNSET:
            field_dict["appName"] = app_name
        if app_type is not UNSET:
            field_dict["appType"] = app_type
        if login_name is not UNSET:
            field_dict["loginName"] = login_name
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        run_as = d.pop("runAs", UNSET)

        _session_options = d.pop("sessionOptions", UNSET)
        session_options: Union[Unset, MapToString]
        if isinstance(_session_options, Unset):
            session_options = UNSET
        else:
            session_options = MapToString.from_dict(_session_options)

        client_computer = d.pop("clientComputer", UNSET)

        valid_seconds = d.pop("validSeconds", UNSET)

        app_version = d.pop("appVersion", UNSET)

        ticket = d.pop("ticket", UNSET)

        best_before = d.pop("bestBefore", UNSET)

        app_name = d.pop("appName", UNSET)

        app_type = d.pop("appType", UNSET)

        login_name = d.pop("loginName", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        session_info = cls(
            run_as=run_as,
            session_options=session_options,
            client_computer=client_computer,
            valid_seconds=valid_seconds,
            app_version=app_version,
            ticket=ticket,
            best_before=best_before,
            app_name=app_name,
            app_type=app_type,
            login_name=login_name,
            user_name=user_name,
            user_id=user_id,
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
