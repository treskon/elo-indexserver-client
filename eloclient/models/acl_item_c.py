from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="AclItemC")


@_attrs_define
class AclItemC:
    """<p>
    Types of ACL items.
     </p>

        Attributes:
            type_user (Union[Unset, int]): ACL item for user.
            type_owner (Union[Unset, int]): ACL item to set rights for the owner.
            type_group (Union[Unset, int]): ACL item for group.
            type_key (Union[Unset, int]): ACL item for key.
            acl_everyone_raw (Union[Unset, str]): String representation of an ACL entry for group "Everyone" with full
                access.
            type_participants (Union[Unset, int]): ACL item to set rights for the workflow participants. Only used for
                workflows.
            acl_everyone (Union[Unset, List['AclItem']]):
            type_inherit (Union[Unset, int]): ACL item to inherit rights.
    """

    type_user: Union[Unset, int] = UNSET
    type_owner: Union[Unset, int] = UNSET
    type_group: Union[Unset, int] = UNSET
    type_key: Union[Unset, int] = UNSET
    acl_everyone_raw: Union[Unset, str] = UNSET
    type_participants: Union[Unset, int] = UNSET
    acl_everyone: Union[Unset, List["AclItem"]] = UNSET
    type_inherit: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_user = self.type_user

        type_owner = self.type_owner

        type_group = self.type_group

        type_key = self.type_key

        acl_everyone_raw = self.acl_everyone_raw

        type_participants = self.type_participants

        acl_everyone: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_everyone, Unset):
            acl_everyone = []
            for acl_everyone_item_data in self.acl_everyone:
                acl_everyone_item = acl_everyone_item_data.to_dict()
                acl_everyone.append(acl_everyone_item)

        type_inherit = self.type_inherit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_user is not UNSET:
            field_dict["TYPE_USER"] = type_user
        if type_owner is not UNSET:
            field_dict["TYPE_OWNER"] = type_owner
        if type_group is not UNSET:
            field_dict["TYPE_GROUP"] = type_group
        if type_key is not UNSET:
            field_dict["TYPE_KEY"] = type_key
        if acl_everyone_raw is not UNSET:
            field_dict["ACL_EVERYONE_RAW"] = acl_everyone_raw
        if type_participants is not UNSET:
            field_dict["TYPE_PARTICIPANTS"] = type_participants
        if acl_everyone is not UNSET:
            field_dict["ACL_EVERYONE"] = acl_everyone
        if type_inherit is not UNSET:
            field_dict["TYPE_INHERIT"] = type_inherit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        type_user = d.pop("TYPE_USER", UNSET)

        type_owner = d.pop("TYPE_OWNER", UNSET)

        type_group = d.pop("TYPE_GROUP", UNSET)

        type_key = d.pop("TYPE_KEY", UNSET)

        acl_everyone_raw = d.pop("ACL_EVERYONE_RAW", UNSET)

        type_participants = d.pop("TYPE_PARTICIPANTS", UNSET)

        acl_everyone = []
        _acl_everyone = d.pop("ACL_EVERYONE", UNSET)
        for acl_everyone_item_data in _acl_everyone or []:
            acl_everyone_item = AclItem.from_dict(acl_everyone_item_data)

            acl_everyone.append(acl_everyone_item)

        type_inherit = d.pop("TYPE_INHERIT", UNSET)

        acl_item_c = cls(
            type_user=type_user,
            type_owner=type_owner,
            type_group=type_group,
            type_key=type_key,
            acl_everyone_raw=acl_everyone_raw,
            type_participants=type_participants,
            acl_everyone=acl_everyone,
            type_inherit=type_inherit,
        )

        acl_item_c.additional_properties = d
        return acl_item_c

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
