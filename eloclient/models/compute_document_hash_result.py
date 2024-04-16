import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComputeDocumentHashResult")


@_attrs_define
class ComputeDocumentHashResult:
    """This class provides the result data computed by
    {@link IXServicePortIF#computeDocumentHash(ClientInfo, ComputeDocumentHashInfo)}.

        Attributes:
            computed_hash (Union[Unset, str]): MD5 hash computed by
                {@link IXServicePortIF#computeDocumentHash(ClientInfo, ComputeDocumentHashInfo)}.
            update_date (Union[Unset, datetime.datetime]): Document update date.
            stored_hash (Union[Unset, str]): MD5 has stored in DB. This value can be empty if MD5 checking is disabled in DM
                configuration.
            access_date (Union[Unset, datetime.datetime]): Document last access date.
            equal_hash (Union[Unset, bool]): True, if {@link #storedHash} is equal to {@link #computedHash}.
            doc_id (Union[Unset, int]): Document ID.
            create_date (Union[Unset, datetime.datetime]): Document create date.
    """

    computed_hash: Union[Unset, str] = UNSET
    update_date: Union[Unset, datetime.datetime] = UNSET
    stored_hash: Union[Unset, str] = UNSET
    access_date: Union[Unset, datetime.datetime] = UNSET
    equal_hash: Union[Unset, bool] = UNSET
    doc_id: Union[Unset, int] = UNSET
    create_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        computed_hash = self.computed_hash

        update_date: Union[Unset, str] = UNSET
        if not isinstance(self.update_date, Unset):
            update_date = self.update_date.isoformat()

        stored_hash = self.stored_hash

        access_date: Union[Unset, str] = UNSET
        if not isinstance(self.access_date, Unset):
            access_date = self.access_date.isoformat()

        equal_hash = self.equal_hash

        doc_id = self.doc_id

        create_date: Union[Unset, str] = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if computed_hash is not UNSET:
            field_dict["computedHash"] = computed_hash
        if update_date is not UNSET:
            field_dict["updateDate"] = update_date
        if stored_hash is not UNSET:
            field_dict["storedHash"] = stored_hash
        if access_date is not UNSET:
            field_dict["accessDate"] = access_date
        if equal_hash is not UNSET:
            field_dict["equalHash"] = equal_hash
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if create_date is not UNSET:
            field_dict["createDate"] = create_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        computed_hash = d.pop("computedHash", UNSET)

        _update_date = d.pop("updateDate", UNSET)
        update_date: Union[Unset, datetime.datetime]
        if isinstance(_update_date, Unset):
            update_date = UNSET
        else:
            update_date = isoparse(_update_date)

        stored_hash = d.pop("storedHash", UNSET)

        _access_date = d.pop("accessDate", UNSET)
        access_date: Union[Unset, datetime.datetime]
        if isinstance(_access_date, Unset):
            access_date = UNSET
        else:
            access_date = isoparse(_access_date)

        equal_hash = d.pop("equalHash", UNSET)

        doc_id = d.pop("docId", UNSET)

        _create_date = d.pop("createDate", UNSET)
        create_date: Union[Unset, datetime.datetime]
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        compute_document_hash_result = cls(
            computed_hash=computed_hash,
            update_date=update_date,
            stored_hash=stored_hash,
            access_date=access_date,
            equal_hash=equal_hash,
            doc_id=doc_id,
            create_date=create_date,
        )

        compute_document_hash_result.additional_properties = d
        return compute_document_hash_result

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
