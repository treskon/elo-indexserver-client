from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_file_z import ConfigFileZ


T = TypeVar("T", bound="ConfigFileC")


@_attrs_define
class ConfigFileC:
    """Constants for the ConfigFile class. These are used for accessing server directories.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            cold (Union[Unset, str]): Directory for COLD background files.
            elo_scripts (Union[Unset, str]): Directory for scripts.
            init_data (Union[Unset, str]): Directory of initialization data.
            postbox (Union[Unset, str]): Directory of Intray/postbox.
            checkout (Union[Unset, str]): Server side checkout directory.
            template (Union[Unset, str]): Old document template directory (ELO 5.0).
            viewer_postbox (Union[Unset, str]): RESERVED
            mb_name (Union[Unset, str]): Member bit: name
            mb_file_data (Union[Unset, str]): Member bit: fileData
            mb_last_modified (Union[Unset, str]): Member bit: lastModified
            mb_size (Union[Unset, str]): Member bit: size
            mb_url (Union[Unset, str]): Member bit: URL
            mb_all_members (Union[Unset, str]): Member bit set: all members.
            mb_all (Union[Unset, ConfigFileZ]): This class encapsulates the constants of ConfigFileC.
            mb_no_file_data (Union[Unset, ConfigFileZ]): This class encapsulates the constants of ConfigFileC.
    """

    cold: Union[Unset, str] = UNSET
    elo_scripts: Union[Unset, str] = UNSET
    init_data: Union[Unset, str] = UNSET
    postbox: Union[Unset, str] = UNSET
    checkout: Union[Unset, str] = UNSET
    template: Union[Unset, str] = UNSET
    viewer_postbox: Union[Unset, str] = UNSET
    mb_name: Union[Unset, str] = UNSET
    mb_file_data: Union[Unset, str] = UNSET
    mb_last_modified: Union[Unset, str] = UNSET
    mb_size: Union[Unset, str] = UNSET
    mb_url: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_all: Union[Unset, "ConfigFileZ"] = UNSET
    mb_no_file_data: Union[Unset, "ConfigFileZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cold = self.cold
        elo_scripts = self.elo_scripts
        init_data = self.init_data
        postbox = self.postbox
        checkout = self.checkout
        template = self.template
        viewer_postbox = self.viewer_postbox
        mb_name = self.mb_name
        mb_file_data = self.mb_file_data
        mb_last_modified = self.mb_last_modified
        mb_size = self.mb_size
        mb_url = self.mb_url
        mb_all_members = self.mb_all_members
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_no_file_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_no_file_data, Unset):
            mb_no_file_data = self.mb_no_file_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cold is not UNSET:
            field_dict["COLD"] = cold
        if elo_scripts is not UNSET:
            field_dict["ELO_SCRIPTS"] = elo_scripts
        if init_data is not UNSET:
            field_dict["INIT_DATA"] = init_data
        if postbox is not UNSET:
            field_dict["POSTBOX"] = postbox
        if checkout is not UNSET:
            field_dict["CHECKOUT"] = checkout
        if template is not UNSET:
            field_dict["TEMPLATE"] = template
        if viewer_postbox is not UNSET:
            field_dict["VIEWER_POSTBOX"] = viewer_postbox
        if mb_name is not UNSET:
            field_dict["mbName"] = mb_name
        if mb_file_data is not UNSET:
            field_dict["mbFileData"] = mb_file_data
        if mb_last_modified is not UNSET:
            field_dict["mbLastModified"] = mb_last_modified
        if mb_size is not UNSET:
            field_dict["mbSize"] = mb_size
        if mb_url is not UNSET:
            field_dict["mbUrl"] = mb_url
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_no_file_data is not UNSET:
            field_dict["mbNoFileData"] = mb_no_file_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.config_file_z import ConfigFileZ

        d = src_dict.copy()
        cold = d.pop("COLD", UNSET)

        elo_scripts = d.pop("ELO_SCRIPTS", UNSET)

        init_data = d.pop("INIT_DATA", UNSET)

        postbox = d.pop("POSTBOX", UNSET)

        checkout = d.pop("CHECKOUT", UNSET)

        template = d.pop("TEMPLATE", UNSET)

        viewer_postbox = d.pop("VIEWER_POSTBOX", UNSET)

        mb_name = d.pop("mbName", UNSET)

        mb_file_data = d.pop("mbFileData", UNSET)

        mb_last_modified = d.pop("mbLastModified", UNSET)

        mb_size = d.pop("mbSize", UNSET)

        mb_url = d.pop("mbUrl", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, ConfigFileZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = ConfigFileZ.from_dict(_mb_all)

        _mb_no_file_data = d.pop("mbNoFileData", UNSET)
        mb_no_file_data: Union[Unset, ConfigFileZ]
        if isinstance(_mb_no_file_data, Unset):
            mb_no_file_data = UNSET
        else:
            mb_no_file_data = ConfigFileZ.from_dict(_mb_no_file_data)

        config_file_c = cls(
            cold=cold,
            elo_scripts=elo_scripts,
            init_data=init_data,
            postbox=postbox,
            checkout=checkout,
            template=template,
            viewer_postbox=viewer_postbox,
            mb_name=mb_name,
            mb_file_data=mb_file_data,
            mb_last_modified=mb_last_modified,
            mb_size=mb_size,
            mb_url=mb_url,
            mb_all_members=mb_all_members,
            mb_all=mb_all,
            mb_no_file_data=mb_no_file_data,
        )

        config_file_c.additional_properties = d
        return config_file_c

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
