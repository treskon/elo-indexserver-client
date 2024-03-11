from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskLineDataC")


@_attrs_define
class DocMaskLineDataC:
    """<p>
    Bit constants for members of DocMaskLine
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_mask_id (Union[Unset, str]): DB column: maskno
            mb_id (Union[Unset, str]): DB column: mlineno
            mb_raw_type (Union[Unset, str]): DB column: linetype
            mb_name (Union[Unset, str]): DB column: linebez
            ln_name (Union[Unset, int]): DB column: linebez
            mb_key (Union[Unset, str]): DB column: linekey
            ln_key (Union[Unset, int]): DB column: linekey
            mb_min (Union[Unset, str]): DB column: linemin
            mb_max (Union[Unset, str]): DB column: linemax
            mb_l_key (Union[Unset, str]): DB column: linelkey
            mb_raw_flags (Union[Unset, str]): DB column: lineflags
            mb_comment (Union[Unset, str]): DB column: linecomment
            ln_comment (Union[Unset, int]): DB column: linecomment
            mb_external_data (Union[Unset, str]): Member bit: External data.
                DB column: lineext
            ln_external_data (Union[Unset, int]): Column length: External data.
                DB column: lineext
            mb_internal_acl (Union[Unset, str]): Member bit: Internal acl.
                DB column: lineacl
            ln_internal_acl (Union[Unset, int]): Column length: Internal acl.
                DB column: lineacl
            mb_default_value (Union[Unset, str]): Member bit: This value is assigned to the ObjKey.data element for a new
                Sord object.
                DB column: linedefault
            ln_default_value (Union[Unset, int]): Column length: This value is assigned to the ObjKey.data element for a new
                Sord object.
                DB column: linedefault
            mb_tab_index (Union[Unset, str]): Member bit: This value represents the number of the tab, this line has to
                appear on.
                DB column: linetab
            mb_server_script_name (Union[Unset, str]): Member bit: A script or plugin at the server can serve as the data
                source of a dynamic keyword DB column:
                linescript
            ln_server_script_name (Union[Unset, int]): Column length: A script or plugin at the server can serve as the data
                source of a dynamic keyword DB column:
                linescript
            mb_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link DocMaskLine#name}.
                DB column: linebeztrkey
            ln_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link DocMaskLine#name}.
                DB column: linebeztrkey
            mb_comment_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link DocMaskLine#comment}.
                DB column: linecommenttrkey
            ln_comment_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link
                DocMaskLine#comment}.
                DB column: linecommenttrkey
            mb_validate_expression (Union[Unset, str]): Member bit: RegEx to validate user input for entry.
                DB column: validateexpression
            ln_validate_expression (Union[Unset, int]): Column length: RegEx to validate user input for entry.
                DB column: validateexpression
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

    mb_mask_id: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_raw_type: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_key: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    mb_min: Union[Unset, str] = UNSET
    mb_max: Union[Unset, str] = UNSET
    mb_l_key: Union[Unset, str] = UNSET
    mb_raw_flags: Union[Unset, str] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    mb_external_data: Union[Unset, str] = UNSET
    ln_external_data: Union[Unset, int] = UNSET
    mb_internal_acl: Union[Unset, str] = UNSET
    ln_internal_acl: Union[Unset, int] = UNSET
    mb_default_value: Union[Unset, str] = UNSET
    ln_default_value: Union[Unset, int] = UNSET
    mb_tab_index: Union[Unset, str] = UNSET
    mb_server_script_name: Union[Unset, str] = UNSET
    ln_server_script_name: Union[Unset, int] = UNSET
    mb_name_translation_key: Union[Unset, str] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    mb_comment_translation_key: Union[Unset, str] = UNSET
    ln_comment_translation_key: Union[Unset, int] = UNSET
    mb_validate_expression: Union[Unset, str] = UNSET
    ln_validate_expression: Union[Unset, int] = UNSET
    mb_allowed_referenced_mask_ids_raw: Union[Unset, str] = UNSET
    ln_allowed_referenced_mask_ids_raw: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_mask_id = self.mb_mask_id
        mb_id = self.mb_id
        mb_raw_type = self.mb_raw_type
        mb_name = self.mb_name
        ln_name = self.ln_name
        mb_key = self.mb_key
        ln_key = self.ln_key
        mb_min = self.mb_min
        mb_max = self.mb_max
        mb_l_key = self.mb_l_key
        mb_raw_flags = self.mb_raw_flags
        mb_comment = self.mb_comment
        ln_comment = self.ln_comment
        mb_external_data = self.mb_external_data
        ln_external_data = self.ln_external_data
        mb_internal_acl = self.mb_internal_acl
        ln_internal_acl = self.ln_internal_acl
        mb_default_value = self.mb_default_value
        ln_default_value = self.ln_default_value
        mb_tab_index = self.mb_tab_index
        mb_server_script_name = self.mb_server_script_name
        ln_server_script_name = self.ln_server_script_name
        mb_name_translation_key = self.mb_name_translation_key
        ln_name_translation_key = self.ln_name_translation_key
        mb_comment_translation_key = self.mb_comment_translation_key
        ln_comment_translation_key = self.ln_comment_translation_key
        mb_validate_expression = self.mb_validate_expression
        ln_validate_expression = self.ln_validate_expression
        mb_allowed_referenced_mask_ids_raw = self.mb_allowed_referenced_mask_ids_raw
        ln_allowed_referenced_mask_ids_raw = self.ln_allowed_referenced_mask_ids_raw
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_mask_id is not UNSET:
            field_dict["mbMaskId"] = mb_mask_id
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_raw_type is not UNSET:
            field_dict["mbRawType"] = mb_raw_type
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if mb_min is not UNSET:
            field_dict["mbMin"] = mb_min
        if mb_max is not UNSET:
            field_dict["mbMax"] = mb_max
        if mb_l_key is not UNSET:
            field_dict["mbLKey"] = mb_l_key
        if mb_raw_flags is not UNSET:
            field_dict["mbRawFlags"] = mb_raw_flags
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if mb_external_data is not UNSET:
            field_dict["mbExternalData"] = mb_external_data
        if ln_external_data is not UNSET:
            field_dict["lnExternalData"] = ln_external_data
        if mb_internal_acl is not UNSET:
            field_dict["mbInternalAcl"] = mb_internal_acl
        if ln_internal_acl is not UNSET:
            field_dict["lnInternalAcl"] = ln_internal_acl
        if mb_default_value is not UNSET:
            field_dict["mbDefaultValue"] = mb_default_value
        if ln_default_value is not UNSET:
            field_dict["lnDefaultValue"] = ln_default_value
        if mb_tab_index is not UNSET:
            field_dict["mbTabIndex"] = mb_tab_index
        if mb_server_script_name is not UNSET:
            field_dict["mbServerScriptName"] = mb_server_script_name
        if ln_server_script_name is not UNSET:
            field_dict["lnServerScriptName"] = ln_server_script_name
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if mb_comment_translation_key is not UNSET:
            field_dict["mbCommentTranslationKey"] = mb_comment_translation_key
        if ln_comment_translation_key is not UNSET:
            field_dict["lnCommentTranslationKey"] = ln_comment_translation_key
        if mb_validate_expression is not UNSET:
            field_dict["mbValidateExpression"] = mb_validate_expression
        if ln_validate_expression is not UNSET:
            field_dict["lnValidateExpression"] = ln_validate_expression
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
        mb_mask_id = d.pop("mbMaskId", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_raw_type = d.pop("mbRawType", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        mb_min = d.pop("mbMin", UNSET)

        mb_max = d.pop("mbMax", UNSET)

        mb_l_key = d.pop("mbLKey", UNSET)

        mb_raw_flags = d.pop("mbRawFlags", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        mb_external_data = d.pop("mbExternalData", UNSET)

        ln_external_data = d.pop("lnExternalData", UNSET)

        mb_internal_acl = d.pop("mbInternalAcl", UNSET)

        ln_internal_acl = d.pop("lnInternalAcl", UNSET)

        mb_default_value = d.pop("mbDefaultValue", UNSET)

        ln_default_value = d.pop("lnDefaultValue", UNSET)

        mb_tab_index = d.pop("mbTabIndex", UNSET)

        mb_server_script_name = d.pop("mbServerScriptName", UNSET)

        ln_server_script_name = d.pop("lnServerScriptName", UNSET)

        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        mb_comment_translation_key = d.pop("mbCommentTranslationKey", UNSET)

        ln_comment_translation_key = d.pop("lnCommentTranslationKey", UNSET)

        mb_validate_expression = d.pop("mbValidateExpression", UNSET)

        ln_validate_expression = d.pop("lnValidateExpression", UNSET)

        mb_allowed_referenced_mask_ids_raw = d.pop("mbAllowedReferencedMaskIdsRaw", UNSET)

        ln_allowed_referenced_mask_ids_raw = d.pop("lnAllowedReferencedMaskIdsRaw", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        doc_mask_line_data_c = cls(
            mb_mask_id=mb_mask_id,
            mb_id=mb_id,
            mb_raw_type=mb_raw_type,
            mb_name=mb_name,
            ln_name=ln_name,
            mb_key=mb_key,
            ln_key=ln_key,
            mb_min=mb_min,
            mb_max=mb_max,
            mb_l_key=mb_l_key,
            mb_raw_flags=mb_raw_flags,
            mb_comment=mb_comment,
            ln_comment=ln_comment,
            mb_external_data=mb_external_data,
            ln_external_data=ln_external_data,
            mb_internal_acl=mb_internal_acl,
            ln_internal_acl=ln_internal_acl,
            mb_default_value=mb_default_value,
            ln_default_value=ln_default_value,
            mb_tab_index=mb_tab_index,
            mb_server_script_name=mb_server_script_name,
            ln_server_script_name=ln_server_script_name,
            mb_name_translation_key=mb_name_translation_key,
            ln_name_translation_key=ln_name_translation_key,
            mb_comment_translation_key=mb_comment_translation_key,
            ln_comment_translation_key=ln_comment_translation_key,
            mb_validate_expression=mb_validate_expression,
            ln_validate_expression=ln_validate_expression,
            mb_allowed_referenced_mask_ids_raw=mb_allowed_referenced_mask_ids_raw,
            ln_allowed_referenced_mask_ids_raw=ln_allowed_referenced_mask_ids_raw,
            mb_all_members=mb_all_members,
        )

        doc_mask_line_data_c.additional_properties = d
        return doc_mask_line_data_c

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
