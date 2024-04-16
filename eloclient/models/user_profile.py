from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """User profile options
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            exclude_group_values (Union[Unset, bool]): Do not read values of option groups. Only valid for
                checkoutUserProfile.
            include_all_group_and_default_options (Union[Unset, bool]): Include all group and default options.
                Set this member as true, if all group and default
                 options shall be returned. If the value is false, only those options are returned that are not
                 particularly defined for the user.
            default_options (Union[Unset, List['KeyValue']]):
            group_id (Union[Unset, int]): The users option group ID. This value is -1, if the user is not member of an
                option group.
                Read-only.
            options (Union[Unset, List['KeyValue']]):
            user_options (Union[Unset, List['KeyValue']]):
            user_id (Union[Unset, str]): The user name or UserProfileC.
                USERID_ALL, if the options for all users are represented by this
                 object. The values null or empty are equal to UserProfileC.USERID_ALL.
            group_options (Union[Unset, List['KeyValue']]):
            exclude_default_values (Union[Unset, bool]): Do not read values for all users. Only valid for
                checkoutUserProfile.
    """

    exclude_group_values: Union[Unset, bool] = UNSET
    include_all_group_and_default_options: Union[Unset, bool] = UNSET
    default_options: Union[Unset, List["KeyValue"]] = UNSET
    group_id: Union[Unset, int] = UNSET
    options: Union[Unset, List["KeyValue"]] = UNSET
    user_options: Union[Unset, List["KeyValue"]] = UNSET
    user_id: Union[Unset, str] = UNSET
    group_options: Union[Unset, List["KeyValue"]] = UNSET
    exclude_default_values: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exclude_group_values = self.exclude_group_values

        include_all_group_and_default_options = self.include_all_group_and_default_options

        default_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.default_options, Unset):
            default_options = []
            for default_options_item_data in self.default_options:
                default_options_item = default_options_item_data.to_dict()
                default_options.append(default_options_item)

        group_id = self.group_id

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        user_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_options, Unset):
            user_options = []
            for user_options_item_data in self.user_options:
                user_options_item = user_options_item_data.to_dict()
                user_options.append(user_options_item)

        user_id = self.user_id

        group_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_options, Unset):
            group_options = []
            for group_options_item_data in self.group_options:
                group_options_item = group_options_item_data.to_dict()
                group_options.append(group_options_item)

        exclude_default_values = self.exclude_default_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_group_values is not UNSET:
            field_dict["excludeGroupValues"] = exclude_group_values
        if include_all_group_and_default_options is not UNSET:
            field_dict["includeAllGroupAndDefaultOptions"] = include_all_group_and_default_options
        if default_options is not UNSET:
            field_dict["defaultOptions"] = default_options
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if options is not UNSET:
            field_dict["options"] = options
        if user_options is not UNSET:
            field_dict["userOptions"] = user_options
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if group_options is not UNSET:
            field_dict["groupOptions"] = group_options
        if exclude_default_values is not UNSET:
            field_dict["excludeDefaultValues"] = exclude_default_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        exclude_group_values = d.pop("excludeGroupValues", UNSET)

        include_all_group_and_default_options = d.pop("includeAllGroupAndDefaultOptions", UNSET)

        default_options = []
        _default_options = d.pop("defaultOptions", UNSET)
        for default_options_item_data in _default_options or []:
            default_options_item = KeyValue.from_dict(default_options_item_data)

            default_options.append(default_options_item)

        group_id = d.pop("groupId", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = KeyValue.from_dict(options_item_data)

            options.append(options_item)

        user_options = []
        _user_options = d.pop("userOptions", UNSET)
        for user_options_item_data in _user_options or []:
            user_options_item = KeyValue.from_dict(user_options_item_data)

            user_options.append(user_options_item)

        user_id = d.pop("userId", UNSET)

        group_options = []
        _group_options = d.pop("groupOptions", UNSET)
        for group_options_item_data in _group_options or []:
            group_options_item = KeyValue.from_dict(group_options_item_data)

            group_options.append(group_options_item)

        exclude_default_values = d.pop("excludeDefaultValues", UNSET)

        user_profile = cls(
            exclude_group_values=exclude_group_values,
            include_all_group_and_default_options=include_all_group_and_default_options,
            default_options=default_options,
            group_id=group_id,
            options=options,
            user_options=user_options,
            user_id=user_id,
            group_options=group_options,
            exclude_default_values=exclude_default_values,
        )

        user_profile.additional_properties = d
        return user_profile

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
