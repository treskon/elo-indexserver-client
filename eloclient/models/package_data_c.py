from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackageDataC")


@_attrs_define
class PackageDataC:
    """<p>Bit constants for members of PackageData</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_description (Union[Unset, int]): Column length: Package description.
                DB column: pkdesc
            ln_content_type (Union[Unset, int]): Column length: Content type of the icon
                DB column: contenttype
            ln_maintainer (Union[Unset, int]): Column length: Maintainer of package
                DB column: maintainer
            mb_t_stamp (Union[Unset, str]): Member bit: Timestamp of last modification.
                DB column: pktstamp
            mb_lock_id (Union[Unset, str]): Member bit: The ID of the user that holds the lock or -1, if the note is not
                locked.
                DB column: lockid
            ln_namespace (Union[Unset, int]): Column length: Name of the package, which can be used (as technical name).
                DB column: namespace
            mb_name (Union[Unset, str]): Member bit: Name of the package, which is displayed.
                DB column: pkname
            mb_description (Union[Unset, str]): Member bit: Package description.
                DB column: pkdesc
            ln_guid (Union[Unset, int]): Column length: Package GUID.
                DB column: pkguid
            ln_name (Union[Unset, int]): Column length: Name of the package, which is displayed.
                DB column: pkname
            mb_namespace (Union[Unset, str]): Member bit: Name of the package, which can be used (as technical name).
                DB column: namespace
            mb_maintainer (Union[Unset, str]): Member bit: Maintainer of package
                DB column: maintainer
            mb_icon_data (Union[Unset, str]): Member bit: Icon of package.
                DB column: icon
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_guid (Union[Unset, str]): Member bit: Package GUID.
                DB column: pkguid
            ln_t_stamp (Union[Unset, int]): Column length: Timestamp of last modification.
                DB column: pktstamp
            mb_content_type (Union[Unset, str]): Member bit: Content type of the icon
                DB column: contenttype
            ln_icon_data (Union[Unset, int]): Column length: Icon of package.
                DB column: icon
    """

    ln_description: Union[Unset, int] = UNSET
    ln_content_type: Union[Unset, int] = UNSET
    ln_maintainer: Union[Unset, int] = UNSET
    mb_t_stamp: Union[Unset, str] = UNSET
    mb_lock_id: Union[Unset, str] = UNSET
    ln_namespace: Union[Unset, int] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_description: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    ln_name: Union[Unset, int] = UNSET
    mb_namespace: Union[Unset, str] = UNSET
    mb_maintainer: Union[Unset, str] = UNSET
    mb_icon_data: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_t_stamp: Union[Unset, int] = UNSET
    mb_content_type: Union[Unset, str] = UNSET
    ln_icon_data: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_description = self.ln_description

        ln_content_type = self.ln_content_type

        ln_maintainer = self.ln_maintainer

        mb_t_stamp = self.mb_t_stamp

        mb_lock_id = self.mb_lock_id

        ln_namespace = self.ln_namespace

        mb_name = self.mb_name

        mb_description = self.mb_description

        ln_guid = self.ln_guid

        ln_name = self.ln_name

        mb_namespace = self.mb_namespace

        mb_maintainer = self.mb_maintainer

        mb_icon_data = self.mb_icon_data

        mb_all_members = self.mb_all_members

        mb_guid = self.mb_guid

        ln_t_stamp = self.ln_t_stamp

        mb_content_type = self.mb_content_type

        ln_icon_data = self.ln_icon_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_description is not UNSET:
            field_dict["lnDescription"] = ln_description
        if ln_content_type is not UNSET:
            field_dict["lnContentType"] = ln_content_type
        if ln_maintainer is not UNSET:
            field_dict["lnMaintainer"] = ln_maintainer
        if mb_t_stamp is not UNSET:
            field_dict["mbTStamp"] = mb_t_stamp
        if mb_lock_id is not UNSET:
            field_dict["mbLockId"] = mb_lock_id
        if ln_namespace is not UNSET:
            field_dict["lnNamespace"] = ln_namespace
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_description is not UNSET:
            field_dict["mbDescription"] = mb_description
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if ln_name is not UNSET:
            field_dict["lnName"] = ln_name
        if mb_namespace is not UNSET:
            field_dict["mbNamespace"] = mb_namespace
        if mb_maintainer is not UNSET:
            field_dict["mbMaintainer"] = mb_maintainer
        if mb_icon_data is not UNSET:
            field_dict["mbIconData"] = mb_icon_data
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_t_stamp is not UNSET:
            field_dict["lnTStamp"] = ln_t_stamp
        if mb_content_type is not UNSET:
            field_dict["mbContentType"] = mb_content_type
        if ln_icon_data is not UNSET:
            field_dict["lnIconData"] = ln_icon_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_description = d.pop("lnDescription", UNSET)

        ln_content_type = d.pop("lnContentType", UNSET)

        ln_maintainer = d.pop("lnMaintainer", UNSET)

        mb_t_stamp = d.pop("mbTStamp", UNSET)

        mb_lock_id = d.pop("mbLockId", UNSET)

        ln_namespace = d.pop("lnNamespace", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_description = d.pop("mbDescription", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        ln_name = d.pop("lnName", UNSET)

        mb_namespace = d.pop("mbNamespace", UNSET)

        mb_maintainer = d.pop("mbMaintainer", UNSET)

        mb_icon_data = d.pop("mbIconData", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_t_stamp = d.pop("lnTStamp", UNSET)

        mb_content_type = d.pop("mbContentType", UNSET)

        ln_icon_data = d.pop("lnIconData", UNSET)

        package_data_c = cls(
            ln_description=ln_description,
            ln_content_type=ln_content_type,
            ln_maintainer=ln_maintainer,
            mb_t_stamp=mb_t_stamp,
            mb_lock_id=mb_lock_id,
            ln_namespace=ln_namespace,
            mb_name=mb_name,
            mb_description=mb_description,
            ln_guid=ln_guid,
            ln_name=ln_name,
            mb_namespace=mb_namespace,
            mb_maintainer=mb_maintainer,
            mb_icon_data=mb_icon_data,
            mb_all_members=mb_all_members,
            mb_guid=mb_guid,
            ln_t_stamp=ln_t_stamp,
            mb_content_type=mb_content_type,
            ln_icon_data=ln_icon_data,
        )

        package_data_c.additional_properties = d
        return package_data_c

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
