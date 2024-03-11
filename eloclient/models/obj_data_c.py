from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjDataC")


@_attrs_define
class ObjDataC:
    """<p>
    Bit constants for members of Sord
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_id (Union[Unset, str]): Member bit: Serialisation version ID DB column: objid
            mb_guid (Union[Unset, str]): DB column: objguid
            ln_guid (Union[Unset, int]): DB column: objguid
            mb_parent_id (Union[Unset, str]): DB column: objparent
            mb_type (Union[Unset, str]): DB column: objtype
            mb_flags (Union[Unset, str]): DB column: objflags
            mb_name (Union[Unset, str]): DB column: objshort
            ln_name (Union[Unset, int]): DB column: objshort
            mb_s_reg (Union[Unset, str]): DB column: objsreg
            ln_s_reg (Union[Unset, int]): DB column: objsreg
            mb_i_date (Union[Unset, str]): DB column: objidate
            mb_x_date (Union[Unset, str]): DB column: objxdate
            mb_key (Union[Unset, str]): DB column: objkey
            mb_kind (Union[Unset, str]): DB column: objkind
            mb_path (Union[Unset, str]): DB column: objpath
            mb_info (Union[Unset, str]): DB column: objinfo
            mb_mask (Union[Unset, str]): DB column: objmask
            mb_doc (Union[Unset, str]): DB column: objdoc
            mb_sig (Union[Unset, str]): DB column: objakey1
            mb_att (Union[Unset, str]): DB column: objattach
            mb_owner_id (Union[Unset, str]): DB column: objuser
            mb_lock_id (Union[Unset, str]): DB column: objlock
            mb_status (Union[Unset, str]): DB column: objstatus
            mb_hist_count (Union[Unset, str]): DB column: objhistcount
            mb_internal_desc (Union[Unset, str]): DB column: objdesc
            ln_internal_desc (Union[Unset, int]): DB column: objdesc
            mb_child_count (Union[Unset, str]): DB column: objchildcount
            mb_del_date (Union[Unset, str]): DB column: objdeldate
            mb_sync_date_loc (Union[Unset, str]): DB column: objsyncdateloc
            mb_sync_date_rem (Union[Unset, str]): DB column: objsyncdaterem
            mb_vt_rep (Union[Unset, str]): DB column: objvtrep
            mb_acl (Union[Unset, str]): DB column: objacl
            ln_acl (Union[Unset, int]): DB column: objacl
            mb_t_stamp (Union[Unset, str]): DB column: objtstamp
            ln_t_stamp (Union[Unset, int]): DB column: objtstamp
            mb_s_name (Union[Unset, str]): DB column: objsdata_off
            ln_s_name (Union[Unset, int]): DB column: objsdata_off
            mb_s_desc (Union[Unset, str]): DB column: objsdesc_off
            ln_s_desc (Union[Unset, int]): DB column: objsdesc_off
            mb_delete_date (Union[Unset, str]): Member bit: The Sord is deleted at this date. ClientInfo determines the
                Timezone.
                DB column: deletedate
            mb_lock_id_sord (Union[Unset, str]): Member bit: This is the id of the user who has a lock on the object (not
                the document).
                DB column: objlock_off
            mb_lock_id_doc (Union[Unset, str]): Member bit: This is the id of the user who has a lock on the document (not
                the object).
                DB column: doclock
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: objtstampsync
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: objtstampsync
            mb_t_stamp_acl (Union[Unset, str]): Member bit: Timestamp of the last ACL change.
                DB column: objtstampacl
            ln_t_stamp_acl (Union[Unset, int]): Column length: Timestamp of the last ACL change.
                DB column: objtstampacl
            mb_t_stamp_acl_sync (Union[Unset, str]): Member bit: Timestamp of this object's ACLs last export by the
                replication.
                DB column: objtstampaclsync
            ln_t_stamp_acl_sync (Union[Unset, int]): Column length: Timestamp of this object's ACLs last export by the
                replication.
                DB column: objtstampaclsync
            mb_delete_user (Union[Unset, str]): Member bit: The Sord is deleted at this user.
                DB column: deleteuser
            mb_encryption_set (Union[Unset, str]): Member bit: The number of the encryptionSet (the value 0 means not
                encrypted).
                DB column: encryptionset
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_id: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_parent_id: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_s_reg: Union[Unset, str] = UNSET
    ln_s_reg: Union[Unset, int] = UNSET
    mb_i_date: Union[Unset, str] = UNSET
    mb_x_date: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    mb_kind: Union[Unset, str] = UNSET
    mb_path: Union[Unset, str] = UNSET
    mb_info: Union[Unset, str] = UNSET
    mb_mask: Union[Unset, str] = UNSET
    mb_doc: Union[Unset, str] = UNSET
    mb_sig: Union[Unset, str] = UNSET
    mb_att: Union[Unset, str] = UNSET
    mb_owner_id: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    mb_hist_count: Union[Unset, str] = UNSET
    mb_internal_desc: Union[Unset, str] = UNSET
    ln_internal_desc: Union[Unset, int] = UNSET
    mb_child_count: Union[Unset, str] = UNSET
    mb_del_date: Union[Unset, str] = UNSET
    mb_sync_date_loc: Union[Unset, str] = UNSET
    mb_sync_date_rem: Union[Unset, str] = UNSET
    mb_vt_rep: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_s_name: Union[Unset, str] = UNSET
    ln_s_name: Union[Unset, int] = UNSET
    mb_s_desc: Union[Unset, str] = UNSET
    ln_s_desc: Union[Unset, int] = UNSET
    mb_delete_date: Union[Unset, str] = UNSET
    mb_lock_id_sord: Union[Unset, str] = UNSET
    mb_lock_id_doc: Union[Unset, str] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_t_stamp_acl: Union[Unset, str] = UNSET
    ln_t_stamp_acl: Union[Unset, int] = UNSET
    mb_t_stamp_acl_sync: Union[Unset, str] = UNSET
    ln_t_stamp_acl_sync: Union[Unset, int] = UNSET
    mb_delete_user: Union[Unset, str] = UNSET
    mb_encryption_set: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_parent_id = self.mb_parent_id
        mb_type = self.mb_type
        mb_flags = self.mb_flags
        mb_name = self.mb_name
        ln_name = self.ln_name
        mb_s_reg = self.mb_s_reg
        ln_s_reg = self.ln_s_reg
        mb_i_date = self.mb_i_date
        mb_x_date = self.mb_x_date
        mb_key = self.mb_key
        mb_kind = self.mb_kind
        mb_path = self.mb_path
        mb_info = self.mb_info
        mb_mask = self.mb_mask
        mb_doc = self.mb_doc
        mb_sig = self.mb_sig
        mb_att = self.mb_att
        mb_owner_id = self.mb_owner_id
        mb_lock_id = self.mb_lock_id
        mb_status = self.mb_status
        mb_hist_count = self.mb_hist_count
        mb_internal_desc = self.mb_internal_desc
        ln_internal_desc = self.ln_internal_desc
        mb_child_count = self.mb_child_count
        mb_del_date = self.mb_del_date
        mb_sync_date_loc = self.mb_sync_date_loc
        mb_sync_date_rem = self.mb_sync_date_rem
        mb_vt_rep = self.mb_vt_rep
        mb_acl = self.mb_acl
        ln_acl = self.ln_acl
        mb_t_stamp = self.mb_t_stamp
        ln_t_stamp = self.ln_t_stamp
        mb_s_name = self.mb_s_name
        ln_s_name = self.ln_s_name
        mb_s_desc = self.mb_s_desc
        ln_s_desc = self.ln_s_desc
        mb_delete_date = self.mb_delete_date
        mb_lock_id_sord = self.mb_lock_id_sord
        mb_lock_id_doc = self.mb_lock_id_doc
        mb_t_stamp_sync = self.mb_t_stamp_sync
        ln_t_stamp_sync = self.ln_t_stamp_sync
        mb_t_stamp_acl = self.mb_t_stamp_acl
        ln_t_stamp_acl = self.ln_t_stamp_acl
        mb_t_stamp_acl_sync = self.mb_t_stamp_acl_sync
        ln_t_stamp_acl_sync = self.ln_t_stamp_acl_sync
        mb_delete_user = self.mb_delete_user
        mb_encryption_set = self.mb_encryption_set
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_parent_id is not UNSET:
            field_dict["mbParentId"] = mb_parent_id
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_s_reg is not UNSET:
            field_dict["mbSReg"] = mb_s_reg
        if ln_s_reg is not UNSET:
            field_dict["lnSReg"] = ln_s_reg
        if mb_i_date is not UNSET:
            field_dict["mbIDate"] = mb_i_date
        if mb_x_date is not UNSET:
            field_dict["mbXDate"] = mb_x_date
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if mb_kind is not UNSET:
            field_dict["mbKind"] = mb_kind
        if mb_path is not UNSET:
            field_dict["mbPath"] = mb_path
        if mb_info is not UNSET:
            field_dict["mbInfo"] = mb_info
        if mb_mask is not UNSET:
            field_dict["mbMask"] = mb_mask
        if mb_doc is not UNSET:
            field_dict["mbDoc"] = mb_doc
        if mb_sig is not UNSET:
            field_dict["mbSig"] = mb_sig
        if mb_att is not UNSET:
            field_dict["mbAtt"] = mb_att
        if mb_owner_id is not UNSET:
            field_dict["mbOwnerId"] = mb_owner_id
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if mb_hist_count is not UNSET:
            field_dict["mbHistCount"] = mb_hist_count
        if mb_internal_desc is not UNSET:
            field_dict["mbInternalDesc"] = mb_internal_desc
        if ln_internal_desc is not UNSET:
            field_dict["lnInternalDesc"] = ln_internal_desc
        if mb_child_count is not UNSET:
            field_dict["mbChildCount"] = mb_child_count
        if mb_del_date is not UNSET:
            field_dict["mbDelDate"] = mb_del_date
        if mb_sync_date_loc is not UNSET:
            field_dict["mbSyncDateLoc"] = mb_sync_date_loc
        if mb_sync_date_rem is not UNSET:
            field_dict["mbSyncDateRem"] = mb_sync_date_rem
        if mb_vt_rep is not UNSET:
            field_dict["mbVtRep"] = mb_vt_rep
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_s_name is not UNSET:
            field_dict["mbSName"] = mb_s_name
        if ln_s_name is not UNSET:
            field_dict["lnSName"] = ln_s_name
        if mb_s_desc is not UNSET:
            field_dict["mbSDesc"] = mb_s_desc
        if ln_s_desc is not UNSET:
            field_dict["lnSDesc"] = ln_s_desc
        if mb_delete_date is not UNSET:
            field_dict["mbDeleteDate"] = mb_delete_date
        if mb_lock_id_sord is not UNSET:
            field_dict["mbLockIdSord"] = mb_lock_id_sord
        if mb_lock_id_doc is not UNSET:
            field_dict["mbLockIdDoc"] = mb_lock_id_doc
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_t_stamp_acl is not UNSET:
            field_dict["mbTStampAcl"] = mb_t_stamp_acl
        if ln_t_stamp_acl is not UNSET:
            field_dict["lnTStampAcl"] = ln_t_stamp_acl
        if mb_t_stamp_acl_sync is not UNSET:
            field_dict["mbTStampAclSync"] = mb_t_stamp_acl_sync
        if ln_t_stamp_acl_sync is not UNSET:
            field_dict["lnTStampAclSync"] = ln_t_stamp_acl_sync
        if mb_delete_user is not UNSET:
            field_dict["mbDeleteUser"] = mb_delete_user
        if mb_encryption_set is not UNSET:
            field_dict["mbEncryptionSet"] = mb_encryption_set
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_parent_id = d.pop("mbParentId", UNSET)

        mb_type = d.pop("mbType", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_s_reg = d.pop("mbSReg", UNSET)

        ln_s_reg = d.pop("lnSReg", UNSET)

        mb_i_date = d.pop("mbIDate", UNSET)

        mb_x_date = d.pop("mbXDate", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        mb_kind = d.pop("mbKind", UNSET)

        mb_path = d.pop("mbPath", UNSET)

        mb_info = d.pop("mbInfo", UNSET)

        mb_mask = d.pop("mbMask", UNSET)

        mb_doc = d.pop("mbDoc", UNSET)

        mb_sig = d.pop("mbSig", UNSET)

        mb_att = d.pop("mbAtt", UNSET)

        mb_owner_id = d.pop("mbOwnerId", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        mb_hist_count = d.pop("mbHistCount", UNSET)

        mb_internal_desc = d.pop("mbInternalDesc", UNSET)

        ln_internal_desc = d.pop("lnInternalDesc", UNSET)

        mb_child_count = d.pop("mbChildCount", UNSET)

        mb_del_date = d.pop("mbDelDate", UNSET)

        mb_sync_date_loc = d.pop("mbSyncDateLoc", UNSET)

        mb_sync_date_rem = d.pop("mbSyncDateRem", UNSET)

        mb_vt_rep = d.pop("mbVtRep", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_s_name = d.pop("mbSName", UNSET)

        ln_s_name = d.pop("lnSName", UNSET)

        mb_s_desc = d.pop("mbSDesc", UNSET)

        ln_s_desc = d.pop("lnSDesc", UNSET)

        mb_delete_date = d.pop("mbDeleteDate", UNSET)

        mb_lock_id_sord = d.pop("mbLockIdSord", UNSET)

        mb_lock_id_doc = d.pop("mbLockIdDoc", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_t_stamp_acl = d.pop("mbTStampAcl", UNSET)

        ln_t_stamp_acl = d.pop("lnTStampAcl", UNSET)

        mb_t_stamp_acl_sync = d.pop("mbTStampAclSync", UNSET)

        ln_t_stamp_acl_sync = d.pop("lnTStampAclSync", UNSET)

        mb_delete_user = d.pop("mbDeleteUser", UNSET)

        mb_encryption_set = d.pop("mbEncryptionSet", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        obj_data_c = cls(
            mb_id=mb_id,
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_parent_id=mb_parent_id,
            mb_type=mb_type,
            mb_flags=mb_flags,
            mb_name=mb_name,
            ln_name=ln_name,
            mb_s_reg=mb_s_reg,
            ln_s_reg=ln_s_reg,
            mb_i_date=mb_i_date,
            mb_x_date=mb_x_date,
            mb_key=mb_key,
            mb_kind=mb_kind,
            mb_path=mb_path,
            mb_info=mb_info,
            mb_mask=mb_mask,
            mb_doc=mb_doc,
            mb_sig=mb_sig,
            mb_att=mb_att,
            mb_owner_id=mb_owner_id,
            mb_lock_id=mb_lock_id,
            mb_status=mb_status,
            mb_hist_count=mb_hist_count,
            mb_internal_desc=mb_internal_desc,
            ln_internal_desc=ln_internal_desc,
            mb_child_count=mb_child_count,
            mb_del_date=mb_del_date,
            mb_sync_date_loc=mb_sync_date_loc,
            mb_sync_date_rem=mb_sync_date_rem,
            mb_vt_rep=mb_vt_rep,
            mb_acl=mb_acl,
            ln_acl=ln_acl,
            mb_t_stamp=mb_t_stamp,
            ln_t_stamp=ln_t_stamp,
            mb_s_name=mb_s_name,
            ln_s_name=ln_s_name,
            mb_s_desc=mb_s_desc,
            ln_s_desc=ln_s_desc,
            mb_delete_date=mb_delete_date,
            mb_lock_id_sord=mb_lock_id_sord,
            mb_lock_id_doc=mb_lock_id_doc,
            mb_t_stamp_sync=mb_t_stamp_sync,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_t_stamp_acl=mb_t_stamp_acl,
            ln_t_stamp_acl=ln_t_stamp_acl,
            mb_t_stamp_acl_sync=mb_t_stamp_acl_sync,
            ln_t_stamp_acl_sync=ln_t_stamp_acl_sync,
            mb_delete_user=mb_delete_user,
            mb_encryption_set=mb_encryption_set,
            mb_all_members=mb_all_members,
        )

        obj_data_c.additional_properties = d
        return obj_data_c

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
