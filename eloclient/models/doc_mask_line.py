from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem


T = TypeVar("T", bound="DocMaskLine")


@_attrs_define
class DocMaskLine:
    """This class contains data for a line in the document mask.

    Attributes:
        access (Union[Unset, int]): Bitset of AccessC.LUR_* constants. It contains the access bits for the current user.
            Only
             AccessC.LUR_READ and AccessC.LUR_WRITE are used.
        hidden (Union[Unset, bool]): This value should not be displayed to the user.
        postfix_asterix (Union[Unset, bool]): Add "*" after index value in search operation.
        not_tokenized (Union[Unset, bool]): Defines whether a index value should be searchable as TOKENIZED or
            UN_TOKENIZED
        default_value (Union[Unset, str]): This value is assigned to the ObjKey.data element for a new Sord object.
        can_edit (Union[Unset, bool]): Determines whether the index line can be modified. Read-only.
        edit_row (Union[Unset, int]): Row postion of edit control
        external_data (Union[Unset, str]): External data. Can be used to store an arbitary string.
        tab_index (Union[Unset, int]): This value represents the number of the tab, this line has to appear on.
            The first tab's index
             value is 0. It is on the client's hand to set valid values when checking in document masks.
        acl (Union[Unset, str]): Access control for mask line.
        value_array (Union[Unset, bool]): Allows multiple values for keywording tables.
            For keywording forms organized as tables, see
             {@link DocMaskC#DATA_ORGANISATION_TABLE}, index lines must be explicitly declared for storing
             multiple values. If this member is true, the index line is able to store an arbitrary number of
             values. For keywording forms organized as name-value pairs, see
             {@link DocMaskC#DATA_ORGANISATION_OBJKEYS}, index lines can store multiple values by default
             and this member has to be ignored.
        type (Union[Unset, int]): The type of the line information. This can be one of the <code>DocMaskLineC.
            TYPE_*</code>
             constants.
        edit_width (Union[Unset, int]): With of edit control
        translate (Union[Unset, bool]): Translate index values into or from the users language.
        required (Union[Unset, bool]): Entry is required.
        min_ (Union[Unset, int]): The minimum value of this attribute.
        inherit_from_parent (Union[Unset, bool]): Do not inherit the parent's value.
        server_script_name (Union[Unset, str]): A script or plugin at the server can serve as the data source of a
            dynamic keyword list.
            This
             value represents the name of that script or plugin. If the value is not empty, the client can
             request a list of available input values by calling the function
             {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)}. In case of a
             plugin, this value starts with the Bundle-SymbolicName and can be optionally appended by a
             path. E.g. serverScriptName="com.partner.dkeywords/invoice-solution". The path has to start
             with a forward slash and is passed to
             {@link de.elo.ix.client.plugin.DynamicKeywordEventsFactory#create}.
        id (Union[Unset, int]): The ID of the line information.
        label_col (Union[Unset, int]): Column position of label control
        key (Union[Unset, str]): The attribute group name. This member corresponds to <code>ObjKey.name</code>.
        edit_col (Union[Unset, int]): Column position of edit control
        prefix_asterix (Union[Unset, bool]): Add "*" before index value in search operation.
        max_ (Union[Unset, int]): The maximum value of this attribute.
        comment_translation_key (Union[Unset, str]): Translation-keyword for {@link DocMaskLine#comment}.
        only_buzzwords (Union[Unset, bool]): The index line can only contain buzzwords.
        disable_word_wheel (Union[Unset, bool]): Disable word wheel.
            Clients should not provide a function to list all existing values for this
             index vlaue. The Indexserver does not set or test this value.
        mask_id (Union[Unset, int]): This line information belongs to a storage mask with the ID MaskId.
        read_only (Union[Unset, bool]): This value should not be edited in a user interface (convention).
            Scripts are allowed to edit
             the value.
        version (Union[Unset, bool]): Display index value in version information dialog when checking in a document.
            This element has
             to be interpreted by the client application. Indexserver ignores this value.
        allowed_mask_ids_for_keywording_relation (Union[Unset, List[int]]):
        important (Union[Unset, bool]): Display index value next to the objects short description.
            This element has to be interpreted
             by the client application. Indexserver ignores this value.
        name_translation_key (Union[Unset, str]): Translation-keyword for {@link DocMaskLine#name}.
        label_row (Union[Unset, int]): Row position of label control
        exclude_from_i_search (Union[Unset, bool]): If true a index value will not be searchable via iSearch. Does not
            affect the index search.
        next_tab (Union[Unset, bool]): Creates a new tab in the keywording dialogue.
        acl_items (Union[Unset, List['AclItem']]):
        tab_order (Union[Unset, int]): Tabulator order of edit control
        inherit (Union[Unset, bool]): Inherit this keywording field to subordinated entries.
            <p>
             This option is used to make sure, that all entries in an archive sub-tree have the same value
             for this keywording field. Thereby the field is identified by its group name
             ({@link DocMaskLine#key} and {@link ObjKey#name}).
             </p>
             <p>
             The option corresponds to {@link #inheritFromParent}. As far as {@link #inheritFromParent} is
             also true in the keywording forms definition of all sub-items, the option {@link #inherit}
             effects the following:
             <ul>
             <li>The value of the keywording field can only be changed in the parent entry of the sub-tree.
             This is the uppermost entry that has the field, which means that the parent's parent does not
             have this field.</li>
             <li>All sub-items of the parent inherit this value during a background process. The value is
             forwarded recursively to the entire sub-tree under the parent. The recursion stops at items
             that are assigned to a keywording form without this field.</li>
             <li>When a child entry under the parent is updated, this field is always corrected to the
             parent's value.</li>
             <li>For an object moved into a parent, the object and all sub-items inherit the keywording
             field.</li>
             </ul>
             </p>
             <p>
             If {@link #inheritFromParent} is false in the keywording form definition of a sub-item,
             inheritance stops for the sub-item. Thus, the index field is treated as a different field
             although it has the same group name.
             </p>
        name (Union[Unset, str]): The name of the attribute. This value is displayed in the lable before the edit field.
            It can
             be translated into reps. from the users language: set
             <code>SessionOptionsC.TRANSLATE_TERM</code>.
        comment (Union[Unset, str]): Quickinfo text for the attribute.
        validate_expression (Union[Unset, str]): RegEx to validate user input for entry.
    """

    access: Union[Unset, int] = UNSET
    hidden: Union[Unset, bool] = UNSET
    postfix_asterix: Union[Unset, bool] = UNSET
    not_tokenized: Union[Unset, bool] = UNSET
    default_value: Union[Unset, str] = UNSET
    can_edit: Union[Unset, bool] = UNSET
    edit_row: Union[Unset, int] = UNSET
    external_data: Union[Unset, str] = UNSET
    tab_index: Union[Unset, int] = UNSET
    acl: Union[Unset, str] = UNSET
    value_array: Union[Unset, bool] = UNSET
    type: Union[Unset, int] = UNSET
    edit_width: Union[Unset, int] = UNSET
    translate: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    min_: Union[Unset, int] = UNSET
    inherit_from_parent: Union[Unset, bool] = UNSET
    server_script_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    label_col: Union[Unset, int] = UNSET
    key: Union[Unset, str] = UNSET
    edit_col: Union[Unset, int] = UNSET
    prefix_asterix: Union[Unset, bool] = UNSET
    max_: Union[Unset, int] = UNSET
    comment_translation_key: Union[Unset, str] = UNSET
    only_buzzwords: Union[Unset, bool] = UNSET
    disable_word_wheel: Union[Unset, bool] = UNSET
    mask_id: Union[Unset, int] = UNSET
    read_only: Union[Unset, bool] = UNSET
    version: Union[Unset, bool] = UNSET
    allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
    important: Union[Unset, bool] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    label_row: Union[Unset, int] = UNSET
    exclude_from_i_search: Union[Unset, bool] = UNSET
    next_tab: Union[Unset, bool] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    tab_order: Union[Unset, int] = UNSET
    inherit: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    validate_expression: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access = self.access

        hidden = self.hidden

        postfix_asterix = self.postfix_asterix

        not_tokenized = self.not_tokenized

        default_value = self.default_value

        can_edit = self.can_edit

        edit_row = self.edit_row

        external_data = self.external_data

        tab_index = self.tab_index

        acl = self.acl

        value_array = self.value_array

        type = self.type

        edit_width = self.edit_width

        translate = self.translate

        required = self.required

        min_ = self.min_

        inherit_from_parent = self.inherit_from_parent

        server_script_name = self.server_script_name

        id = self.id

        label_col = self.label_col

        key = self.key

        edit_col = self.edit_col

        prefix_asterix = self.prefix_asterix

        max_ = self.max_

        comment_translation_key = self.comment_translation_key

        only_buzzwords = self.only_buzzwords

        disable_word_wheel = self.disable_word_wheel

        mask_id = self.mask_id

        read_only = self.read_only

        version = self.version

        allowed_mask_ids_for_keywording_relation: Union[Unset, List[int]] = UNSET
        if not isinstance(self.allowed_mask_ids_for_keywording_relation, Unset):
            allowed_mask_ids_for_keywording_relation = self.allowed_mask_ids_for_keywording_relation

        important = self.important

        name_translation_key = self.name_translation_key

        label_row = self.label_row

        exclude_from_i_search = self.exclude_from_i_search

        next_tab = self.next_tab

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        tab_order = self.tab_order

        inherit = self.inherit

        name = self.name

        comment = self.comment

        validate_expression = self.validate_expression

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access is not UNSET:
            field_dict["access"] = access
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if postfix_asterix is not UNSET:
            field_dict["postfixAsterix"] = postfix_asterix
        if not_tokenized is not UNSET:
            field_dict["notTokenized"] = not_tokenized
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if can_edit is not UNSET:
            field_dict["canEdit"] = can_edit
        if edit_row is not UNSET:
            field_dict["editRow"] = edit_row
        if external_data is not UNSET:
            field_dict["externalData"] = external_data
        if tab_index is not UNSET:
            field_dict["tabIndex"] = tab_index
        if acl is not UNSET:
            field_dict["acl"] = acl
        if value_array is not UNSET:
            field_dict["valueArray"] = value_array
        if type is not UNSET:
            field_dict["type"] = type
        if edit_width is not UNSET:
            field_dict["editWidth"] = edit_width
        if translate is not UNSET:
            field_dict["translate"] = translate
        if required is not UNSET:
            field_dict["required"] = required
        if min_ is not UNSET:
            field_dict["min"] = min_
        if inherit_from_parent is not UNSET:
            field_dict["inheritFromParent"] = inherit_from_parent
        if server_script_name is not UNSET:
            field_dict["serverScriptName"] = server_script_name
        if id is not UNSET:
            field_dict["id"] = id
        if label_col is not UNSET:
            field_dict["labelCol"] = label_col
        if key is not UNSET:
            field_dict["key"] = key
        if edit_col is not UNSET:
            field_dict["editCol"] = edit_col
        if prefix_asterix is not UNSET:
            field_dict["prefixAsterix"] = prefix_asterix
        if max_ is not UNSET:
            field_dict["max"] = max_
        if comment_translation_key is not UNSET:
            field_dict["commentTranslationKey"] = comment_translation_key
        if only_buzzwords is not UNSET:
            field_dict["onlyBuzzwords"] = only_buzzwords
        if disable_word_wheel is not UNSET:
            field_dict["disableWordWheel"] = disable_word_wheel
        if mask_id is not UNSET:
            field_dict["maskId"] = mask_id
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if version is not UNSET:
            field_dict["version"] = version
        if allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["allowedMaskIdsForKeywordingRelation"] = allowed_mask_ids_for_keywording_relation
        if important is not UNSET:
            field_dict["important"] = important
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if label_row is not UNSET:
            field_dict["labelRow"] = label_row
        if exclude_from_i_search is not UNSET:
            field_dict["excludeFromISearch"] = exclude_from_i_search
        if next_tab is not UNSET:
            field_dict["nextTab"] = next_tab
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if tab_order is not UNSET:
            field_dict["tabOrder"] = tab_order
        if inherit is not UNSET:
            field_dict["inherit"] = inherit
        if name is not UNSET:
            field_dict["name"] = name
        if comment is not UNSET:
            field_dict["comment"] = comment
        if validate_expression is not UNSET:
            field_dict["validateExpression"] = validate_expression

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem

        d = src_dict.copy()
        access = d.pop("access", UNSET)

        hidden = d.pop("hidden", UNSET)

        postfix_asterix = d.pop("postfixAsterix", UNSET)

        not_tokenized = d.pop("notTokenized", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        can_edit = d.pop("canEdit", UNSET)

        edit_row = d.pop("editRow", UNSET)

        external_data = d.pop("externalData", UNSET)

        tab_index = d.pop("tabIndex", UNSET)

        acl = d.pop("acl", UNSET)

        value_array = d.pop("valueArray", UNSET)

        type = d.pop("type", UNSET)

        edit_width = d.pop("editWidth", UNSET)

        translate = d.pop("translate", UNSET)

        required = d.pop("required", UNSET)

        min_ = d.pop("min", UNSET)

        inherit_from_parent = d.pop("inheritFromParent", UNSET)

        server_script_name = d.pop("serverScriptName", UNSET)

        id = d.pop("id", UNSET)

        label_col = d.pop("labelCol", UNSET)

        key = d.pop("key", UNSET)

        edit_col = d.pop("editCol", UNSET)

        prefix_asterix = d.pop("prefixAsterix", UNSET)

        max_ = d.pop("max", UNSET)

        comment_translation_key = d.pop("commentTranslationKey", UNSET)

        only_buzzwords = d.pop("onlyBuzzwords", UNSET)

        disable_word_wheel = d.pop("disableWordWheel", UNSET)

        mask_id = d.pop("maskId", UNSET)

        read_only = d.pop("readOnly", UNSET)

        version = d.pop("version", UNSET)

        allowed_mask_ids_for_keywording_relation = cast(List[int], d.pop("allowedMaskIdsForKeywordingRelation", UNSET))

        important = d.pop("important", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        label_row = d.pop("labelRow", UNSET)

        exclude_from_i_search = d.pop("excludeFromISearch", UNSET)

        next_tab = d.pop("nextTab", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        tab_order = d.pop("tabOrder", UNSET)

        inherit = d.pop("inherit", UNSET)

        name = d.pop("name", UNSET)

        comment = d.pop("comment", UNSET)

        validate_expression = d.pop("validateExpression", UNSET)

        doc_mask_line = cls(
            access=access,
            hidden=hidden,
            postfix_asterix=postfix_asterix,
            not_tokenized=not_tokenized,
            default_value=default_value,
            can_edit=can_edit,
            edit_row=edit_row,
            external_data=external_data,
            tab_index=tab_index,
            acl=acl,
            value_array=value_array,
            type=type,
            edit_width=edit_width,
            translate=translate,
            required=required,
            min_=min_,
            inherit_from_parent=inherit_from_parent,
            server_script_name=server_script_name,
            id=id,
            label_col=label_col,
            key=key,
            edit_col=edit_col,
            prefix_asterix=prefix_asterix,
            max_=max_,
            comment_translation_key=comment_translation_key,
            only_buzzwords=only_buzzwords,
            disable_word_wheel=disable_word_wheel,
            mask_id=mask_id,
            read_only=read_only,
            version=version,
            allowed_mask_ids_for_keywording_relation=allowed_mask_ids_for_keywording_relation,
            important=important,
            name_translation_key=name_translation_key,
            label_row=label_row,
            exclude_from_i_search=exclude_from_i_search,
            next_tab=next_tab,
            acl_items=acl_items,
            tab_order=tab_order,
            inherit=inherit,
            name=name,
            comment=comment,
            validate_expression=validate_expression,
        )

        doc_mask_line.additional_properties = d
        return doc_mask_line

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
