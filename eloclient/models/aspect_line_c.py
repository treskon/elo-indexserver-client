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
            type_user (Union[Unset, int]): Aspect line contains user guid information.
            type_status (Union[Unset, int]): Aspect line contains a text which is defined by a mandatory keyword list with a
                localized
                display value.
            mb_type (Union[Unset, str]): Member bit: The type of the line information.
                This can be one of the
                 <code>DocMaskLineC.LINETYPE_*</code> constants.
            type_relation (Union[Unset, int]): Aspect line contains a relation.
                A Relation consists of a {@link Sord#guid} which references a
                 {@link Sord}. with a allowed DocMask {@link DocMaskDetails#keywordingRelationAllowed}.
            mb_translate (Union[Unset, str]):
            mb_important (Union[Unset, str]):
            mb_allowed_mask_ids_for_keywording_relation (Union[Unset, str]): Member bit: allowedMaskIds
            type_offset_types_for_aspects (Union[Unset, int]): Types above this value are supported only by newer docMasks
                with aspects.
            mb_postfix_asterix (Union[Unset, str]):
            mb_prefix_asterix (Union[Unset, str]):
            type_double (Union[Unset, int]): Aspect line contains a floating point number value with 15 significant digits.
                To assign a
                 value of this type to {@link IndexValue#doubleValue}, the String representation has to conform
                 to the Double.toString() method of Java. Use dot to separate the fraction part and character
                 'E' to prefix the exponent.
            type_integer (Union[Unset, int]): Aspect line contains a number value without fraction in the range of (-2^31)
                to (2^31)-1.
            mb_flags (Union[Unset, str]): Member bit: Line flags
            type_text (Union[Unset, int]): Aspect line contains text information.
            type_iso_date_time (Union[Unset, int]): Aspect line contains a date in ISO format with time digits.
            type_iso_date_only (Union[Unset, int]): Aspect line contains a date in ISO format without time digits.
    """

    type_user: Union[Unset, int] = UNSET
    type_status: Union[Unset, int] = UNSET
    mb_type: Union[Unset, str] = UNSET
    type_relation: Union[Unset, int] = UNSET
    mb_translate: Union[Unset, str] = UNSET
    mb_important: Union[Unset, str] = UNSET
    mb_allowed_mask_ids_for_keywording_relation: Union[Unset, str] = UNSET
    type_offset_types_for_aspects: Union[Unset, int] = UNSET
    mb_postfix_asterix: Union[Unset, str] = UNSET
    mb_prefix_asterix: Union[Unset, str] = UNSET
    type_double: Union[Unset, int] = UNSET
    type_integer: Union[Unset, int] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    type_text: Union[Unset, int] = UNSET
    type_iso_date_time: Union[Unset, int] = UNSET
    type_iso_date_only: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_user = self.type_user

        type_status = self.type_status

        mb_type = self.mb_type

        type_relation = self.type_relation

        mb_translate = self.mb_translate

        mb_important = self.mb_important

        mb_allowed_mask_ids_for_keywording_relation = self.mb_allowed_mask_ids_for_keywording_relation

        type_offset_types_for_aspects = self.type_offset_types_for_aspects

        mb_postfix_asterix = self.mb_postfix_asterix

        mb_prefix_asterix = self.mb_prefix_asterix

        type_double = self.type_double

        type_integer = self.type_integer

        mb_flags = self.mb_flags

        type_text = self.type_text

        type_iso_date_time = self.type_iso_date_time

        type_iso_date_only = self.type_iso_date_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_user is not UNSET:
            field_dict["TYPE_USER"] = type_user
        if type_status is not UNSET:
            field_dict["TYPE_STATUS"] = type_status
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if type_relation is not UNSET:
            field_dict["TYPE_RELATION"] = type_relation
        if mb_translate is not UNSET:
            field_dict["mbTranslate"] = mb_translate
        if mb_important is not UNSET:
            field_dict["mbImportant"] = mb_important
        if mb_allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["mbAllowedMaskIdsForKeywordingRelation"] = mb_allowed_mask_ids_for_keywording_relation
        if type_offset_types_for_aspects is not UNSET:
            field_dict["TYPE_OFFSET_TYPES_FOR_ASPECTS"] = type_offset_types_for_aspects
        if mb_postfix_asterix is not UNSET:
            field_dict["mbPostfixAsterix"] = mb_postfix_asterix
        if mb_prefix_asterix is not UNSET:
            field_dict["mbPrefixAsterix"] = mb_prefix_asterix
        if type_double is not UNSET:
            field_dict["TYPE_DOUBLE"] = type_double
        if type_integer is not UNSET:
            field_dict["TYPE_INTEGER"] = type_integer
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if type_text is not UNSET:
            field_dict["TYPE_TEXT"] = type_text
        if type_iso_date_time is not UNSET:
            field_dict["TYPE_ISO_DATE_TIME"] = type_iso_date_time
        if type_iso_date_only is not UNSET:
            field_dict["TYPE_ISO_DATE_ONLY"] = type_iso_date_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_user = d.pop("TYPE_USER", UNSET)

        type_status = d.pop("TYPE_STATUS", UNSET)

        mb_type = d.pop("mbType", UNSET)

        type_relation = d.pop("TYPE_RELATION", UNSET)

        mb_translate = d.pop("mbTranslate", UNSET)

        mb_important = d.pop("mbImportant", UNSET)

        mb_allowed_mask_ids_for_keywording_relation = d.pop("mbAllowedMaskIdsForKeywordingRelation", UNSET)

        type_offset_types_for_aspects = d.pop("TYPE_OFFSET_TYPES_FOR_ASPECTS", UNSET)

        mb_postfix_asterix = d.pop("mbPostfixAsterix", UNSET)

        mb_prefix_asterix = d.pop("mbPrefixAsterix", UNSET)

        type_double = d.pop("TYPE_DOUBLE", UNSET)

        type_integer = d.pop("TYPE_INTEGER", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        type_text = d.pop("TYPE_TEXT", UNSET)

        type_iso_date_time = d.pop("TYPE_ISO_DATE_TIME", UNSET)

        type_iso_date_only = d.pop("TYPE_ISO_DATE_ONLY", UNSET)

        aspect_line_c = cls(
            type_user=type_user,
            type_status=type_status,
            mb_type=mb_type,
            type_relation=type_relation,
            mb_translate=mb_translate,
            mb_important=mb_important,
            mb_allowed_mask_ids_for_keywording_relation=mb_allowed_mask_ids_for_keywording_relation,
            type_offset_types_for_aspects=type_offset_types_for_aspects,
            mb_postfix_asterix=mb_postfix_asterix,
            mb_prefix_asterix=mb_prefix_asterix,
            type_double=type_double,
            type_integer=type_integer,
            mb_flags=mb_flags,
            type_text=type_text,
            type_iso_date_time=type_iso_date_time,
            type_iso_date_only=type_iso_date_only,
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
