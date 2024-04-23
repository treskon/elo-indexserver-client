from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grouping_type import GroupingType


T = TypeVar("T", bound="ConfigResultOptions")


@_attrs_define
class ConfigResultOptions:
    """This options control grouping of configuration entries returned by
    {@link ConfigService#checkoutConfigurations(de.elo.ix.client.ClientInfo, ConfigInfo, ConfigResultOptions)}.

        Attributes:
            exploded (Union[Unset, bool]): If true, entries are not merged by their {@link ConfigRecord#level} values.
            grouping_type (Union[Unset, GroupingType]): {@link ConfigService#checkoutConfigurations(de.elo.ix.client.
                ClientInfo, ConfigInfo, ConfigResultOptions)}
                 maps the returned configuration entries on this value types.
    """

    exploded: Union[Unset, bool] = UNSET
    grouping_type: Union[Unset, "GroupingType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exploded = self.exploded

        grouping_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grouping_type, Unset):
            grouping_type = self.grouping_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exploded is not UNSET:
            field_dict["exploded"] = exploded
        if grouping_type is not UNSET:
            field_dict["groupingType"] = grouping_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.grouping_type import GroupingType

        d = src_dict.copy()
        exploded = d.pop("exploded", UNSET)

        _grouping_type = d.pop("groupingType", UNSET)
        grouping_type: Union[Unset, GroupingType]
        if isinstance(_grouping_type, Unset):
            grouping_type = UNSET
        else:
            grouping_type = GroupingType.from_dict(_grouping_type)

        config_result_options = cls(
            exploded=exploded,
            grouping_type=grouping_type,
        )

        config_result_options.additional_properties = d
        return config_result_options

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
