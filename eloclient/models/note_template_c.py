from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note_template_z import NoteTemplateZ


T = TypeVar("T", bound="NoteTemplateC")


@_attrs_define
class NoteTemplateC:
    """Constants for class NoteTemplate

    Attributes:
        mb_id (Union[Unset, str]): Member bit: id
        mb_name (Union[Unset, str]): Member bit: name
        mb_user_id (Union[Unset, str]): Member bit: UserId
        mb_note_text (Union[Unset, str]): Member bit: noteText
        mb_note_image (Union[Unset, str]): Member bit: noteImage
        mb_acl (Union[Unset, str]): Member bit: acl, aclItems
        mb_all_members (Union[Unset, str]): Member bit: all members
        mb_min (Union[Unset, NoteTemplateZ]):
        mb_all (Union[Unset, NoteTemplateZ]):
        placeholder_username (Union[Unset, str]): Placeholder for user name. This constant can be used in
            NoteTemplate.textInfo.
            text as a placeholder for the current
             user name.
        placeholder_date (Union[Unset, str]): Placeholder for date. This constant can be used in NoteTemplate.textInfo.
            text as a placeholder for the current
             date.
        placeholder_time (Union[Unset, str]): Placeholder for time. This constant can be used in NoteTemplate.textInfo.
            text as a placeholder for the current
             time.
        userid_all (Union[Unset, str]): Read/write note template visible for all users
        raw_item_separator (Union[Unset, str]): Separates the values in the raw data representation.
        raw_subitem_separator (Union[Unset, str]): Separates the values of the subitems in the raw data representation.
        raw_stampinfo_separator (Union[Unset, str]): Separates the values of the name and text in the raw data
            representation.
        ln_name (Union[Unset, int]): Length of note template name.
        ln_text (Union[Unset, int]): Length of text in class NoteText.
    """

    mb_id: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_note_text: Union[Unset, str] = UNSET
    mb_note_image: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_min: Union[Unset, "NoteTemplateZ"] = UNSET
    mb_all: Union[Unset, "NoteTemplateZ"] = UNSET
    placeholder_username: Union[Unset, str] = UNSET
    placeholder_date: Union[Unset, str] = UNSET
    placeholder_time: Union[Unset, str] = UNSET
    userid_all: Union[Unset, str] = UNSET
    raw_item_separator: Union[Unset, str] = UNSET
    raw_subitem_separator: Union[Unset, str] = UNSET
    raw_stampinfo_separator: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    ln_text: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id
        mb_name = self.mb_name
        mb_user_id = self.mb_user_id
        mb_note_text = self.mb_note_text
        mb_note_image = self.mb_note_image
        mb_acl = self.mb_acl
        mb_all_members = self.mb_all_members
        mb_min: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_min, Unset):
            mb_min = self.mb_min.to_dict()

        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        placeholder_username = self.placeholder_username
        placeholder_date = self.placeholder_date
        placeholder_time = self.placeholder_time
        userid_all = self.userid_all
        raw_item_separator = self.raw_item_separator
        raw_subitem_separator = self.raw_subitem_separator
        raw_stampinfo_separator = self.raw_stampinfo_separator
        ln_name = self.ln_name
        ln_text = self.ln_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_note_text is not UNSET:
            field_dict["mbNoteText"] = mb_note_text
        if mb_note_image is not UNSET:
            field_dict["mbNoteImage"] = mb_note_image
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_min is not UNSET:
            field_dict["mbMin"] = mb_min
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if placeholder_username is not UNSET:
            field_dict["PLACEHOLDER_USERNAME"] = placeholder_username
        if placeholder_date is not UNSET:
            field_dict["PLACEHOLDER_DATE"] = placeholder_date
        if placeholder_time is not UNSET:
            field_dict["PLACEHOLDER_TIME"] = placeholder_time
        if userid_all is not UNSET:
            field_dict["USERID_ALL"] = userid_all
        if raw_item_separator is not UNSET:
            field_dict["RAW_ITEM_SEPARATOR"] = raw_item_separator
        if raw_subitem_separator is not UNSET:
            field_dict["RAW_SUBITEM_SEPARATOR"] = raw_subitem_separator
        if raw_stampinfo_separator is not UNSET:
            field_dict["RAW_STAMPINFO_SEPARATOR"] = raw_stampinfo_separator
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note_template_z import NoteTemplateZ

        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_note_text = d.pop("mbNoteText", UNSET)

        mb_note_image = d.pop("mbNoteImage", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        _mb_min = d.pop("mbMin", UNSET)
        mb_min: Union[Unset, NoteTemplateZ]
        if isinstance(_mb_min, Unset):
            mb_min = UNSET
        else:
            mb_min = NoteTemplateZ.from_dict(_mb_min)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, NoteTemplateZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = NoteTemplateZ.from_dict(_mb_all)

        placeholder_username = d.pop("PLACEHOLDER_USERNAME", UNSET)

        placeholder_date = d.pop("PLACEHOLDER_DATE", UNSET)

        placeholder_time = d.pop("PLACEHOLDER_TIME", UNSET)

        userid_all = d.pop("USERID_ALL", UNSET)

        raw_item_separator = d.pop("RAW_ITEM_SEPARATOR", UNSET)

        raw_subitem_separator = d.pop("RAW_SUBITEM_SEPARATOR", UNSET)

        raw_stampinfo_separator = d.pop("RAW_STAMPINFO_SEPARATOR", UNSET)

        ln_name = d.pop("lnName", UNSET)

        ln_text = d.pop("lnText", UNSET)

        note_template_c = cls(
            mb_id=mb_id,
            mb_name=mb_name,
            mb_user_id=mb_user_id,
            mb_note_text=mb_note_text,
            mb_note_image=mb_note_image,
            mb_acl=mb_acl,
            mb_all_members=mb_all_members,
            mb_min=mb_min,
            mb_all=mb_all,
            placeholder_username=placeholder_username,
            placeholder_date=placeholder_date,
            placeholder_time=placeholder_time,
            userid_all=userid_all,
            raw_item_separator=raw_item_separator,
            raw_subitem_separator=raw_subitem_separator,
            raw_stampinfo_separator=raw_stampinfo_separator,
            ln_name=ln_name,
            ln_text=ln_text,
        )

        note_template_c.additional_properties = d
        return note_template_c

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
