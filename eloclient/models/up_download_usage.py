from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpDownloadUsage")


@_attrs_define
class UpDownloadUsage:
    """This enumeration defines constants that describe, from where an event in {@link DocumentEvents}
    is called.

        Attributes:
            intern (Union[Unset, UpDownloadUsage]): This enumeration defines constants that describe, from where an event in
                {@link DocumentEvents}
                is called.
            api (Union[Unset, UpDownloadUsage]): This enumeration defines constants that describe, from where an event in
                {@link DocumentEvents}
                is called.
    """

    intern: Union[Unset, "UpDownloadUsage"] = UNSET
    api: Union[Unset, "UpDownloadUsage"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        intern: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.intern, Unset):
            intern = self.intern.to_dict()

        api: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api, Unset):
            api = self.api.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intern is not UNSET:
            field_dict["INTERN"] = intern
        if api is not UNSET:
            field_dict["API"] = api

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _intern = d.pop("INTERN", UNSET)
        intern: Union[Unset, UpDownloadUsage]
        if isinstance(_intern, Unset):
            intern = UNSET
        else:
            intern = UpDownloadUsage.from_dict(_intern)

        _api = d.pop("API", UNSET)
        api: Union[Unset, UpDownloadUsage]
        if isinstance(_api, Unset):
            api = UNSET
        else:
            api = UpDownloadUsage.from_dict(_api)

        up_download_usage = cls(
            intern=intern,
            api=api,
        )

        up_download_usage.additional_properties = d
        return up_download_usage

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
