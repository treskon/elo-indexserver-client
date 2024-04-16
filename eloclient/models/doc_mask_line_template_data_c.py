from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskLineTemplateDataC")


@_attrs_define
class DocMaskLineTemplateDataC:
    """<p>Bit constants for members of DocMaskLineTemplate</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_l_key (Union[Unset, str]): DB column: linelkey
            mb_name_translation_key (Union[Unset, str]): DB column: linebeztrkey
            ln_validate_expression (Union[Unset, int]): Column length: RegEx to validate user input for entry.
                DB column: validateexpression
            ln_comment (Union[Unset, int]): DB column: linecomment
            ln_comment_translation_key (Union[Unset, int]): DB column: linecommenttrkey
            mb_t_stamp (Union[Unset, str]): DB column: linetstamp
            mb_raw_flags (Union[Unset, str]): DB column: lineflags
            mb_name (Union[Unset, str]): DB column: linebez
            ln_default_value (Union[Unset, int]): DB column: linedefault
            mb_min (Union[Unset, str]): DB column: linemin
            mb_t_stamp_sync (Union[Unset, str]): DB column: linetstampsync
            mb_allowed_referenced_mask_ids_raw (Union[Unset, str]): Member bit: Specifies the {@link DocMask#id} allowed in
                a {@link DocMaskLineC#TYPE_RELATION}.
                DB column: allowedrefmaskids
            ln_name_translation_key (Union[Unset, int]): DB column: linebeztrkey
            ln_name (Union[Unset, int]): DB column: linebez
            ln_internal_acl (Union[Unset, int]): DB column: lineacl
            mb_internal_acl (Union[Unset, str]): DB column: lineacl
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_key (Union[Unset, int]): DB column: linekey
            ln_t_stamp (Union[Unset, int]): DB column: linetstamp
            ln_t_stamp_sync (Union[Unset, int]): DB column: linetstampsync
            mb_validate_expression (Union[Unset, str]): Member bit: RegEx to validate user input for entry.
                DB column: validateexpression
            mb_max (Union[Unset, str]): DB column: linemax
            mb_id (Union[Unset, str]): DB column: mlineno
            mb_comment_translation_key (Union[Unset, str]): DB column: linecommenttrkey
            mb_lock_id (Union[Unset, str]): DB column: linelock
            mb_key (Union[Unset, str]): DB column: linekey
            ln_server_script_name (Union[Unset, int]): DB column: linescript
            ln_allowed_referenced_mask_ids_raw (Union[Unset, int]): Column length: Specifies the {@link DocMask#id} allowed
                in a {@link DocMaskLineC#TYPE_RELATION}.
                DB column: allowedrefmaskids
            ln_external_data (Union[Unset, int]): DB column: lineext
            mb_external_data (Union[Unset, str]): DB column: lineext
            mb_server_script_name (Union[Unset, str]): DB column: linescript
            mb_default_value (Union[Unset, str]): DB column: linedefault
            mb_raw_type (Union[Unset, str]): DB column: linetype
            mb_comment (Union[Unset, str]): DB column: linecomment
    """

    mb_l_key: Union[Unset, str] = UNSET
    mb_name_translation_key: Union[Unset, str] = UNSET
    ln_validate_expression: Union[Unset, int] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    ln_comment_translation_key: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_raw_flags: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_default_value: Union[Unset, int] = UNSET
    mb_min: Union[Unset, str] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_allowed_referenced_mask_ids_raw: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    ln_internal_acl: Union[Unset, int] = UNSET
    mb_internal_acl: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_validate_expression: Union[Unset, str] = UNSET
    mb_max: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_comment_translation_key: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    ln_server_script_name: Union[Unset, int] = UNSET
    ln_allowed_referenced_mask_ids_raw: Union[Unset, int] = UNSET
    ln_external_data: Union[Unset, int] = UNSET
    mb_external_data: Union[Unset, str] = UNSET
    mb_server_script_name: Union[Unset, str] = UNSET
    mb_default_value: Union[Unset, str] = UNSET
    mb_raw_type: Union[Unset, str] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_l_key = self.mb_l_key

        mb_name_translation_key = self.mb_name_translation_key

        ln_validate_expression = self.ln_validate_expression

        ln_comment = self.ln_comment

        ln_comment_translation_key = self.ln_comment_translation_key

        mb_t_stamp = self.mb_t_stamp

        mb_raw_flags = self.mb_raw_flags

        mb_name = self.mb_name

        ln_default_value = self.ln_default_value

        mb_min = self.mb_min

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_allowed_referenced_mask_ids_raw = self.mb_allowed_referenced_mask_ids_raw

        ln_name_translation_key = self.ln_name_translation_key

        ln_name = self.ln_name

        ln_internal_acl = self.ln_internal_acl

        mb_internal_acl = self.mb_internal_acl

        mb_all_members = self.mb_all_members

        ln_key = self.ln_key

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_validate_expression = self.mb_validate_expression

        mb_max = self.mb_max

        mb_id = self.mb_id

        mb_comment_translation_key = self.mb_comment_translation_key

        mb_lock_id = self.mb_lock_id

        mb_key = self.mb_key

        ln_server_script_name = self.ln_server_script_name

        ln_allowed_referenced_mask_ids_raw = self.ln_allowed_referenced_mask_ids_raw

        ln_external_data = self.ln_external_data

        mb_external_data = self.mb_external_data

        mb_server_script_name = self.mb_server_script_name

        mb_default_value = self.mb_default_value

        mb_raw_type = self.mb_raw_type

        mb_comment = self.mb_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_l_key is not UNSET:
            field_dict["mbLKey"] = mb_l_key
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if ln_validate_expression is not UNSET:
            field_dict["lnValidateExpression"] = ln_validate_expression
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if ln_comment_translation_key is not UNSET:
            field_dict["lnCommentTranslationKey"] = ln_comment_translation_key
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_raw_flags is not UNSET:
            field_dict["mbRawFlags"] = mb_raw_flags
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_default_value is not UNSET:
            field_dict["lnDefaultValue"] = ln_default_value
        if mb_min is not UNSET:
            field_dict["mbMin"] = mb_min
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_allowed_referenced_mask_ids_raw is not UNSET:
            field_dict["mbAllowedReferencedMaskIdsRaw"] = mb_allowed_referenced_mask_ids_raw
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if ln_internal_acl is not UNSET:
            field_dict["lnInternalAcl"] = ln_internal_acl
        if mb_internal_acl is not UNSET:
            field_dict["mbInternalAcl"] = mb_internal_acl
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_validate_expression is not UNSET:
            field_dict["mbValidateExpression"] = mb_validate_expression
        if mb_max is not UNSET:
            field_dict["mbMax"] = mb_max
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_comment_translation_key is not UNSET:
            field_dict["mbCommentTranslationKey"] = mb_comment_translation_key
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if ln_server_script_name is not UNSET:
            field_dict["lnServerScriptName"] = ln_server_script_name
        if ln_allowed_referenced_mask_ids_raw is not UNSET:
            field_dict["lnAllowedReferencedMaskIdsRaw"] = ln_allowed_referenced_mask_ids_raw
        if ln_external_data is not UNSET:
            field_dict["lnExternalData"] = ln_external_data
        if mb_external_data is not UNSET:
            field_dict["mbExternalData"] = mb_external_data
        if mb_server_script_name is not UNSET:
            field_dict["mbServerScriptName"] = mb_server_script_name
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
        mb_l_key = d.pop("mbLKey", UNSET)

        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        ln_validate_expression = d.pop("lnValidateExpression", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        ln_comment_translation_key = d.pop("lnCommentTranslationKey", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_raw_flags = d.pop("mbRawFlags", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_default_value = d.pop("lnDefaultValue", UNSET)

        mb_min = d.pop("mbMin", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_allowed_referenced_mask_ids_raw = d.pop("mbAllowedReferencedMaskIdsRaw", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        ln_name = d.pop("lnName", UNSET)

        ln_internal_acl = d.pop("lnInternalAcl", UNSET)

        mb_internal_acl = d.pop("mbInternalAcl", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_validate_expression = d.pop("mbValidateExpression", UNSET)

        mb_max = d.pop("mbMax", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_comment_translation_key = d.pop("mbCommentTranslationKey", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        ln_server_script_name = d.pop("lnServerScriptName", UNSET)

        ln_allowed_referenced_mask_ids_raw = d.pop("lnAllowedReferencedMaskIdsRaw", UNSET)

        ln_external_data = d.pop("lnExternalData", UNSET)

        mb_external_data = d.pop("mbExternalData", UNSET)

        mb_server_script_name = d.pop("mbServerScriptName", UNSET)

        mb_default_value = d.pop("mbDefaultValue", UNSET)

        mb_raw_type = d.pop("mbRawType", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        doc_mask_line_template_data_c = cls(
            mb_l_key=mb_l_key,
            mb_name_translation_key=mb_name_translation_key,
            ln_validate_expression=ln_validate_expression,
            ln_comment=ln_comment,
            ln_comment_translation_key=ln_comment_translation_key,
            mb_t_stamp=mb_t_stamp,
            mb_raw_flags=mb_raw_flags,
            mb_name=mb_name,
            ln_default_value=ln_default_value,
            mb_min=mb_min,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_allowed_referenced_mask_ids_raw=mb_allowed_referenced_mask_ids_raw,
            ln_name_translation_key=ln_name_translation_key,
            ln_name=ln_name,
            ln_internal_acl=ln_internal_acl,
            mb_internal_acl=mb_internal_acl,
            mb_all_members=mb_all_members,
            ln_key=ln_key,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_validate_expression=mb_validate_expression,
            mb_max=mb_max,
            mb_id=mb_id,
            mb_comment_translation_key=mb_comment_translation_key,
            mb_lock_id=mb_lock_id,
            mb_key=mb_key,
            ln_server_script_name=ln_server_script_name,
            ln_allowed_referenced_mask_ids_raw=ln_allowed_referenced_mask_ids_raw,
            ln_external_data=ln_external_data,
            mb_external_data=mb_external_data,
            mb_server_script_name=mb_server_script_name,
            mb_default_value=mb_default_value,
            mb_raw_type=mb_raw_type,
            mb_comment=mb_comment,
        )

        doc_mask_line_template_data_c.additional_properties = d
        return doc_mask_line_template_data_c

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
