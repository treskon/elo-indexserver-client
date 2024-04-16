from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublicDownloadDataC")


@_attrs_define
class PublicDownloadDataC:
    """<p>Bit constants for members of PublicDownload</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: guid
            mb_remaining (Union[Unset, str]): DB column: remaining
            mb_user_id (Union[Unset, str]): DB column: userid
            mb_doc_id (Union[Unset, str]): DB column: docid
            ln_file_name (Union[Unset, int]): Column length: The fileName in the download url. It is readonly.
                DB column: fname
            mb_file_name (Union[Unset, str]): Member bit: The fileName in the download url. It is readonly.
                DB column: fname
            ln_expiration (Union[Unset, int]): DB column: expiration
            ln_id (Union[Unset, int]): DB column: guid
            mb_expiration (Union[Unset, str]): DB column: expiration
            mb_time_stamp (Union[Unset, str]): DB column: tstamp
            mb_obj_id (Union[Unset, str]): DB column: objid
            mb_attachment_code (Union[Unset, str]): Member bit: Indicates whether the download is inline or as attachment.
                this field is ignored in ELO 11.
                03
                 DB column: acode
            ln_time_stamp (Union[Unset, int]): DB column: tstamp
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_attachment_code (Union[Unset, int]): Column length: Indicates whether the download is inline or as
                attachment. this field is ignored in ELO 11.
                03
                 DB column: acode
    """

    mb_id: Union[Unset, str] = UNSET
    mb_remaining: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_doc_id: Union[Unset, str] = UNSET
    ln_file_name: Union[Unset, int] = UNSET
    mb_file_name: Union[Unset, str] = UNSET
    ln_expiration: Union[Unset, int] = UNSET
    ln_id: Union[Unset, int] = UNSET
    mb_expiration: Union[Unset, str] = UNSET
    mb_time_stamp: Union[Unset, str] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_attachment_code: Union[Unset, str] = UNSET
    ln_time_stamp: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_attachment_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id

        mb_remaining = self.mb_remaining

        mb_user_id = self.mb_user_id

        mb_doc_id = self.mb_doc_id

        ln_file_name = self.ln_file_name

        mb_file_name = self.mb_file_name

        ln_expiration = self.ln_expiration

        ln_id = self.ln_id

        mb_expiration = self.mb_expiration

        mb_time_stamp = self.mb_time_stamp

        mb_obj_id = self.mb_obj_id

        mb_attachment_code = self.mb_attachment_code

        ln_time_stamp = self.ln_time_stamp

        mb_all_members = self.mb_all_members

        ln_attachment_code = self.ln_attachment_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_remaining is not UNSET:
            field_dict["mbRemaining"] = mb_remaining
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_doc_id is not UNSET:
            field_dict["mbDocId"] = mb_doc_id
        if ln_file_name is not UNSET:
            field_dict["lnFileName"] = ln_file_name
        if mb_file_name is not UNSET:
            field_dict["mbFileName"] = mb_file_name
        if ln_expiration is not UNSET:
            field_dict["lnExpiration"] = ln_expiration
        if ln_id is not UNSET:
            field_dict["lnId"] = ln_id
        if mb_expiration is not UNSET:
            field_dict["mbExpiration"] = mb_expiration
        if mb_time_stamp is not UNSET:
            field_dict["mbTimeStamp"] = mb_time_stamp
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_attachment_code is not UNSET:
            field_dict["mbAttachmentCode"] = mb_attachment_code
        if ln_time_stamp is not UNSET:
            field_dict["lnTimeStamp"] = ln_time_stamp
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_attachment_code is not UNSET:
            field_dict["lnAttachmentCode"] = ln_attachment_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_remaining = d.pop("mbRemaining", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_doc_id = d.pop("mbDocId", UNSET)

        ln_file_name = d.pop("lnFileName", UNSET)

        mb_file_name = d.pop("mbFileName", UNSET)

        ln_expiration = d.pop("lnExpiration", UNSET)

        ln_id = d.pop("lnId", UNSET)

        mb_expiration = d.pop("mbExpiration", UNSET)

        mb_time_stamp = d.pop("mbTimeStamp", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_attachment_code = d.pop("mbAttachmentCode", UNSET)

        ln_time_stamp = d.pop("lnTimeStamp", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_attachment_code = d.pop("lnAttachmentCode", UNSET)

        public_download_data_c = cls(
            mb_id=mb_id,
            mb_remaining=mb_remaining,
            mb_user_id=mb_user_id,
            mb_doc_id=mb_doc_id,
            ln_file_name=ln_file_name,
            mb_file_name=mb_file_name,
            ln_expiration=ln_expiration,
            ln_id=ln_id,
            mb_expiration=mb_expiration,
            mb_time_stamp=mb_time_stamp,
            mb_obj_id=mb_obj_id,
            mb_attachment_code=mb_attachment_code,
            ln_time_stamp=ln_time_stamp,
            mb_all_members=mb_all_members,
            ln_attachment_code=ln_attachment_code,
        )

        public_download_data_c.additional_properties = d
        return public_download_data_c

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
