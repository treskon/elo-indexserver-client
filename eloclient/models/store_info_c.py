from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreInfoC")


@_attrs_define
class StoreInfoC:
    """Definition of a document path.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            sp_flat (Union[Unset, int]): No sub directories.
            sp_64k (Union[Unset, int]): 64k documents per sub directory
            sp_16 (Union[Unset, int]): 16k documents per sub directory
            sp_4k (Union[Unset, int]): 4k documents per sub directory
            sp_1k (Union[Unset, int]): 1k documents per sub directory
            sp_full (Union[Unset, int]): 256 folders with 256 documents
            sp_md5_hash (Union[Unset, int]): Store using MD5 hash.
            sp_centera (Union[Unset, int]): Store on CENTERA device.
            sp_tsm (Union[Unset, int]): Store on TSM device.
            sp_rel_file_path (Union[Unset, int]): External storage definition. A physical (relative) path is specified for
                each document.
            sp_activator (Union[Unset, int]): Store in KGS Activator.
            sp_s3 (Union[Unset, int]): Store on S3 Cloud Storage
            sp_s3_external (Union[Unset, int]): Use S3 Cloud Storage as Backup Device
            flag_elo5_path_changed (Union[Unset, int]): Only ELO 5.0: path has been changed.
            flag_elo5_path_protected (Union[Unset, int]): Only ELO 5.0: path is protected.
            flag_elo5_no_nt_security (Union[Unset, int]): Only ELO 5.0: no NT security.
            flag_backup (Union[Unset, int]): Backup path.
            flag_readonly (Union[Unset, int]): Path is read-only.
            flag_no_restore (Union[Unset, int]): Used with FLAG_BACKUP, document files are not restored in a normal path.
            flag_worm (Union[Unset, int]): Path can only be written once. DM does not use temporary files.
            dmpath_elosys (Union[Unset, str]): Reserved path name. Documents stored within DMPATH_ELOSYS will not be purged.
            cloud_minio (Union[Unset, int]): Minio Cloud Storage.
            cloud_s3 (Union[Unset, int]): Amazon S3 Cloud Storage.
            cloud_google (Union[Unset, int]): Google Cloud Storage. not yet implemented.
            no_file_encryption (Union[Unset, str]): Cloud storage encryption is set by default. If this constant is set in
                field StoreInfo.
                encryptionKey there will be
                 no encryption.
    """

    sp_flat: Union[Unset, int] = UNSET
    sp_64k: Union[Unset, int] = UNSET
    sp_16: Union[Unset, int] = UNSET
    sp_4k: Union[Unset, int] = UNSET
    sp_1k: Union[Unset, int] = UNSET
    sp_full: Union[Unset, int] = UNSET
    sp_md5_hash: Union[Unset, int] = UNSET
    sp_centera: Union[Unset, int] = UNSET
    sp_tsm: Union[Unset, int] = UNSET
    sp_rel_file_path: Union[Unset, int] = UNSET
    sp_activator: Union[Unset, int] = UNSET
    sp_s3: Union[Unset, int] = UNSET
    sp_s3_external: Union[Unset, int] = UNSET
    flag_elo5_path_changed: Union[Unset, int] = UNSET
    flag_elo5_path_protected: Union[Unset, int] = UNSET
    flag_elo5_no_nt_security: Union[Unset, int] = UNSET
    flag_backup: Union[Unset, int] = UNSET
    flag_readonly: Union[Unset, int] = UNSET
    flag_no_restore: Union[Unset, int] = UNSET
    flag_worm: Union[Unset, int] = UNSET
    dmpath_elosys: Union[Unset, str] = UNSET
    cloud_minio: Union[Unset, int] = UNSET
    cloud_s3: Union[Unset, int] = UNSET
    cloud_google: Union[Unset, int] = UNSET
    no_file_encryption: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sp_flat = self.sp_flat
        sp_64k = self.sp_64k
        sp_16 = self.sp_16
        sp_4k = self.sp_4k
        sp_1k = self.sp_1k
        sp_full = self.sp_full
        sp_md5_hash = self.sp_md5_hash
        sp_centera = self.sp_centera
        sp_tsm = self.sp_tsm
        sp_rel_file_path = self.sp_rel_file_path
        sp_activator = self.sp_activator
        sp_s3 = self.sp_s3
        sp_s3_external = self.sp_s3_external
        flag_elo5_path_changed = self.flag_elo5_path_changed
        flag_elo5_path_protected = self.flag_elo5_path_protected
        flag_elo5_no_nt_security = self.flag_elo5_no_nt_security
        flag_backup = self.flag_backup
        flag_readonly = self.flag_readonly
        flag_no_restore = self.flag_no_restore
        flag_worm = self.flag_worm
        dmpath_elosys = self.dmpath_elosys
        cloud_minio = self.cloud_minio
        cloud_s3 = self.cloud_s3
        cloud_google = self.cloud_google
        no_file_encryption = self.no_file_encryption

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sp_flat is not UNSET:
            field_dict["SP_FLAT"] = sp_flat
        if sp_64k is not UNSET:
            field_dict["SP_64K"] = sp_64k
        if sp_16 is not UNSET:
            field_dict["SP_16"] = sp_16
        if sp_4k is not UNSET:
            field_dict["SP_4K"] = sp_4k
        if sp_1k is not UNSET:
            field_dict["SP_1K"] = sp_1k
        if sp_full is not UNSET:
            field_dict["SP_FULL"] = sp_full
        if sp_md5_hash is not UNSET:
            field_dict["SP_MD5_HASH"] = sp_md5_hash
        if sp_centera is not UNSET:
            field_dict["SP_CENTERA"] = sp_centera
        if sp_tsm is not UNSET:
            field_dict["SP_TSM"] = sp_tsm
        if sp_rel_file_path is not UNSET:
            field_dict["SP_REL_FILE_PATH"] = sp_rel_file_path
        if sp_activator is not UNSET:
            field_dict["SP_ACTIVATOR"] = sp_activator
        if sp_s3 is not UNSET:
            field_dict["SP_S3"] = sp_s3
        if sp_s3_external is not UNSET:
            field_dict["SP_S3_EXTERNAL"] = sp_s3_external
        if flag_elo5_path_changed is not UNSET:
            field_dict["FLAG_ELO5_PATH_CHANGED"] = flag_elo5_path_changed
        if flag_elo5_path_protected is not UNSET:
            field_dict["FLAG_ELO5_PATH_PROTECTED"] = flag_elo5_path_protected
        if flag_elo5_no_nt_security is not UNSET:
            field_dict["FLAG_ELO5_NO_NT_SECURITY"] = flag_elo5_no_nt_security
        if flag_backup is not UNSET:
            field_dict["FLAG_BACKUP"] = flag_backup
        if flag_readonly is not UNSET:
            field_dict["FLAG_READONLY"] = flag_readonly
        if flag_no_restore is not UNSET:
            field_dict["FLAG_NO_RESTORE"] = flag_no_restore
        if flag_worm is not UNSET:
            field_dict["FLAG_WORM"] = flag_worm
        if dmpath_elosys is not UNSET:
            field_dict["DMPATH_ELOSYS"] = dmpath_elosys
        if cloud_minio is not UNSET:
            field_dict["CLOUD_MINIO"] = cloud_minio
        if cloud_s3 is not UNSET:
            field_dict["CLOUD_S3"] = cloud_s3
        if cloud_google is not UNSET:
            field_dict["CLOUD_GOOGLE"] = cloud_google
        if no_file_encryption is not UNSET:
            field_dict["NO_FILE_ENCRYPTION"] = no_file_encryption

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sp_flat = d.pop("SP_FLAT", UNSET)

        sp_64k = d.pop("SP_64K", UNSET)

        sp_16 = d.pop("SP_16", UNSET)

        sp_4k = d.pop("SP_4K", UNSET)

        sp_1k = d.pop("SP_1K", UNSET)

        sp_full = d.pop("SP_FULL", UNSET)

        sp_md5_hash = d.pop("SP_MD5_HASH", UNSET)

        sp_centera = d.pop("SP_CENTERA", UNSET)

        sp_tsm = d.pop("SP_TSM", UNSET)

        sp_rel_file_path = d.pop("SP_REL_FILE_PATH", UNSET)

        sp_activator = d.pop("SP_ACTIVATOR", UNSET)

        sp_s3 = d.pop("SP_S3", UNSET)

        sp_s3_external = d.pop("SP_S3_EXTERNAL", UNSET)

        flag_elo5_path_changed = d.pop("FLAG_ELO5_PATH_CHANGED", UNSET)

        flag_elo5_path_protected = d.pop("FLAG_ELO5_PATH_PROTECTED", UNSET)

        flag_elo5_no_nt_security = d.pop("FLAG_ELO5_NO_NT_SECURITY", UNSET)

        flag_backup = d.pop("FLAG_BACKUP", UNSET)

        flag_readonly = d.pop("FLAG_READONLY", UNSET)

        flag_no_restore = d.pop("FLAG_NO_RESTORE", UNSET)

        flag_worm = d.pop("FLAG_WORM", UNSET)

        dmpath_elosys = d.pop("DMPATH_ELOSYS", UNSET)

        cloud_minio = d.pop("CLOUD_MINIO", UNSET)

        cloud_s3 = d.pop("CLOUD_S3", UNSET)

        cloud_google = d.pop("CLOUD_GOOGLE", UNSET)

        no_file_encryption = d.pop("NO_FILE_ENCRYPTION", UNSET)

        store_info_c = cls(
            sp_flat=sp_flat,
            sp_64k=sp_64k,
            sp_16=sp_16,
            sp_4k=sp_4k,
            sp_1k=sp_1k,
            sp_full=sp_full,
            sp_md5_hash=sp_md5_hash,
            sp_centera=sp_centera,
            sp_tsm=sp_tsm,
            sp_rel_file_path=sp_rel_file_path,
            sp_activator=sp_activator,
            sp_s3=sp_s3,
            sp_s3_external=sp_s3_external,
            flag_elo5_path_changed=flag_elo5_path_changed,
            flag_elo5_path_protected=flag_elo5_path_protected,
            flag_elo5_no_nt_security=flag_elo5_no_nt_security,
            flag_backup=flag_backup,
            flag_readonly=flag_readonly,
            flag_no_restore=flag_no_restore,
            flag_worm=flag_worm,
            dmpath_elosys=dmpath_elosys,
            cloud_minio=cloud_minio,
            cloud_s3=cloud_s3,
            cloud_google=cloud_google,
            no_file_encryption=no_file_encryption,
        )

        store_info_c.additional_properties = d
        return store_info_c

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
