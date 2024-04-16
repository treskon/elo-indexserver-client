from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocHistoryC")


@_attrs_define
class DocHistoryC:
    """<p>Bit constants for members of DocHistory</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_comment (Union[Unset, int]): DB column: histcomment
            mb_t_stamp (Union[Unset, str]): DB column: doctstamp
            mb_version (Union[Unset, str]): DB column: histversion
            mb_delete_date (Union[Unset, str]): Member bit: The version is deleted at this date. The value is an ELO date
                format.
                The value is zero, if
                 DB column: deletedate
            mb_user (Union[Unset, str]): DB column: userid
            ln_guid (Union[Unset, int]): DB column: docguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: doctstampsync
            mb_status (Union[Unset, str]): DB column: docstatus
            mb_obj_id (Union[Unset, str]): DB column: objectid
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_t_stamp (Union[Unset, int]): DB column: doctstamp
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: doctstampsync
            mb_type (Union[Unset, str]): Member bit: The type of this DocHistory makes the difference between attachments
                and document versions.
                DB column: doctype
            ln_doc_md5 (Union[Unset, int]): DB column: docmd5
            mb_create_date (Union[Unset, str]): DB column: createdate
            mb_language (Union[Unset, str]): Member bit: Language of the document content.
                DB column: language
            mb_doc_id (Union[Unset, str]): DB column: documentid
            ln_language (Union[Unset, int]): Column length: Language of the document content.
                DB column: language
            mb_doc_md5 (Union[Unset, str]): DB column: docmd5
            mb_sig_id (Union[Unset, str]): DB column: docsignature
            mb_nb_of_valid_signatures (Union[Unset, str]): Member bit: Number of valid signatures.
                DB column: nbofvalidsignatures
            mb_guid (Union[Unset, str]): DB column: docguid
            ln_version (Union[Unset, int]): DB column: histversion
            mb_flags (Union[Unset, str]): DB column: docflags
            mb_comment (Union[Unset, str]): DB column: histcomment
    """

    ln_comment: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_version: Union[Unset, str] = UNSET
    mb_delete_date: Union[Unset, str] = UNSET
    mb_user: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_obj_id: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_type: Union[Unset, str] = UNSET
    ln_doc_md5: Union[Unset, int] = UNSET
    mb_create_date: Union[Unset, str] = UNSET
    mb_language: Union[Unset, str] = UNSET
    mb_doc_id: Union[Unset, str] = UNSET
    ln_language: Union[Unset, int] = UNSET
    mb_doc_md5: Union[Unset, str] = UNSET
    mb_sig_id: Union[Unset, str] = UNSET
    mb_nb_of_valid_signatures: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_version: Union[Unset, int] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_comment = self.ln_comment

        mb_t_stamp = self.mb_t_stamp

        mb_version = self.mb_version

        mb_delete_date = self.mb_delete_date

        mb_user = self.mb_user

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_status = self.mb_status

        mb_obj_id = self.mb_obj_id

        mb_all_members = self.mb_all_members

        ln_t_stamp = self.ln_t_stamp

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_type = self.mb_type

        ln_doc_md5 = self.ln_doc_md5

        mb_create_date = self.mb_create_date

        mb_language = self.mb_language

        mb_doc_id = self.mb_doc_id

        ln_language = self.ln_language

        mb_doc_md5 = self.mb_doc_md5

        mb_sig_id = self.mb_sig_id

        mb_nb_of_valid_signatures = self.mb_nb_of_valid_signatures

        mb_guid = self.mb_guid

        ln_version = self.ln_version

        mb_flags = self.mb_flags

        mb_comment = self.mb_comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_version is not UNSET:
            field_dict["mbVersion"] = mb_version
        if mb_delete_date is not UNSET:
            field_dict["mbDeleteDate"] = mb_delete_date
        if mb_user is not UNSET:
            field_dict["mbUser"] = mb_user
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if ln_doc_md5 is not UNSET:
            field_dict["lnDocMD5"] = ln_doc_md5
        if mb_create_date is not UNSET:
            field_dict["mbCreateDate"] = mb_create_date
        if mb_language is not UNSET:
            field_dict["mbLanguage"] = mb_language
        if mb_doc_id is not UNSET:
            field_dict["mbDocId"] = mb_doc_id
        if ln_language is not UNSET:
            field_dict["lnLanguage"] = ln_language
        if mb_doc_md5 is not UNSET:
            field_dict["mbDocMD5"] = mb_doc_md5
        if mb_sig_id is not UNSET:
            field_dict["mbSigId"] = mb_sig_id
        if mb_nb_of_valid_signatures is not UNSET:
            field_dict["mbNbOfValidSignatures"] = mb_nb_of_valid_signatures
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_version is not UNSET:
            field_dict["lnVersion"] = ln_version
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_comment = d.pop("lnComment", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_version = d.pop("mbVersion", UNSET)

        mb_delete_date = d.pop("mbDeleteDate", UNSET)

        mb_user = d.pop("mbUser", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_type = d.pop("mbType", UNSET)

        ln_doc_md5 = d.pop("lnDocMD5", UNSET)

        mb_create_date = d.pop("mbCreateDate", UNSET)

        mb_language = d.pop("mbLanguage", UNSET)

        mb_doc_id = d.pop("mbDocId", UNSET)

        ln_language = d.pop("lnLanguage", UNSET)

        mb_doc_md5 = d.pop("mbDocMD5", UNSET)

        mb_sig_id = d.pop("mbSigId", UNSET)

        mb_nb_of_valid_signatures = d.pop("mbNbOfValidSignatures", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_version = d.pop("lnVersion", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        doc_history_c = cls(
            ln_comment=ln_comment,
            mb_t_stamp=mb_t_stamp,
            mb_version=mb_version,
            mb_delete_date=mb_delete_date,
            mb_user=mb_user,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_status=mb_status,
            mb_obj_id=mb_obj_id,
            mb_all_members=mb_all_members,
            ln_t_stamp=ln_t_stamp,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_type=mb_type,
            ln_doc_md5=ln_doc_md5,
            mb_create_date=mb_create_date,
            mb_language=mb_language,
            mb_doc_id=mb_doc_id,
            ln_language=ln_language,
            mb_doc_md5=mb_doc_md5,
            mb_sig_id=mb_sig_id,
            mb_nb_of_valid_signatures=mb_nb_of_valid_signatures,
            mb_guid=mb_guid,
            ln_version=ln_version,
            mb_flags=mb_flags,
            mb_comment=mb_comment,
        )

        doc_history_c.additional_properties = d
        return doc_history_c

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
