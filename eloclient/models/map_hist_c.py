from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hist_z import MapHistZ


T = TypeVar("T", bound="MapHistC")


@_attrs_define
class MapHistC:
    """Element selectors for class MapHist.

    Attributes:
        mb_all (Union[Unset, MapHistZ]):
        mb_all_members (Union[Unset, str]):
        mb_hist_items (Union[Unset, str]):
        mb_all_no_items (Union[Unset, MapHistZ]):
        mb_all_members_no_items (Union[Unset, str]):
    """

    mb_all: Union[Unset, "MapHistZ"] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_hist_items: Union[Unset, str] = UNSET
    mb_all_no_items: Union[Unset, "MapHistZ"] = UNSET
    mb_all_members_no_items: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_all_members = self.mb_all_members

        mb_hist_items = self.mb_hist_items

        mb_all_no_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_no_items, Unset):
            mb_all_no_items = self.mb_all_no_items.to_dict()

        mb_all_members_no_items = self.mb_all_members_no_items

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_hist_items is not UNSET:
            field_dict["mbHistItems"] = mb_hist_items
        if mb_all_no_items is not UNSET:
            field_dict["mbAllNoItems"] = mb_all_no_items
        if mb_all_members_no_items is not UNSET:
            field_dict["mbAllMembersNoItems"] = mb_all_members_no_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_hist_z import MapHistZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, MapHistZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = MapHistZ.from_dict(_mb_all)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_hist_items = d.pop("mbHistItems", UNSET)

        _mb_all_no_items = d.pop("mbAllNoItems", UNSET)
        mb_all_no_items: Union[Unset, MapHistZ]
        if isinstance(_mb_all_no_items, Unset):
            mb_all_no_items = UNSET
        else:
            mb_all_no_items = MapHistZ.from_dict(_mb_all_no_items)

        mb_all_members_no_items = d.pop("mbAllMembersNoItems", UNSET)

        map_hist_c = cls(
            mb_all=mb_all,
            mb_all_members=mb_all_members,
            mb_hist_items=mb_hist_items,
            mb_all_no_items=mb_all_no_items,
            mb_all_members_no_items=mb_all_members_no_items,
        )

        map_hist_c.additional_properties = d
        return map_hist_c

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
