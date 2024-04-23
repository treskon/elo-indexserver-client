from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask_line_template_z import DocMaskLineTemplateZ


T = TypeVar("T", bound="DocMaskLineTemplateC")


@_attrs_define
class DocMaskLineTemplateC:
    """<p>
    Constants related to class <code>DocMaskLineTemplate</code>.

        Attributes:
            mb_all (Union[Unset, DocMaskLineTemplateZ]): This class encapsulates the constants of the DocMaskLineTemplateC
                class.
            mb_type (Union[Unset, str]): Member bit: The type of the line information.
                This can be one of the
                 <code>DocMaskLineC.LINETYPE_*</code> constants.
            mb_version (Union[Unset, str]):
            mb_hidden (Union[Unset, str]):
            mb_translate (Union[Unset, str]):
            ln_acl (Union[Unset, int]): ACL length
            mb_important (Union[Unset, str]):
            mb_allowed_mask_ids_for_keywording_relation (Union[Unset, str]): Member bit: allowedMaskIds
            mb_read_only (Union[Unset, str]):
            mb_postfix_asterix (Union[Unset, str]):
            mb_only_buzzwords (Union[Unset, str]):
            mb_only_lock (Union[Unset, DocMaskLineTemplateZ]): This class encapsulates the constants of the
                DocMaskLineTemplateC class.
            mb_prefix_asterix (Union[Unset, str]):
            mb_acl (Union[Unset, str]): Member bit: ACL
            mb_acl_items (Union[Unset, str]):
            mb_flags (Union[Unset, str]): Member bit: Line flags
    """

    mb_all: Union[Unset, "DocMaskLineTemplateZ"] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_version: Union[Unset, str] = UNSET
    mb_hidden: Union[Unset, str] = UNSET
    mb_translate: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_important: Union[Unset, str] = UNSET
    mb_allowed_mask_ids_for_keywording_relation: Union[Unset, str] = UNSET
    mb_read_only: Union[Unset, str] = UNSET
    mb_postfix_asterix: Union[Unset, str] = UNSET
    mb_only_buzzwords: Union[Unset, str] = UNSET
    mb_only_lock: Union[Unset, "DocMaskLineTemplateZ"] = UNSET
    mb_prefix_asterix: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    mb_acl_items: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_type = self.mb_type

        mb_version = self.mb_version

        mb_hidden = self.mb_hidden

        mb_translate = self.mb_translate

        ln_acl = self.ln_acl

        mb_important = self.mb_important

        mb_allowed_mask_ids_for_keywording_relation = self.mb_allowed_mask_ids_for_keywording_relation

        mb_read_only = self.mb_read_only

        mb_postfix_asterix = self.mb_postfix_asterix

        mb_only_buzzwords = self.mb_only_buzzwords

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_prefix_asterix = self.mb_prefix_asterix

        mb_acl = self.mb_acl

        mb_acl_items = self.mb_acl_items

        mb_flags = self.mb_flags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_version is not UNSET:
            field_dict["mbVersion"] = mb_version
        if mb_hidden is not UNSET:
            field_dict["mbHidden"] = mb_hidden
        if mb_translate is not UNSET:
            field_dict["mbTranslate"] = mb_translate
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_important is not UNSET:
            field_dict["mbImportant"] = mb_important
        if mb_allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["mbAllowedMaskIdsForKeywordingRelation"] = mb_allowed_mask_ids_for_keywording_relation
        if mb_read_only is not UNSET:
            field_dict["mbReadOnly"] = mb_read_only
        if mb_postfix_asterix is not UNSET:
            field_dict["mbPostfixAsterix"] = mb_postfix_asterix
        if mb_only_buzzwords is not UNSET:
            field_dict["mbOnlyBuzzwords"] = mb_only_buzzwords
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_prefix_asterix is not UNSET:
            field_dict["mbPrefixAsterix"] = mb_prefix_asterix
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if mb_acl_items is not UNSET:
            field_dict["mbAclItems"] = mb_acl_items
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask_line_template_z import DocMaskLineTemplateZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, DocMaskLineTemplateZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = DocMaskLineTemplateZ.from_dict(_mb_all)

        mb_type = d.pop("mbType", UNSET)

        mb_version = d.pop("mbVersion", UNSET)

        mb_hidden = d.pop("mbHidden", UNSET)

        mb_translate = d.pop("mbTranslate", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_important = d.pop("mbImportant", UNSET)

        mb_allowed_mask_ids_for_keywording_relation = d.pop("mbAllowedMaskIdsForKeywordingRelation", UNSET)

        mb_read_only = d.pop("mbReadOnly", UNSET)

        mb_postfix_asterix = d.pop("mbPostfixAsterix", UNSET)

        mb_only_buzzwords = d.pop("mbOnlyBuzzwords", UNSET)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, DocMaskLineTemplateZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = DocMaskLineTemplateZ.from_dict(_mb_only_lock)

        mb_prefix_asterix = d.pop("mbPrefixAsterix", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        mb_acl_items = d.pop("mbAclItems", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        doc_mask_line_template_c = cls(
            mb_all=mb_all,
            mb_type=mb_type,
            mb_version=mb_version,
            mb_hidden=mb_hidden,
            mb_translate=mb_translate,
            ln_acl=ln_acl,
            mb_important=mb_important,
            mb_allowed_mask_ids_for_keywording_relation=mb_allowed_mask_ids_for_keywording_relation,
            mb_read_only=mb_read_only,
            mb_postfix_asterix=mb_postfix_asterix,
            mb_only_buzzwords=mb_only_buzzwords,
            mb_only_lock=mb_only_lock,
            mb_prefix_asterix=mb_prefix_asterix,
            mb_acl=mb_acl,
            mb_acl_items=mb_acl_items,
            mb_flags=mb_flags,
        )

        doc_mask_line_template_c.additional_properties = d
        return doc_mask_line_template_c

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
