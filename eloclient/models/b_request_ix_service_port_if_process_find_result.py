from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.process_info import ProcessInfo


T = TypeVar("T", bound="BRequestIXServicePortIFProcessFindResult")


@_attrs_define
class BRequestIXServicePortIFProcessFindResult:
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
        proc_info (Union[Unset, ProcessInfo]): Specific processing information for each node of processTrees(...) or
            processFindResults(...).
            The operations will be
             for existence (not null) in order of their appearance in ProcessInfo. Some of the underlying structures may
            allow
             toggling between prefix and postfix processing when used with processTrees.

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    search_id: Union[Unset, str] = UNSET
    proc_info: Union[Unset, "ProcessInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        search_id = self.search_id
        proc_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_info, Unset):
            proc_info = self.proc_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if proc_info is not UNSET:
            field_dict["procInfo"] = proc_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.process_info import ProcessInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        search_id = d.pop("searchId", UNSET)

        _proc_info = d.pop("procInfo", UNSET)
        proc_info: Union[Unset, ProcessInfo]
        if isinstance(_proc_info, Unset):
            proc_info = UNSET
        else:
            proc_info = ProcessInfo.from_dict(_proc_info)

        b_request_ix_service_port_if_process_find_result = cls(
            ci=ci,
            search_id=search_id,
            proc_info=proc_info,
        )

        b_request_ix_service_port_if_process_find_result.additional_properties = d
        return b_request_ix_service_port_if_process_find_result

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
