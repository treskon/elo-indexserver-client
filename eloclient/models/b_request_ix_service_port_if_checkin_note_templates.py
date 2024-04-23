from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.note_template import NoteTemplate
    from ..models.note_template_z import NoteTemplateZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinNoteTemplates")


@_attrs_define
class BRequestIXServicePortIFCheckinNoteTemplates:
    """
    Attributes:
        ntempl_z (Union[Unset, NoteTemplateZ]):
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        note_templates (Union[Unset, List['NoteTemplate']]):
    """

    ntempl_z: Union[Unset, "NoteTemplateZ"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    note_templates: Union[Unset, List["NoteTemplate"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ntempl_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ntempl_z, Unset):
            ntempl_z = self.ntempl_z.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        note_templates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.note_templates, Unset):
            note_templates = []
            for note_templates_item_data in self.note_templates:
                note_templates_item = note_templates_item_data.to_dict()
                note_templates.append(note_templates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ntempl_z is not UNSET:
            field_dict["ntemplZ"] = ntempl_z
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if note_templates is not UNSET:
            field_dict["noteTemplates"] = note_templates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.note_template import NoteTemplate
        from ..models.note_template_z import NoteTemplateZ

        d = src_dict.copy()
        _ntempl_z = d.pop("ntemplZ", UNSET)
        ntempl_z: Union[Unset, NoteTemplateZ]
        if isinstance(_ntempl_z, Unset):
            ntempl_z = UNSET
        else:
            ntempl_z = NoteTemplateZ.from_dict(_ntempl_z)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        note_templates = []
        _note_templates = d.pop("noteTemplates", UNSET)
        for note_templates_item_data in _note_templates or []:
            note_templates_item = NoteTemplate.from_dict(note_templates_item_data)

            note_templates.append(note_templates_item)

        b_request_ix_service_port_if_checkin_note_templates = cls(
            ntempl_z=ntempl_z,
            unlock_z=unlock_z,
            ci=ci,
            note_templates=note_templates,
        )

        b_request_ix_service_port_if_checkin_note_templates.additional_properties = d
        return b_request_ix_service_port_if_checkin_note_templates

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
