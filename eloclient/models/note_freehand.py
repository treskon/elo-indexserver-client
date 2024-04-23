from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.point_info import PointInfo


T = TypeVar("T", bound="NoteFreehand")


@_attrs_define
class NoteFreehand:
    """This class describes a freehand line annotation.

    Attributes:
        width (Union[Unset, int]): Line width.
        strikeout_color (Union[Unset, int]): Color for strikeout pen (only TYPE_ANNOTATION_STRIKEOUT).
        strikeout_width (Union[Unset, int]): Line width for strikeout pen (only TYPE_ANNOTATION_STRIKEOUT).
        points (Union[Unset, List['PointInfo']]):
    """

    width: Union[Unset, int] = UNSET
    strikeout_color: Union[Unset, int] = UNSET
    strikeout_width: Union[Unset, int] = UNSET
    points: Union[Unset, List["PointInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        width = self.width

        strikeout_color = self.strikeout_color

        strikeout_width = self.strikeout_width

        points: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.points, Unset):
            points = []
            for points_item_data in self.points:
                points_item = points_item_data.to_dict()
                points.append(points_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if strikeout_color is not UNSET:
            field_dict["strikeoutColor"] = strikeout_color
        if strikeout_width is not UNSET:
            field_dict["strikeoutWidth"] = strikeout_width
        if points is not UNSET:
            field_dict["points"] = points

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.point_info import PointInfo

        d = src_dict.copy()
        width = d.pop("width", UNSET)

        strikeout_color = d.pop("strikeoutColor", UNSET)

        strikeout_width = d.pop("strikeoutWidth", UNSET)

        points = []
        _points = d.pop("points", UNSET)
        for points_item_data in _points or []:
            points_item = PointInfo.from_dict(points_item_data)

            points.append(points_item)

        note_freehand = cls(
            width=width,
            strikeout_color=strikeout_color,
            strikeout_width=strikeout_width,
            points=points,
        )

        note_freehand.additional_properties = d
        return note_freehand

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
