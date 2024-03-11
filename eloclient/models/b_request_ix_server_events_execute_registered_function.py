from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_ import Any
    from ..models.ix_server_events_context import IXServerEventsContext


T = TypeVar("T", bound="BRequestIXServerEventsExecuteRegisteredFunction")


@_attrs_define
class BRequestIXServerEventsExecuteRegisteredFunction:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        function_name (Union[Unset, str]):
        any_ (Union[Unset, Any]): This class is a container for one value of a serializable type.
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    function_name: Union[Unset, str] = UNSET
    any_: Union[Unset, "Any"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_ import Any

        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        function_name = self.function_name
        any_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.any_, Unset):
            any_ = self.any_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if any_ is not UNSET:
            field_dict["any"] = any_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_ import Any
        from ..models.ix_server_events_context import IXServerEventsContext

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        function_name = d.pop("functionName", UNSET)

        _any_ = d.pop("any", UNSET)
        any_: Union[Unset, Any]
        if isinstance(_any_, Unset):
            any_ = UNSET
        else:
            any_ = Any.from_dict(_any_)

        b_request_ix_server_events_execute_registered_function = cls(
            ec=ec,
            function_name=function_name,
            any_=any_,
        )

        b_request_ix_server_events_execute_registered_function.additional_properties = d
        return b_request_ix_server_events_execute_registered_function

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
