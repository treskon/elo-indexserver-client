from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_ import Any
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFExecuteRegisteredFunction")


@_attrs_define
class BRequestIXServicePortIFExecuteRegisteredFunction:
    """
    Attributes:
        function_name (Union[Unset, str]):
        param (Union[Unset, Any]): This class is a container for one value of a serializable type.
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

    function_name: Union[Unset, str] = UNSET
    param: Union[Unset, "Any"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_ import Any

        function_name = self.function_name

        param: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.param, Unset):
            param = self.param.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if param is not UNSET:
            field_dict["param"] = param
        if ci is not UNSET:
            field_dict["ci"] = ci

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_ import Any
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        function_name = d.pop("functionName", UNSET)

        _param = d.pop("param", UNSET)
        param: Union[Unset, Any]
        if isinstance(_param, Unset):
            param = UNSET
        else:
            param = Any.from_dict(_param)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        b_request_ix_service_port_if_execute_registered_function = cls(
            function_name=function_name,
            param=param,
            ci=ci,
        )

        b_request_ix_service_port_if_execute_registered_function.additional_properties = d
        return b_request_ix_service_port_if_execute_registered_function

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
