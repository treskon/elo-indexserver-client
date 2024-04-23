from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ObjDataC")


@_attrs_define
class ObjDataC:
    """<p>Bit constants for members of Sord</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_encryption_set (Union[Unset, str]): Member bit: The number of the encryptionSet (the value 0 means not
                encrypted).
                DB column: encryptionset
            mb_t_stamp (Union[Unset, str]): DB column: objtstamp
            mb_t_stamp_acl_sync (Union[Unset, str]): Member bit: Timestamp of this object's ACLs last export by the
                replication.
                DB column: objtstampaclsync
            mb_x_date (Union[Unset, str]): DB column: objxdate
            ln_acl (Union[Unset, int]): DB column: objacl
            mb_space_guid (Union[Unset, str]): Member bit: If the sord belongs to a workspace, this value contains the GUID
                of that workspace.
                DB column: spaceguid
            mb_acl (Union[Unset, str]): DB column: objacl
            ln_t_stamp_sync (Union[Unset, int]): Column length: Timestamp of this object's last export by the replication.
                DB column: objtstampsync
            mb_sync_date_loc (Union[Unset, str]): DB column: objsyncdateloc
            mb_id (Union[Unset, str]): Member bit: Serialisation version ID
                DB column: objid
            mb_hist_count (Union[Unset, str]): DB column: objhistcount
            mb_delete_user (Union[Unset, str]): Member bit: The Sord is deleted at this user.
                DB column: deleteuser
            mb_t_stamp_local (Union[Unset, str]): Member bit: Timestamp that indicates the next iSearch Index run The format
                is JJJJ.MM.DD.hh.mm.
                ss
                 DB column: objtstamplocal
            mb_key (Union[Unset, str]): DB column: objkey
            mb_mask (Union[Unset, str]): DB column: objmask
            ln_s_name (Union[Unset, int]): DB column: objsdata_off
            mb_internal_desc (Union[Unset, str]): DB column: objdesc
            mb_guid (Union[Unset, str]): DB column: objguid
            ln_t_stamp_acl_sync (Union[Unset, int]): Column length: Timestamp of this object's ACLs last export by the
                replication.
                DB column: objtstampaclsync
            mb_flags (Union[Unset, str]): DB column: objflags
            ln_package_name (Union[Unset, int]): Column length: Package name of sord
                DB column: packagename
            mb_kind (Union[Unset, str]): DB column: objkind
            ln_s_reg (Union[Unset, int]): DB column: objsreg
            mb_package_name (Union[Unset, str]): Member bit: Package name of sord
                DB column: packagename
            mb_i_date (Union[Unset, str]): DB column: objidate
            mb_t_stamp_acl (Union[Unset, str]): Member bit: Timestamp of the last ACL change. The format is
                JJJJ.MM.DD.hh.mm.
                ss
                 DB column: objtstampacl
            mb_parent_id (Union[Unset, str]): DB column: objparent
            mb_region_id (Union[Unset, str]): Member bit: This is a RESERVED field for future use. Do not use.
                <br>
                 DB column: regionid
            mb_delete_date (Union[Unset, str]): Member bit: The Sord is deleted at this date. ClientInfo determines the
                Timezone.
                DB column: deletedate
            ln_t_stamp_local (Union[Unset, int]): Column length: Timestamp that indicates the next iSearch Index run The
                format is JJJJ.MM.DD.hh.mm.
                ss
                 DB column: objtstamplocal
            mb_name (Union[Unset, str]): DB column: objshort
            ln_s_desc (Union[Unset, int]): DB column: objsdesc_off
            ln_internal_desc (Union[Unset, int]): DB column: objdesc
            mb_doc (Union[Unset, str]): DB column: objdoc
            ln_guid (Union[Unset, int]): DB column: objguid
            mb_t_stamp_sync (Union[Unset, str]): Member bit: Timestamp of this object's last export by the replication.
                DB column: objtstampsync
            mb_path (Union[Unset, str]): DB column: objpath
            mb_sig (Union[Unset, str]): DB column: objakey1
            mb_status (Union[Unset, str]): DB column: objstatus
            ln_name (Union[Unset, int]): DB column: objshort
            ln_space_guid (Union[Unset, int]): Column length: If the sord belongs to a workspace, this value contains the
                GUID of that workspace.
                DB column: spaceguid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_s_reg (Union[Unset, str]): DB column: objsreg
            ln_t_stamp (Union[Unset, int]): DB column: objtstamp
            mb_vt_rep (Union[Unset, str]): DB column: objvtrep
            mb_lock_id_doc (Union[Unset, str]): Member bit: This is the id of the user who has a lock on the document (not
                the object).
                The object is
                 DB column: doclock
            mb_att (Union[Unset, str]): DB column: objattach
            mb_type (Union[Unset, str]): DB column: objtype
            mb_lock_id (Union[Unset, str]): DB column: objlock
            mb_owner_id (Union[Unset, str]): DB column: objuser
            mb_info (Union[Unset, str]): DB column: objinfo
            mb_del_date (Union[Unset, str]): DB column: objdeldate
            mb_s_name (Union[Unset, str]): DB column: objsdata_off
            mb_child_count (Union[Unset, str]): DB column: objchildcount
            ln_t_stamp_acl (Union[Unset, int]): Column length: Timestamp of the last ACL change. The format is
                JJJJ.MM.DD.hh.mm.
                ss
                 DB column: objtstampacl
            mb_lock_id_sord (Union[Unset, str]): Member bit: This is the id of the user who has a lock on the object (not
                the document).
                The object is
                 DB column: objlock_off
            mb_s_desc (Union[Unset, str]): DB column: objsdesc_off
            mb_sync_date_rem (Union[Unset, str]): DB column: objsyncdaterem
    """

    mb_encryption_set: Union[Unset, str] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_t_stamp_acl_sync: Union[Unset, str] = UNSET
    mb_x_date: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_space_guid: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    ln_t_stamp_sync: Union[Unset, int] = UNSET
    mb_sync_date_loc: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_hist_count: Union[Unset, str] = UNSET
    mb_delete_user: Union[Unset, str] = UNSET
    mb_t_stamp_local: Union[Unset, str] = UNSET
    mb_key: Union[Unset, str] = UNSET
    mb_mask: Union[Unset, str] = UNSET
    ln_s_name: Union[Unset, int] = UNSET
    mb_internal_desc: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp_acl_sync: Union[Unset, int] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    ln_package_name: Union[Unset, int] = UNSET
    mb_kind: Union[Unset, str] = UNSET
    ln_s_reg: Union[Unset, int] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    mb_i_date: Union[Unset, str] = UNSET
    mb_t_stamp_acl: Union[Unset, str] = UNSET
    mb_parent_id: Union[Unset, str] = UNSET
    mb_region_id: Union[Unset, str] = UNSET
    mb_delete_date: Union[Unset, str] = UNSET
    ln_t_stamp_local: Union[Unset, int] = UNSET
    mb_name: Union[Unset, str] = UNSET
    ln_s_desc: Union[Unset, int] = UNSET
    ln_internal_desc: Union[Unset, int] = UNSET
    mb_doc: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_t_stamp_sync: Union[Unset, str] = UNSET
    mb_path: Union[Unset, str] = UNSET
    mb_sig: Union[Unset, str] = UNSET
    mb_status: Union[Unset, str] = UNSET
    ln_name: Union[Unset, int] = UNSET
    ln_space_guid: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_s_reg: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_vt_rep: Union[Unset, str] = UNSET
    mb_lock_id_doc: Union[Unset, str] = UNSET
    mb_att: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    mb_owner_id: Union[Unset, str] = UNSET
    mb_info: Union[Unset, str] = UNSET
    mb_del_date: Union[Unset, str] = UNSET
    mb_s_name: Union[Unset, str] = UNSET
    mb_child_count: Union[Unset, str] = UNSET
    ln_t_stamp_acl: Union[Unset, int] = UNSET
    mb_lock_id_sord: Union[Unset, str] = UNSET
    mb_s_desc: Union[Unset, str] = UNSET
    mb_sync_date_rem: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_encryption_set = self.mb_encryption_set

        mb_t_stamp = self.mb_t_stamp

        mb_t_stamp_acl_sync = self.mb_t_stamp_acl_sync

        mb_x_date = self.mb_x_date

        ln_acl = self.ln_acl

        mb_space_guid = self.mb_space_guid

        mb_acl = self.mb_acl

        ln_t_stamp_sync = self.ln_t_stamp_sync

        mb_sync_date_loc = self.mb_sync_date_loc

        mb_id = self.mb_id

        mb_hist_count = self.mb_hist_count

        mb_delete_user = self.mb_delete_user

        mb_t_stamp_local = self.mb_t_stamp_local

        mb_key = self.mb_key

        mb_mask = self.mb_mask

        ln_s_name = self.ln_s_name

        mb_internal_desc = self.mb_internal_desc

        mb_guid = self.mb_guid

        ln_t_stamp_acl_sync = self.ln_t_stamp_acl_sync

        mb_flags = self.mb_flags

        ln_package_name = self.ln_package_name

        mb_kind = self.mb_kind

        ln_s_reg = self.ln_s_reg

        mb_package_name = self.mb_package_name

        mb_i_date = self.mb_i_date

        mb_t_stamp_acl = self.mb_t_stamp_acl

        mb_parent_id = self.mb_parent_id

        mb_region_id = self.mb_region_id

        mb_delete_date = self.mb_delete_date

        ln_t_stamp_local = self.ln_t_stamp_local

        mb_name = self.mb_name

        ln_s_desc = self.ln_s_desc

        ln_internal_desc = self.ln_internal_desc

        mb_doc = self.mb_doc

        ln_guid = self.ln_guid

        mb_t_stamp_sync = self.mb_t_stamp_sync

        mb_path = self.mb_path

        mb_sig = self.mb_sig

        mb_status = self.mb_status

        ln_name = self.ln_name

        ln_space_guid = self.ln_space_guid

        mb_all_members = self.mb_all_members

        mb_s_reg = self.mb_s_reg

        ln_t_stamp = self.ln_t_stamp

        mb_vt_rep = self.mb_vt_rep

        mb_lock_id_doc = self.mb_lock_id_doc

        mb_att = self.mb_att

        mb_type = self.mb_type

        mb_lock_id = self.mb_lock_id

        mb_owner_id = self.mb_owner_id

        mb_info = self.mb_info

        mb_del_date = self.mb_del_date

        mb_s_name = self.mb_s_name

        mb_child_count = self.mb_child_count

        ln_t_stamp_acl = self.ln_t_stamp_acl

        mb_lock_id_sord = self.mb_lock_id_sord

        mb_s_desc = self.mb_s_desc

        mb_sync_date_rem = self.mb_sync_date_rem

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_encryption_set is not UNSET:
            field_dict["mbEncryptionSet"] = mb_encryption_set
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_t_stamp_acl_sync is not UNSET:
            field_dict["mbTStampAclSync"] = mb_t_stamp_acl_sync
        if mb_x_date is not UNSET:
            field_dict["mbXDate"] = mb_x_date
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_space_guid is not UNSET:
            field_dict["mbSpaceGuid"] = mb_space_guid
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if ln_t_stamp_sync is not UNSET:
            field_dict["lnTStampSync"] = ln_t_stamp_sync
        if mb_sync_date_loc is not UNSET:
            field_dict["mbSyncDateLoc"] = mb_sync_date_loc
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_hist_count is not UNSET:
            field_dict["mbHistCount"] = mb_hist_count
        if mb_delete_user is not UNSET:
            field_dict["mbDeleteUser"] = mb_delete_user
        if mb_t_stamp_local is not UNSET:
            field_dict["mbTStampLocal"] = mb_t_stamp_local
        if mb_key is not UNSET:
            field_dict["mbKey"] = mb_key
        if mb_mask is not UNSET:
            field_dict["mbMask"] = mb_mask
        if ln_s_name is not UNSET:
            field_dict["lnSName"] = ln_s_name
        if mb_internal_desc is not UNSET:
            field_dict["mbInternalDesc"] = mb_internal_desc
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp_acl_sync is not UNSET:
            field_dict["lnTStampAclSync"] = ln_t_stamp_acl_sync
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if ln_package_name is not UNSET:
            field_dict["lnPackageName"] = ln_package_name
        if mb_kind is not UNSET:
            field_dict["mbKind"] = mb_kind
        if ln_s_reg is not UNSET:
            field_dict["lnSReg"] = ln_s_reg
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if mb_i_date is not UNSET:
            field_dict["mbIDate"] = mb_i_date
        if mb_t_stamp_acl is not UNSET:
            field_dict["mbTStampAcl"] = mb_t_stamp_acl
        if mb_parent_id is not UNSET:
            field_dict["mbParentId"] = mb_parent_id
        if mb_region_id is not UNSET:
            field_dict["mbRegionId"] = mb_region_id
        if mb_delete_date is not UNSET:
            field_dict["mbDeleteDate"] = mb_delete_date
        if ln_t_stamp_local is not UNSET:
            field_dict["lnTStampLocal"] = ln_t_stamp_local
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if ln_s_desc is not UNSET:
            field_dict["lnSDesc"] = ln_s_desc
        if ln_internal_desc is not UNSET:
            field_dict["lnInternalDesc"] = ln_internal_desc
        if mb_doc is not UNSET:
            field_dict["mbDoc"] = mb_doc
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_t_stamp_sync is not UNSET:
            field_dict["mbTStampSync"] = mb_t_stamp_sync
        if mb_path is not UNSET:
            field_dict["mbPath"] = mb_path
        if mb_sig is not UNSET:
            field_dict["mbSig"] = mb_sig
        if mb_status is not UNSET:
            field_dict["mbStatus"] = mb_status
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if ln_space_guid is not UNSET:
            field_dict["lnSpaceGuid"] = ln_space_guid
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_s_reg is not UNSET:
            field_dict["mbSReg"] = mb_s_reg
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_vt_rep is not UNSET:
            field_dict["mbVtRep"] = mb_vt_rep
        if mb_lock_id_doc is not UNSET:
            field_dict["mbLockIdDoc"] = mb_lock_id_doc
        if mb_att is not UNSET:
            field_dict["mbAtt"] = mb_att
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if mb_owner_id is not UNSET:
            field_dict["mbOwnerId"] = mb_owner_id
        if mb_info is not UNSET:
            field_dict["mbInfo"] = mb_info
        if mb_del_date is not UNSET:
            field_dict["mbDelDate"] = mb_del_date
        if mb_s_name is not UNSET:
            field_dict["mbSName"] = mb_s_name
        if mb_child_count is not UNSET:
            field_dict["mbChildCount"] = mb_child_count
        if ln_t_stamp_acl is not UNSET:
            field_dict["lnTStampAcl"] = ln_t_stamp_acl
        if mb_lock_id_sord is not UNSET:
            field_dict["mbLockIdSord"] = mb_lock_id_sord
        if mb_s_desc is not UNSET:
            field_dict["mbSDesc"] = mb_s_desc
        if mb_sync_date_rem is not UNSET:
            field_dict["mbSyncDateRem"] = mb_sync_date_rem

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_encryption_set = d.pop("mbEncryptionSet", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_t_stamp_acl_sync = d.pop("mbTStampAclSync", UNSET)

        mb_x_date = d.pop("mbXDate", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_space_guid = d.pop("mbSpaceGuid", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        ln_t_stamp_sync = d.pop("lnTStampSync", UNSET)

        mb_sync_date_loc = d.pop("mbSyncDateLoc", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_hist_count = d.pop("mbHistCount", UNSET)

        mb_delete_user = d.pop("mbDeleteUser", UNSET)

        mb_t_stamp_local = d.pop("mbTStampLocal", UNSET)

        mb_key = d.pop("mbKey", UNSET)

        mb_mask = d.pop("mbMask", UNSET)

        ln_s_name = d.pop("lnSName", UNSET)

        mb_internal_desc = d.pop("mbInternalDesc", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp_acl_sync = d.pop("lnTStampAclSync", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        ln_package_name = d.pop("lnPackageName", UNSET)

        mb_kind = d.pop("mbKind", UNSET)

        ln_s_reg = d.pop("lnSReg", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        mb_i_date = d.pop("mbIDate", UNSET)

        mb_t_stamp_acl = d.pop("mbTStampAcl", UNSET)

        mb_parent_id = d.pop("mbParentId", UNSET)

        mb_region_id = d.pop("mbRegionId", UNSET)

        mb_delete_date = d.pop("mbDeleteDate", UNSET)

        ln_t_stamp_local = d.pop("lnTStampLocal", UNSET)

        mb_name = d.pop("mbName", UNSET)

        ln_s_desc = d.pop("lnSDesc", UNSET)

        ln_internal_desc = d.pop("lnInternalDesc", UNSET)

        mb_doc = d.pop("mbDoc", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_t_stamp_sync = d.pop("mbTStampSync", UNSET)

        mb_path = d.pop("mbPath", UNSET)

        mb_sig = d.pop("mbSig", UNSET)

        mb_status = d.pop("mbStatus", UNSET)

        ln_name = d.pop("lnName", UNSET)

        ln_space_guid = d.pop("lnSpaceGuid", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_s_reg = d.pop("mbSReg", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_vt_rep = d.pop("mbVtRep", UNSET)

        mb_lock_id_doc = d.pop("mbLockIdDoc", UNSET)

        mb_att = d.pop("mbAtt", UNSET)

        mb_type = d.pop("mbType", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        mb_owner_id = d.pop("mbOwnerId", UNSET)

        mb_info = d.pop("mbInfo", UNSET)

        mb_del_date = d.pop("mbDelDate", UNSET)

        mb_s_name = d.pop("mbSName", UNSET)

        mb_child_count = d.pop("mbChildCount", UNSET)

        ln_t_stamp_acl = d.pop("lnTStampAcl", UNSET)

        mb_lock_id_sord = d.pop("mbLockIdSord", UNSET)

        mb_s_desc = d.pop("mbSDesc", UNSET)

        mb_sync_date_rem = d.pop("mbSyncDateRem", UNSET)

        obj_data_c = cls(
            mb_encryption_set=mb_encryption_set,
            mb_t_stamp=mb_t_stamp,
            mb_t_stamp_acl_sync=mb_t_stamp_acl_sync,
            mb_x_date=mb_x_date,
            ln_acl=ln_acl,
            mb_space_guid=mb_space_guid,
            mb_acl=mb_acl,
            ln_t_stamp_sync=ln_t_stamp_sync,
            mb_sync_date_loc=mb_sync_date_loc,
            mb_id=mb_id,
            mb_hist_count=mb_hist_count,
            mb_delete_user=mb_delete_user,
            mb_t_stamp_local=mb_t_stamp_local,
            mb_key=mb_key,
            mb_mask=mb_mask,
            ln_s_name=ln_s_name,
            mb_internal_desc=mb_internal_desc,
            mb_guid=mb_guid,
            ln_t_stamp_acl_sync=ln_t_stamp_acl_sync,
            mb_flags=mb_flags,
            ln_package_name=ln_package_name,
            mb_kind=mb_kind,
            ln_s_reg=ln_s_reg,
            mb_package_name=mb_package_name,
            mb_i_date=mb_i_date,
            mb_t_stamp_acl=mb_t_stamp_acl,
            mb_parent_id=mb_parent_id,
            mb_region_id=mb_region_id,
            mb_delete_date=mb_delete_date,
            ln_t_stamp_local=ln_t_stamp_local,
            mb_name=mb_name,
            ln_s_desc=ln_s_desc,
            ln_internal_desc=ln_internal_desc,
            mb_doc=mb_doc,
            ln_guid=ln_guid,
            mb_t_stamp_sync=mb_t_stamp_sync,
            mb_path=mb_path,
            mb_sig=mb_sig,
            mb_status=mb_status,
            ln_name=ln_name,
            ln_space_guid=ln_space_guid,
            mb_all_members=mb_all_members,
            mb_s_reg=mb_s_reg,
            ln_t_stamp=ln_t_stamp,
            mb_vt_rep=mb_vt_rep,
            mb_lock_id_doc=mb_lock_id_doc,
            mb_att=mb_att,
            mb_type=mb_type,
            mb_lock_id=mb_lock_id,
            mb_owner_id=mb_owner_id,
            mb_info=mb_info,
            mb_del_date=mb_del_date,
            mb_s_name=mb_s_name,
            mb_child_count=mb_child_count,
            ln_t_stamp_acl=ln_t_stamp_acl,
            mb_lock_id_sord=mb_lock_id_sord,
            mb_s_desc=mb_s_desc,
            mb_sync_date_rem=mb_sync_date_rem,
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
