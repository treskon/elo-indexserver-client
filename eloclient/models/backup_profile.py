from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupProfile")


@_attrs_define
class BackupProfile:
    """This class represents settings of a ELOdm backup profile.

    Attributes:
        name (Union[Unset, str]): Backup profile name
        path_id (Union[Unset, int]): Storage path id
        slot (Union[Unset, int]): Backup slot
        write_keywording (Union[Unset, bool]): Store keywording too
        sql_doc_select (Union[Unset, str]): Optional SQL command to select the documents to be stored.
        nb_of_docs_per_loop (Union[Unset, int]): Maximum number of documents per backup loop.
        retention (Union[Unset, int]): Reserved
    """

    name: Union[Unset, str] = UNSET
    path_id: Union[Unset, int] = UNSET
    slot: Union[Unset, int] = UNSET
    write_keywording: Union[Unset, bool] = UNSET
    sql_doc_select: Union[Unset, str] = UNSET
    nb_of_docs_per_loop: Union[Unset, int] = UNSET
    retention: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        path_id = self.path_id
        slot = self.slot
        write_keywording = self.write_keywording
        sql_doc_select = self.sql_doc_select
        nb_of_docs_per_loop = self.nb_of_docs_per_loop
        retention = self.retention

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if path_id is not UNSET:
            field_dict["pathId"] = path_id
        if slot is not UNSET:
            field_dict["slot"] = slot
        if write_keywording is not UNSET:
            field_dict["writeKeywording"] = write_keywording
        if sql_doc_select is not UNSET:
            field_dict["sqlDocSelect"] = sql_doc_select
        if nb_of_docs_per_loop is not UNSET:
            field_dict["nbOfDocsPerLoop"] = nb_of_docs_per_loop
        if retention is not UNSET:
            field_dict["retention"] = retention

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        path_id = d.pop("pathId", UNSET)

        slot = d.pop("slot", UNSET)

        write_keywording = d.pop("writeKeywording", UNSET)

        sql_doc_select = d.pop("sqlDocSelect", UNSET)

        nb_of_docs_per_loop = d.pop("nbOfDocsPerLoop", UNSET)

        retention = d.pop("retention", UNSET)

        backup_profile = cls(
            name=name,
            path_id=path_id,
            slot=slot,
            write_keywording=write_keywording,
            sql_doc_select=sql_doc_select,
            nb_of_docs_per_loop=nb_of_docs_per_loop,
            retention=retention,
        )

        backup_profile.additional_properties = d
        return backup_profile

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
