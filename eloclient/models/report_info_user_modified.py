from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_info_user_props import ReportInfoUserProps


T = TypeVar("T", bound="ReportInfoUserModified")


@_attrs_define
class ReportInfoUserModified:
    """Additional report information for modified user.

    Attributes:
        new_props (Union[Unset, ReportInfoUserProps]): Additional report information for user modifications.
        old_props (Union[Unset, ReportInfoUserProps]): Additional report information for user modifications.
    """

    new_props: Union[Unset, "ReportInfoUserProps"] = UNSET
    old_props: Union[Unset, "ReportInfoUserProps"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new_props: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_props, Unset):
            new_props = self.new_props.to_dict()

        old_props: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.old_props, Unset):
            old_props = self.old_props.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if new_props is not UNSET:
            field_dict["newProps"] = new_props
        if old_props is not UNSET:
            field_dict["oldProps"] = old_props

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_info_user_props import ReportInfoUserProps

        d = src_dict.copy()
        _new_props = d.pop("newProps", UNSET)
        new_props: Union[Unset, ReportInfoUserProps]
        if isinstance(_new_props, Unset):
            new_props = UNSET
        else:
            new_props = ReportInfoUserProps.from_dict(_new_props)

        _old_props = d.pop("oldProps", UNSET)
        old_props: Union[Unset, ReportInfoUserProps]
        if isinstance(_old_props, Unset):
            old_props = UNSET
        else:
            old_props = ReportInfoUserProps.from_dict(_old_props)

        report_info_user_modified = cls(
            new_props=new_props,
            old_props=old_props,
        )

        report_info_user_modified.additional_properties = d
        return report_info_user_modified

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
