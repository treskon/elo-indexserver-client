from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectLineDataC")


@_attrs_define
class AspectLineDataC:
    """<p>Bit constants for members of AspectLine</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link AspectLine#displayName}.
                DB column: linenametrkey
            ln_sub_type (Union[Unset, int]): Column length: This field can be used by clients to determine a subtype of the
                given type.
                For the purpose of
                 DB column: subtype
            ln_comment (Union[Unset, int]): Column length: Quickinfo text for the attribute.
                DB column: linecomment
            ln_comment_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link
                AspectLine#comment}.
                DB column: linecommenttrkey
            mb_raw_flags (Union[Unset, str]): Member bit: Internal flags representation.
                DB column: lineflags
            ln_default_value (Union[Unset, int]): Column length: This value is assigned to the element for a new Sord
                object.
                DB column: linedefault
            mb_allowed_referenced_mask_ids_raw (Union[Unset, str]): Member bit: Specifies the {@link DocMask#id} allowed in
                a {@link AspectLineC#TYPE_RELATION}.
                DB column: allowedrefmaskids
            ln_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link
                AspectLine#displayName}.
                DB column: linenametrkey
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_key (Union[Unset, int]): Column length: The attribute identifier.
                DB column: linekey
            mb_keyword_list_id (Union[Unset, str]): Member bit: Keyword List ID.
                DB column: swlgroupid
            ln_keyword_list_id (Union[Unset, int]): Column length: Keyword List ID.
                DB column: swlgroupid
            mb_dynamic_keyword_reference (Union[Unset, str]): Member bit: A script or plugin at the server can serve as the
                data source of a dynamic keyword list.
                This
                 DB column: dynkeywordreference
            mb_comment_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link AspectLine#comment}.
                DB column: linecommenttrkey
            mb_aspect_id (Union[Unset, str]): Member bit: This line information belongs to an aspect with the ID AspectId.
                DB column: aspectid
            mb_key (Union[Unset, str]): Member bit: The attribute identifier.
                DB column: linekey
            mb_sub_type (Union[Unset, str]): Member bit: This field can be used by clients to determine a subtype of the
                given type.
                For the purpose of
                 DB column: subtype
            ln_allowed_referenced_mask_ids_raw (Union[Unset, int]): Column length: Specifies the {@link DocMask#id} allowed
                in a {@link AspectLineC#TYPE_RELATION}.
                DB column: allowedrefmaskids
            ln_dynamic_keyword_reference (Union[Unset, int]): Column length: A script or plugin at the server can serve as
                the data source of a dynamic keyword list.
                This
                 DB column: dynkeywordreference
            ln_external_data (Union[Unset, int]): Column length: External data. Can be used to store an arbitary string.
                DB column: lineext
            mb_external_data (Union[Unset, str]): Member bit: External data. Can be used to store an arbitary string.
                DB column: lineext
            mb_display_name (Union[Unset, str]): Member bit: The display name of the attribute. This value is displayed in
                the lable before the edit field.
                DB column: linedisplayName
            ln_display_name (Union[Unset, int]): Column length: The display name of the attribute. This value is displayed
                in the lable before the edit field.
                DB column: linedisplayName
            mb_default_value (Union[Unset, str]): Member bit: This value is assigned to the element for a new Sord object.
                DB column: linedefault
            mb_raw_type (Union[Unset, str]): Member bit: The type of the line information.
                <br>
                 DB column: linetype
            mb_comment (Union[Unset, str]): Member bit: Quickinfo text for the attribute.
                DB column: linecomment
    """

    mb_name_translation_key: Union[Unset, str] = UNSET
    ln_sub_type: Union[Unset, int] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    ln_comment_translation_key: Union[Unset, int] = UNSET
    mb_raw_flags: Union[Unset, str] = UNSET
    ln_default_value: Union[Unset, int] = UNSET
    mb_allowed_referenced_mask_ids_raw: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    mb_keyword_list_id: Union[Unset, str] = UNSET
    ln_keyword_list_id: Union[Unset, int] = UNSET
    mb_dynamic_keyword_reference: Union[Unset, str] = UNSET
    mb_comment_translation_key: Union[Unset, str] = UNSET
    mb_aspect_id: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    mb_sub_type: Union[Unset, str] = UNSET
    ln_allowed_referenced_mask_ids_raw: Union[Unset, int] = UNSET
    ln_dynamic_keyword_reference: Union[Unset, int] = UNSET
    ln_external_data: Union[Unset, int] = UNSET
    mb_external_data: Union[Unset, str] = UNSET
    mb_display_name: Union[Unset, str] = UNSET
    ln_display_name: Union[Unset, int] = UNSET
    mb_default_value: Union[Unset, str] = UNSET
    mb_raw_type: Union[Unset, str] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_name_translation_key = self.mb_name_translation_key

        ln_sub_type = self.ln_sub_type

        ln_comment = self.ln_comment

        ln_comment_translation_key = self.ln_comment_translation_key

        mb_raw_flags = self.mb_raw_flags

        ln_default_value = self.ln_default_value

        mb_allowed_referenced_mask_ids_raw = self.mb_allowed_referenced_mask_ids_raw

        ln_name_translation_key = self.ln_name_translation_key

        mb_all_members = self.mb_all_members

        ln_key = self.ln_key

        mb_keyword_list_id = self.mb_keyword_list_id

        ln_keyword_list_id = self.ln_keyword_list_id

        mb_dynamic_keyword_reference = self.mb_dynamic_keyword_reference

        mb_comment_translation_key = self.mb_comment_translation_key

        mb_aspect_id = self.mb_aspect_id

        mb_key = self.mb_key

        mb_sub_type = self.mb_sub_type

        ln_allowed_referenced_mask_ids_raw = self.ln_allowed_referenced_mask_ids_raw

        ln_dynamic_keyword_reference = self.ln_dynamic_keyword_reference

        ln_external_data = self.ln_external_data

        mb_external_data = self.mb_external_data

        mb_display_name = self.mb_display_name

        ln_display_name = self.ln_display_name

        mb_default_value = self.mb_default_value

        mb_raw_type = self.mb_raw_type

        mb_comment = self.mb_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if ln_sub_type is not UNSET:
            field_dict["lnSubType"] = ln_sub_type
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if ln_comment_translation_key is not UNSET:
            field_dict["lnCommentTranslationKey"] = ln_comment_translation_key
        if mb_raw_flags is not UNSET:
            field_dict["mbRawFlags"] = mb_raw_flags
        if ln_default_value is not UNSET:
            field_dict["lnDefaultValue"] = ln_default_value
        if mb_allowed_referenced_mask_ids_raw is not UNSET:
            field_dict["mbAllowedReferencedMaskIdsRaw"] = mb_allowed_referenced_mask_ids_raw
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if mb_keyword_list_id is not UNSET:
            field_dict["mbKeywordListId"] = mb_keyword_list_id
        if ln_keyword_list_id is not UNSET:
            field_dict["lnKeywordListId"] = ln_keyword_list_id
        if mb_dynamic_keyword_reference is not UNSET:
            field_dict["mbDynamicKeywordReference"] = mb_dynamic_keyword_reference
        if mb_comment_translation_key is not UNSET:
            field_dict["mbCommentTranslationKey"] = mb_comment_translation_key
        if mb_aspect_id is not UNSET:
            field_dict["mbAspectId"] = mb_aspect_id
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if mb_sub_type is not UNSET:
            field_dict["mbSubType"] = mb_sub_type
        if ln_allowed_referenced_mask_ids_raw is not UNSET:
            field_dict["lnAllowedReferencedMaskIdsRaw"] = ln_allowed_referenced_mask_ids_raw
        if ln_dynamic_keyword_reference is not UNSET:
            field_dict["lnDynamicKeywordReference"] = ln_dynamic_keyword_reference
        if ln_external_data is not UNSET:
            field_dict["lnExternalData"] = ln_external_data
        if mb_external_data is not UNSET:
            field_dict["mbExternalData"] = mb_external_data
        if mb_display_name is not UNSET:
            field_dict["mbDisplayName"] = mb_display_name
        if ln_display_name is not UNSET:
            field_dict["lnDisplayName"] = ln_display_name
        if mb_default_value is not UNSET:
            field_dict["mbDefaultValue"] = mb_default_value
        if mb_raw_type is not UNSET:
            field_dict["mbRawType"] = mb_raw_type
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        ln_sub_type = d.pop("lnSubType", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        ln_comment_translation_key = d.pop("lnCommentTranslationKey", UNSET)

        mb_raw_flags = d.pop("mbRawFlags", UNSET)

        ln_default_value = d.pop("lnDefaultValue", UNSET)

        mb_allowed_referenced_mask_ids_raw = d.pop("mbAllowedReferencedMaskIdsRaw", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        mb_keyword_list_id = d.pop("mbKeywordListId", UNSET)

        ln_keyword_list_id = d.pop("lnKeywordListId", UNSET)

        mb_dynamic_keyword_reference = d.pop("mbDynamicKeywordReference", UNSET)

        mb_comment_translation_key = d.pop("mbCommentTranslationKey", UNSET)

        mb_aspect_id = d.pop("mbAspectId", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        mb_sub_type = d.pop("mbSubType", UNSET)

        ln_allowed_referenced_mask_ids_raw = d.pop("lnAllowedReferencedMaskIdsRaw", UNSET)

        ln_dynamic_keyword_reference = d.pop("lnDynamicKeywordReference", UNSET)

        ln_external_data = d.pop("lnExternalData", UNSET)

        mb_external_data = d.pop("mbExternalData", UNSET)

        mb_display_name = d.pop("mbDisplayName", UNSET)

        ln_display_name = d.pop("lnDisplayName", UNSET)

        mb_default_value = d.pop("mbDefaultValue", UNSET)

        mb_raw_type = d.pop("mbRawType", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        aspect_line_data_c = cls(
            mb_name_translation_key=mb_name_translation_key,
            ln_sub_type=ln_sub_type,
            ln_comment=ln_comment,
            ln_comment_translation_key=ln_comment_translation_key,
            mb_raw_flags=mb_raw_flags,
            ln_default_value=ln_default_value,
            mb_allowed_referenced_mask_ids_raw=mb_allowed_referenced_mask_ids_raw,
            ln_name_translation_key=ln_name_translation_key,
            mb_all_members=mb_all_members,
            ln_key=ln_key,
            mb_keyword_list_id=mb_keyword_list_id,
            ln_keyword_list_id=ln_keyword_list_id,
            mb_dynamic_keyword_reference=mb_dynamic_keyword_reference,
            mb_comment_translation_key=mb_comment_translation_key,
            mb_aspect_id=mb_aspect_id,
            mb_key=mb_key,
            mb_sub_type=mb_sub_type,
            ln_allowed_referenced_mask_ids_raw=ln_allowed_referenced_mask_ids_raw,
            ln_dynamic_keyword_reference=ln_dynamic_keyword_reference,
            ln_external_data=ln_external_data,
            mb_external_data=mb_external_data,
            mb_display_name=mb_display_name,
            ln_display_name=ln_display_name,
            mb_default_value=mb_default_value,
            mb_raw_type=mb_raw_type,
            mb_comment=mb_comment,
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
