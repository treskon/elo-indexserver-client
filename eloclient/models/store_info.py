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
            create_date_iso (Union[Unset, str]): Create date (UTC).
            dir_ (Union[Unset, str]): Physical directory where the documents of this path are stored. Length of the field in
                database: 255byte.
            flags (Union[Unset, int]): Bitset of options.
            id (Union[Unset, int]): Path ID Set this value to -1 in order to create a new storage path.
            name (Union[Unset, str]): Path name. Length of the field in database: 16byte.
            scatter (Union[Unset, int]): Granularity of subdirectories in the physical directory.
            std_path (Union[Unset, bool]): standard path? read-only
            update_date_iso (Union[Unset, str]): Update date (UTC).
            preview_dir (Union[Unset, str]): Physical directory where previews stored. Length of the field in database:
                255byte.
            fulltext_dir (Union[Unset, str]): Physical directory where fulltext content is stored. Length of the field in
                database: 255byte.
            cloud_type (Union[Unset, int]): Type of Cloud Storage.
            endpoint (Union[Unset, str]): Endpoint (URL/IP/PORT) for Cloud Storage.
            access_key (Union[Unset, str]): AccessKey for Cloud Storage.
            secret_key (Union[Unset, str]): SecretKey for Cloud Storage.
            bucket (Union[Unset, str]): Bucket name for Cloud Storage. Bucket names must be unique across all existing
                bucket names in Amazon S3.
            region (Union[Unset, str]): Region for Amazon S3 Cloud Storage.
            encryption_key (Union[Unset, str]): Encryption key for Cloud Storage.
    """

    create_date_iso: Union[Unset, str] = UNSET
    dir_: Union[Unset, str] = UNSET
    flags: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    scatter: Union[Unset, int] = UNSET
    std_path: Union[Unset, bool] = UNSET
    update_date_iso: Union[Unset, str] = UNSET
    preview_dir: Union[Unset, str] = UNSET
    fulltext_dir: Union[Unset, str] = UNSET
    cloud_type: Union[Unset, int] = UNSET
    endpoint: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    secret_key: Union[Unset, str] = UNSET
    bucket: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    encryption_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_date_iso = self.create_date_iso
        dir_ = self.dir_
        flags = self.flags
        id = self.id
        name = self.name
        scatter = self.scatter
        std_path = self.std_path
        update_date_iso = self.update_date_iso
        preview_dir = self.preview_dir
        fulltext_dir = self.fulltext_dir
        cloud_type = self.cloud_type
        endpoint = self.endpoint
        access_key = self.access_key
        secret_key = self.secret_key
        bucket = self.bucket
        region = self.region
        encryption_key = self.encryption_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_date_iso is not UNSET:
            field_dict["createDateISO"] = create_date_iso
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if flags is not UNSET:
            field_dict["flags"] = flags
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scatter is not UNSET:
            field_dict["scatter"] = scatter
        if std_path is not UNSET:
            field_dict["stdPath"] = std_path
        if update_date_iso is not UNSET:
            field_dict["updateDateISO"] = update_date_iso
        if preview_dir is not UNSET:
            field_dict["previewDir"] = preview_dir
        if fulltext_dir is not UNSET:
            field_dict["fulltextDir"] = fulltext_dir
        if cloud_type is not UNSET:
            field_dict["cloudType"] = cloud_type
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if access_key is not UNSET:
            field_dict["accessKey"] = access_key
        if secret_key is not UNSET:
            field_dict["secretKey"] = secret_key
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if region is not UNSET:
            field_dict["region"] = region
        if encryption_key is not UNSET:
            field_dict["encryptionKey"] = encryption_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        create_date_iso = d.pop("createDateISO", UNSET)

        dir_ = d.pop("dir", UNSET)

        flags = d.pop("flags", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        scatter = d.pop("scatter", UNSET)

        std_path = d.pop("stdPath", UNSET)

        update_date_iso = d.pop("updateDateISO", UNSET)

        preview_dir = d.pop("previewDir", UNSET)

        fulltext_dir = d.pop("fulltextDir", UNSET)

        cloud_type = d.pop("cloudType", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        access_key = d.pop("accessKey", UNSET)

        secret_key = d.pop("secretKey", UNSET)

        bucket = d.pop("bucket", UNSET)

        region = d.pop("region", UNSET)

        encryption_key = d.pop("encryptionKey", UNSET)

        store_info = cls(
            create_date_iso=create_date_iso,
            dir_=dir_,
            flags=flags,
            id=id,
            name=name,
            scatter=scatter,
            std_path=std_path,
            update_date_iso=update_date_iso,
            preview_dir=preview_dir,
            fulltext_dir=fulltext_dir,
            cloud_type=cloud_type,
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
            bucket=bucket,
            region=region,
            encryption_key=encryption_key,
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
