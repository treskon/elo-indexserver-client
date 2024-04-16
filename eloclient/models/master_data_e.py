from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MasterDataE")


@_attrs_define
class MasterDataE:
    """Enumeration for the master data

    Attributes:
        colors (Union[Unset, MasterDataE]): Enumeration for the master data
        keywording_forms (Union[Unset, MasterDataE]): Enumeration for the master data
        entry_types (Union[Unset, MasterDataE]): Enumeration for the master data
        organizational_units (Union[Unset, MasterDataE]): Enumeration for the master data
        users (Union[Unset, MasterDataE]): Enumeration for the master data
        index_field_templates (Union[Unset, MasterDataE]): Enumeration for the master data
        keyword_lists (Union[Unset, MasterDataE]): Enumeration for the master data
    """

    colors: Union[Unset, "MasterDataE"] = UNSET
    keywording_forms: Union[Unset, "MasterDataE"] = UNSET
    entry_types: Union[Unset, "MasterDataE"] = UNSET
    organizational_units: Union[Unset, "MasterDataE"] = UNSET
    users: Union[Unset, "MasterDataE"] = UNSET
    index_field_templates: Union[Unset, "MasterDataE"] = UNSET
    keyword_lists: Union[Unset, "MasterDataE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        colors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors.to_dict()

        keywording_forms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keywording_forms, Unset):
            keywording_forms = self.keywording_forms.to_dict()

        entry_types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entry_types, Unset):
            entry_types = self.entry_types.to_dict()

        organizational_units: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organizational_units, Unset):
            organizational_units = self.organizational_units.to_dict()

        users: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users.to_dict()

        index_field_templates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.index_field_templates, Unset):
            index_field_templates = self.index_field_templates.to_dict()

        keyword_lists: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keyword_lists, Unset):
            keyword_lists = self.keyword_lists.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if colors is not UNSET:
            field_dict["COLORS"] = colors
        if keywording_forms is not UNSET:
            field_dict["KEYWORDING_FORMS"] = keywording_forms
        if entry_types is not UNSET:
            field_dict["ENTRY_TYPES"] = entry_types
        if organizational_units is not UNSET:
            field_dict["ORGANIZATIONAL_UNITS"] = organizational_units
        if users is not UNSET:
            field_dict["USERS"] = users
        if index_field_templates is not UNSET:
            field_dict["INDEX_FIELD_TEMPLATES"] = index_field_templates
        if keyword_lists is not UNSET:
            field_dict["KEYWORD_LISTS"] = keyword_lists

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _colors = d.pop("COLORS", UNSET)
        colors: Union[Unset, MasterDataE]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = MasterDataE.from_dict(_colors)

        _keywording_forms = d.pop("KEYWORDING_FORMS", UNSET)
        keywording_forms: Union[Unset, MasterDataE]
        if isinstance(_keywording_forms, Unset):
            keywording_forms = UNSET
        else:
            keywording_forms = MasterDataE.from_dict(_keywording_forms)

        _entry_types = d.pop("ENTRY_TYPES", UNSET)
        entry_types: Union[Unset, MasterDataE]
        if isinstance(_entry_types, Unset):
            entry_types = UNSET
        else:
            entry_types = MasterDataE.from_dict(_entry_types)

        _organizational_units = d.pop("ORGANIZATIONAL_UNITS", UNSET)
        organizational_units: Union[Unset, MasterDataE]
        if isinstance(_organizational_units, Unset):
            organizational_units = UNSET
        else:
            organizational_units = MasterDataE.from_dict(_organizational_units)

        _users = d.pop("USERS", UNSET)
        users: Union[Unset, MasterDataE]
        if isinstance(_users, Unset):
            users = UNSET
        else:
            users = MasterDataE.from_dict(_users)

        _index_field_templates = d.pop("INDEX_FIELD_TEMPLATES", UNSET)
        index_field_templates: Union[Unset, MasterDataE]
        if isinstance(_index_field_templates, Unset):
            index_field_templates = UNSET
        else:
            index_field_templates = MasterDataE.from_dict(_index_field_templates)

        _keyword_lists = d.pop("KEYWORD_LISTS", UNSET)
        keyword_lists: Union[Unset, MasterDataE]
        if isinstance(_keyword_lists, Unset):
            keyword_lists = UNSET
        else:
            keyword_lists = MasterDataE.from_dict(_keyword_lists)

        master_data_e = cls(
            colors=colors,
            keywording_forms=keywording_forms,
            entry_types=entry_types,
            organizational_units=organizational_units,
            users=users,
            index_field_templates=index_field_templates,
            keyword_lists=keyword_lists,
        )

        master_data_e.additional_properties = d
        return master_data_e

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
