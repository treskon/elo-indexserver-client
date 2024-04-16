from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFFindNextWorkflows")


@_attrs_define
class BRequestIXServicePortIFFindNextWorkflows:
    """
    Attributes:
        search_id (Union[Unset, str]):
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
        max_results (Union[Unset, int]):
        index (Union[Unset, int]):
    """

    search_id: Union[Unset, str] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    max_results: Union[Unset, int] = UNSET
    index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        search_id = self.search_id

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        max_results = self.max_results

        index = self.index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_id is not UNSET:
            field_dict["searchId"] = search_id
        if ci is not UNSET:
            field_dict["ci"] = ci
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        search_id = d.pop("searchId", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        max_results = d.pop("maxResults", UNSET)

        index = d.pop("index", UNSET)

        b_request_ix_service_port_if_find_next_workflows = cls(
            search_id=search_id,
            ci=ci,
            max_results=max_results,
            index=index,
        )

        b_request_ix_service_port_if_find_next_workflows.additional_properties = d
        return b_request_ix_service_port_if_find_next_workflows

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
