from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="HashTag")


@_attrs_define
class HashTag:
    """This class represents a HashTag

    Attributes:
        hstg_name (Union[Unset, str]): HashTag Name.
        last_used_iso (Union[Unset, str]): Last used.
            It holds the ISO formatted date of the last use of this HashTag In order to convert
             this value into a date object, invoke function {@link de.elo.ix.client.IXConnection#isoToDate}.
        hstg_guid (Union[Unset, str]): HashTag GUID. Unique identifier.
        create_date_iso (Union[Unset, str]): Create date. It holds the ISO formatted create date in the time zone of the
            client application.
            In order to convert this value into a date object, invoke function
             {@link de.elo.ix.client.IXConnection#isoToDate}.
        t_stamp (Union[Unset, str]): Timestamp for replication.
        counter (Union[Unset, int]): Counter. Counts how often this HashTag is used.
        status (Union[Unset, int]): Status.
    """

    hstg_name: Union[Unset, str] = UNSET
    last_used_iso: Union[Unset, str] = UNSET
    hstg_guid: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    counter: Union[Unset, int] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hstg_name = self.hstg_name

        last_used_iso = self.last_used_iso

        hstg_guid = self.hstg_guid

        create_date_iso = self.create_date_iso

        t_stamp = self.t_stamp

        counter = self.counter

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hstg_name is not UNSET:
            field_dict["hstgName"] = hstg_name
        if last_used_iso is not UNSET:
            field_dict["lastUsedIso"] = last_used_iso
        if hstg_guid is not UNSET:
            field_dict["hstgGuid"] = hstg_guid
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if counter is not UNSET:
            field_dict["counter"] = counter
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hstg_name = d.pop("hstgName", UNSET)

        last_used_iso = d.pop("lastUsedIso", UNSET)

        hstg_guid = d.pop("hstgGuid", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        counter = d.pop("counter", UNSET)

        status = d.pop("status", UNSET)

        hash_tag = cls(
            hstg_name=hstg_name,
            last_used_iso=last_used_iso,
            hstg_guid=hstg_guid,
            create_date_iso=create_date_iso,
            t_stamp=t_stamp,
            counter=counter,
            status=status,
        )

        hash_tag.additional_properties = d
        return hash_tag

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
