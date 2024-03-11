from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicDownload")


@_attrs_define
class PublicDownload:
    """This class describes the public download information.
    <p>
     Internal use.
     </p>

        Attributes:
            id (Union[Unset, str]): The download ID.
            remaining (Union[Unset, int]): The download count.
            expiration (Union[Unset, str]): The expired time.
            time_stamp (Union[Unset, str]): The time stamp.
            doc_id (Union[Unset, int]): The document ID.
            obj_id (Union[Unset, int]): The object ID.
            user_id (Union[Unset, int]): The user ID.
            url (Union[Unset, str]): The download URL
            file_name (Union[Unset, str]): The fileName in the download url. It is readonly.
            attachment_code (Union[Unset, str]): Indicates whether the download is inline or as attachment. this field is
                ignored in ELO 11.03 and ongoing versions.
    """

    id: Union[Unset, str] = UNSET
    remaining: Union[Unset, int] = UNSET
    expiration: Union[Unset, str] = UNSET
    time_stamp: Union[Unset, str] = UNSET
    doc_id: Union[Unset, int] = UNSET
    obj_id: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    url: Union[Unset, str] = UNSET
    file_name: Union[Unset, str] = UNSET
    attachment_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        remaining = self.remaining
        expiration = self.expiration
        time_stamp = self.time_stamp
        doc_id = self.doc_id
        obj_id = self.obj_id
        user_id = self.user_id
        url = self.url
        file_name = self.file_name
        attachment_code = self.attachment_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if remaining is not UNSET:
            field_dict["remaining"] = remaining
        if expiration is not UNSET:
            field_dict["expiration"] = expiration
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if url is not UNSET:
            field_dict["url"] = url
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if attachment_code is not UNSET:
            field_dict["attachmentCode"] = attachment_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        remaining = d.pop("remaining", UNSET)

        expiration = d.pop("expiration", UNSET)

        time_stamp = d.pop("timeStamp", UNSET)

        doc_id = d.pop("docId", UNSET)

        obj_id = d.pop("objId", UNSET)

        user_id = d.pop("userId", UNSET)

        url = d.pop("url", UNSET)

        file_name = d.pop("fileName", UNSET)

        attachment_code = d.pop("attachmentCode", UNSET)

        public_download = cls(
            id=id,
            remaining=remaining,
            expiration=expiration,
            time_stamp=time_stamp,
            doc_id=doc_id,
            obj_id=obj_id,
            user_id=user_id,
            url=url,
            file_name=file_name,
            attachment_code=attachment_code,
        )

        public_download.additional_properties = d
        return public_download

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
