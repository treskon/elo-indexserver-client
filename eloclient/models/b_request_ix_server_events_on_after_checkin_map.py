from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.key_value import KeyValue
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServerEventsOnAfterCheckinMap")


@_attrs_define
class BRequestIXServerEventsOnAfterCheckinMap:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        domain_name (Union[Unset, str]):
        id (Union[Unset, str]):
        obj_id (Union[Unset, int]):
        data (Union[Unset, List['KeyValue']]):
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    domain_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    data: Union[Unset, List["KeyValue"]] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        domain_name = self.domain_name
        id = self.id
        obj_id = self.obj_id
        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if domain_name is not UNSET:
            field_dict["domainName"] = domain_name
        if id is not UNSET:
            field_dict["id"] = id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if data is not UNSET:
            field_dict["data"] = data
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.key_value import KeyValue
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        domain_name = d.pop("domainName", UNSET)

        id = d.pop("id", UNSET)

        obj_id = d.pop("objId", UNSET)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = KeyValue.from_dict(data_item_data)

            data.append(data_item)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_server_events_on_after_checkin_map = cls(
            ec=ec,
            domain_name=domain_name,
            id=id,
            obj_id=obj_id,
            data=data,
            unlock_z=unlock_z,
        )

        b_request_ix_server_events_on_after_checkin_map.additional_properties = d
        return b_request_ix_server_events_on_after_checkin_map

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
