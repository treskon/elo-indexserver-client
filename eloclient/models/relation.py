from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Relation")


@_attrs_define
class Relation:
    """Internal class.

    Attributes:
        parent_id (Union[Unset, int]): DB column: parentid
        obj_id (Union[Unset, int]): DB column: objectid
        ordinal (Union[Unset, int]): DB column: ordinal
        status (Union[Unset, int]): DB column: relstatus
        t_stamp (Union[Unset, str]): DB column: reltstamp
        guid (Union[Unset, str]): GUID
        delete_date_iso (Union[Unset, str]): The Relation is deleted at this date. ClientInfo determines the Timezone.
            <p>
             Is undefined if status==0.
             </p>
        main_relation (Union[Unset, bool]): This Relation represents the main relation of an object, if this value is
            <code>true</code>.
        t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
        obj_guid (Union[Unset, str]): GUID of the child object.
        parent_guid (Union[Unset, str]): GUID of the parent object.
    """

    parent_id: Union[Unset, int] = UNSET
    obj_id: Union[Unset, int] = UNSET
    ordinal: Union[Unset, int] = UNSET
    status: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    main_relation: Union[Unset, bool] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    parent_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_id = self.parent_id
        obj_id = self.obj_id
        ordinal = self.ordinal
        status = self.status
        t_stamp = self.t_stamp
        guid = self.guid
        delete_date_iso = self.delete_date_iso
        main_relation = self.main_relation
        t_stamp_sync = self.t_stamp_sync
        obj_guid = self.obj_guid
        parent_guid = self.parent_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if ordinal is not UNSET:
            field_dict["ordinal"] = ordinal
        if status is not UNSET:
            field_dict["status"] = status
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if guid is not UNSET:
            field_dict["guid"] = guid
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso
        if main_relation is not UNSET:
            field_dict["mainRelation"] = main_relation
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if parent_guid is not UNSET:
            field_dict["parentGuid"] = parent_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parent_id = d.pop("parentId", UNSET)

        obj_id = d.pop("objId", UNSET)

        ordinal = d.pop("ordinal", UNSET)

        status = d.pop("status", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        guid = d.pop("guid", UNSET)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        main_relation = d.pop("mainRelation", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        parent_guid = d.pop("parentGuid", UNSET)

        relation = cls(
            parent_id=parent_id,
            obj_id=obj_id,
            ordinal=ordinal,
            status=status,
            t_stamp=t_stamp,
            guid=guid,
            delete_date_iso=delete_date_iso,
            main_relation=main_relation,
            t_stamp_sync=t_stamp_sync,
            obj_guid=obj_guid,
            parent_guid=parent_guid,
        )

        relation.additional_properties = d
        return relation

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
