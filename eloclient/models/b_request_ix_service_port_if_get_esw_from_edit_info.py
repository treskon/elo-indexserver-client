from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.edit_info import EditInfo
    from ..models.edit_info_esw_options import EditInfoEswOptions


T = TypeVar("T", bound="BRequestIXServicePortIFGetESWFromEditInfo")


@_attrs_define
class BRequestIXServicePortIFGetESWFromEditInfo:
    """
    Attributes:
        edit_infos (Union[Unset, List['EditInfo']]):
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
        esw_options (Union[Unset, EditInfoEswOptions]): Options for reading or writing of esw-files.
    """

    edit_infos: Union[Unset, List["EditInfo"]] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    esw_options: Union[Unset, "EditInfoEswOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edit_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.edit_infos, Unset):
            edit_infos = []
            for edit_infos_item_data in self.edit_infos:
                edit_infos_item = edit_infos_item_data.to_dict()
                edit_infos.append(edit_infos_item)

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        esw_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.esw_options, Unset):
            esw_options = self.esw_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if edit_infos is not UNSET:
            field_dict["editInfos"] = edit_infos
        if ci is not UNSET:
            field_dict["ci"] = ci
        if esw_options is not UNSET:
            field_dict["eswOptions"] = esw_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.edit_info import EditInfo
        from ..models.edit_info_esw_options import EditInfoEswOptions

        d = src_dict.copy()
        edit_infos = []
        _edit_infos = d.pop("editInfos", UNSET)
        for edit_infos_item_data in _edit_infos or []:
            edit_infos_item = EditInfo.from_dict(edit_infos_item_data)

            edit_infos.append(edit_infos_item)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _esw_options = d.pop("eswOptions", UNSET)
        esw_options: Union[Unset, EditInfoEswOptions]
        if isinstance(_esw_options, Unset):
            esw_options = UNSET
        else:
            esw_options = EditInfoEswOptions.from_dict(_esw_options)

        b_request_ix_service_port_if_get_esw_from_edit_info = cls(
            edit_infos=edit_infos,
            ci=ci,
            esw_options=esw_options,
        )

        b_request_ix_service_port_if_get_esw_from_edit_info.additional_properties = d
        return b_request_ix_service_port_if_get_esw_from_edit_info

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
