from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocHistoryC")


@_attrs_define
class DocHistoryC:
    """<p>
    Bit constants for members of DocHistory
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_obj_id (Union[Unset, str]): DB column: objectid
            mb_doc_id (Union[Unset, str]): DB column: documentid
            mb_user (Union[Unset, str]): DB column: userid
            mb_create_date (Union[Unset, str]): DB column: createdate
            mb_comment (Union[Unset, str]): DB column: histcomment
            ln_comment (Union[Unset, int]): DB column: histcomment
            mb_version (Union[Unset, str]): DB column: histversion
            ln_version (Union[Unset, int]): DB column: histversion
            mb_doc_md5 (Union[Unset, str]): DB column: docmd5
            ln_doc_md5 (Union[Unset, int]): DB column: docmd5
            mb_guid (Union[Unset, str]): DB column: docguid
            ln_guid (Union[Unset, int]): DB column: docguid
            mb_t_stamp (Union[Unset, str]): DB column: doctstamp
            ln_t_stamp (Union[Unset, int]): DB column: doctstamp
            mb_sig_id (Union[Unset, str]): DB column: docsignature
            mb_status (Union[Unset, str]): DB column: docstatus
            mb_flags (Union[Unset, str]): DB column: docflags
            mb_delete_date (Union[Unset, str]): Member bit: The version is deleted at this date. The value is an ELO date
                format.
                The DB column: deletedate
            mb_nb_of_valid_signatures (Union[Unset, str]): Member bit: Number of valid signatures.
                DB column: nbofvalidsignatures
            mb_type (Union[Unset, str]): Member bit: The type of this DocHistory makes the difference between attachments
                and DB column: doctype
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: doctstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: doctstampsync
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_obj_id: Union[Unset, str] = UNSET
    mb_doc_id: Union[Unset, str] = UNSET
    mb_user: Union[Unset, str] = UNSET
    mb_create_date: Union[Unset, str] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    ln_comment: Union[Unset, int] = UNSET
    mb_version: Union[Unset, str] = UNSET
    ln_version: Union[Unset, int] = UNSET
    mb_doc_md5: Union[Unset, str] = UNSET
    ln_doc_md5: Union[Unset, int] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_sig_id: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_delete_date: Union[Unset, str] = UNSET
    mb_nb_of_valid_signatures: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_obj_id = self.mb_obj_id
        mb_doc_id = self.mb_doc_id
        mb_user = self.mb_user
        mb_create_date = self.mb_create_date
        mb_comment = self.mb_comment
        ln_comment = self.ln_comment
        mb_version = self.mb_version
        ln_version = self.ln_version
        mb_doc_md5 = self.mb_doc_md5
        ln_doc_md5 = self.ln_doc_md5
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_sig_id = self.mb_sig_id
        mb_status = self.mb_status
        mb_flags = self.mb_flags
        mb_delete_date = self.mb_delete_date
        mb_nb_of_valid_signatures = self.mb_nb_of_valid_signatures
        mb_type = self.mb_type
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_obj_id is not UNSET:
            field_dict["mbObjId"] = mb_obj_id
        if mb_doc_id is not UNSET:
            field_dict["mbDocId"] = mb_doc_id
        if mb_user is not UNSET:
            field_dict["mbUser"] = mb_user
        if mb_create_date is not UNSET:
            field_dict["mbCreateDate"] = mb_create_date
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment
        if ln_comment is not UNSET:
            field_dict["lnComment"] = ln_comment
        if mb_version is not UNSET:
            field_dict["mbVersion"] = mb_version
        if ln_version is not UNSET:
            field_dict["lnVersion"] = ln_version
        if mb_doc_md5 is not UNSET:
            field_dict["mbDocMD5"] = mb_doc_md5
        if ln_doc_md5 is not UNSET:
            field_dict["lnDocMD5"] = ln_doc_md5
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_sig_id is not UNSET:
            field_dict["mbSigId"] = mb_sig_id
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_delete_date is not UNSET:
            field_dict["mbDeleteDate"] = mb_delete_date
        if mb_nb_of_valid_signatures is not UNSET:
            field_dict["mbNbOfValidSignatures"] = mb_nb_of_valid_signatures
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_obj_id = d.pop("mbObjId", UNSET)

        mb_doc_id = d.pop("mbDocId", UNSET)

        mb_user = d.pop("mbUser", UNSET)

        mb_create_date = d.pop("mbCreateDate", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        ln_comment = d.pop("lnComment", UNSET)

        mb_version = d.pop("mbVersion", UNSET)

        ln_version = d.pop("lnVersion", UNSET)

        mb_doc_md5 = d.pop("mbDocMD5", UNSET)

        ln_doc_md5 = d.pop("lnDocMD5", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_sig_id = d.pop("mbSigId", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_delete_date = d.pop("mbDeleteDate", UNSET)

        mb_nb_of_valid_signatures = d.pop("mbNbOfValidSignatures", UNSET)

        mb_type = d.pop("mbType", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        doc_history_c = cls(
            mb_obj_id=mb_obj_id,
            mb_doc_id=mb_doc_id,
            mb_user=mb_user,
            mb_create_date=mb_create_date,
            mb_comment=mb_comment,
            ln_comment=ln_comment,
            mb_version=mb_version,
            ln_version=ln_version,
            mb_doc_md5=mb_doc_md5,
            ln_doc_md5=ln_doc_md5,
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_sig_id=mb_sig_id,
            mb_status=mb_status,
            mb_flags=mb_flags,
            mb_delete_date=mb_delete_date,
            mb_nb_of_valid_signatures=mb_nb_of_valid_signatures,
            mb_type=mb_type,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_all_members=mb_all_members,
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
