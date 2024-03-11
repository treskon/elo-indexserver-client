from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectLine")


@_attrs_define
class AspectLine:
    """This class contains data for a line in a document mask, if {@link DocMask#dataOrganisation} =
    {@link DocMaskC#DATA_ORGANISATION_ASPECT}. AspectLines are contained in keywording {@link Aspect}s.

        Attributes:
            aspect_id (Union[Unset, int]): This line information belongs to an aspect with the ID AspectId.
            type (Union[Unset, int]): The type of the line information. This can be one of the
                <code>DocMaskLineC.TYPE_*</code> constants.
            display_name (Union[Unset, str]): The display name of the attribute. This value is displayed in the lable before
                the edit field.
                It can be translated
                 into reps. from the users language: set <code>SessionOptionsC.TRANSLATE_TERM</code>.
            key (Union[Unset, str]): The attribute identifier.
            external_data (Union[Unset, str]): External data. Can be used to store an arbitary string.
            access (Union[Unset, int]): Bitset of AccessC.LUR_* constants. It contains the access bits for the current user.
                Only AccessC.
                LUR_READ and
                 AccessC.LUR_WRITE are used.
            default_value (Union[Unset, str]): This value is assigned to the element for a new Sord object.
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link AspectLine#displayName}.
            allowed_mask_ids_for_keywording_relation (Union[Unset, List[int]]):
            postfix_asterix (Union[Unset, bool]): Add "*" after index value in search operation.
            prefix_asterix (Union[Unset, bool]): Add "*" before index value in search operation.
            important (Union[Unset, bool]): Display index value next to the objects short description.
                This element has to be interpreted by the client
                 application. Further it is used while generating dynamic keywords.
            not_tokenized (Union[Unset, bool]): Defines whether a index value should be searchable as TOKENIZED or
                UN_TOKENIZED
            exclude_from_i_search (Union[Unset, bool]): If true a index value will not be searchable via iSearch. Does not
                affect the index search.
            translate (Union[Unset, bool]): Translate index values into or from the users language.
    """

    aspect_id: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    external_data: Union[Unset, str] = UNSET
    access: Union[Unset, int] = UNSET
    default_value: Union[Unset, str] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
    postfix_asterix: Union[Unset, bool] = UNSET
    prefix_asterix: Union[Unset, bool] = UNSET
    important: Union[Unset, bool] = UNSET
    not_tokenized: Union[Unset, bool] = UNSET
    exclude_from_i_search: Union[Unset, bool] = UNSET
    translate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aspect_id = self.aspect_id
        type = self.type
        display_name = self.display_name
        key = self.key
        external_data = self.external_data
        access = self.access
        default_value = self.default_value
        name_translation_key = self.name_translation_key
        allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
        if not isinstance(self.allowed_mask_ids_for_keywording_relation, Unset):
            allowed_mask_ids_for_keywording_relation = self.allowed_mask_ids_for_keywording_relation

        postfix_asterix = self.postfix_asterix
        prefix_asterix = self.prefix_asterix
        important = self.important
        not_tokenized = self.not_tokenized
        exclude_from_i_search = self.exclude_from_i_search
        translate = self.translate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_id is not UNSET:
            field_dict["aspectId"] = aspect_id
        if type is not UNSET:
            field_dict["type"] = type
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if key is not UNSET:
            field_dict["key"] = key
        if external_data is not UNSET:
            field_dict["externalData"] = external_data
        if access is not UNSET:
            field_dict["access"] = access
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["allowedMaskIdsForKeywordingRelation"] = allowed_mask_ids_for_keywording_relation
        if postfix_asterix is not UNSET:
            field_dict["postfixAsterix"] = postfix_asterix
        if prefix_asterix is not UNSET:
            field_dict["prefixAsterix"] = prefix_asterix
        if important is not UNSET:
            field_dict["important"] = important
        if not_tokenized is not UNSET:
            field_dict["notTokenized"] = not_tokenized
        if exclude_from_i_search is not UNSET:
            field_dict["excludeFromISearch"] = exclude_from_i_search
        if translate is not UNSET:
            field_dict["translate"] = translate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aspect_id = d.pop("aspectId", UNSET)

        type = d.pop("type", UNSET)

        display_name = d.pop("displayName", UNSET)

        key = d.pop("key", UNSET)

        external_data = d.pop("externalData", UNSET)

        access = d.pop("access", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        allowed_mask_ids_for_keywording_relation = cast(List[int], d.pop("allowedMaskIdsForKeywordingRelation", UNSET))

        postfix_asterix = d.pop("postfixAsterix", UNSET)

        prefix_asterix = d.pop("prefixAsterix", UNSET)

        important = d.pop("important", UNSET)

        not_tokenized = d.pop("notTokenized", UNSET)

        exclude_from_i_search = d.pop("excludeFromISearch", UNSET)

        translate = d.pop("translate", UNSET)

        aspect_line = cls(
            aspect_id=aspect_id,
            type=type,
            display_name=display_name,
            key=key,
            external_data=external_data,
            access=access,
            default_value=default_value,
            name_translation_key=name_translation_key,
            allowed_mask_ids_for_keywording_relation=allowed_mask_ids_for_keywording_relation,
            postfix_asterix=postfix_asterix,
            prefix_asterix=prefix_asterix,
            important=important,
            not_tokenized=not_tokenized,
            exclude_from_i_search=exclude_from_i_search,
            translate=translate,
        )

        aspect_line.additional_properties = d
        return aspect_line

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
