from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerInfoDM")


@_attrs_define
class ServerInfoDM:
    """This class contains infomation about the filing paths of the document manager (DM).

    Attributes:
        basis_store_ids (Union[Unset, List[int]]):
        backup_store_ids (Union[Unset, List[int]]):
        store_mode (Union[Unset, int]): Mode to be used to fill the filing paths. This value is a bitset of the
            ServerInfoDMC.STOREMODE_* constants.
        blackening_enabled (Union[Unset, bool]): DM is enabled for blackening of document parts.
        restore_store_id (Union[Unset, int]): ID of restore path.
        proxy_mode (Union[Unset, int]): DM proxy mode. Read-only.
            <table>
             <tr>
             <td>-1</td>
             <td>Proxy mode is not active</td>
             </tr>
             <tr>
             <td>0</td>
             <td>Main instance</td>
             </tr>
             <tr>
             <td>&gt;0</td>
             <td>Branch instance</td>
             </tr>
             </table>
    """

    basis_store_ids: Union[Unset, List[int]] = UNSET
    backup_store_ids: Union[Unset, List[int]] = UNSET
    store_mode: Union[Unset, int] = UNSET
    blackening_enabled: Union[Unset, bool] = UNSET
    restore_store_id: Union[Unset, int] = UNSET
    proxy_mode: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        basis_store_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.basis_store_ids, Unset):
            basis_store_ids = self.basis_store_ids

        backup_store_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.backup_store_ids, Unset):
            backup_store_ids = self.backup_store_ids

        store_mode = self.store_mode

        blackening_enabled = self.blackening_enabled

        restore_store_id = self.restore_store_id

        proxy_mode = self.proxy_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basis_store_ids is not UNSET:
            field_dict["basisStoreIds"] = basis_store_ids
        if backup_store_ids is not UNSET:
            field_dict["backupStoreIds"] = backup_store_ids
        if store_mode is not UNSET:
            field_dict["storeMode"] = store_mode
        if blackening_enabled is not UNSET:
            field_dict["blackeningEnabled"] = blackening_enabled
        if restore_store_id is not UNSET:
            field_dict["restoreStoreId"] = restore_store_id
        if proxy_mode is not UNSET:
            field_dict["proxyMode"] = proxy_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        basis_store_ids = cast(List[int], d.pop("basisStoreIds", UNSET))

        backup_store_ids = cast(List[int], d.pop("backupStoreIds", UNSET))

        store_mode = d.pop("storeMode", UNSET)

        blackening_enabled = d.pop("blackeningEnabled", UNSET)

        restore_store_id = d.pop("restoreStoreId", UNSET)

        proxy_mode = d.pop("proxyMode", UNSET)

        server_info_dm = cls(
            basis_store_ids=basis_store_ids,
            backup_store_ids=backup_store_ids,
            store_mode=store_mode,
            blackening_enabled=blackening_enabled,
            restore_store_id=restore_store_id,
            proxy_mode=proxy_mode,
        )

        server_info_dm.additional_properties = d
        return server_info_dm

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
