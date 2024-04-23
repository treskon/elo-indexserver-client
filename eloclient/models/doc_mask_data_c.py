from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskDataC")


@_attrs_define
class DocMaskDataC:
    """<p>Bit constants for members of DocMask</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_name_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link DocMask#name}.
                DB column: masknametrkey
            mb_encryption_set (Union[Unset, str]): Member bit: The number of the encryptionSet (the value 0 means not
                encrypted).
                DB column: encryptionset
            mb_t_stamp (Union[Unset, str]): DB column: masktstamp
            mb_barcode (Union[Unset, str]): DB column: maskbarcode
            mb_data_organisation (Union[Unset, str]): Member bit: This member specifies how the index values are stored in
                database.
                DB column: dataorg
            ln_raw_pos_info_3 (Union[Unset, int]): Column length: This field extends <code>RawPosInfo</code> for more
                docMask lines (EIX-739).
                DB column: maskposinfo3
            ln_raw_pos_info_2 (Union[Unset, int]): Column length: This field extends <code>RawPosInfo</code> for more
                docMask lines (EIX-739).
                DB column: maskposinfo2
            mb_raw_pos_info_3 (Union[Unset, str]): Member bit: This field extends <code>RawPosInfo</code> for more docMask
                lines (EIX-739).
                DB column: maskposinfo3
            mb_raw_pos_info_2 (Union[Unset, str]): Member bit: This field extends <code>RawPosInfo</code> for more docMask
                lines (EIX-739).
                DB column: maskposinfo2
            mb_d_key (Union[Unset, str]): DB column: maskdkey
            ln_lifetime (Union[Unset, int]): DB column: lifetime
            mb_internal_acl (Union[Unset, str]): Member bit: Internal acl.
                DB column: maskacl
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: masktstampsync
            mb_id (Union[Unset, str]): DB column: maskno
            mb_key (Union[Unset, str]): DB column: maskkey
            mb_d_kind (Union[Unset, str]): DB column: maskdkind
            ln_raw_mask_ids_for_child_entries (Union[Unset, int]): Column length: Child entries in the archive hierarchy
                should only use this keywording forms.
                If this element
                 DB column: maskidsforchildentries
            mb_d_path (Union[Unset, str]): DB column: maskdpath
            mb_guid (Union[Unset, str]): Member bit: GUID
                DB column: maskguid
            mb_raw_mask_ids_for_child_entries (Union[Unset, str]): Member bit: Child entries in the archive hierarchy should
                only use this keywording forms.
                If this element
                 DB column: maskidsforchildentries
            mb_flags (Union[Unset, str]): DB column: maskflags
            mb_d_acl (Union[Unset, str]): DB column: maskdacl
            ln_package_name (Union[Unset, int]): Column length: Package name of DocMask
                DB column: packagename
            ln_text_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link DocMask#text}.
                DB column: masktexttrkey
            mb_flow_id (Union[Unset, str]): DB column: maskflowid
            mb_package_name (Union[Unset, str]): Member bit: Package name of DocMask
                DB column: packagename
            mb_index (Union[Unset, str]): DB column: maskindex
            mb_name (Union[Unset, str]): DB column: maskname
            ln_text (Union[Unset, int]): DB column: masktext
            ln_guid (Union[Unset, int]): Column length: GUID
                DB column: maskguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: masktstampsync
            ln_d_acl (Union[Unset, int]): DB column: maskdacl
            ln_name_translation_key (Union[Unset, int]): Column length: Translation-keyword for {@link DocMask#name}.
                DB column: masknametrkey
            mb_status (Union[Unset, str]): Member bit: Deleted status.
                DB column: maskstatus
            ln_name (Union[Unset, int]): DB column: maskname
            ln_internal_acl (Union[Unset, int]): Column length: Internal acl.
                DB column: maskacl
            ln_raw_pos_info (Union[Unset, int]): DB column: maskposinfo
            mb_all_members (Union[Unset, str]): All valid member bits.
            ln_t_stamp (Union[Unset, int]): DB column: masktstamp
            mb_deletion_deadline (Union[Unset, str]): Member bit: Deletion deadline for new objects.
                DB column: deletiondeadline
            mb_sord_type (Union[Unset, str]): Member bit: Prepare this type for a new Sord object.
                DB column: sordType
            mb_lock_id (Union[Unset, str]): DB column: masklock
            ln_barcode (Union[Unset, int]): DB column: maskbarcode
            mb_raw_pos_info (Union[Unset, str]): DB column: maskposinfo
            mb_lifetime (Union[Unset, str]): DB column: lifetime
            mb_text (Union[Unset, str]): DB column: masktext
            ln_deletion_deadline (Union[Unset, int]): Column length: Deletion deadline for new objects.
                DB column: deletiondeadline
            mb_text_translation_key (Union[Unset, str]): Member bit: Translation-keyword for {@link DocMask#text}.
                DB column: masktexttrkey
            mb_flow_id_2 (Union[Unset, str]): Member bit: The ID of a workflow that is to be started if a new version of an
                associated document is
                DB column: maskflowid2
            ln_index (Union[Unset, int]): DB column: maskindex
    """

    mb_name_translation_key: Union[Unset, str] = UNSET
    mb_encryption_set: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_barcode: Union[Unset, str] = UNSET
    mb_data_organisation: Union[Unset, str] = UNSET
    ln_raw_pos_info_3: Union[Unset, int] = UNSET
    ln_raw_pos_info_2: Union[Unset, int] = UNSET
    mb_raw_pos_info_3: Union[Unset, str] = UNSET
    mb_raw_pos_info_2: Union[Unset, str] = UNSET
    mb_d_key: Union[Unset, str] = UNSET
    ln_lifetime: Union[Unset, int] = UNSET
    mb_internal_acl: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    mb_d_kind: Union[Unset, str] = UNSET
    ln_raw_mask_ids_for_child_entries: Union[Unset, int] = UNSET
    mb_d_path: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    mb_raw_mask_ids_for_child_entries: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_d_acl: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    ln_text_translation_key: Union[Unset, int] = UNSET
    mb_flow_id: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_index: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_text: Union[Unset, int] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_d_acl: Union[Unset, int] = UNSET
    ln_name_translation_key: Union[Unset, int] = UNSET
    mb_status: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    ln_internal_acl: Union[Unset, int] = UNSET
    ln_raw_pos_info: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_deletion_deadline: Union[Unset, str] = UNSET
    mb_sord_type: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    ln_barcode: Union[Unset, int] = UNSET
    mb_raw_pos_info: Union[Unset, str] = UNSET
    mb_lifetime: Union[Unset, str] = UNSET
    mb_text: Union[Unset, str] = UNSET
    ln_deletion_deadline: Union[Unset, int] = UNSET
    mb_text_translation_key: Union[Unset, str] = UNSET
    mb_flow_id_2: Union[Unset, str] = UNSET
    ln_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_name_translation_key = self.mb_name_translation_key

        mb_encryption_set = self.mb_encryption_set

        mb_t_stamp = self.mb_t_stamp

        mb_barcode = self.mb_barcode

        mb_data_organisation = self.mb_data_organisation

        ln_raw_pos_info_3 = self.ln_raw_pos_info_3

        ln_raw_pos_info_2 = self.ln_raw_pos_info_2

        mb_raw_pos_info_3 = self.mb_raw_pos_info_3

        mb_raw_pos_info_2 = self.mb_raw_pos_info_2

        mb_d_key = self.mb_d_key

        ln_lifetime = self.ln_lifetime

        mb_internal_acl = self.mb_internal_acl

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_id = self.mb_id

        mb_key = self.mb_key

        mb_d_kind = self.mb_d_kind

        ln_raw_mask_ids_for_child_entries = self.ln_raw_mask_ids_for_child_entries

        mb_d_path = self.mb_d_path

        mb_guid = self.mb_guid

        mb_raw_mask_ids_for_child_entries = self.mb_raw_mask_ids_for_child_entries

        mb_flags = self.mb_flags

        mb_d_acl = self.mb_d_acl

        ln_package_name = self.ln_package_name

        ln_text_translation_key = self.ln_text_translation_key

        mb_flow_id = self.mb_flow_id

        mb_package_name = self.mb_package_name

        mb_index = self.mb_index

        mb_name = self.mb_name

        ln_text = self.ln_text

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        ln_d_acl = self.ln_d_acl

        ln_name_translation_key = self.ln_name_translation_key

        mb_status = self.mb_status

        ln_name = self.ln_name

        ln_internal_acl = self.ln_internal_acl

        ln_raw_pos_info = self.ln_raw_pos_info

        mb_all_members = self.mb_all_members

        ln_t_stamp = self.ln_t_stamp

        mb_deletion_deadline = self.mb_deletion_deadline

        mb_sord_type = self.mb_sord_type

        mb_lock_id = self.mb_lock_id

        ln_barcode = self.ln_barcode

        mb_raw_pos_info = self.mb_raw_pos_info

        mb_lifetime = self.mb_lifetime

        mb_text = self.mb_text

        ln_deletion_deadline = self.ln_deletion_deadline

        mb_text_translation_key = self.mb_text_translation_key

        mb_flow_id_2 = self.mb_flow_id_2

        ln_index = self.ln_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_name_translation_key is not UNSET:
            field_dict["mbNameTranslationKey"] = mb_name_translation_key
        if mb_encryption_set is not UNSET:
            field_dict["mbEncryptionSet"] = mb_encryption_set
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_barcode is not UNSET:
            field_dict["mbBarcode"] = mb_barcode
        if mb_data_organisation is not UNSET:
            field_dict["mbDataOrganisation"] = mb_data_organisation
        if ln_raw_pos_info_3 is not UNSET:
            field_dict["lnRawPosInfo3"] = ln_raw_pos_info_3
        if ln_raw_pos_info_2 is not UNSET:
            field_dict["lnRawPosInfo2"] = ln_raw_pos_info_2
        if mb_raw_pos_info_3 is not UNSET:
            field_dict["mbRawPosInfo3"] = mb_raw_pos_info_3
        if mb_raw_pos_info_2 is not UNSET:
            field_dict["mbRawPosInfo2"] = mb_raw_pos_info_2
        if mb_d_key is not UNSET:
            field_dict["mbDKey"] = mb_d_key
        if ln_lifetime is not UNSET:
            field_dict["lnLifetime"] = ln_lifetime
        if mb_internal_acl is not UNSET:
            field_dict["mbInternalAcl"] = mb_internal_acl
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if mb_d_kind is not UNSET:
            field_dict["mbDKind"] = mb_d_kind
        if ln_raw_mask_ids_for_child_entries is not UNSET:
            field_dict["lnRawMaskIdsForChildEntries"] = ln_raw_mask_ids_for_child_entries
        if mb_d_path is not UNSET:
            field_dict["mbDPath"] = mb_d_path
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if mb_raw_mask_ids_for_child_entries is not UNSET:
            field_dict["mbRawMaskIdsForChildEntries"] = mb_raw_mask_ids_for_child_entries
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_d_acl is not UNSET:
            field_dict["mbDAcl"] = mb_d_acl
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name
        if ln_text_translation_key is not UNSET:
            field_dict["lnTextTranslationKey"] = ln_text_translation_key
        if mb_flow_id is not UNSET:
            field_dict["mbFlowId"] = mb_flow_id
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_index is not UNSET:
            field_dict["mbIndex"] = mb_index
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_text is not UNSET:
            field_dict["lnText"] = ln_text
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_d_acl is not UNSET:
            field_dict["lnDAcl"] = ln_d_acl
        if ln_name_translation_key is not UNSET:
            field_dict["lnNameTranslationKey"] = ln_name_translation_key
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if ln_internal_acl is not UNSET:
            field_dict["lnInternalAcl"] = ln_internal_acl
        if ln_raw_pos_info is not UNSET:
            field_dict["lnRawPosInfo"] = ln_raw_pos_info
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_deletion_deadline is not UNSET:
            field_dict["mbDeletionDeadline"] = mb_deletion_deadline
        if mb_sord_type is not UNSET:
            field_dict["mbSordType"] = mb_sord_type
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if ln_barcode is not UNSET:
            field_dict["lnBarcode"] = ln_barcode
        if mb_raw_pos_info is not UNSET:
            field_dict["mbRawPosInfo"] = mb_raw_pos_info
        if mb_lifetime is not UNSET:
            field_dict["mbLifetime"] = mb_lifetime
        if mb_text is not UNSET:
            field_dict["mbText"] = mb_text
        if ln_deletion_deadline is not UNSET:
            field_dict["lnDeletionDeadline"] = ln_deletion_deadline
        if mb_text_translation_key is not UNSET:
            field_dict["mbTextTranslationKey"] = mb_text_translation_key
        if mb_flow_id_2 is not UNSET:
            field_dict["mbFlowId2"] = mb_flow_id_2
        if ln_index is not UNSET:
            field_dict["lnIndex"] = ln_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_name_translation_key = d.pop("mbNameTranslationKey", UNSET)

        mb_encryption_set = d.pop("mbEncryptionSet", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_barcode = d.pop("mbBarcode", UNSET)

        mb_data_organisation = d.pop("mbDataOrganisation", UNSET)

        ln_raw_pos_info_3 = d.pop("lnRawPosInfo3", UNSET)

        ln_raw_pos_info_2 = d.pop("lnRawPosInfo2", UNSET)

        mb_raw_pos_info_3 = d.pop("mbRawPosInfo3", UNSET)

        mb_raw_pos_info_2 = d.pop("mbRawPosInfo2", UNSET)

        mb_d_key = d.pop("mbDKey", UNSET)

        ln_lifetime = d.pop("lnLifetime", UNSET)

        mb_internal_acl = d.pop("mbInternalAcl", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        mb_d_kind = d.pop("mbDKind", UNSET)

        ln_raw_mask_ids_for_child_entries = d.pop("lnRawMaskIdsForChildEntries", UNSET)

        mb_d_path = d.pop("mbDPath", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        mb_raw_mask_ids_for_child_entries = d.pop("mbRawMaskIdsForChildEntries", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_d_acl = d.pop("mbDAcl", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        ln_text_translation_key = d.pop("lnTextTranslationKey", UNSET)

        mb_flow_id = d.pop("mbFlowId", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_index = d.pop("mbIndex", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_text = d.pop("lnText", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_d_acl = d.pop("lnDAcl", UNSET)

        ln_name_translation_key = d.pop("lnNameTranslationKey", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        ln_name = d.pop("lnName", UNSET)

        ln_internal_acl = d.pop("lnInternalAcl", UNSET)

        ln_raw_pos_info = d.pop("lnRawPosInfo", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_deletion_deadline = d.pop("mbDeletionDeadline", UNSET)

        mb_sord_type = d.pop("mbSordType", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        ln_barcode = d.pop("lnBarcode", UNSET)

        mb_raw_pos_info = d.pop("mbRawPosInfo", UNSET)

        mb_lifetime = d.pop("mbLifetime", UNSET)

        mb_text = d.pop("mbText", UNSET)

        ln_deletion_deadline = d.pop("lnDeletionDeadline", UNSET)

        mb_text_translation_key = d.pop("mbTextTranslationKey", UNSET)

        mb_flow_id_2 = d.pop("mbFlowId2", UNSET)

        ln_index = d.pop("lnIndex", UNSET)

        doc_mask_data_c = cls(
            mb_name_translation_key=mb_name_translation_key,
            mb_encryption_set=mb_encryption_set,
            mb_t_stamp=mb_t_stamp,
            mb_barcode=mb_barcode,
            mb_data_organisation=mb_data_organisation,
            ln_raw_pos_info_3=ln_raw_pos_info_3,
            ln_raw_pos_info_2=ln_raw_pos_info_2,
            mb_raw_pos_info_3=mb_raw_pos_info_3,
            mb_raw_pos_info_2=mb_raw_pos_info_2,
            mb_d_key=mb_d_key,
            ln_lifetime=ln_lifetime,
            mb_internal_acl=mb_internal_acl,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_id=mb_id,
            mb_key=mb_key,
            mb_d_kind=mb_d_kind,
            ln_raw_mask_ids_for_child_entries=ln_raw_mask_ids_for_child_entries,
            mb_d_path=mb_d_path,
            mb_guid=mb_guid,
            mb_raw_mask_ids_for_child_entries=mb_raw_mask_ids_for_child_entries,
            mb_flags=mb_flags,
            mb_d_acl=mb_d_acl,
            ln_package_name=ln_package_name,
            ln_text_translation_key=ln_text_translation_key,
            mb_flow_id=mb_flow_id,
            mb_package_name=mb_package_name,
            mb_index=mb_index,
            mb_name=mb_name,
            ln_text=ln_text,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_d_acl=ln_d_acl,
            ln_name_translation_key=ln_name_translation_key,
            mb_status=mb_status,
            ln_name=ln_name,
            ln_internal_acl=ln_internal_acl,
            ln_raw_pos_info=ln_raw_pos_info,
            mb_all_members=mb_all_members,
            ln_t_stamp=ln_t_stamp,
            mb_deletion_deadline=mb_deletion_deadline,
            mb_sord_type=mb_sord_type,
            mb_lock_id=mb_lock_id,
            ln_barcode=ln_barcode,
            mb_raw_pos_info=mb_raw_pos_info,
            mb_lifetime=mb_lifetime,
            mb_text=mb_text,
            ln_deletion_deadline=ln_deletion_deadline,
            mb_text_translation_key=mb_text_translation_key,
            mb_flow_id_2=mb_flow_id_2,
            ln_index=ln_index,
        )

        doc_mask_data_c.additional_properties = d
        return doc_mask_data_c

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
