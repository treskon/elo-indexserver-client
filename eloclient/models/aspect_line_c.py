from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectLineC")


@_attrs_define
class AspectLineC:
    """<p>
    Constants for class <code>AspectLine</code>
     </p>
     <p>
     Copyright: Copyright (c) 2019
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_type (Union[Unset, str]): Member bit: The type of the line information. This can be one of the
                <code>DocMaskLineC.
                LINETYPE_*</code>
                 constants.
            mb_flags (Union[Unset, str]): Member bit: Line flags
            mb_allowed_mask_ids_for_keywording_relation (Union[Unset, str]): Member bit: allowedMaskIds
            type_offset_types_for_aspects (Union[Unset, int]): Types above this value are supported only by newer docMasks
                with aspects.
            mb_postfix_asterix (Union[Unset, str]):
            mb_prefix_asterix (Union[Unset, str]):
            mb_translate (Union[Unset, str]):
            mb_important (Union[Unset, str]):
    """

    mb_type: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_allowed_mask_ids_for_keywording_relation: Union[Unset, str] = UNSET
    type_offset_types_for_aspects: Union[Unset, int] = UNSET
    mb_postfix_asterix: Union[Unset, str] = UNSET
    mb_prefix_asterix: Union[Unset, str] = UNSET
    mb_translate: Union[Unset, str] = UNSET
    mb_important: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_type = self.mb_type
        mb_flags = self.mb_flags
        mb_allowed_mask_ids_for_keywording_relation = self.mb_allowed_mask_ids_for_keywording_relation
        type_offset_types_for_aspects = self.type_offset_types_for_aspects
        mb_postfix_asterix = self.mb_postfix_asterix
        mb_prefix_asterix = self.mb_prefix_asterix
        mb_translate = self.mb_translate
        mb_important = self.mb_important

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["mbAllowedMaskIdsForKeywordingRelation"] = mb_allowed_mask_ids_for_keywording_relation
        if type_offset_types_for_aspects is not UNSET:
            field_dict["TYPE_OFFSET_TYPES_FOR_ASPECTS"] = type_offset_types_for_aspects
        if mb_postfix_asterix is not UNSET:
            field_dict["mbPostfixAsterix"] = mb_postfix_asterix
        if mb_prefix_asterix is not UNSET:
            field_dict["mbPrefixAsterix"] = mb_prefix_asterix
        if mb_translate is not UNSET:
            field_dict["mbTranslate"] = mb_translate
        if mb_important is not UNSET:
            field_dict["mbImportant"] = mb_important

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_type = d.pop("mbType", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_allowed_mask_ids_for_keywording_relation = d.pop("mbAllowedMaskIdsForKeywordingRelation", UNSET)

        type_offset_types_for_aspects = d.pop("TYPE_OFFSET_TYPES_FOR_ASPECTS", UNSET)

        mb_postfix_asterix = d.pop("mbPostfixAsterix", UNSET)

        mb_prefix_asterix = d.pop("mbPrefixAsterix", UNSET)

        mb_translate = d.pop("mbTranslate", UNSET)

        mb_important = d.pop("mbImportant", UNSET)

        aspect_line_c = cls(
            mb_type=mb_type,
            mb_flags=mb_flags,
            mb_allowed_mask_ids_for_keywording_relation=mb_allowed_mask_ids_for_keywording_relation,
            type_offset_types_for_aspects=type_offset_types_for_aspects,
            mb_postfix_asterix=mb_postfix_asterix,
            mb_prefix_asterix=mb_prefix_asterix,
            mb_translate=mb_translate,
            mb_important=mb_important,
        )

        aspect_line_c.additional_properties = d
        return aspect_line_c

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
