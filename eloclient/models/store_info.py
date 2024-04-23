from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StoreInfo")


@_attrs_define
class StoreInfo:
    """<p>
    This class represents a storage path.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            preview_dir (Union[Unset, str]): Physical directory where previews stored. Length of the field in database:
                255byte.
            secret_key (Union[Unset, str]): SecretKey for Cloud Storage.
            retention_mode (Union[Unset, int]): RetentionMode for S3 Storage
            flags (Union[Unset, int]): Bitset of options.
            encryption_key (Union[Unset, str]): Encryption key for Cloud Storage.
            dir_ (Union[Unset, str]): Physical directory where the documents of this path are stored.
                Length of the field in
                 database: 255byte.
            std_path (Union[Unset, bool]): standard path? read-only
            bucket (Union[Unset, str]): Bucket name for Cloud Storage.
                Bucket names must be unique across all existing bucket names in
                 Amazon S3.
            update_date_iso (Union[Unset, str]): Update date (UTC).
            endpoint (Union[Unset, str]): Endpoint (URL/IP/PORT) for Cloud Storage.
            create_date_iso (Union[Unset, str]): Create date (UTC).
            access_key (Union[Unset, str]): AccessKey for Cloud Storage.
            cloud_type (Union[Unset, int]): Type of Cloud Storage.
            scatter (Union[Unset, int]): Granularity of subdirectories in the physical directory.
            name (Union[Unset, str]): Path name. Length of the field in database: 16byte.
            id (Union[Unset, int]): Path ID Set this value to -1 in order to create a new storage path.
            fulltext_dir (Union[Unset, str]): Physical directory where fulltext content is stored. Length of the field in
                database: 255byte.
            region (Union[Unset, str]): Region for Amazon S3 Cloud Storage.
    """

    preview_dir: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    retention_mode: Union[Unset, int] = UNSET
    flags: Union[Unset, int] = UNSET
    encryption_key: Union[Unset, str] = UNSET
    dir_: Union[Unset, str] = UNSET
    std_path: Union[Unset, bool] = UNSET
    bucket: Union[Unset, str] = UNSET
    update_date_iso: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    cloud_type: Union[Unset, int] = UNSET
    scatter: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    fulltext_dir: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        preview_dir = self.preview_dir

        secret_key = self.secret_key

        retention_mode = self.retention_mode

        flags = self.flags

        encryption_key = self.encryption_key

        dir_ = self.dir_

        std_path = self.std_path

        bucket = self.bucket

        update_date_iso = self.update_date_iso

        endpoint = self.endpoint

        create_date_iso = self.create_date_iso

        access_key = self.access_key

        cloud_type = self.cloud_type

        scatter = self.scatter

        name = self.name

        id = self.id

        fulltext_dir = self.fulltext_dir

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if preview_dir is not UNSET:
            field_dict["previewDir"] = preview_dir
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if retention_mode is not UNSET:
            field_dict["retentionMode"] = retention_mode
        if flags is not UNSET:
            field_dict["flags"] = flags
        if encryption_key is not UNSET:
            field_dict["encryptionKey"] = encryption_key
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if std_path is not UNSET:
            field_dict["stdPath"] = std_path
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if update_date_iso is not UNSET:
            field_dict["updateDateISO"] = update_date_iso
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if create_date_iso is not UNSET:
            field_dict["createDateISO"] = create_date_iso
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if cloud_type is not UNSET:
            field_dict["cloudType"] = cloud_type
        if scatter is not UNSET:
            field_dict["scatter"] = scatter
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if fulltext_dir is not UNSET:
            field_dict["fulltextDir"] = fulltext_dir
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        preview_dir = d.pop("previewDir", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        retention_mode = d.pop("retentionMode", UNSET)

        flags = d.pop("flags", UNSET)

        encryption_key = d.pop("encryptionKey", UNSET)

        dir_ = d.pop("dir", UNSET)

        std_path = d.pop("stdPath", UNSET)

        bucket = d.pop("bucket", UNSET)

        update_date_iso = d.pop("updateDateISO", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        create_date_iso = d.pop("createDateISO", UNSET)

        access_key = d.pop("accessKey", UNSET)

        cloud_type = d.pop("cloudType", UNSET)

        scatter = d.pop("scatter", UNSET)

        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        fulltext_dir = d.pop("fulltextDir", UNSET)

        region = d.pop("region", UNSET)

        store_info = cls(
            preview_dir=preview_dir,
            secret_key=secret_key,
            retention_mode=retention_mode,
            flags=flags,
            encryption_key=encryption_key,
            dir_=dir_,
            std_path=std_path,
            bucket=bucket,
            update_date_iso=update_date_iso,
            endpoint=endpoint,
            create_date_iso=create_date_iso,
            access_key=access_key,
            cloud_type=cloud_type,
            scatter=scatter,
            name=name,
            id=id,
            fulltext_dir=fulltext_dir,
            region=region,
        )

        store_info.additional_properties = d
        return store_info

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
