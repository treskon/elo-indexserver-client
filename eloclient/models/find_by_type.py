from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByType")


@_attrs_define
class FindByType:
    """This class holds additional information for FindInfo, in order to restrict a search using
    document types. The default resolving sequence is ordered by the grade of restriction: <br>
     1. typeIDs, typeNames, typeExtensions is the most specialised information, <br>
     2. typeDocuments containing all document types (IDs, Names, Extensions), <br>
     3. and typeStructures including all levels of structure elements. <br>
     4. If none of the parameters above is valid, the complete restriction FindByType is omitted. <br>

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            type_structures (Union[Unset, bool]): Include all structure elements
            type_names (Union[Unset, List[str]]):
            type_documents (Union[Unset, bool]): Include all document types
            type_extensions (Union[Unset, List[str]]):
            type_i_ds (Union[Unset, List[int]]):
    """

    type_structures: Union[Unset, bool] = UNSET
    type_names: Union[Unset, List[str]] = UNSET
    type_documents: Union[Unset, bool] = UNSET
    type_extensions: Union[Unset, List[str]] = UNSET
    type_i_ds: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_structures = self.type_structures

        type_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.type_names, Unset):
            type_names = self.type_names

        type_documents = self.type_documents

        type_extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.type_extensions, Unset):
            type_extensions = self.type_extensions

        type_i_ds: Union[Unset, List[int]] = UNSET
        if not isinstance(self.type_i_ds, Unset):
            type_i_ds = self.type_i_ds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_structures is not UNSET:
            field_dict["typeStructures"] = type_structures
        if type_names is not UNSET:
            field_dict["typeNames"] = type_names
        if type_documents is not UNSET:
            field_dict["typeDocuments"] = type_documents
        if type_extensions is not UNSET:
            field_dict["typeExtensions"] = type_extensions
        if type_i_ds is not UNSET:
            field_dict["typeIDs"] = type_i_ds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_structures = d.pop("typeStructures", UNSET)

        type_names = cast(List[str], d.pop("typeNames", UNSET))

        type_documents = d.pop("typeDocuments", UNSET)

        type_extensions = cast(List[str], d.pop("typeExtensions", UNSET))

        type_i_ds = cast(List[int], d.pop("typeIDs", UNSET))

        find_by_type = cls(
            type_structures=type_structures,
            type_names=type_names,
            type_documents=type_documents,
            type_extensions=type_extensions,
            type_i_ds=type_i_ds,
        )

        find_by_type.additional_properties = d
        return find_by_type

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
