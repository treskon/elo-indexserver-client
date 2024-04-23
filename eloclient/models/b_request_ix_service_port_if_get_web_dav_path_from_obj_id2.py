from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.get_web_dav_path_options import GetWebDAVPathOptions


T = TypeVar("T", bound="BRequestIXServicePortIFGetWebDAVPathFromObjID2")


@_attrs_define
class BRequestIXServicePortIFGetWebDAVPathFromObjID2:
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
        options (Union[Unset, GetWebDAVPathOptions]): Parameter class for the function {@link
            IXServicePortIF#getWebDAVPathFromObjID2}
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    options: Union[Unset, "GetWebDAVPathOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.get_web_dav_path_options import GetWebDAVPathOptions

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _options = d.pop("options", UNSET)
        options: Union[Unset, GetWebDAVPathOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = GetWebDAVPathOptions.from_dict(_options)

        b_request_ix_service_port_if_get_web_dav_path_from_obj_id2 = cls(
            ci=ci,
            options=options,
        )

        b_request_ix_service_port_if_get_web_dav_path_from_obj_id2.additional_properties = d
        return b_request_ix_service_port_if_get_web_dav_path_from_obj_id2

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
