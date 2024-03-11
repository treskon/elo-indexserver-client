from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectLineDataC")


@_attrs_define
class AspectLineDataC:
    """<p>
    Bit constants for members of AspectLine
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_aspect_id (Union[Unset, str]): Member bit: This line information belongs to an aspect with the ID AspectId.
                DB column: aspectid
            mb_raw_type (Union[Unset, str]): Member bit: The type of the line information.
                DB column: linetype
            mb_display_name (Union[Unset, str]): Member bit: The display name of the attribute.
                DB column: linedisplayName
            ln_display_name (Union[Unset, int]): Column length: The display name of the attribute.
                DB column: linedisplayName
            mb_key (Union[Unset, str]): Member bit: The attribute identifier.
                DB column: linekey
            ln_key (Union[Unset, int]): Column length: The attribute identifier.
                DB column: linekey
            mb_raw_flags (Union[Unset, str]): Member bit: Internal flags representation.
                DB column: lineflags
            mb_external_data (Union[Unset, str]): Member bit: External data.
                DB column: lineext
            ln_external_data (Union[Unset, int]): Column length: External data.
                DB column: lineext
            mb_default_value (Union[Unset, str]): Member bit: This value is assigned to the element for a new Sord object.
                DB column: linedefault
            ln_default_value (Union[Unset, int]): Column length: This value is assigned to the element for a new Sord
                object.
                DB column: linedefault
            mb_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link AspectLine#name}.
                DB column: linenametrkey
            ln_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link AspectLine#name}.
                DB column: linenametrkey
            mb_allowed_referenced_mask_ids_raw (Union[Unset, str]): Member bit: Specifies the {@link DocMask#id} allowed in
                a {@link DocMaskLineC#TYPE_RELATION}.
                DB column:
                 allowedrefmaskids
            ln_allowed_referenced_mask_ids_raw (Union[Unset, int]): Column length: Specifies the {@link DocMask#id} allowed
                in a {@link DocMaskLineC#TYPE_RELATION}.
                DB column:
                 allowedrefmaskids
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_aspect_id: Union[Unset, str] = UNSET
    mb_raw_type: Union[Unset, str] = UNSET
    mb_display_name: Union[Unset, str] = UNSET
    ln_display_name: Union[Unset, int] = UNSET
    mb_key: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    mb_raw_flags: Union[Unset, str] = UNSET
    mb_external_data: Union[Unset, str] = UNSET
    ln_external_data: Union[Unset, int] = UNSET
    mb_default_value: Union[Unset, str] = UNSET
    ln_default_value: Union[Unset, int] = UNSET
    mb_name_translation_key: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    mb_allowed_referenced_mask_ids_raw: Union[Unset, str] = UNSET
    ln_allowed_referenced_mask_ids_raw: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_aspect_id = self.mb_aspect_id
        mb_raw_type = self.mb_raw_type
        mb_display_name = self.mb_display_name
        ln_display_name = self.ln_display_name
        mb_key = self.mb_key
        ln_key = self.ln_key
        mb_raw_flags = self.mb_raw_flags
        mb_external_data = self.mb_external_data
        ln_external_data = self.ln_external_data
        mb_default_value = self.mb_default_value
        ln_default_value = self.ln_default_value
        mb_name_translation_key = self.mb_name_translation_key
        ln_name_translation_key = self.ln_name_translation_key
        mb_allowed_referenced_mask_ids_raw = self.mb_allowed_referenced_mask_ids_raw
        ln_allowed_referenced_mask_ids_raw = self.ln_allowed_referenced_mask_ids_raw
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_aspect_id is not UNSET:
            field_dict["mbAspectId"] = mb_aspect_id
        if mb_raw_type is not UNSET:
            field_dict["mbRawType"] = mb_raw_type
        if mb_display_name is not UNSET:
            field_dict["mbDisplayName"] = mb_display_name
        if ln_display_name is not UNSET:
            field_dict["lnDisplayName"] = ln_display_name
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if mb_raw_flags is not UNSET:
            field_dict["mbRawFlags"] = mb_raw_flags
        if mb_external_data is not UNSET:
            field_dict["mbExternalData"] = mb_external_data
        if ln_external_data is not UNSET:
            field_dict["lnExternalData"] = ln_external_data
        if mb_default_value is not UNSET:
            field_dict["mbDefaultValue"] = mb_default_value
        if ln_default_value is not UNSET:
            field_dict["lnDefaultValue"] = ln_default_value
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if mb_allowed_referenced_mask_ids_raw is not UNSET:
            field_dict["mbAllowedReferencedMaskIdsRaw"] = mb_allowed_referenced_mask_ids_raw
        if ln_allowed_referenced_mask_ids_raw is not UNSET:
            field_dict["lnAllowedReferencedMaskIdsRaw"] = ln_allowed_referenced_mask_ids_raw
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_aspect_id = d.pop("mbAspectId", UNSET)

        mb_raw_type = d.pop("mbRawType", UNSET)

        mb_display_name = d.pop("mbDisplayName", UNSET)

        ln_display_name = d.pop("lnDisplayName", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        mb_raw_flags = d.pop("mbRawFlags", UNSET)

        mb_external_data = d.pop("mbExternalData", UNSET)

        ln_external_data = d.pop("lnExternalData", UNSET)

        mb_default_value = d.pop("mbDefaultValue", UNSET)

        ln_default_value = d.pop("lnDefaultValue", UNSET)

        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        mb_allowed_referenced_mask_ids_raw = d.pop("mbAllowedReferencedMaskIdsRaw", UNSET)

        ln_allowed_referenced_mask_ids_raw = d.pop("lnAllowedReferencedMaskIdsRaw", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        aspect_line_data_c = cls(
            mb_aspect_id=mb_aspect_id,
            mb_raw_type=mb_raw_type,
            mb_display_name=mb_display_name,
            ln_display_name=ln_display_name,
            mb_key=mb_key,
            ln_key=ln_key,
            mb_raw_flags=mb_raw_flags,
            mb_external_data=mb_external_data,
            ln_external_data=ln_external_data,
            mb_default_value=mb_default_value,
            ln_default_value=ln_default_value,
            mb_name_translation_key=mb_name_translation_key,
            ln_name_translation_key=ln_name_translation_key,
            mb_allowed_referenced_mask_ids_raw=mb_allowed_referenced_mask_ids_raw,
            ln_allowed_referenced_mask_ids_raw=ln_allowed_referenced_mask_ids_raw,
            mb_all_members=mb_all_members,
        )

        aspect_line_data_c.additional_properties = d
        return aspect_line_data_c

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
