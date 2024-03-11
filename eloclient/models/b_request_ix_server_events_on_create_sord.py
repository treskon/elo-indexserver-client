from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_info_z import EditInfoZ
    from ..models.ix_server_events_context import IXServerEventsContext


T = TypeVar("T", bound="BRequestIXServerEventsOnCreateSord")


@_attrs_define
class BRequestIXServerEventsOnCreateSord:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        parent_id (Union[Unset, str]):
        mask_id (Union[Unset, str]):
        edit_z (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
            EditInfo also returns a Sord object and a SordZ member
             is included to control the Sord data returned.

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    parent_id: Union[Unset, str] = UNSET
    mask_id: Union[Unset, str] = UNSET
    edit_z: Union[Unset, "EditInfoZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        parent_id = self.parent_id
        mask_id = self.mask_id
        edit_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_z, Unset):
            edit_z = self.edit_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if mask_id is not UNSET:
            field_dict["maskId"] = mask_id
        if edit_z is not UNSET:
            field_dict["editZ"] = edit_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.edit_info_z import EditInfoZ
        from ..models.ix_server_events_context import IXServerEventsContext

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        parent_id = d.pop("parentId", UNSET)

        mask_id = d.pop("maskId", UNSET)

        _edit_z = d.pop("editZ", UNSET)
        edit_z: Union[Unset, EditInfoZ]
        if isinstance(_edit_z, Unset):
            edit_z = UNSET
        else:
            edit_z = EditInfoZ.from_dict(_edit_z)

        b_request_ix_server_events_on_create_sord = cls(
            ec=ec,
            parent_id=parent_id,
            mask_id=mask_id,
            edit_z=edit_z,
        )

        b_request_ix_server_events_on_create_sord.additional_properties = d
        return b_request_ix_server_events_on_create_sord

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
