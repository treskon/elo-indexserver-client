from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """Alerts are messages shown in the alert tab of ELO client.

    Attributes:
        dest (Union[Unset, int]):
        dest_name (Union[Unset, str]): User name of the recipient.
        source (Union[Unset, int]): User ID of the sender.
            DB column: source
        source_name (Union[Unset, str]): User name of the sender.
        type (Union[Unset, int]): Alert type.
            DB column: alerttype
        obj_id (Union[Unset, int]): Object ID.
            DB column: objid
        extra1 (Union[Unset, int]): Extra data 1.
            DB column: extra1
        extra2 (Union[Unset, int]): Extra data 2.
            DB column: extra2
        memo (Union[Unset, str]): Comment text.
            DB column: alertmemo
        time (Union[Unset, int]): Date and time when the alert was created.
            DB column: alerttime
        time_iso (Union[Unset, str]): ISO date when the alert was created. Timezone is related to ClientInfo.timezone.
    """

    dest: Union[Unset, int] = UNSET
    dest_name: Union[Unset, str] = UNSET
    source: Union[Unset, int] = UNSET
    source_name: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    obj_id: Union[Unset, int] = UNSET
    extra1: Union[Unset, int] = UNSET
    extra2: Union[Unset, int] = UNSET
    memo: Union[Unset, str] = UNSET
    time: Union[Unset, int] = UNSET
    time_iso: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dest = self.dest
        dest_name = self.dest_name
        source = self.source
        source_name = self.source_name
        type = self.type
        obj_id = self.obj_id
        extra1 = self.extra1
        extra2 = self.extra2
        memo = self.memo
        time = self.time
        time_iso = self.time_iso

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dest is not UNSET:
            field_dict["dest"] = dest
        if dest_name is not UNSET:
            field_dict["destName"] = dest_name
        if source is not UNSET:
            field_dict["source"] = source
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if type is not UNSET:
            field_dict["type"] = type
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if extra1 is not UNSET:
            field_dict["extra1"] = extra1
        if extra2 is not UNSET:
            field_dict["extra2"] = extra2
        if memo is not UNSET:
            field_dict["memo"] = memo
        if time is not UNSET:
            field_dict["time"] = time
        if time_iso is not UNSET:
            field_dict["timeIso"] = time_iso

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dest = d.pop("dest", UNSET)

        dest_name = d.pop("destName", UNSET)

        source = d.pop("source", UNSET)

        source_name = d.pop("sourceName", UNSET)

        type = d.pop("type", UNSET)

        obj_id = d.pop("objId", UNSET)

        extra1 = d.pop("extra1", UNSET)

        extra2 = d.pop("extra2", UNSET)

        memo = d.pop("memo", UNSET)

        time = d.pop("time", UNSET)

        time_iso = d.pop("timeIso", UNSET)

        alert = cls(
            dest=dest,
            dest_name=dest_name,
            source=source,
            source_name=source_name,
            type=type,
            obj_id=obj_id,
            extra1=extra1,
            extra2=extra2,
            memo=memo,
            time=time,
            time_iso=time_iso,
        )

        alert.additional_properties = d
        return alert

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
