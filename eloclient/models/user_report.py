from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_name import UserName


T = TypeVar("T", bound="UserReport")


@_attrs_define
class UserReport:
    """User report for AdminConsole.

    Attributes:
        user_names (Union[Unset, List['UserName']]):
        counter_total (Union[Unset, int]): Total count of all users.
        counter_user (Union[Unset, int]): Count of users.
        counter_group (Union[Unset, int]): Count of groups.
        counter_no_login (Union[Unset, int]): Count of users without login flag.
        subadmin_ids (Union[Unset, List[int]]):
        dms_desktop_user_ids (Union[Unset, List[int]]):
        option_group_ids (Union[Unset, List[int]]):
        child_ids (Union[Unset, List[int]]):
    """

    user_names: Union[Unset, List["UserName"]] = UNSET
    counter_total: Union[Unset, int] = UNSET
    counter_user: Union[Unset, int] = UNSET
    counter_group: Union[Unset, int] = UNSET
    counter_no_login: Union[Unset, int] = UNSET
    subadmin_ids: Union[Unset, List[int]] = UNSET
    dms_desktop_user_ids: Union[Unset, List[int]] = UNSET
    option_group_ids: Union[Unset, List[int]] = UNSET
    child_ids: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_names, Unset):
            user_names = []
            for componentsschemas_list_of_user_name_item_data in self.user_names:
                componentsschemas_list_of_user_name_item = componentsschemas_list_of_user_name_item_data.to_dict()

                user_names.append(componentsschemas_list_of_user_name_item)

        counter_total = self.counter_total
        counter_user = self.counter_user
        counter_group = self.counter_group
        counter_no_login = self.counter_no_login
        subadmin_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.subadmin_ids, Unset):
            subadmin_ids = self.subadmin_ids

        dms_desktop_user_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.dms_desktop_user_ids, Unset):
            dms_desktop_user_ids = self.dms_desktop_user_ids

        option_group_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.option_group_ids, Unset):
            option_group_ids = self.option_group_ids

        child_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.child_ids, Unset):
            child_ids = self.child_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_names is not UNSET:
            field_dict["userNames"] = user_names
        if counter_total is not UNSET:
            field_dict["counterTotal"] = counter_total
        if counter_user is not UNSET:
            field_dict["counterUser"] = counter_user
        if counter_group is not UNSET:
            field_dict["counterGroup"] = counter_group
        if counter_no_login is not UNSET:
            field_dict["counterNoLogin"] = counter_no_login
        if subadmin_ids is not UNSET:
            field_dict["subadminIds"] = subadmin_ids
        if dms_desktop_user_ids is not UNSET:
            field_dict["dmsDesktopUserIds"] = dms_desktop_user_ids
        if option_group_ids is not UNSET:
            field_dict["optionGroupIds"] = option_group_ids
        if child_ids is not UNSET:
            field_dict["childIds"] = child_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_name import UserName

        d = src_dict.copy()
        user_names = []
        _user_names = d.pop("userNames", UNSET)
        for componentsschemas_list_of_user_name_item_data in _user_names or []:
            componentsschemas_list_of_user_name_item = UserName.from_dict(componentsschemas_list_of_user_name_item_data)

            user_names.append(componentsschemas_list_of_user_name_item)

        counter_total = d.pop("counterTotal", UNSET)

        counter_user = d.pop("counterUser", UNSET)

        counter_group = d.pop("counterGroup", UNSET)

        counter_no_login = d.pop("counterNoLogin", UNSET)

        subadmin_ids = cast(List[int], d.pop("subadminIds", UNSET))

        dms_desktop_user_ids = cast(List[int], d.pop("dmsDesktopUserIds", UNSET))

        option_group_ids = cast(List[int], d.pop("optionGroupIds", UNSET))

        child_ids = cast(List[int], d.pop("childIds", UNSET))

        user_report = cls(
            user_names=user_names,
            counter_total=counter_total,
            counter_user=counter_user,
            counter_group=counter_group,
            counter_no_login=counter_no_login,
            subadmin_ids=subadmin_ids,
            dms_desktop_user_ids=dms_desktop_user_ids,
            option_group_ids=option_group_ids,
            child_ids=child_ids,
        )

        user_report.additional_properties = d
        return user_report

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
