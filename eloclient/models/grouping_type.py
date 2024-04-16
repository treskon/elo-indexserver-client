from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupingType")


@_attrs_define
class GroupingType:
    """{@link ConfigService#checkoutConfigurations(de.elo.ix.client.
    ClientInfo, ConfigInfo, ConfigResultOptions)}
     maps the returned configuration entries on this value types.

        Attributes:
            legacy (Union[Unset, GroupingType]): {@link ConfigService#checkoutConfigurations(de.elo.ix.client.
                ClientInfo, ConfigInfo, ConfigResultOptions)}
                 maps the returned configuration entries on this value types.
            by_group (Union[Unset, GroupingType]): {@link ConfigService#checkoutConfigurations(de.elo.ix.client.
                ClientInfo, ConfigInfo, ConfigResultOptions)}
                 maps the returned configuration entries on this value types.
            by_key (Union[Unset, GroupingType]): {@link ConfigService#checkoutConfigurations(de.elo.ix.client.
                ClientInfo, ConfigInfo, ConfigResultOptions)}
                 maps the returned configuration entries on this value types.
    """

    legacy: Union[Unset, "GroupingType"] = UNSET
    by_group: Union[Unset, "GroupingType"] = UNSET
    by_key: Union[Unset, "GroupingType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        legacy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.legacy, Unset):
            legacy = self.legacy.to_dict()

        by_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_group, Unset):
            by_group = self.by_group.to_dict()

        by_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_key, Unset):
            by_key = self.by_key.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if legacy is not UNSET:
            field_dict["LEGACY"] = legacy
        if by_group is not UNSET:
            field_dict["BY_GROUP"] = by_group
        if by_key is not UNSET:
            field_dict["BY_KEY"] = by_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _legacy = d.pop("LEGACY", UNSET)
        legacy: Union[Unset, GroupingType]
        if isinstance(_legacy, Unset):
            legacy = UNSET
        else:
            legacy = GroupingType.from_dict(_legacy)

        _by_group = d.pop("BY_GROUP", UNSET)
        by_group: Union[Unset, GroupingType]
        if isinstance(_by_group, Unset):
            by_group = UNSET
        else:
            by_group = GroupingType.from_dict(_by_group)

        _by_key = d.pop("BY_KEY", UNSET)
        by_key: Union[Unset, GroupingType]
        if isinstance(_by_key, Unset):
            by_key = UNSET
        else:
            by_key = GroupingType.from_dict(_by_key)

        grouping_type = cls(
            legacy=legacy,
            by_group=by_group,
            by_key=by_key,
        )

        grouping_type.additional_properties = d
        return grouping_type

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
