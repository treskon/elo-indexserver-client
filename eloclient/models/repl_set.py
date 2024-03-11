from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplSet")


@_attrs_define
class ReplSet:
    """<p>
    Objects of this class store the replication information of archive entries.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            dw (Union[Unset, List[int]]):
            dw_sync (Union[Unset, List[int]]):
            obj_id (Union[Unset, int]): This replication information belongs to the archive entry with ID <code>objId</code>
            t_stamp (Union[Unset, str]): Timestamp of the last alteration of replication sets for the corresponding archive
                entry.
                The format is
                 JJJJ.MM.DD.hh.mm.ss
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            combi_guid (Union[Unset, str]):
    """

    dw: Union[Unset, List[int]] = UNSET
    dw_sync: Union[Unset, List[int]] = UNSET
    obj_id: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    combi_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dw: Union[Unset, List[int]] = UNSET
        if not isinstance(self.dw, Unset):
            dw = self.dw

        dw_sync: Union[Unset, List[int]] = UNSET
        if not isinstance(self.dw_sync, Unset):
            dw_sync = self.dw_sync

        obj_id = self.obj_id
        t_stamp = self.t_stamp
        t_stamp_sync = self.t_stamp_sync
        combi_guid = self.combi_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dw is not UNSET:
            field_dict["dw"] = dw
        if dw_sync is not UNSET:
            field_dict["dwSync"] = dw_sync
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if combi_guid is not UNSET:
            field_dict["combiGuid"] = combi_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dw = cast(List[int], d.pop("dw", UNSET))

        dw_sync = cast(List[int], d.pop("dwSync", UNSET))

        obj_id = d.pop("objId", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        combi_guid = d.pop("combiGuid", UNSET)

        repl_set = cls(
            dw=dw,
            dw_sync=dw_sync,
            obj_id=obj_id,
            t_stamp=t_stamp,
            t_stamp_sync=t_stamp_sync,
            combi_guid=combi_guid,
        )

        repl_set.additional_properties = d
        return repl_set

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
