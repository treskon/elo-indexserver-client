from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="ConfigFile")


@_attrs_define
class ConfigFile:
    """Used for accessing directories or files on the server.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            size (Union[Unset, str]): File size.
            upload_result (Union[Unset, str]): HTTP-Response returned when file is uploaded.
            last_modified_iso (Union[Unset, str]): The last-modified date of the script file. This value is related to the
                UTC time-zone.
            file_data (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            name (Union[Unset, str]): The name of the file or the extension.
            dir_ (Union[Unset, str]): The path to the file.
            is_directory (Union[Unset, bool]): Returns true if the object is a directory, false if it is a file.
            url (Union[Unset, str]): Download or upload URL.
    """

    size: Union[Unset, str] = UNSET
    upload_result: Union[Unset, str] = UNSET
    last_modified_iso: Union[Unset, str] = UNSET
    file_data: Union[Unset, "FileData"] = UNSET
    name: Union[Unset, str] = UNSET
    dir_: Union[Unset, str] = UNSET
    is_directory: Union[Unset, bool] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        size = self.size

        upload_result = self.upload_result

        last_modified_iso = self.last_modified_iso

        file_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_data, Unset):
            file_data = self.file_data.to_dict()

        name = self.name

        dir_ = self.dir_

        is_directory = self.is_directory

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if size is not UNSET:
            field_dict["size"] = size
        if upload_result is not UNSET:
            field_dict["uploadResult"] = upload_result
        if last_modified_iso is not UNSET:
            field_dict["lastModifiedISO"] = last_modified_iso
        if file_data is not UNSET:
            field_dict["fileData"] = file_data
        if name is not UNSET:
            field_dict["name"] = name
        if dir_ is not UNSET:
            field_dict["dir"] = dir_
        if is_directory is not UNSET:
            field_dict["isDirectory"] = is_directory
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        size = d.pop("size", UNSET)

        upload_result = d.pop("uploadResult", UNSET)

        last_modified_iso = d.pop("lastModifiedISO", UNSET)

        _file_data = d.pop("fileData", UNSET)
        file_data: Union[Unset, FileData]
        if isinstance(_file_data, Unset):
            file_data = UNSET
        else:
            file_data = FileData.from_dict(_file_data)

        name = d.pop("name", UNSET)

        dir_ = d.pop("dir", UNSET)

        is_directory = d.pop("isDirectory", UNSET)

        url = d.pop("url", UNSET)

        config_file = cls(
            size=size,
            upload_result=upload_result,
            last_modified_iso=last_modified_iso,
            file_data=file_data,
            name=name,
            dir_=dir_,
            is_directory=is_directory,
            url=url,
        )

        config_file.additional_properties = d
        return config_file

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
