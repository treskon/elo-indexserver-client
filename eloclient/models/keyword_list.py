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
        id (Union[Unset, str]): ID
        guid (Union[Unset, str]): GUID
        t_stamp (Union[Unset, str]): Last modified, ISO - UTC Read-only.
        deleted (Union[Unset, bool]): RESERVED
        user_id (Union[Unset, int]): ID of the user that has written the keyword list at last. Read-only.
        user_name (Union[Unset, str]): Name of the user that has written the keyword list at last. Read-only.
        children (Union[Unset, List['Keyword']]):
        lock_id (Union[Unset, int]): ID of the user who holds a lock on the keyword list.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        package_name (Union[Unset, str]): Package name of KeywordList
    """

    id: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    user_id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    children: Union[Unset, List["Keyword"]] = UNSET
    lock_id: Union[Unset, int] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        guid = self.guid
        t_stamp = self.t_stamp
        deleted = self.deleted
        user_id = self.user_id
        user_name = self.user_name
        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()

                children.append(children_item)

        lock_id = self.lock_id
        t_stamp_sync = self.t_stamp_sync
        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if children is not UNSET:
            field_dict["children"] = children
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword import Keyword

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        guid = d.pop("guid", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        deleted = d.pop("deleted", UNSET)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = Keyword.from_dict(children_item_data)

            children.append(children_item)

        lock_id = d.pop("lockId", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        package_name = d.pop("packageName", UNSET)

        keyword_list = cls(
            id=id,
            guid=guid,
            t_stamp=t_stamp,
            deleted=deleted,
            user_id=user_id,
            user_name=user_name,
            children=children,
            lock_id=lock_id,
            t_stamp_sync=t_stamp_sync,
            package_name=package_name,
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
