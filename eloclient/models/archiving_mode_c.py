from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArchivingModeC")


@_attrs_define
class ArchivingModeC:
    """
    Attributes:
        readwrite (Union[Unset, int]): Version flag: no versioning.
        version (Union[Unset, int]): Version flag: version controlled.
        readonly (Union[Unset, int]): Version flag: read only.
        default (Union[Unset, int]):
        none (Union[Unset, int]):
        dummy (Union[Unset, int]):
    """

    readwrite: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    readonly: Union[Unset, int] = UNSET
    default: Union[Unset, int] = UNSET
    none: Union[Unset, int] = UNSET
    dummy: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        readwrite = self.readwrite
        version = self.version
        readonly = self.readonly
        default = self.default
        none = self.none
        dummy = self.dummy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if readwrite is not UNSET:
            field_dict["READWRITE"] = readwrite
        if version is not UNSET:
            field_dict["VERSION"] = version
        if readonly is not UNSET:
            field_dict["READONLY"] = readonly
        if default is not UNSET:
            field_dict["DEFAULT"] = default
        if none is not UNSET:
            field_dict["NONE"] = none
        if dummy is not UNSET:
            field_dict["dummy"] = dummy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        readwrite = d.pop("READWRITE", UNSET)

        version = d.pop("VERSION", UNSET)

        readonly = d.pop("READONLY", UNSET)

        default = d.pop("DEFAULT", UNSET)

        none = d.pop("NONE", UNSET)

        dummy = d.pop("dummy", UNSET)

        archiving_mode_c = cls(
            readwrite=readwrite,
            version=version,
            readonly=readonly,
            default=default,
            none=none,
            dummy=dummy,
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
