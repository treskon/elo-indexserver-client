from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData
    from ..models.package_level_data import PackageLevelData


T = TypeVar("T", bound="PackageData")


@_attrs_define
class PackageData:
    """This class defines a package.
    EIX-1895

        Attributes:
            lock_id (Union[Unset, int]): The ID of the user that holds the lock or -1, if the note is not locked.
            t_stamp (Union[Unset, str]): Timestamp of last modification.
            name (Union[Unset, str]): Name of the package, which is displayed.
            icon (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            namespace (Union[Unset, str]): Name of the package, which can be used (as technical name).
            guid (Union[Unset, str]): Package GUID.
            description (Union[Unset, str]): Package description.
            lock_name (Union[Unset, str]): The user name that holds the lock or an empty string if the note is not locked.
            content_type (Union[Unset, str]): Content type of the icon
            maintainer (Union[Unset, str]): Maintainer of package
            levels (Union[Unset, List['PackageLevelData']]):
    """

    lock_id: Union[Unset, int] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    icon: Union[Unset, "FileData"] = UNSET
    namespace: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    content_type: Union[Unset, str] = UNSET
    maintainer: Union[Unset, str] = UNSET
    levels: Union[Unset, List["PackageLevelData"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lock_id = self.lock_id

        t_stamp = self.t_stamp

        name = self.name

        icon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        namespace = self.namespace

        guid = self.guid

        description = self.description

        lock_name = self.lock_name

        content_type = self.content_type

        maintainer = self.maintainer

        levels: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.levels, Unset):
            levels = []
            for componentsschemas_list_of_package_level_data_item_data in self.levels:
                componentsschemas_list_of_package_level_data_item = (
                    componentsschemas_list_of_package_level_data_item_data.to_dict()
                )
                levels.append(componentsschemas_list_of_package_level_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if t_stamp is not UNSET:
            field_dict["tStamp"] = t_stamp
        if name is not UNSET:
            field_dict["name"] = name
        if icon is not UNSET:
            field_dict["icon"] = icon
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if guid is not UNSET:
            field_dict["guid"] = guid
        if description is not UNSET:
            field_dict["description"] = description
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if content_type is not UNSET:
            field_dict["contentType"] = content_type
        if maintainer is not UNSET:
            field_dict["maintainer"] = maintainer
        if levels is not UNSET:
            field_dict["levels"] = levels

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData
        from ..models.package_level_data import PackageLevelData

        d = src_dict.copy()
        lock_id = d.pop("lockId", UNSET)

        t_stamp = d.pop("tStamp", UNSET)

        name = d.pop("name", UNSET)

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, FileData]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = FileData.from_dict(_icon)

        namespace = d.pop("namespace", UNSET)

        guid = d.pop("guid", UNSET)

        description = d.pop("description", UNSET)

        lock_name = d.pop("lockName", UNSET)

        content_type = d.pop("contentType", UNSET)

        maintainer = d.pop("maintainer", UNSET)

        levels = []
        _levels = d.pop("levels", UNSET)
        for componentsschemas_list_of_package_level_data_item_data in _levels or []:
            componentsschemas_list_of_package_level_data_item = PackageLevelData.from_dict(
                componentsschemas_list_of_package_level_data_item_data
            )

            levels.append(componentsschemas_list_of_package_level_data_item)

        package_data = cls(
            lock_id=lock_id,
            t_stamp=t_stamp,
            name=name,
            icon=icon,
            namespace=namespace,
            guid=guid,
            description=description,
            lock_name=lock_name,
            content_type=content_type,
            maintainer=maintainer,
            levels=levels,
        )

        package_data.additional_properties = d
        return package_data

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
