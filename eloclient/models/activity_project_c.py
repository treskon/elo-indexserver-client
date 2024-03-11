from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityProjectC")


@_attrs_define
class ActivityProjectC:
    """Constants for class ActivityProject.

    Attributes:
        mb_options (Union[Unset, str]):
        system (Union[Unset, str]): Reserved. This name is used internally only. Do not use this name in your code.
        default (Union[Unset, str]): Default project name.
        request (Union[Unset, str]): Activity for observing documents and folders.
        notify (Union[Unset, str]): Activity used to notify about a new document version or new sub-item.
    """

    mb_options: Union[Unset, str] = UNSET
    system: Union[Unset, str] = UNSET
    default: Union[Unset, str] = UNSET
    request: Union[Unset, str] = UNSET
    notify: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_options = self.mb_options
        system = self.system
        default = self.default
        request = self.request
        notify = self.notify

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_options is not UNSET:
            field_dict["mbOptions"] = mb_options
        if system is not UNSET:
            field_dict["SYSTEM"] = system
        if default is not UNSET:
            field_dict["DEFAULT"] = default
        if request is not UNSET:
            field_dict["REQUEST"] = request
        if notify is not UNSET:
            field_dict["NOTIFY"] = notify

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_options = d.pop("mbOptions", UNSET)

        system = d.pop("SYSTEM", UNSET)

        default = d.pop("DEFAULT", UNSET)

        request = d.pop("REQUEST", UNSET)

        notify = d.pop("NOTIFY", UNSET)

        activity_project_c = cls(
            mb_options=mb_options,
            system=system,
            default=default,
            request=request,
            notify=notify,
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
