from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConflictHandlingE")


@_attrs_define
class ConflictHandlingE:
    """FIXME: add javadoc

    Attributes:
        tstamp (Union[Unset, ConflictHandlingE]): FIXME: add javadoc
        override (Union[Unset, ConflictHandlingE]): FIXME: add javadoc
        retain (Union[Unset, ConflictHandlingE]): FIXME: add javadoc
    """

    tstamp: Union[Unset, "ConflictHandlingE"] = UNSET
    override: Union[Unset, "ConflictHandlingE"] = UNSET
    retain: Union[Unset, "ConflictHandlingE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tstamp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tstamp, Unset):
            tstamp = self.tstamp.to_dict()

        override: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.override, Unset):
            override = self.override.to_dict()

        retain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retain, Unset):
            retain = self.retain.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tstamp is not UNSET:
            field_dict["TSTAMP"] = tstamp
        if override is not UNSET:
            field_dict["OVERRIDE"] = override
        if retain is not UNSET:
            field_dict["RETAIN"] = retain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tstamp = d.pop("TSTAMP", UNSET)
        tstamp: Union[Unset, ConflictHandlingE]
        if isinstance(_tstamp, Unset):
            tstamp = UNSET
        else:
            tstamp = ConflictHandlingE.from_dict(_tstamp)

        _override = d.pop("OVERRIDE", UNSET)
        override: Union[Unset, ConflictHandlingE]
        if isinstance(_override, Unset):
            override = UNSET
        else:
            override = ConflictHandlingE.from_dict(_override)

        _retain = d.pop("RETAIN", UNSET)
        retain: Union[Unset, ConflictHandlingE]
        if isinstance(_retain, Unset):
            retain = UNSET
        else:
            retain = ConflictHandlingE.from_dict(_retain)

        conflict_handling_e = cls(
            tstamp=tstamp,
            override=override,
            retain=retain,
        )

        conflict_handling_e.additional_properties = d
        return conflict_handling_e

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
