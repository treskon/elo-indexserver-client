from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectLine")


@_attrs_define
class AspectLine:
    """This class contains data for a line in a document mask, if {@link DocMask#dataOrganisation} =
    {@link DocMaskC#DATA_ORGANISATION_ASPECT}. AspectLines are contained in keywording
     {@link Aspect}s.

        Attributes:
            access (Union[Unset, int]): Bitset of AccessC.LUR_* constants. It contains the access bits for the current user.
                Only
                 AccessC.LUR_READ and AccessC.LUR_WRITE are used.
            prefix_asterix (Union[Unset, bool]): Add "*" before index value in search operation.
            postfix_asterix (Union[Unset, bool]): Add "*" after index value in search operation.
            display_name (Union[Unset, str]): The display name of the attribute. This value is displayed in the lable before
                the edit field.
                It can be translated into reps. from the users language: set
                 <code>SessionOptionsC.TRANSLATE_TERM</code>.
            default_value (Union[Unset, str]): This value is assigned to the element for a new Sord object.
            not_tokenized (Union[Unset, bool]): Defines whether a index value should be searchable as TOKENIZED or
                UN_TOKENIZED
            comment_translation_key (Union[Unset, str]): Translation-keyword for {@link AspectLine#comment}.
            keyword_list_id (Union[Unset, str]): Keyword List ID.
            aspect_id (Union[Unset, int]): This line information belongs to an aspect with the ID AspectId.
            external_data (Union[Unset, str]): External data. Can be used to store an arbitary string.
            type (Union[Unset, int]): The type of the line information.
                <br>
                 This can be one of the <code>AspectLineC.TYPE_*</code> constants but none of the
                 <code>DocMaskLineC.TYPE_*</code> constants.
            allowed_mask_ids_for_keywording_relation (Union[Unset, List[int]]):
            translate (Union[Unset, bool]): Translate index values into or from the users language.
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link AspectLine#displayName}.
            important (Union[Unset, bool]): Display index value next to the objects short description.
                This element has to be interpreted
                 by the client application. Further it is used while generating dynamic keywords.
            can_be_found_via_keywording_relation (Union[Unset, bool]): If the sord is referenced by keywording-relation,
                this flag must be true if this index value
                should be available for search in iSearch within the referencing sord.
            exclude_from_i_search (Union[Unset, bool]): If true a index value will not be searchable via iSearch. Does not
                affect the index search.
            dynamic_keyword_reference (Union[Unset, str]): A script or plugin at the server can serve as the data source of
                a dynamic keyword list.
                This
                 value represents the name of that script or plugin. If the value is not empty, the client can
                 request a list of available input values by calling the function
                 {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)}. In case of a
                 plugin, this value starts with the Bundle-SymbolicName and can be optionally appended by a
                 path. E.g. serverScriptName="com.partner.dkeywords/invoice-solution". The path has to start
                 with a forward slash and is passed to
                 {@link de.elo.ix.client.plugin.DynamicKeywordEventsFactory#create}.<br>
            sub_type (Union[Unset, str]): This field can be used by clients to determine a subtype of the given type.
                For the purpose of
                 properly displaying a value there are subtypes defined at client side.<br>
                 The server does not evaluate the subtype.
            comment (Union[Unset, str]): Quickinfo text for the attribute.
            key (Union[Unset, str]): The attribute identifier.
    """

    access: Union[Unset, int] = UNSET
    prefix_asterix: Union[Unset, bool] = UNSET
    postfix_asterix: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    not_tokenized: Union[Unset, bool] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    keyword_list_id: Union[Unset, str] = UNSET
    aspect_id: Union[Unset, int] = UNSET
    external_data: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
    translate: Union[Unset, bool] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    important: Union[Unset, bool] = UNSET
    can_be_found_via_keywording_relation: Union[Unset, bool] = UNSET
    exclude_from_i_search: Union[Unset, bool] = UNSET
    dynamic_keyword_reference: Union[Unset, str] = UNSET
    sub_type: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access

        prefix_asterix = self.prefix_asterix

        postfix_asterix = self.postfix_asterix

        display_name = self.display_name

        default_value = self.default_value

        not_tokenized = self.not_tokenized

        comment_translation_key = self.comment_translation_key

        keyword_list_id = self.keyword_list_id

        aspect_id = self.aspect_id

        external_data = self.external_data

        type = self.type

        allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
        if not isinstance(self.allowed_mask_ids_for_keywording_relation, Unset):
            allowed_mask_ids_for_keywording_relation = self.allowed_mask_ids_for_keywording_relation

        translate = self.translate

        name_translation_key = self.name_translation_key

        important = self.important

        can_be_found_via_keywording_relation = self.can_be_found_via_keywording_relation

        exclude_from_i_search = self.exclude_from_i_search

        dynamic_keyword_reference = self.dynamic_keyword_reference

        sub_type = self.sub_type

        comment = self.comment

        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if prefix_asterix is not UNSET:
            field_dict["prefixAsterix"] = prefix_asterix
        if postfix_asterix is not UNSET:
            field_dict["postfixAsterix"] = postfix_asterix
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if not_tokenized is not UNSET:
            field_dict["notTokenized"] = not_tokenized
        if comment_translation_key is not UNSET:
            field_dict["commentTranslationKey"] = comment_translation_key
        if keyword_list_id is not UNSET:
            field_dict["keywordListId"] = keyword_list_id
        if aspect_id is not UNSET:
            field_dict["aspectId"] = aspect_id
        if external_data is not UNSET:
            field_dict["externalData"] = external_data
        if type is not UNSET:
            field_dict["type"] = type
        if allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["allowedMaskIdsForKeywordingRelation"] = allowed_mask_ids_for_keywording_relation
        if translate is not UNSET:
            field_dict["translate"] = translate
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if important is not UNSET:
            field_dict["important"] = important
        if can_be_found_via_keywording_relation is not UNSET:
            field_dict["canBeFoundViaKeywordingRelation"] = can_be_found_via_keywording_relation
        if exclude_from_i_search is not UNSET:
            field_dict["excludeFromISearch"] = exclude_from_i_search
        if dynamic_keyword_reference is not UNSET:
            field_dict["dynamicKeywordReference"] = dynamic_keyword_reference
        if sub_type is not UNSET:
            field_dict["subType"] = sub_type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access = d.pop("access", UNSET)

        prefix_asterix = d.pop("prefixAsterix", UNSET)

        postfix_asterix = d.pop("postfixAsterix", UNSET)

        display_name = d.pop("displayName", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        not_tokenized = d.pop("notTokenized", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        keyword_list_id = d.pop("keywordListId", UNSET)

        aspect_id = d.pop("aspectId", UNSET)

        external_data = d.pop("externalData", UNSET)

        type = d.pop("type", UNSET)

        allowed_mask_ids_for_keywording_relation = cast(List[int], d.pop("allowedMaskIdsForKeywordingRelation", UNSET))

        translate = d.pop("translate", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        important = d.pop("important", UNSET)

        can_be_found_via_keywording_relation = d.pop("canBeFoundViaKeywordingRelation", UNSET)

        exclude_from_i_search = d.pop("excludeFromISearch", UNSET)

        dynamic_keyword_reference = d.pop("dynamicKeywordReference", UNSET)

        sub_type = d.pop("subType", UNSET)

        comment = d.pop("comment", UNSET)

        key = d.pop("key", UNSET)

        aspect_line = cls(
            access=access,
            prefix_asterix=prefix_asterix,
            postfix_asterix=postfix_asterix,
            display_name=display_name,
            default_value=default_value,
            not_tokenized=not_tokenized,
            comment_translation_key=comment_translation_key,
            keyword_list_id=keyword_list_id,
            aspect_id=aspect_id,
            external_data=external_data,
            type=type,
            allowed_mask_ids_for_keywording_relation=allowed_mask_ids_for_keywording_relation,
            translate=translate,
            name_translation_key=name_translation_key,
            important=important,
            can_be_found_via_keywording_relation=can_be_found_via_keywording_relation,
            exclude_from_i_search=exclude_from_i_search,
            dynamic_keyword_reference=dynamic_keyword_reference,
            sub_type=sub_type,
            comment=comment,
            key=key,
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
