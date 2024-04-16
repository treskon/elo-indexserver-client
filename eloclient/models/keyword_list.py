from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword import Keyword


T = TypeVar("T", bound="KeywordList")


@_attrs_define
class KeywordList:
    """This class provides general informations for a keyword list.

    Attributes:
        lock_id (Union[Unset, int]): ID of the user who holds a lock on the keyword list.
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link KeywordList#displayName}.
        deleted (Union[Unset, bool]): RESERVED
        children (Union[Unset, List['Keyword']]):
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        t_stamp (Union[Unset, str]): Last modified, ISO - UTC Read-only.
        display_name (Union[Unset, str]): The display name of the keyword. This value is displayed in the label before
            the edit field.
            It
             can be translated into reps. from the users language: set
             <code>SessionOptionsC.TRANSLATE_TERM</code>.
        guid (Union[Unset, str]): GUID
        id (Union[Unset, str]): ID
        package_name (Union[Unset, str]): Package name of KeywordList
        user_name (Union[Unset, str]): Name of the user that has written the keyword list at last. Read-only.
        user_id (Union[Unset, int]): ID of the user that has written the keyword list at last. Read-only.
    """

    lock_id: Union[Unset, int] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    children: Union[Unset, List["Keyword"]] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lock_id = self.lock_id

        name_translation_key = self.name_translation_key

        deleted = self.deleted

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        t_stamp_sync = self.t_stamp_sync

        t_stamp = self.t_stamp

        display_name = self.display_name

        guid = self.guid

        id = self.id

        package_name = self.package_name

        user_name = self.user_name

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if children is not UNSET:
            field_dict["children"] = children
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword import Keyword

        d = src_dict.copy()
        lock_id = d.pop("lockId", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        deleted = d.pop("deleted", UNSET)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = Keyword.from_dict(children_item_data)

            children.append(children_item)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        display_name = d.pop("displayName", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        package_name = d.pop("packageName", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        keyword_list = cls(
            lock_id=lock_id,
            name_translation_key=name_translation_key,
            deleted=deleted,
            children=children,
            t_stamp_sync=t_stamp_sync,
            t_stamp=t_stamp,
            display_name=display_name,
            guid=guid,
            id=id,
            package_name=package_name,
            user_name=user_name,
            user_id=user_id,
        )

        keyword_list.additional_properties = d
        return keyword_list

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
