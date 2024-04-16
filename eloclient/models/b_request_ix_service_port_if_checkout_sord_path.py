from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkout_sord_path_info import CheckoutSordPathInfo
    from ..models.client_info import ClientInfo
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutSordPath")


@_attrs_define
class BRequestIXServicePortIFCheckoutSordPath:
    """
    Attributes:
        sord_z (Union[Unset, SordZ]): <p>
            This class encapsulates the constants of <code>SordC</code>
             </p>

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
        obj_id (Union[Unset, str]):
        csi (Union[Unset, CheckoutSordPathInfo]):
    """

    sord_z: Union[Unset, "SordZ"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    obj_id: Union[Unset, str] = UNSET
    csi: Union[Unset, "CheckoutSordPathInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        obj_id = self.obj_id

        csi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.csi, Unset):
            csi = self.csi.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if ci is not UNSET:
            field_dict["ci"] = ci
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if csi is not UNSET:
            field_dict["csi"] = csi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkout_sord_path_info import CheckoutSordPathInfo
        from ..models.client_info import ClientInfo
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        obj_id = d.pop("objId", UNSET)

        _csi = d.pop("csi", UNSET)
        csi: Union[Unset, CheckoutSordPathInfo]
        if isinstance(_csi, Unset):
            csi = UNSET
        else:
            csi = CheckoutSordPathInfo.from_dict(_csi)

        b_request_ix_service_port_if_checkout_sord_path = cls(
            sord_z=sord_z,
            ci=ci,
            obj_id=obj_id,
            csi=csi,
        )

        b_request_ix_service_port_if_checkout_sord_path.additional_properties = d
        return b_request_ix_service_port_if_checkout_sord_path

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
