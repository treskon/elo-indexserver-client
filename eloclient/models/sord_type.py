from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="SordType")


@_attrs_define
class SordType:
    """Each file structure element is assigned a SordType.
    This SordType has three icons , which are used in the different
     view in the client: a standard icon, a disabled icon (empty folders or references) and a workflow icon.<br>
     The icons are available in BMP, ICO and JPEG format.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

     see@ SordTypeC SordTypeC

        Attributes:
            disabled_icon (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            extensions (Union[Unset, List[str]]):
            icon (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            id (Union[Unset, int]): Sord type ID.
            name (Union[Unset, str]): Type name.
            workflow_icon (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            package_name (Union[Unset, str]): Package name of SordType
    """

    disabled_icon: Union[Unset, "FileData"] = UNSET
    extensions: Union[Unset, List[str]] = UNSET
    icon: Union[Unset, "FileData"] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    workflow_icon: Union[Unset, "FileData"] = UNSET
    package_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disabled_icon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disabled_icon, Unset):
            disabled_icon = self.disabled_icon.to_dict()

        extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions

        icon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.icon, Unset):
            icon = self.icon.to_dict()

        id = self.id
        name = self.name
        workflow_icon: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow_icon, Unset):
            workflow_icon = self.workflow_icon.to_dict()

        package_name = self.package_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disabled_icon is not UNSET:
            field_dict["disabledIcon"] = disabled_icon
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if icon is not UNSET:
            field_dict["icon"] = icon
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if workflow_icon is not UNSET:
            field_dict["workflowIcon"] = workflow_icon
        if package_name is not UNSET:
            field_dict["packageName"] = package_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        _disabled_icon = d.pop("disabledIcon", UNSET)
        disabled_icon: Union[Unset, FileData]
        if isinstance(_disabled_icon, Unset):
            disabled_icon = UNSET
        else:
            disabled_icon = FileData.from_dict(_disabled_icon)

        extensions = cast(List[str], d.pop("extensions", UNSET))

        _icon = d.pop("icon", UNSET)
        icon: Union[Unset, FileData]
        if isinstance(_icon, Unset):
            icon = UNSET
        else:
            icon = FileData.from_dict(_icon)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _workflow_icon = d.pop("workflowIcon", UNSET)
        workflow_icon: Union[Unset, FileData]
        if isinstance(_workflow_icon, Unset):
            workflow_icon = UNSET
        else:
            workflow_icon = FileData.from_dict(_workflow_icon)

        package_name = d.pop("packageName", UNSET)

        sord_type = cls(
            disabled_icon=disabled_icon,
            extensions=extensions,
            icon=icon,
            id=id,
            name=name,
            workflow_icon=workflow_icon,
            package_name=package_name,
        )

        sord_type.additional_properties = d
        return sord_type

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
