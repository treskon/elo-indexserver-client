from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.my_elo_info import MyELOInfo
    from ..models.my_elo_state import MyELOState


T = TypeVar("T", bound="BRequestMyELOServiceReadContent")


@_attrs_define
class BRequestMyELOServiceReadContent:
    """
    Attributes:
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
        state (Union[Unset, MyELOState]):
        info (Union[Unset, MyELOInfo]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    state: Union[Unset, "MyELOState"] = UNSET
    info: Union[Unset, "MyELOInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if state is not UNSET:
            field_dict["state"] = state
        if info is not UNSET:
            field_dict["info"] = info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.my_elo_info import MyELOInfo
        from ..models.my_elo_state import MyELOState

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _state = d.pop("state", UNSET)
        state: Union[Unset, MyELOState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = MyELOState.from_dict(_state)

        _info = d.pop("info", UNSET)
        info: Union[Unset, MyELOInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = MyELOInfo.from_dict(_info)

        b_request_my_elo_service_read_content = cls(
            ci=ci,
            state=state,
            info=info,
        )

        b_request_my_elo_service_read_content.additional_properties = d
        return b_request_my_elo_service_read_content

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
