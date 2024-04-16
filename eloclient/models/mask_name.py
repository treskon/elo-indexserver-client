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
            keywording_relation_allowed (Union[Unset, bool]): Mask can be referenced from a DocMaskLine of type {@link
                DocMaskLineC#TYPE_RELATION}.
                <br>
                 If this mask has a data organisation {@link DocMaskC#DATA_ORGANISATION_ASPECT} the value
                 determines if it can be referenced by an AspectLine of type {@link AspectLineC#TYPE_RELATION}.
            access (Union[Unset, int]): Access mode for the current user. A combination of AccessC.LUR_* constants.
            data_organisation (Union[Unset, int]): This member specifies how the index values are stored in database.
            display_name (Union[Unset, str]): Translated name of this mask.
                This value is read-only and therefore ignored when changed and
                 checked-in. Furthermore, the Indexserver always translates this value into the client language
                 regardless whether the translation settings is enabled or not.
            document_mask (Union[Unset, bool]): Mask can be used as storage mask for indexing.
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link MaskName#name}.
            barcode_mask (Union[Unset, bool]): Mask has a barcode definition.
            search_mask (Union[Unset, bool]): Mask can be used for searching.
            name (Union[Unset, str]): Mask name.
            guid (Union[Unset, str]): GUID
            id (Union[Unset, int]): Mask ID.
            folder_mask (Union[Unset, bool]): Mask can be used as storage mask for folders.
            package_name (Union[Unset, str]): Package name.
            region (Union[Unset, bool]): Sords of this mask establish a region within the repository tree.
                <br>
                 This flag is only valid for masks of data organisation
                 {@link DocMaskC#DATA_ORGANISATION_ASPECT}.
    """

    keywording_relation_allowed: Union[Unset, bool] = UNSET
    access: Union[Unset, int] = UNSET
    data_organisation: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    document_mask: Union[Unset, bool] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    barcode_mask: Union[Unset, bool] = UNSET
    search_mask: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    folder_mask: Union[Unset, bool] = UNSET
    package_name: Union[Unset, str] = UNSET
    region: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keywording_relation_allowed = self.keywording_relation_allowed

        access = self.access

        data_organisation = self.data_organisation

        display_name = self.display_name

        document_mask = self.document_mask

        name_translation_key = self.name_translation_key

        barcode_mask = self.barcode_mask

        search_mask = self.search_mask

        name = self.name

        guid = self.guid

        id = self.id

        folder_mask = self.folder_mask

        package_name = self.package_name

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keywording_relation_allowed is not UNSET:
            field_dict["keywordingRelationAllowed"] = keywording_relation_allowed
        if access is not UNSET:
            field_dict["access"] = access
        if data_organisation is not UNSET:
            field_dict["dataOrganisation"] = data_organisation
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if document_mask is not UNSET:
            field_dict["documentMask"] = document_mask
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if barcode_mask is not UNSET:
            field_dict["barcodeMask"] = barcode_mask
        if search_mask is not UNSET:
            field_dict["searchMask"] = search_mask
        if name is not UNSET:
            field_dict["name"] = name
        if guid is not UNSET:
            field_dict["guid"] = guid
        if id is not UNSET:
            field_dict["id"] = id
        if folder_mask is not UNSET:
            field_dict["folderMask"] = folder_mask
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keywording_relation_allowed = d.pop("keywordingRelationAllowed", UNSET)

        access = d.pop("access", UNSET)

        data_organisation = d.pop("dataOrganisation", UNSET)

        display_name = d.pop("displayName", UNSET)

        document_mask = d.pop("documentMask", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        barcode_mask = d.pop("barcodeMask", UNSET)

        search_mask = d.pop("searchMask", UNSET)

        name = d.pop("name", UNSET)

        guid = d.pop("guid", UNSET)

        id = d.pop("id", UNSET)

        folder_mask = d.pop("folderMask", UNSET)

        package_name = d.pop("packageName", UNSET)

        region = d.pop("region", UNSET)

        mask_name = cls(
            keywording_relation_allowed=keywording_relation_allowed,
            access=access,
            data_organisation=data_organisation,
            display_name=display_name,
            document_mask=document_mask,
            name_translation_key=name_translation_key,
            barcode_mask=barcode_mask,
            search_mask=search_mask,
            name=name,
            guid=guid,
            id=id,
            folder_mask=folder_mask,
            package_name=package_name,
            region=region,
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
