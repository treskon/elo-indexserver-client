from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectInfo")


@_attrs_define
class AspectInfo:
    """Aspect info object.
    <p>
     Copyright: Copyright (c) 2020
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            translation_key (Union[Unset, str]): Translation-keyword for {@link AspectInfo#name}.
            display_name (Union[Unset, str]): Translated name of this aspect.
                This value is read-only and therefore ignored when changed and
                 checked-in. Furthermore, the Indexserver always translates this value into the client language
                 regardless whether the translation settings is enabled or not.
            name (Union[Unset, str]): Aspect name.
            guid (Union[Unset, str]): GUID
            id (Union[Unset, int]): Aspect ID.
            package_name (Union[Unset, str]): Package name.
    """

    translation_key: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        translation_key = self.translation_key

        display_name = self.display_name

        name = self.name

        guid = self.guid

        id = self.id

        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        translation_key = d.pop("translationKey", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        package_name = d.pop("packageName", UNSET)

        aspect_info = cls(
            translation_key=translation_key,
            display_name=display_name,
            name=name,
            guid=guid,
            id=id,
            package_name=package_name,
        )

        aspect_info.additional_properties = d
        return aspect_info

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
