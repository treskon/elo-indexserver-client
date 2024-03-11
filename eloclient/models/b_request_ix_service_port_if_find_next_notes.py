from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.note_z import NoteZ


T = TypeVar("T", bound="BRequestIXServicePortIFFindNextNotes")


@_attrs_define
class BRequestIXServicePortIFFindNextNotes:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        search_id (Union[Unset, str]):
        idx (Union[Unset, int]):
        max_ (Union[Unset, int]):
        note_z (Union[Unset, NoteZ]): This class encapsulates the constants of the NoteC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    search_id: Union[Unset, str] = UNSET
    idx: Union[Unset, int] = UNSET
    max_: Union[Unset, int] = UNSET
    note_z: Union[Unset, "NoteZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        search_id = self.search_id
        idx = self.idx
        max_ = self.max_
        note_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.note_z, Unset):
            note_z = self.note_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if idx is not UNSET:
            field_dict["idx"] = idx
        if max_ is not UNSET:
            field_dict["max"] = max_
        if note_z is not UNSET:
            field_dict["noteZ"] = note_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.note_z import NoteZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        search_id = d.pop("searchId", UNSET)

        idx = d.pop("idx", UNSET)

        max_ = d.pop("max", UNSET)

        _note_z = d.pop("noteZ", UNSET)
        note_z: Union[Unset, NoteZ]
        if isinstance(_note_z, Unset):
            note_z = UNSET
        else:
            note_z = NoteZ.from_dict(_note_z)

        b_request_ix_service_port_if_find_next_notes = cls(
            ci=ci,
            search_id=search_id,
            idx=idx,
            max_=max_,
            note_z=note_z,
        )

        b_request_ix_service_port_if_find_next_notes.additional_properties = d
        return b_request_ix_service_port_if_find_next_notes

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
