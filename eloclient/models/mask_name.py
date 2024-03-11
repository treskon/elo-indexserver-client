from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaskName")


@_attrs_define
class MaskName:
    """Mask name object.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            document_mask (Union[Unset, bool]): Mask can be used as storage mask for indexing.
            id (Union[Unset, int]): Mask ID.
            name (Union[Unset, str]): Mask name.
            search_mask (Union[Unset, bool]): Mask can be used for searching.
            folder_mask (Union[Unset, bool]): Mask can be used as storage mask for folders.
            guid (Union[Unset, str]): GUID
            access (Union[Unset, int]): Access mode for the current user. A combination of AccessC.LUR_* constants.
            barcode_mask (Union[Unset, bool]): Mask has a barcode definition.
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link MaskName#name}.
    """

    document_mask: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    search_mask: Union[Unset, bool] = UNSET
    folder_mask: Union[Unset, bool] = UNSET
    guid: Union[Unset, str] = UNSET
    access: Union[Unset, int] = UNSET
    barcode_mask: Union[Unset, bool] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        document_mask = self.document_mask
        id = self.id
        name = self.name
        search_mask = self.search_mask
        folder_mask = self.folder_mask
        guid = self.guid
        access = self.access
        barcode_mask = self.barcode_mask
        name_translation_key = self.name_translation_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_mask is not UNSET:
            field_dict["documentMask"] = document_mask
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if search_mask is not UNSET:
            field_dict["searchMask"] = search_mask
        if folder_mask is not UNSET:
            field_dict["folderMask"] = folder_mask
        if guid is not UNSET:
            field_dict["guid"] = guid
        if access is not UNSET:
            field_dict["access"] = access
        if barcode_mask is not UNSET:
            field_dict["barcodeMask"] = barcode_mask
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        document_mask = d.pop("documentMask", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        search_mask = d.pop("searchMask", UNSET)

        folder_mask = d.pop("folderMask", UNSET)

        guid = d.pop("guid", UNSET)

        access = d.pop("access", UNSET)

        barcode_mask = d.pop("barcodeMask", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        mask_name = cls(
            document_mask=document_mask,
            id=id,
            name=name,
            search_mask=search_mask,
            folder_mask=folder_mask,
            guid=guid,
            access=access,
            barcode_mask=barcode_mask,
            name_translation_key=name_translation_key,
        )

        mask_name.additional_properties = d
        return mask_name

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
