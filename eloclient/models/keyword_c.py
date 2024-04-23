from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyword_z import KeywordZ


T = TypeVar("T", bound="KeywordC")


@_attrs_define
class KeywordC:
    """
    Attributes:
        kwid_user_list (Union[Unset, str]): Root ID of user keyword list.
        placeholder_counter_begin (Union[Unset, str]): Placeholder for the value of the specified counter name.
            The counter name follows the place
             holder and is suffixed with an extra "%". E. g.
             <code>text=PLACEHOLDER_COUNTER_BEGIN + "myRecordCounter" + PLACEHOLDER_COUNTER_END + ". record"</code>
             is expanded to <code>text="17. record"</code> assuming myRecordCounter has value 17.
        max_children (Union[Unset, int]): The maximum number of children per keyword.
            This value is valid for all keyword lists except
             the user keyword list (<code>KWID_USER_LIST</code>). The user keyword list might contain more
             children below a keyword node.
        ln_text (Union[Unset, int]): Maximum length of keyword text.
        ln_id (Union[Unset, int]): Maximum length of keyword ID.
        separator_groupid_for_aspectlines (Union[Unset, str]): Do no longer use this field.
        mb_raw_text (Union[Unset, str]): Return raw text in <code>checkoutKeywords</code>. Placeholders are not
            substituted.
        separator_aspectid_linekey (Union[Unset, str]): Do no longer use this field.
        placeholder_date (Union[Unset, str]): Placeholder for current date.
            The format depends on the date format
             <code>UserProfileC.SORD_DATE_FORMAT</code> specified in the user or standard profile.
        kwid_version (Union[Unset, str]): Root ID of keyword list used for version numbers.
        kwid_version_comment (Union[Unset, str]): Root ID of keyword list used for version comments.
        placeholder_counter_end (Union[Unset, str]): End of placeholder for counter name.
        kwid_workflow (Union[Unset, str]): Root ID of keyword list used for workflows.
        placeholder_day (Union[Unset, str]): Placeholder for day of month (2 digits).
        max_tree_depth (Union[Unset, int]): Maximum depth of a keyword tree.
            This value is valid for all keyword lists except the user
             keyword list (<code>KWID_USER_LIST</code>). The user keyword list might contain a deeper tree.
        ln_root_id (Union[Unset, int]): Maximum length of a root keyword ID.
            If a new keyword list is checked in, the ID of the root
             keyword must not exceed this length.
        kwid_standard_list (Union[Unset, str]): Root ID of standard keyword list.
        mb_view (Union[Unset, KeywordZ]): This class encapsulates the constants of KeywordC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        placeholder_year (Union[Unset, str]): Placeholder for year (4 digits).
        mb_edit (Union[Unset, KeywordZ]): This class encapsulates the constants of KeywordC.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        placeholder_month (Union[Unset, str]): Placeholder for month (2 digits).
        mb_pre_cooked_text (Union[Unset, str]): Return raw text in <code>checkoutKeywords</code>. Placeholders except
            counters are substituted.
        placeholder_user_name (Union[Unset, str]): Placeholder for current user name.
    """

    kwid_user_list: Union[Unset, str] = UNSET
    placeholder_counter_begin: Union[Unset, str] = UNSET
    max_children: Union[Unset, int] = UNSET
    ln_text: Union[Unset, int] = UNSET
    ln_id: Union[Unset, int] = UNSET
    separator_groupid_for_aspectlines: Union[Unset, str] = UNSET
    mb_raw_text: Union[Unset, str] = UNSET
    separator_aspectid_linekey: Union[Unset, str] = UNSET
    placeholder_date: Union[Unset, str] = UNSET
    kwid_version: Union[Unset, str] = UNSET
    kwid_version_comment: Union[Unset, str] = UNSET
    placeholder_counter_end: Union[Unset, str] = UNSET
    kwid_workflow: Union[Unset, str] = UNSET
    placeholder_day: Union[Unset, str] = UNSET
    max_tree_depth: Union[Unset, int] = UNSET
    ln_root_id: Union[Unset, int] = UNSET
    kwid_standard_list: Union[Unset, str] = UNSET
    mb_view: Union[Unset, "KeywordZ"] = UNSET
    placeholder_year: Union[Unset, str] = UNSET
    mb_edit: Union[Unset, "KeywordZ"] = UNSET
    placeholder_month: Union[Unset, str] = UNSET
    mb_pre_cooked_text: Union[Unset, str] = UNSET
    placeholder_user_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kwid_user_list = self.kwid_user_list

        placeholder_counter_begin = self.placeholder_counter_begin

        max_children = self.max_children

        ln_text = self.ln_text

        ln_id = self.ln_id

        separator_groupid_for_aspectlines = self.separator_groupid_for_aspectlines

        mb_raw_text = self.mb_raw_text

        separator_aspectid_linekey = self.separator_aspectid_linekey

        placeholder_date = self.placeholder_date

        kwid_version = self.kwid_version

        kwid_version_comment = self.kwid_version_comment

        placeholder_counter_end = self.placeholder_counter_end

        kwid_workflow = self.kwid_workflow

        placeholder_day = self.placeholder_day

        max_tree_depth = self.max_tree_depth

        ln_root_id = self.ln_root_id

        kwid_standard_list = self.kwid_standard_list

        mb_view: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_view, Unset):
            mb_view = self.mb_view.to_dict()

        placeholder_year = self.placeholder_year

        mb_edit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_edit, Unset):
            mb_edit = self.mb_edit.to_dict()

        placeholder_month = self.placeholder_month

        mb_pre_cooked_text = self.mb_pre_cooked_text

        placeholder_user_name = self.placeholder_user_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kwid_user_list is not UNSET:
            field_dict["KWID_USER_LIST"] = kwid_user_list
        if placeholder_counter_begin is not UNSET:
            field_dict["PLACEHOLDER_COUNTER_BEGIN"] = placeholder_counter_begin
        if max_children is not UNSET:
            field_dict["MAX_CHILDREN"] = max_children
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if separator_groupid_for_aspectlines is not UNSET:
            field_dict["SEPARATOR_GROUPID_FOR_ASPECTLINES"] = separator_groupid_for_aspectlines
        if mb_raw_text is not UNSET:
            field_dict["mbRawText"] = mb_raw_text
        if separator_aspectid_linekey is not UNSET:
            field_dict["SEPARATOR_ASPECTID_LINEKEY"] = separator_aspectid_linekey
        if placeholder_date is not UNSET:
            field_dict["PLACEHOLDER_DATE"] = placeholder_date
        if kwid_version is not UNSET:
            field_dict["KWID_VERSION"] = kwid_version
        if kwid_version_comment is not UNSET:
            field_dict["KWID_VERSION_COMMENT"] = kwid_version_comment
        if placeholder_counter_end is not UNSET:
            field_dict["PLACEHOLDER_COUNTER_END"] = placeholder_counter_end
        if kwid_workflow is not UNSET:
            field_dict["KWID_WORKFLOW"] = kwid_workflow
        if placeholder_day is not UNSET:
            field_dict["PLACEHOLDER_DAY"] = placeholder_day
        if max_tree_depth is not UNSET:
            field_dict["MAX_TREE_DEPTH"] = max_tree_depth
        if ln_root_id is not UNSET:
            field_dict["lnRootId"] = ln_root_id
        if kwid_standard_list is not UNSET:
            field_dict["KWID_STANDARD_LIST"] = kwid_standard_list
        if mb_view is not UNSET:
            field_dict["mbView"] = mb_view
        if placeholder_year is not UNSET:
            field_dict["PLACEHOLDER_YEAR"] = placeholder_year
        if mb_edit is not UNSET:
            field_dict["mbEdit"] = mb_edit
        if placeholder_month is not UNSET:
            field_dict["PLACEHOLDER_MONTH"] = placeholder_month
        if mb_pre_cooked_text is not UNSET:
            field_dict["mbPreCookedText"] = mb_pre_cooked_text
        if placeholder_user_name is not UNSET:
            field_dict["PLACEHOLDER_USER_NAME"] = placeholder_user_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.keyword_z import KeywordZ

        d = src_dict.copy()
        kwid_user_list = d.pop("KWID_USER_LIST", UNSET)

        placeholder_counter_begin = d.pop("PLACEHOLDER_COUNTER_BEGIN", UNSET)

        max_children = d.pop("MAX_CHILDREN", UNSET)

        ln_text = d.pop("lnText", UNSET)

        ln_id = d.pop("lnId", UNSET)

        separator_groupid_for_aspectlines = d.pop("SEPARATOR_GROUPID_FOR_ASPECTLINES", UNSET)

        mb_raw_text = d.pop("mbRawText", UNSET)

        separator_aspectid_linekey = d.pop("SEPARATOR_ASPECTID_LINEKEY", UNSET)

        placeholder_date = d.pop("PLACEHOLDER_DATE", UNSET)

        kwid_version = d.pop("KWID_VERSION", UNSET)

        kwid_version_comment = d.pop("KWID_VERSION_COMMENT", UNSET)

        placeholder_counter_end = d.pop("PLACEHOLDER_COUNTER_END", UNSET)

        kwid_workflow = d.pop("KWID_WORKFLOW", UNSET)

        placeholder_day = d.pop("PLACEHOLDER_DAY", UNSET)

        max_tree_depth = d.pop("MAX_TREE_DEPTH", UNSET)

        ln_root_id = d.pop("lnRootId", UNSET)

        kwid_standard_list = d.pop("KWID_STANDARD_LIST", UNSET)

        _mb_view = d.pop("mbView", UNSET)
        mb_view: Union[Unset, KeywordZ]
        if isinstance(_mb_view, Unset):
            mb_view = UNSET
        else:
            mb_view = KeywordZ.from_dict(_mb_view)

        placeholder_year = d.pop("PLACEHOLDER_YEAR", UNSET)

        _mb_edit = d.pop("mbEdit", UNSET)
        mb_edit: Union[Unset, KeywordZ]
        if isinstance(_mb_edit, Unset):
            mb_edit = UNSET
        else:
            mb_edit = KeywordZ.from_dict(_mb_edit)

        placeholder_month = d.pop("PLACEHOLDER_MONTH", UNSET)

        mb_pre_cooked_text = d.pop("mbPreCookedText", UNSET)

        placeholder_user_name = d.pop("PLACEHOLDER_USER_NAME", UNSET)

        keyword_c = cls(
            kwid_user_list=kwid_user_list,
            placeholder_counter_begin=placeholder_counter_begin,
            max_children=max_children,
            ln_text=ln_text,
            ln_id=ln_id,
            separator_groupid_for_aspectlines=separator_groupid_for_aspectlines,
            mb_raw_text=mb_raw_text,
            separator_aspectid_linekey=separator_aspectid_linekey,
            placeholder_date=placeholder_date,
            kwid_version=kwid_version,
            kwid_version_comment=kwid_version_comment,
            placeholder_counter_end=placeholder_counter_end,
            kwid_workflow=kwid_workflow,
            placeholder_day=placeholder_day,
            max_tree_depth=max_tree_depth,
            ln_root_id=ln_root_id,
            kwid_standard_list=kwid_standard_list,
            mb_view=mb_view,
            placeholder_year=placeholder_year,
            mb_edit=mb_edit,
            placeholder_month=placeholder_month,
            mb_pre_cooked_text=mb_pre_cooked_text,
            placeholder_user_name=placeholder_user_name,
        )

        keyword_c.additional_properties = d
        return keyword_c

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
