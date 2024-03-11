from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.execute_script_params import ExecuteScriptParams


T = TypeVar("T", bound="BRequestIXServicePortIFExecuteScript")


@_attrs_define
class BRequestIXServicePortIFExecuteScript:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        params (Union[Unset, ExecuteScriptParams]): This class is used to specify which script has to be executed in
            function executeScript.
            The script has to be an ELO
             Windows CLIENT OLE-Automation script.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    params: Union[Unset, "ExecuteScriptParams"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.execute_script_params import ExecuteScriptParams

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ExecuteScriptParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ExecuteScriptParams.from_dict(_params)

        b_request_ix_service_port_if_execute_script = cls(
            ci=ci,
            params=params,
        )

        b_request_ix_service_port_if_execute_script.additional_properties = d
        return b_request_ix_service_port_if_execute_script

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
