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
            doc_id (Union[Unset, int]): Document ID.
            computed_hash (Union[Unset, str]): MD5 hash computed by {@link IXServicePortIF#computeDocumentHash(ClientInfo,
                ComputeDocumentHashInfo)}.
            stored_hash (Union[Unset, str]): MD5 has stored in DB. This value can be empty if MD5 checking is disabled in DM
                configuration.
            equal_hash (Union[Unset, bool]): True, if {@link #storedHash} is equal to {@link #computedHash}.
            create_date (Union[Unset, datetime.datetime]): Document create date.
            update_date (Union[Unset, datetime.datetime]): Document update date.
            access_date (Union[Unset, datetime.datetime]): Document last access date.
    """

    doc_id: Union[Unset, int] = UNSET
    computed_hash: Union[Unset, str] = UNSET
    stored_hash: Union[Unset, str] = UNSET
    equal_hash: Union[Unset, bool] = UNSET
    create_date: Union[Unset, datetime.datetime] = UNSET
    update_date: Union[Unset, datetime.datetime] = UNSET
    access_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc_id = self.doc_id
        computed_hash = self.computed_hash
        stored_hash = self.stored_hash
        equal_hash = self.equal_hash
        create_date: Union[Unset, str] = UNSET
        if not isinstance(self.create_date, Unset):
            create_date = self.create_date.isoformat()

        update_date: Union[Unset, str] = UNSET
        if not isinstance(self.update_date, Unset):
            update_date = self.update_date.isoformat()

        access_date: Union[Unset, str] = UNSET
        if not isinstance(self.access_date, Unset):
            access_date = self.access_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if computed_hash is not UNSET:
            field_dict["computedHash"] = computed_hash
        if stored_hash is not UNSET:
            field_dict["storedHash"] = stored_hash
        if equal_hash is not UNSET:
            field_dict["equalHash"] = equal_hash
        if create_date is not UNSET:
            field_dict["createDate"] = create_date
        if update_date is not UNSET:
            field_dict["updateDate"] = update_date
        if access_date is not UNSET:
            field_dict["accessDate"] = access_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc_id = d.pop("docId", UNSET)

        computed_hash = d.pop("computedHash", UNSET)

        stored_hash = d.pop("storedHash", UNSET)

        equal_hash = d.pop("equalHash", UNSET)

        _create_date = d.pop("createDate", UNSET)
        create_date: Union[Unset, datetime.datetime]
        if isinstance(_create_date, Unset):
            create_date = UNSET
        else:
            create_date = isoparse(_create_date)

        _update_date = d.pop("updateDate", UNSET)
        update_date: Union[Unset, datetime.datetime]
        if isinstance(_update_date, Unset):
            update_date = UNSET
        else:
            update_date = isoparse(_update_date)

        _access_date = d.pop("accessDate", UNSET)
        access_date: Union[Unset, datetime.datetime]
        if isinstance(_access_date, Unset):
            access_date = UNSET
        else:
            access_date = isoparse(_access_date)

        compute_document_hash_result = cls(
            doc_id=doc_id,
            computed_hash=computed_hash,
            stored_hash=stored_hash,
            equal_hash=equal_hash,
            create_date=create_date,
            update_date=update_date,
            access_date=access_date,
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
