from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ColorDataC")


@_attrs_define
class ColorDataC:
    """
    Attributes:
        guid_green (Union[Unset, str]): Color green
        guid_system (Union[Unset, str]): System color
        guid_blue (Union[Unset, str]): Color blue
        mb_hidden (Union[Unset, str]): Hidden flag.
        guid_red (Union[Unset, str]): Color red
        inclusive_hidden (Union[Unset, int]): Read colors inclusive hidden colors.
            This option can be passed to
             {@link IXServicePortIF#checkoutColors2(ClientInfo, int, LockZ)}.
        sord_colors (Union[Unset, int]): Read colors that can be assigned to Sord objects.
            This option can be passed to
             {@link IXServicePortIF#checkoutColors2(ClientInfo, int, LockZ)}.
        inclusive_deleted (Union[Unset, int]): Read colors inclusive logically deleted colors.
            This option can be passed to
             {@link IXServicePortIF#checkoutColors2(ClientInfo, int, LockZ)}.
        mb_deleted (Union[Unset, str]):
        all_colors (Union[Unset, int]): Read all colors.
            This option can be passed to
             {@link IXServicePortIF#checkoutColors2(ClientInfo, int, LockZ)}.
    """

    guid_green: Union[Unset, str] = UNSET
    guid_system: Union[Unset, str] = UNSET
    guid_blue: Union[Unset, str] = UNSET
    mb_hidden: Union[Unset, str] = UNSET
    guid_red: Union[Unset, str] = UNSET
    inclusive_hidden: Union[Unset, int] = UNSET
    sord_colors: Union[Unset, int] = UNSET
    inclusive_deleted: Union[Unset, int] = UNSET
    mb_deleted: Union[Unset, str] = UNSET
    all_colors: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid_green = self.guid_green

        guid_system = self.guid_system

        guid_blue = self.guid_blue

        mb_hidden = self.mb_hidden

        guid_red = self.guid_red

        inclusive_hidden = self.inclusive_hidden

        sord_colors = self.sord_colors

        inclusive_deleted = self.inclusive_deleted

        mb_deleted = self.mb_deleted

        all_colors = self.all_colors

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid_green is not UNSET:
            field_dict["GUID_GREEN"] = guid_green
        if guid_system is not UNSET:
            field_dict["GUID_SYSTEM"] = guid_system
        if guid_blue is not UNSET:
            field_dict["GUID_BLUE"] = guid_blue
        if mb_hidden is not UNSET:
            field_dict["mbHidden"] = mb_hidden
        if guid_red is not UNSET:
            field_dict["GUID_RED"] = guid_red
        if inclusive_hidden is not UNSET:
            field_dict["INCLUSIVE_HIDDEN"] = inclusive_hidden
        if sord_colors is not UNSET:
            field_dict["SORD_COLORS"] = sord_colors
        if inclusive_deleted is not UNSET:
            field_dict["INCLUSIVE_DELETED"] = inclusive_deleted
        if mb_deleted is not UNSET:
            field_dict["mbDeleted"] = mb_deleted
        if all_colors is not UNSET:
            field_dict["ALL_COLORS"] = all_colors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guid_green = d.pop("GUID_GREEN", UNSET)

        guid_system = d.pop("GUID_SYSTEM", UNSET)

        guid_blue = d.pop("GUID_BLUE", UNSET)

        mb_hidden = d.pop("mbHidden", UNSET)

        guid_red = d.pop("GUID_RED", UNSET)

        inclusive_hidden = d.pop("INCLUSIVE_HIDDEN", UNSET)

        sord_colors = d.pop("SORD_COLORS", UNSET)

        inclusive_deleted = d.pop("INCLUSIVE_DELETED", UNSET)

        mb_deleted = d.pop("mbDeleted", UNSET)

        all_colors = d.pop("ALL_COLORS", UNSET)

        color_data_c = cls(
            guid_green=guid_green,
            guid_system=guid_system,
            guid_blue=guid_blue,
            mb_hidden=mb_hidden,
            guid_red=guid_red,
            inclusive_hidden=inclusive_hidden,
            sord_colors=sord_colors,
            inclusive_deleted=inclusive_deleted,
            mb_deleted=mb_deleted,
            all_colors=all_colors,
        )

        color_data_c.additional_properties = d
        return color_data_c

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
