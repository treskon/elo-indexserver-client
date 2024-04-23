from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindActivityInfo")


@_attrs_define
class FindActivityInfo:
    """This class specifies constraints for the API function
    {@link IXServicePortIF#findFirstActivities(ClientInfo, FindActivityInfo, int, ActivityZ)}.
     <p>
     By default, the members of this class are combined by AND. If {@link #senderOrReceiver} is set,
     senderId and receiverId are combined by OR.
     </p>
     <p>
     If neither senderId nor receiverId is set, the function findFirstActivities collects all
     activities that can be read by the current session.
     </p>

        Attributes:
            incl_deputy (Union[Unset, bool]): Search for the activities of the deputized users too.
            sender_id (Union[Unset, str]): Find activities created by this user. Can be set to a user ID, user GUID or user
                name.
                Optional.
            receiver_id (Union[Unset, str]): Find activities created for this receiver. Can be set to a user ID, user GUID
                or user name.
                Optional.
            incl_group (Union[Unset, bool]): Search for all groups of sender and receiver too.
            obj_id (Union[Unset, str]): Find by object ID. Find activities assigned to this object. Optional.
            sender_or_receiver (Union[Unset, bool]): Search for sender or receiver. Combine the senderId and receiverId by
                logical OR operation.
            incl_deleted (Union[Unset, bool]): Find activities for deleted folders and documents too.
    """

    incl_deputy: Union[Unset, bool] = UNSET
    sender_id: Union[Unset, str] = UNSET
    receiver_id: Union[Unset, str] = UNSET
    incl_group: Union[Unset, bool] = UNSET
    obj_id: Union[Unset, str] = UNSET
    sender_or_receiver: Union[Unset, bool] = UNSET
    incl_deleted: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incl_deputy = self.incl_deputy

        sender_id = self.sender_id

        receiver_id = self.receiver_id

        incl_group = self.incl_group

        obj_id = self.obj_id

        sender_or_receiver = self.sender_or_receiver

        incl_deleted = self.incl_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incl_deputy is not UNSET:
            field_dict["inclDeputy"] = incl_deputy
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if receiver_id is not UNSET:
            field_dict["receiverId"] = receiver_id
        if incl_group is not UNSET:
            field_dict["inclGroup"] = incl_group
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if sender_or_receiver is not UNSET:
            field_dict["senderOrReceiver"] = sender_or_receiver
        if incl_deleted is not UNSET:
            field_dict["inclDeleted"] = incl_deleted

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incl_deputy = d.pop("inclDeputy", UNSET)

        sender_id = d.pop("senderId", UNSET)

        receiver_id = d.pop("receiverId", UNSET)

        incl_group = d.pop("inclGroup", UNSET)

        obj_id = d.pop("objId", UNSET)

        sender_or_receiver = d.pop("senderOrReceiver", UNSET)

        incl_deleted = d.pop("inclDeleted", UNSET)

        find_activity_info = cls(
            incl_deputy=incl_deputy,
            sender_id=sender_id,
            receiver_id=receiver_id,
            incl_group=incl_group,
            obj_id=obj_id,
            sender_or_receiver=sender_or_receiver,
            incl_deleted=incl_deleted,
        )

        find_activity_info.additional_properties = d
        return find_activity_info

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
