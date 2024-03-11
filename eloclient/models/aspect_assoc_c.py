from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectAssocC")


@_attrs_define
class AspectAssocC:
    """<p>
    Bit constants for members of AspectAssoc
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_mask_id (Union[Unset, str]): DB column: maskid
            mb_name (Union[Unset, str]): Member bit: Technical aspect association name.
                DB column: name
            ln_name (Union[Unset, int]): Column length: Technical aspect association name.
                DB column: name
            mb_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link AspectAssoc#displayName}.
                DB column: translationkey
            ln_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link AspectAssoc#displayName}.
                DB column: translationkey
            mb_aspect_id (Union[Unset, str]): Member bit: ID of the referenced aspect.
                DB column: aspectid
            mb_raw_cardinality (Union[Unset, str]): Member bit: Cardinality.
                DB column: cardinality
            mb_acl (Union[Unset, str]): Member bit: Access control list.
                DB column: acl
            ln_acl (Union[Unset, int]): Column length: Access control list.
                DB column: acl
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_mask_id: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_translation_key: Union[Unset, str] = UNSET
    ln_translation_key: Union[Unset, int] = UNSET
    mb_aspect_id: Union[Unset, str] = UNSET
    mb_raw_cardinality: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_mask_id = self.mb_mask_id
        mb_name = self.mb_name
        ln_name = self.ln_name
        mb_translation_key = self.mb_translation_key
        ln_translation_key = self.ln_translation_key
        mb_aspect_id = self.mb_aspect_id
        mb_raw_cardinality = self.mb_raw_cardinality
        mb_acl = self.mb_acl
        ln_acl = self.ln_acl
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_mask_id is not UNSET:
            field_dict["mbMaskId"] = mb_mask_id
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_translation_key is not UNSET:
            field_dict["mbTranslationKey"] = mb_translation_key
        if ln_translation_key is not UNSET:
            field_dict["lnTranslationKey"] = ln_translation_key
        if mb_aspect_id is not UNSET:
            field_dict["mbAspectId"] = mb_aspect_id
        if mb_raw_cardinality is not UNSET:
            field_dict["mbRawCardinality"] = mb_raw_cardinality
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_mask_id = d.pop("mbMaskId", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_translation_key = d.pop("mbTranslationKey", UNSET)

        ln_translation_key = d.pop("lnTranslationKey", UNSET)

        mb_aspect_id = d.pop("mbAspectId", UNSET)

        mb_raw_cardinality = d.pop("mbRawCardinality", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        aspect_assoc_c = cls(
            mb_mask_id=mb_mask_id,
            mb_name=mb_name,
            ln_name=ln_name,
            mb_translation_key=mb_translation_key,
            ln_translation_key=ln_translation_key,
            mb_aspect_id=mb_aspect_id,
            mb_raw_cardinality=mb_raw_cardinality,
            mb_acl=mb_acl,
            ln_acl=ln_acl,
            mb_all_members=mb_all_members,
        )

        aspect_assoc_c.additional_properties = d
        return aspect_assoc_c

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
