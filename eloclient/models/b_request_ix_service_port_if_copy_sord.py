from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.copy_info import CopyInfo
    from ..models.copy_sord_z import CopySordZ


T = TypeVar("T", bound="BRequestIXServicePortIFCopySord")


@_attrs_define
class BRequestIXServicePortIFCopySord:
    """
    Attributes:
        copy_info (Union[Unset, CopyInfo]): Controls the options of de.elo.ix.IXServicePortIF.copySord().
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        copy_sord_z (Union[Unset, CopySordZ]): This class encapsulates the constants of the CopySordsC class.
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
        new_parent_id (Union[Unset, str]):
        obj_id (Union[Unset, str]):
    """

    copy_info: Union[Unset, "CopyInfo"] = UNSET
    copy_sord_z: Union[Unset, "CopySordZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    new_parent_id: Union[Unset, str] = UNSET
    obj_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        copy_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_info, Unset):
            copy_info = self.copy_info.to_dict()

        copy_sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_sord_z, Unset):
            copy_sord_z = self.copy_sord_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        new_parent_id = self.new_parent_id

        obj_id = self.obj_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if copy_info is not UNSET:
            field_dict["copyInfo"] = copy_info
        if copy_sord_z is not UNSET:
            field_dict["copySordZ"] = copy_sord_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if new_parent_id is not UNSET:
            field_dict["newParentId"] = new_parent_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.copy_info import CopyInfo
        from ..models.copy_sord_z import CopySordZ

        d = src_dict.copy()
        _copy_info = d.pop("copyInfo", UNSET)
        copy_info: Union[Unset, CopyInfo]
        if isinstance(_copy_info, Unset):
            copy_info = UNSET
        else:
            copy_info = CopyInfo.from_dict(_copy_info)

        _copy_sord_z = d.pop("copySordZ", UNSET)
        copy_sord_z: Union[Unset, CopySordZ]
        if isinstance(_copy_sord_z, Unset):
            copy_sord_z = UNSET
        else:
            copy_sord_z = CopySordZ.from_dict(_copy_sord_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        new_parent_id = d.pop("newParentId", UNSET)

        obj_id = d.pop("objId", UNSET)

        b_request_ix_service_port_if_copy_sord = cls(
            copy_info=copy_info,
            copy_sord_z=copy_sord_z,
            ci=ci,
            new_parent_id=new_parent_id,
            obj_id=obj_id,
        )

        b_request_ix_service_port_if_copy_sord.additional_properties = d
        return b_request_ix_service_port_if_copy_sord

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
