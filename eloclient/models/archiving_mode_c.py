from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchivingModeC")


@_attrs_define
class ArchivingModeC:
    """
    Attributes:
        dummy (Union[Unset, int]):
        readwrite (Union[Unset, int]): Version flag: no versioning.
        version (Union[Unset, int]): Version flag: version controlled.
        none (Union[Unset, int]):
        readonly (Union[Unset, int]): Version flag: read only.
        default (Union[Unset, int]):
    """

    dummy: Union[Unset, int] = UNSET
    readwrite: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    none: Union[Unset, int] = UNSET
    readonly: Union[Unset, int] = UNSET
    default: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dummy = self.dummy

        readwrite = self.readwrite

        version = self.version

        none = self.none

        readonly = self.readonly

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dummy is not UNSET:
            field_dict["dummy"] = dummy
        if readwrite is not UNSET:
            field_dict["READWRITE"] = readwrite
        if version is not UNSET:
            field_dict["VERSION"] = version
        if none is not UNSET:
            field_dict["NONE"] = none
        if readonly is not UNSET:
            field_dict["READONLY"] = readonly
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dummy = d.pop("dummy", UNSET)

        readwrite = d.pop("READWRITE", UNSET)

        version = d.pop("VERSION", UNSET)

        none = d.pop("NONE", UNSET)

        readonly = d.pop("READONLY", UNSET)

        default = d.pop("DEFAULT", UNSET)

        archiving_mode_c = cls(
            dummy=dummy,
            readwrite=readwrite,
            version=version,
            none=none,
            readonly=readonly,
            default=default,
        )

        archiving_mode_c.additional_properties = d
        return archiving_mode_c

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
