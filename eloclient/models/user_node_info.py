from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_time_limit import WFTimeLimit


T = TypeVar("T", bound="UserNodeInfo")


@_attrs_define
class UserNodeInfo:
    """This class contains the information of a user node using to create a AdHocWorkflow.
    This class is
     used by the method IXServicePortIF.startAdHocWorkFlow2.

        Attributes:
            node_name (Union[Unset, str]):
            time_limit (Union[Unset, int]): The time-limit to process the node. This member is only valid for person nodes.
            time_limit_iso (Union[Unset, str]): After this date the node exceeds the time-limit for processing.
                This member is only valid for
                 person nodes.
            time_limit_escalations (Union[Unset, List['WFTimeLimit']]):
            flags (Union[Unset, int]): Control flags for the node, a combination of WFNode.C.FLAG_* constants.
            user_id (Union[Unset, str]):
    """

    node_name: Union[Unset, str] = UNSET
    time_limit: Union[Unset, int] = UNSET
    time_limit_iso: Union[Unset, str] = UNSET
    time_limit_escalations: Union[Unset, List["WFTimeLimit"]] = UNSET
    flags: Union[Unset, int] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_name = self.node_name

        time_limit = self.time_limit

        time_limit_iso = self.time_limit_iso

        time_limit_escalations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.time_limit_escalations, Unset):
            time_limit_escalations = []
            for time_limit_escalations_item_data in self.time_limit_escalations:
                time_limit_escalations_item = time_limit_escalations_item_data.to_dict()
                time_limit_escalations.append(time_limit_escalations_item)

        flags = self.flags

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if time_limit is not UNSET:
            field_dict["timeLimit"] = time_limit
        if time_limit_iso is not UNSET:
            field_dict["timeLimitIso"] = time_limit_iso
        if time_limit_escalations is not UNSET:
            field_dict["timeLimitEscalations"] = time_limit_escalations
        if flags is not UNSET:
            field_dict["flags"] = flags
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_time_limit import WFTimeLimit

        d = src_dict.copy()
        node_name = d.pop("nodeName", UNSET)

        time_limit = d.pop("timeLimit", UNSET)

        time_limit_iso = d.pop("timeLimitIso", UNSET)

        time_limit_escalations = []
        _time_limit_escalations = d.pop("timeLimitEscalations", UNSET)
        for time_limit_escalations_item_data in _time_limit_escalations or []:
            time_limit_escalations_item = WFTimeLimit.from_dict(time_limit_escalations_item_data)

            time_limit_escalations.append(time_limit_escalations_item)

        flags = d.pop("flags", UNSET)

        user_id = d.pop("userId", UNSET)

        user_node_info = cls(
            node_name=node_name,
            time_limit=time_limit,
            time_limit_iso=time_limit_iso,
            time_limit_escalations=time_limit_escalations,
            flags=flags,
            user_id=user_id,
        )

        user_node_info.additional_properties = d
        return user_node_info

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
