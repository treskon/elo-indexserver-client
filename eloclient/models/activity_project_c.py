from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityProjectC")


@_attrs_define
class ActivityProjectC:
    """Constants for class ActivityProject.

    Attributes:
        system (Union[Unset, str]): Reserved. This name is used internally only. Do not use this name in your code.
        notify (Union[Unset, str]): Activity used to notify about a new document version or new sub-item.
        request (Union[Unset, str]): Activity for observing documents and folders.
        mb_options (Union[Unset, str]):
        default (Union[Unset, str]): Default project name.
    """

    system: Union[Unset, str] = UNSET
    notify: Union[Unset, str] = UNSET
    request: Union[Unset, str] = UNSET
    mb_options: Union[Unset, str] = UNSET
    default: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        system = self.system

        notify = self.notify

        request = self.request

        mb_options = self.mb_options

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system is not UNSET:
            field_dict["SYSTEM"] = system
        if notify is not UNSET:
            field_dict["NOTIFY"] = notify
        if request is not UNSET:
            field_dict["REQUEST"] = request
        if mb_options is not UNSET:
            field_dict["mbOptions"] = mb_options
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        system = d.pop("SYSTEM", UNSET)

        notify = d.pop("NOTIFY", UNSET)

        request = d.pop("REQUEST", UNSET)

        mb_options = d.pop("mbOptions", UNSET)

        default = d.pop("DEFAULT", UNSET)

        activity_project_c = cls(
            system=system,
            notify=notify,
            request=request,
            mb_options=mb_options,
            default=default,
        )

        activity_project_c.additional_properties = d
        return activity_project_c

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
