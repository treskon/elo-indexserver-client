from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.lock_z import LockZ
    from ..models.note_template_z import NoteTemplateZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutNoteTemplates")


@_attrs_define
class BRequestIXServicePortIFCheckoutNoteTemplates:
    """
    Attributes:
        ntempl_z (Union[Unset, NoteTemplateZ]):
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
        ids (Union[Unset, List[str]]):
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        user_id (Union[Unset, str]):
    """

    ntempl_z: Union[Unset, "NoteTemplateZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    ids: Union[Unset, List[str]] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ntempl_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ntempl_z, Unset):
            ntempl_z = self.ntempl_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ntempl_z is not UNSET:
            field_dict["ntemplZ"] = ntempl_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if ids is not UNSET:
            field_dict["ids"] = ids
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.lock_z import LockZ
        from ..models.note_template_z import NoteTemplateZ

        d = src_dict.copy()
        _ntempl_z = d.pop("ntemplZ", UNSET)
        ntempl_z: Union[Unset, NoteTemplateZ]
        if isinstance(_ntempl_z, Unset):
            ntempl_z = UNSET
        else:
            ntempl_z = NoteTemplateZ.from_dict(_ntempl_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        ids = cast(List[str], d.pop("ids", UNSET))

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        user_id = d.pop("userId", UNSET)

        b_request_ix_service_port_if_checkout_note_templates = cls(
            ntempl_z=ntempl_z,
            ci=ci,
            ids=ids,
            lock_z=lock_z,
            user_id=user_id,
        )

        b_request_ix_service_port_if_checkout_note_templates.additional_properties = d
        return b_request_ix_service_port_if_checkout_note_templates

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
