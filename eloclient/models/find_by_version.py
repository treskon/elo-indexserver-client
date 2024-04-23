from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByVersion")


@_attrs_define
class FindByVersion:
    """This class holds additional information for FindInfo, in order to restrict a search using the
    document history (version).

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            version_comment (Union[Unset, str]): User defined version description.
                The wildcard * is allowed, it matches any number of
                 characters.
            version_md5 (Union[Unset, str]): The md5 Hash value for the file.
            version_number (Union[Unset, str]): User defined version number or version id.
                The wildcard * is allowed, it matches any number of
                 characters.
            work_version_only (Union[Unset, bool]): Optional flag to restrict the search to active versions only.
    """

    version_comment: Union[Unset, str] = UNSET
    version_md5: Union[Unset, str] = UNSET
    version_number: Union[Unset, str] = UNSET
    work_version_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version_comment = self.version_comment

        version_md5 = self.version_md5

        version_number = self.version_number

        work_version_only = self.work_version_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version_comment is not UNSET:
            field_dict["versionComment"] = version_comment
        if version_md5 is not UNSET:
            field_dict["versionMD5"] = version_md5
        if version_number is not UNSET:
            field_dict["versionNumber"] = version_number
        if work_version_only is not UNSET:
            field_dict["workVersionOnly"] = work_version_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version_comment = d.pop("versionComment", UNSET)

        version_md5 = d.pop("versionMD5", UNSET)

        version_number = d.pop("versionNumber", UNSET)

        work_version_only = d.pop("workVersionOnly", UNSET)

        find_by_version = cls(
            version_comment=version_comment,
            version_md5=version_md5,
            version_number=version_number,
            work_version_only=work_version_only,
        )

        find_by_version.additional_properties = d
        return find_by_version

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
