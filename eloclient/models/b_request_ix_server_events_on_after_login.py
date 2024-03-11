from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.login_script_options import LoginScriptOptions


T = TypeVar("T", bound="BRequestIXServerEventsOnAfterLogin")


@_attrs_define
class BRequestIXServerEventsOnAfterLogin:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        user_name (Union[Unset, str]):
        opts (Union[Unset, LoginScriptOptions]): Options for function {@link
            IXServerEvents#onBeforeLogin(IXServerEventsContext, String, LoginScriptOptions)}
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    user_name: Union[Unset, str] = UNSET
    opts: Union[Unset, "LoginScriptOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        user_name = self.user_name
        opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opts, Unset):
            opts = self.opts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if opts is not UNSET:
            field_dict["opts"] = opts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.login_script_options import LoginScriptOptions

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        user_name = d.pop("userName", UNSET)

        _opts = d.pop("opts", UNSET)
        opts: Union[Unset, LoginScriptOptions]
        if isinstance(_opts, Unset):
            opts = UNSET
        else:
            opts = LoginScriptOptions.from_dict(_opts)

        b_request_ix_server_events_on_after_login = cls(
            ec=ec,
            user_name=user_name,
            opts=opts,
        )

        b_request_ix_server_events_on_after_login.additional_properties = d
        return b_request_ix_server_events_on_after_login

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
