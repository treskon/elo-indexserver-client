from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.note_image import NoteImage
    from ..models.note_text import NoteText


T = TypeVar("T", bound="NoteTemplate")


@_attrs_define
class NoteTemplate:
    """This class describes the template information for a stamp.

    Attributes:
        note_text (Union[Unset, NoteText]): This class conatins additional information for textual notes.
            NoteText objects can be used in
             NoteTemplate and Note objects.
        note_image (Union[Unset, NoteImage]): This class contains additional information for image stamps.
        acl_items (Union[Unset, List['AclItem']]):
        name (Union[Unset, str]): Stamp name.
        id (Union[Unset, int]): Stamp ID.
        acl (Union[Unset, str]): ACL. Member aclItems has preceedence on checkin.
        user_id (Union[Unset, str]): User ID or name. NoteTemplate objects can be defined for all users and for a
            specific user.
    """

    note_text: Union[Unset, "NoteText"] = UNSET
    note_image: Union[Unset, "NoteImage"] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    acl: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        note_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_text, Unset):
            note_text = self.note_text.to_dict()

        note_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_image, Unset):
            note_image = self.note_image.to_dict()

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        name = self.name

        id = self.id

        acl = self.acl

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if note_text is not UNSET:
            field_dict["noteText"] = note_text
        if note_image is not UNSET:
            field_dict["noteImage"] = note_image
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if acl is not UNSET:
            field_dict["acl"] = acl
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.note_image import NoteImage
        from ..models.note_text import NoteText

        d = src_dict.copy()
        _note_text = d.pop("noteText", UNSET)
        note_text: Union[Unset, NoteText]
        if isinstance(_note_text, Unset):
            note_text = UNSET
        else:
            note_text = NoteText.from_dict(_note_text)

        _note_image = d.pop("noteImage", UNSET)
        note_image: Union[Unset, NoteImage]
        if isinstance(_note_image, Unset):
            note_image = UNSET
        else:
            note_image = NoteImage.from_dict(_note_image)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        acl = d.pop("acl", UNSET)

        user_id = d.pop("userId", UNSET)

        note_template = cls(
            note_text=note_text,
            note_image=note_image,
            acl_items=acl_items,
            name=name,
            id=id,
            acl=acl,
            user_id=user_id,
        )

        note_template.additional_properties = d
        return note_template

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
