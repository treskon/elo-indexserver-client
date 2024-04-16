from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.edit_info_z import EditInfoZ


T = TypeVar("T", bound="BRequestIXServicePortIFCreateSord")


@_attrs_define
class BRequestIXServicePortIFCreateSord:
    """
    Attributes:
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
        mask_id (Union[Unset, str]):
        edit_info_z (Union[Unset, EditInfoZ]): This class encapsulates the constants of the EditInfoC class.
            EditInfo also returns a Sord object
             and a SordZ member is included to control the Sord data returned.

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        parent_id (Union[Unset, str]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    mask_id: Union[Unset, str] = UNSET
    edit_info_z: Union[Unset, "EditInfoZ"] = UNSET
    parent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        mask_id = self.mask_id

        edit_info_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.edit_info_z, Unset):
            edit_info_z = self.edit_info_z.to_dict()

        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if mask_id is not UNSET:
            field_dict["maskId"] = mask_id
        if edit_info_z is not UNSET:
            field_dict["editInfoZ"] = edit_info_z
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.edit_info_z import EditInfoZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        mask_id = d.pop("maskId", UNSET)

        _edit_info_z = d.pop("editInfoZ", UNSET)
        edit_info_z: Union[Unset, EditInfoZ]
        if isinstance(_edit_info_z, Unset):
            edit_info_z = UNSET
        else:
            edit_info_z = EditInfoZ.from_dict(_edit_info_z)

        parent_id = d.pop("parentId", UNSET)

        b_request_ix_service_port_if_create_sord = cls(
            ci=ci,
            mask_id=mask_id,
            edit_info_z=edit_info_z,
            parent_id=parent_id,
        )

        b_request_ix_service_port_if_create_sord.additional_properties = d
        return b_request_ix_service_port_if_create_sord

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
