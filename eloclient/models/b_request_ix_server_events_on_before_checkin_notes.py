from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.lock_z import LockZ
    from ..models.note import Note
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServerEventsOnBeforeCheckinNotes")


@_attrs_define
class BRequestIXServerEventsOnBeforeCheckinNotes:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        notes (Union[Unset, List['Note']]):
        sords (Union[Unset, List['Sord']]):
        note_c (Union[Unset, str]):
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    notes: Union[Unset, List["Note"]] = UNSET
    sords: Union[Unset, List["Sord"]] = UNSET
    note_c: Union[Unset, str] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        notes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()

                notes.append(notes_item)

        sords: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sords, Unset):
            sords = []
            for sords_item_data in self.sords:
                sords_item = sords_item_data.to_dict()

                sords.append(sords_item)

        note_c = self.note_c
        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if notes is not UNSET:
            field_dict["notes"] = notes
        if sords is not UNSET:
            field_dict["sords"] = sords
        if note_c is not UNSET:
            field_dict["noteC"] = note_c
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.lock_z import LockZ
        from ..models.note import Note
        from ..models.sord import Sord

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        notes = []
        _notes = d.pop("notes", UNSET)
        for notes_item_data in _notes or []:
            notes_item = Note.from_dict(notes_item_data)

            notes.append(notes_item)

        sords = []
        _sords = d.pop("sords", UNSET)
        for sords_item_data in _sords or []:
            sords_item = Sord.from_dict(sords_item_data)

            sords.append(sords_item)

        note_c = d.pop("noteC", UNSET)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_server_events_on_before_checkin_notes = cls(
            ec=ec,
            notes=notes,
            sords=sords,
            note_c=note_c,
            unlock_z=unlock_z,
        )

        b_request_ix_server_events_on_before_checkin_notes.additional_properties = d
        return b_request_ix_server_events_on_before_checkin_notes

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
