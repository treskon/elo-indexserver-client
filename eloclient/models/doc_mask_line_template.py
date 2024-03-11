from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="DocMaskLineTemplate")


@_attrs_define
class DocMaskLineTemplate:
    """This class contains data for a document mask line template.

    Attributes:
        t_stamp (Union[Unset, str]): Last update time of the storage template data.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        lock_id (Union[Unset, int]): User ID of the user that has locked the mask line template. If -1, no lock is held.
        comment (Union[Unset, str]): Quickinfo text for the attribute.
        id (Union[Unset, int]): The ID of the line information.
        key (Union[Unset, str]): The attribute group name. This member corresponds to <code>ObjKey.name</code>.
        max_ (Union[Unset, int]): The maximum value of this attribute.
        min_ (Union[Unset, int]): The minimum value of this attribute.
        name (Union[Unset, str]): The name of the attribute. This value is displayed in the lable before the edit field.
            It can be translated into
             reps. from the users language: set <code>SessionOptionsC.TRANSLATE_TERM</code>.
        acl_items (Union[Unset, List['AclItem']]):
        hidden (Union[Unset, bool]): This value should not be displayed to the user.
        only_buzzwords (Union[Unset, bool]): The index line can only contain buzzwords.
        postfix_asterix (Union[Unset, bool]): Add "*" after index value in search operation.
        prefix_asterix (Union[Unset, bool]): Add "*" before index value in search operation.
        read_only (Union[Unset, bool]): This value should not be edited in a user interface (convention). Scripts are
            allowed to edit the value.
        type (Union[Unset, int]): The type of the line information. This can be one of the
            <code>DocMaskLineC.TYPE_*</code> constants.
        external_data (Union[Unset, str]): External data. Can be used to store an arbitary string.
        important (Union[Unset, bool]): Display index value next to the objects short description.
            This element has to be interpreted by the client
             application. Indexserver ignores this value.
        not_tokenized (Union[Unset, bool]): Defines whether a index value should be searchable as TOKENIZED or
            UN_TOKENIZED
        exclude_from_i_search (Union[Unset, bool]): If true a index value will not be searchable via iSearch. Does not
            affect the index search.
        version (Union[Unset, bool]): Display index value in version information dialog when checking in a document.
            This element has to be interpreted
             by the client application. Indexserver ignores this value.
        translate (Union[Unset, bool]): Translate index values into or from the users language.
        acl (Union[Unset, str]): Access control for mask line.
        disable_word_wheel (Union[Unset, bool]): Disable word wheel. Clients should not provide a function to list all
            existing values for this index vlaue.
            The
             Indexserver does not set or test this value.
        default_value (Union[Unset, str]): This value is assigned to the ObjKey.data element for a new Sord object.
        server_script_name (Union[Unset, str]): A script at the server can serve as the data source of a dynamic keyword
            list.
            This value represents the name of
             that script. If the value is not empty, the client can request a list of available input values by calling the
             function {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)}.
        inherit (Union[Unset, bool]): Inherit this keywording field to subordinated entries.
            <p>
             This option is used to make sure, that all entries in an archive sub-tree have the same value for this
            keywording
             field. Thereby the field is identified by its group name ({@link DocMaskLine#key} and {@link ObjKey#name}).
             </p>
             <p>
             The option corresponds to {@link #inheritFromParent}. As far as {@link #inheritFromParent} is also true in the
             keywording forms definition of all sub-items, the option {@link #inherit} effects the following:
             <ul>
             <li>The value of the keywording field can only be changed in the parent entry of the sub-tree. This is the
             uppermost entry that has the field, which means that the parent's parent does not have this field.</li>
             <li>All sub-items of the parent inherit this value during a background process. The value is forwarded
            recursively
             to the entire sub-tree under the parent. The recursion stops at items that are assigned to a keywording form
             without this field.</li>
             <li>When a child entry under the parent is updated, this field is always corrected to the parent's value.</li>
             <li>For an object moved into a parent, the object and all sub-items inherit the keywording field.</li>
             </ul>
             </p>
             <p>
             If {@link #inheritFromParent} is false in the keywording form definition of a sub-item, inheritance stops for
            the
             sub-item. Thus, the index field is treated as a different field although it has the same group name.
             </p>
        inherit_from_parent (Union[Unset, bool]): Do not inherit the parent's value.
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link DocMaskLine#name}.
        comment_translation_key (Union[Unset, str]): Translation-keyword for {@link DocMaskLine#comment}.
        lock_name (Union[Unset, str]): Name of the user that has locked the mask line template. Read-only, ignored in
            checkinDocMaskLineTemplate.
        validate_expression (Union[Unset, str]): RegEx to validate user input for entry.
        required (Union[Unset, bool]): Entry is required.
        allowed_mask_ids_for_keywording_relation (Union[Unset, List[int]]):
    """

    t_stamp: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    lock_id: Union[Unset, int] = UNSET
    comment: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    max_: Union[Unset, int] = UNSET
    min_: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    hidden: Union[Unset, bool] = UNSET
    only_buzzwords: Union[Unset, bool] = UNSET
    postfix_asterix: Union[Unset, bool] = UNSET
    prefix_asterix: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    type: Union[Unset, int] = UNSET
    external_data: Union[Unset, str] = UNSET
    important: Union[Unset, bool] = UNSET
    not_tokenized: Union[Unset, bool] = UNSET
    exclude_from_i_search: Union[Unset, bool] = UNSET
    version: Union[Unset, bool] = UNSET
    translate: Union[Unset, bool] = UNSET
    acl: Union[Unset, str] = UNSET
    disable_word_wheel: Union[Unset, bool] = UNSET
    default_value: Union[Unset, str] = UNSET
    server_script_name: Union[Unset, str] = UNSET
    inherit: Union[Unset, bool] = UNSET
    inherit_from_parent: Union[Unset, bool] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    validate_expression: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp
        t_stamp_sync = self.t_stamp_sync
        lock_id = self.lock_id
        comment = self.comment
        id = self.id
        key = self.key
        max_ = self.max_
        min_ = self.min_
        name = self.name
        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()

                acl_items.append(acl_items_item)

        hidden = self.hidden
        only_buzzwords = self.only_buzzwords
        postfix_asterix = self.postfix_asterix
        prefix_asterix = self.prefix_asterix
        read_only = self.read_only
        type = self.type
        external_data = self.external_data
        important = self.important
        not_tokenized = self.not_tokenized
        exclude_from_i_search = self.exclude_from_i_search
        version = self.version
        translate = self.translate
        acl = self.acl
        disable_word_wheel = self.disable_word_wheel
        default_value = self.default_value
        server_script_name = self.server_script_name
        inherit = self.inherit
        inherit_from_parent = self.inherit_from_parent
        name_translation_key = self.name_translation_key
        comment_translation_key = self.comment_translation_key
        lock_name = self.lock_name
        validate_expression = self.validate_expression
        required = self.required
        allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
        if not isinstance(self.allowed_mask_ids_for_keywording_relation, Unset):
            allowed_mask_ids_for_keywording_relation = self.allowed_mask_ids_for_keywording_relation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if id is not UNSET:
            field_dict["id"] = id
        if key is not UNSET:
            field_dict["key"] = key
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name is not UNSET:
            field_dict["name"] = name
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if only_buzzwords is not UNSET:
            field_dict["onlyBuzzwords"] = only_buzzwords
        if postfix_asterix is not UNSET:
            field_dict["postfixAsterix"] = postfix_asterix
        if prefix_asterix is not UNSET:
            field_dict["prefixAsterix"] = prefix_asterix
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if type is not UNSET:
            field_dict["type"] = type
        if external_data is not UNSET:
            field_dict["externalData"] = external_data
        if important is not UNSET:
            field_dict["important"] = important
        if not_tokenized is not UNSET:
            field_dict["notTokenized"] = not_tokenized
        if exclude_from_i_search is not UNSET:
            field_dict["excludeFromISearch"] = exclude_from_i_search
        if version is not UNSET:
            field_dict["version"] = version
        if translate is not UNSET:
            field_dict["translate"] = translate
        if acl is not UNSET:
            field_dict["acl"] = acl
        if disable_word_wheel is not UNSET:
            field_dict["disableWordWheel"] = disable_word_wheel
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if server_script_name is not UNSET:
            field_dict["serverScriptName"] = server_script_name
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if inherit_from_parent is not UNSET:
            field_dict["inheritFromParent"] = inherit_from_parent
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if comment_translation_key is not UNSET:
            field_dict["commentTranslationKey"] = comment_translation_key
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if validate_expression is not UNSET:
            field_dict["validateExpression"] = validate_expression
        if required is not UNSET:
            field_dict["required"] = required
        if allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["allowedMaskIdsForKeywordingRelation"] = allowed_mask_ids_for_keywording_relation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        t_stamp = d.pop("TStamp", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        lock_id = d.pop("lockId", UNSET)

        comment = d.pop("comment", UNSET)

        id = d.pop("id", UNSET)

        key = d.pop("key", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        name = d.pop("name", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        hidden = d.pop("hidden", UNSET)

        only_buzzwords = d.pop("onlyBuzzwords", UNSET)

        postfix_asterix = d.pop("postfixAsterix", UNSET)

        prefix_asterix = d.pop("prefixAsterix", UNSET)

        read_only = d.pop("readOnly", UNSET)

        type = d.pop("type", UNSET)

        external_data = d.pop("externalData", UNSET)

        important = d.pop("important", UNSET)

        not_tokenized = d.pop("notTokenized", UNSET)

        exclude_from_i_search = d.pop("excludeFromISearch", UNSET)

        version = d.pop("version", UNSET)

        translate = d.pop("translate", UNSET)

        acl = d.pop("acl", UNSET)

        disable_word_wheel = d.pop("disableWordWheel", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        server_script_name = d.pop("serverScriptName", UNSET)

        inherit = d.pop("inherit", UNSET)

        inherit_from_parent = d.pop("inheritFromParent", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        lock_name = d.pop("lockName", UNSET)

        validate_expression = d.pop("validateExpression", UNSET)

        required = d.pop("required", UNSET)

        allowed_mask_ids_for_keywording_relation = cast(List[int], d.pop("allowedMaskIdsForKeywordingRelation", UNSET))

        doc_mask_line_template = cls(
            t_stamp=t_stamp,
            t_stamp_sync=t_stamp_sync,
            lock_id=lock_id,
            comment=comment,
            id=id,
            key=key,
            max_=max_,
            min_=min_,
            name=name,
            acl_items=acl_items,
            hidden=hidden,
            only_buzzwords=only_buzzwords,
            postfix_asterix=postfix_asterix,
            prefix_asterix=prefix_asterix,
            read_only=read_only,
            type=type,
            external_data=external_data,
            important=important,
            not_tokenized=not_tokenized,
            exclude_from_i_search=exclude_from_i_search,
            version=version,
            translate=translate,
            acl=acl,
            disable_word_wheel=disable_word_wheel,
            default_value=default_value,
            server_script_name=server_script_name,
            inherit=inherit,
            inherit_from_parent=inherit_from_parent,
            name_translation_key=name_translation_key,
            comment_translation_key=comment_translation_key,
            lock_name=lock_name,
            validate_expression=validate_expression,
            required=required,
            allowed_mask_ids_for_keywording_relation=allowed_mask_ids_for_keywording_relation,
        )

        doc_mask_line_template.additional_properties = d
        return doc_mask_line_template

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
