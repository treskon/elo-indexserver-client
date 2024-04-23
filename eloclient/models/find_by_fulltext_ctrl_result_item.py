from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.note import Note
    from ..models.sord import Sord


T = TypeVar("T", bound="FindByFulltextCtrlResultItem")


@_attrs_define
class FindByFulltextCtrlResultItem:
    """A search using FindByFulltextCtrl returns this result items in addition to findResult.sords.

    Attributes:
        t_stamp (Union[Unset, str]): Timestamp of the last change of either indexing information, note data, fulltext
            content or
            attachment fulltext content.
        note (Union[Unset, Note]): <p>
            This helper class inherits all members from <code>NoteData</code> and adds a static member to
             access the bit constants for the <code>NoteData</code> members.
             </p>
        select_type (Union[Unset, int]): Corresponds to the table from which the Sord/ Note was selected.
            <p>
             <i>Note: For internal use only.</i>
             </p>
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    t_stamp: Union[Unset, str] = UNSET
    note: Union[Unset, "Note"] = UNSET
    select_type: Union[Unset, int] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        t_stamp = self.t_stamp

        note: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note, Unset):
            note = self.note.to_dict()

        select_type = self.select_type

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if note is not UNSET:
            field_dict["note"] = note
        if select_type is not UNSET:
            field_dict["selectType"] = select_type
        if sord is not UNSET:
            field_dict["sord"] = sord

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.note import Note
        from ..models.sord import Sord

        d = src_dict.copy()
        t_stamp = d.pop("TStamp", UNSET)

        _note = d.pop("note", UNSET)
        note: Union[Unset, Note]
        if isinstance(_note, Unset):
            note = UNSET
        else:
            note = Note.from_dict(_note)

        select_type = d.pop("selectType", UNSET)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        find_by_fulltext_ctrl_result_item = cls(
            t_stamp=t_stamp,
            note=note,
            select_type=select_type,
            sord=sord,
        )

        find_by_fulltext_ctrl_result_item.additional_properties = d
        return find_by_fulltext_ctrl_result_item

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
