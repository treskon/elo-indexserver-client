from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invalidate_cache_info_param import InvalidateCacheInfoParam
    from ..models.wf_cache_sync_info import WFCacheSyncInfo


T = TypeVar("T", bound="InvalidateCacheInfo")


@_attrs_define
class InvalidateCacheInfo:
    """This class contains the parameters for the API function invalidateCache2

    Attributes:
        flags (Union[Unset, int]): A combination of bits defined in InvalidateCacheC.
        id (Union[Unset, int]): A numeric ID to specify an object, workflow etc. If <code>flags</code> contains
            <code>InvalidateC.
            WORKFLOWS</code>
             this element defines the ID of the active workflow to be updated in the cache.
        guid (Union[Unset, str]): A GUID to specify the modified object.
        value (Union[Unset, str]): Optional value related to {@link #flags} member.
            If flags specifies {@link InvalidateCacheC#OBJKEY_DISPLAY_DATA},
             this value contains the
        parameters (Union[Unset, List['InvalidateCacheInfoParam']]):
        workflow_cache_sync_infos (Union[Unset, List['WFCacheSyncInfo']]):
        ticket (Union[Unset, str]): Refresh options of this session.
    """

    flags: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    parameters: Union[Unset, List["InvalidateCacheInfoParam"]] = UNSET
    workflow_cache_sync_infos: Union[Unset, List["WFCacheSyncInfo"]] = UNSET
    ticket: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flags = self.flags
        id = self.id
        guid = self.guid
        value = self.value
        parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = []
            for componentsschemas_list_of_invalidate_cache_info_param_item_data in self.parameters:
                componentsschemas_list_of_invalidate_cache_info_param_item = (
                    componentsschemas_list_of_invalidate_cache_info_param_item_data.to_dict()
                )

                parameters.append(componentsschemas_list_of_invalidate_cache_info_param_item)

        workflow_cache_sync_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.workflow_cache_sync_infos, Unset):
            workflow_cache_sync_infos = []
            for componentsschemas_list_of_wf_cache_sync_info_item_data in self.workflow_cache_sync_infos:
                componentsschemas_list_of_wf_cache_sync_info_item = (
                    componentsschemas_list_of_wf_cache_sync_info_item_data.to_dict()
                )

                workflow_cache_sync_infos.append(componentsschemas_list_of_wf_cache_sync_info_item)

        ticket = self.ticket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flags is not UNSET:
            field_dict["flags"] = flags
        if id is not UNSET:
            field_dict["id"] = id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if value is not UNSET:
            field_dict["value"] = value
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if workflow_cache_sync_infos is not UNSET:
            field_dict["workflowCacheSyncInfos"] = workflow_cache_sync_infos
        if ticket is not UNSET:
            field_dict["ticket"] = ticket

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invalidate_cache_info_param import InvalidateCacheInfoParam
        from ..models.wf_cache_sync_info import WFCacheSyncInfo

        d = src_dict.copy()
        flags = d.pop("flags", UNSET)

        id = d.pop("id", UNSET)

        guid = d.pop("guid", UNSET)

        value = d.pop("value", UNSET)

        parameters = []
        _parameters = d.pop("parameters", UNSET)
        for componentsschemas_list_of_invalidate_cache_info_param_item_data in _parameters or []:
            componentsschemas_list_of_invalidate_cache_info_param_item = InvalidateCacheInfoParam.from_dict(
                componentsschemas_list_of_invalidate_cache_info_param_item_data
            )

            parameters.append(componentsschemas_list_of_invalidate_cache_info_param_item)

        workflow_cache_sync_infos = []
        _workflow_cache_sync_infos = d.pop("workflowCacheSyncInfos", UNSET)
        for componentsschemas_list_of_wf_cache_sync_info_item_data in _workflow_cache_sync_infos or []:
            componentsschemas_list_of_wf_cache_sync_info_item = WFCacheSyncInfo.from_dict(
                componentsschemas_list_of_wf_cache_sync_info_item_data
            )

            workflow_cache_sync_infos.append(componentsschemas_list_of_wf_cache_sync_info_item)

        ticket = d.pop("ticket", UNSET)

        invalidate_cache_info = cls(
            flags=flags,
            id=id,
            guid=guid,
            value=value,
            parameters=parameters,
            workflow_cache_sync_infos=workflow_cache_sync_infos,
            ticket=ticket,
        )

        invalidate_cache_info.additional_properties = d
        return invalidate_cache_info

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
