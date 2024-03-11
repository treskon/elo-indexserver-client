from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCreateNote2")


@_attrs_define
class BRequestIXServicePortIFCreateNote2:
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
        obj_id (Union[Unset, str]):
        note_type (Union[Unset, int]):
        templ_id (Union[Unset, str]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    obj_id: Union[Unset, str] = UNSET
    note_type: Union[Unset, int] = UNSET
    templ_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        obj_id = self.obj_id
        note_type = self.note_type
        templ_id = self.templ_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if note_type is not UNSET:
            field_dict["noteType"] = note_type
        if templ_id is not UNSET:
            field_dict["templId"] = templ_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        obj_id = d.pop("objId", UNSET)

        note_type = d.pop("noteType", UNSET)

        templ_id = d.pop("templId", UNSET)

        b_request_ix_service_port_if_create_note_2 = cls(
            ci=ci,
            obj_id=obj_id,
            note_type=note_type,
            templ_id=templ_id,
        )

        b_request_ix_service_port_if_create_note_2.additional_properties = d
        return b_request_ix_service_port_if_create_note_2

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
