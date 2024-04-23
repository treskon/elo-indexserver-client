from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFVersion")


@_attrs_define
class WFVersion:
    """Version information for a workflow template.

    Attributes:
        create_date_iso (Union[Unset, str]): Create date in ISO format.
        comment (Union[Unset, str]): Version comment.
        id (Union[Unset, int]): Version ID. Set this member -1, to check in a new workflow template version.
            A value of 0
             indicates the current working version.
        user_name (Union[Unset, str]): Name of the user who created the version.
        user_id (Union[Unset, int]): ID of the user who created the version.
        version (Union[Unset, str]): Version number.
    """

    create_date_iso: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_date_iso = self.create_date_iso

        comment = self.comment

        id = self.id

        user_name = self.user_name

        user_id = self.user_id

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if comment is not UNSET:
            field_dict["comment"] = comment
        if id is not UNSET:
            field_dict["id"] = id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_date_iso = d.pop("createDateIso", UNSET)

        comment = d.pop("comment", UNSET)

        id = d.pop("id", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        version = d.pop("version", UNSET)

        wf_version = cls(
            create_date_iso=create_date_iso,
            comment=comment,
            id=id,
            user_name=user_name,
            user_id=user_id,
            version=version,
        )

        wf_version.additional_properties = d
        return wf_version

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
