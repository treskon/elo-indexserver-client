from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord_type_z import SordTypeZ


T = TypeVar("T", bound="SordTypeC")


@_attrs_define
class SordTypeC:
    """Constants for folder or document types.

    Attributes:
        max_folder_types (Union[Unset, int]): Maximum number of folder types (=253).
        max_document_types (Union[Unset, int]): Maximum number of document types (=746).
        mb_id_name_ext (Union[Unset, str]): ID, name, extension.
        mb_icon_member (Union[Unset, str]): Return icon file data in <code>checkoutSordType</code>.
        mb_workflow_icon_member (Union[Unset, str]): Return file data of workflow icon in <code>checkoutSordType</code>.
        mb_disabled_icon_member (Union[Unset, str]): Return file data of disabled icon in <code>checkoutSordType</code>.
        mb_jpg (Union[Unset, str]):
        mb_bmp (Union[Unset, str]):
        mb_ico (Union[Unset, str]):
        mb_png (Union[Unset, str]):
        mb_no_icons (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icon_jpg (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icon_bmp (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icon_ico (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icon_png (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icons_jpg (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icons_bmp (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icons_ico (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_icons_png (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_all_jpg (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_all_bmp (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_all_ico (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_all_png (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_sord_type_icons (Union[Unset, str]): GUID for folder "/Administration/Sord Type Icons"
    """

    max_folder_types: Union[Unset, int] = UNSET
    max_document_types: Union[Unset, int] = UNSET
    mb_id_name_ext: Union[Unset, str] = UNSET
    mb_icon_member: Union[Unset, str] = UNSET
    mb_workflow_icon_member: Union[Unset, str] = UNSET
    mb_disabled_icon_member: Union[Unset, str] = UNSET
    mb_jpg: Union[Unset, str] = UNSET
    mb_bmp: Union[Unset, str] = UNSET
    mb_ico: Union[Unset, str] = UNSET
    mb_png: Union[Unset, str] = UNSET
    mb_no_icons: Union[Unset, "SordTypeZ"] = UNSET
    mb_icon_jpg: Union[Unset, "SordTypeZ"] = UNSET
    mb_icon_bmp: Union[Unset, "SordTypeZ"] = UNSET
    mb_icon_ico: Union[Unset, "SordTypeZ"] = UNSET
    mb_icon_png: Union[Unset, "SordTypeZ"] = UNSET
    mb_icons_jpg: Union[Unset, "SordTypeZ"] = UNSET
    mb_icons_bmp: Union[Unset, "SordTypeZ"] = UNSET
    mb_icons_ico: Union[Unset, "SordTypeZ"] = UNSET
    mb_icons_png: Union[Unset, "SordTypeZ"] = UNSET
    mb_all_jpg: Union[Unset, "SordTypeZ"] = UNSET
    mb_all_bmp: Union[Unset, "SordTypeZ"] = UNSET
    mb_all_ico: Union[Unset, "SordTypeZ"] = UNSET
    mb_all_png: Union[Unset, "SordTypeZ"] = UNSET
    guid_sord_type_icons: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_folder_types = self.max_folder_types
        max_document_types = self.max_document_types
        mb_id_name_ext = self.mb_id_name_ext
        mb_icon_member = self.mb_icon_member
        mb_workflow_icon_member = self.mb_workflow_icon_member
        mb_disabled_icon_member = self.mb_disabled_icon_member
        mb_jpg = self.mb_jpg
        mb_bmp = self.mb_bmp
        mb_ico = self.mb_ico
        mb_png = self.mb_png
        mb_no_icons: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_no_icons, Unset):
            mb_no_icons = self.mb_no_icons.to_dict()

        mb_icon_jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_jpg, Unset):
            mb_icon_jpg = self.mb_icon_jpg.to_dict()

        mb_icon_bmp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_bmp, Unset):
            mb_icon_bmp = self.mb_icon_bmp.to_dict()

        mb_icon_ico: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_ico, Unset):
            mb_icon_ico = self.mb_icon_ico.to_dict()

        mb_icon_png: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_png, Unset):
            mb_icon_png = self.mb_icon_png.to_dict()

        mb_icons_jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_jpg, Unset):
            mb_icons_jpg = self.mb_icons_jpg.to_dict()

        mb_icons_bmp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_bmp, Unset):
            mb_icons_bmp = self.mb_icons_bmp.to_dict()

        mb_icons_ico: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_ico, Unset):
            mb_icons_ico = self.mb_icons_ico.to_dict()

        mb_icons_png: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_png, Unset):
            mb_icons_png = self.mb_icons_png.to_dict()

        mb_all_jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_jpg, Unset):
            mb_all_jpg = self.mb_all_jpg.to_dict()

        mb_all_bmp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_bmp, Unset):
            mb_all_bmp = self.mb_all_bmp.to_dict()

        mb_all_ico: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_ico, Unset):
            mb_all_ico = self.mb_all_ico.to_dict()

        mb_all_png: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_png, Unset):
            mb_all_png = self.mb_all_png.to_dict()

        guid_sord_type_icons = self.guid_sord_type_icons

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_folder_types is not UNSET:
            field_dict["MAX_FOLDER_TYPES"] = max_folder_types
        if max_document_types is not UNSET:
            field_dict["MAX_DOCUMENT_TYPES"] = max_document_types
        if mb_id_name_ext is not UNSET:
            field_dict["mbIdNameExt"] = mb_id_name_ext
        if mb_icon_member is not UNSET:
            field_dict["mbIconMember"] = mb_icon_member
        if mb_workflow_icon_member is not UNSET:
            field_dict["mbWorkflowIconMember"] = mb_workflow_icon_member
        if mb_disabled_icon_member is not UNSET:
            field_dict["mbDisabledIconMember"] = mb_disabled_icon_member
        if mb_jpg is not UNSET:
            field_dict["mbJPG"] = mb_jpg
        if mb_bmp is not UNSET:
            field_dict["mbBMP"] = mb_bmp
        if mb_ico is not UNSET:
            field_dict["mbICO"] = mb_ico
        if mb_png is not UNSET:
            field_dict["mbPNG"] = mb_png
        if mb_no_icons is not UNSET:
            field_dict["mbNoIcons"] = mb_no_icons
        if mb_icon_jpg is not UNSET:
            field_dict["mbIconJPG"] = mb_icon_jpg
        if mb_icon_bmp is not UNSET:
            field_dict["mbIconBMP"] = mb_icon_bmp
        if mb_icon_ico is not UNSET:
            field_dict["mbIconICO"] = mb_icon_ico
        if mb_icon_png is not UNSET:
            field_dict["mbIconPNG"] = mb_icon_png
        if mb_icons_jpg is not UNSET:
            field_dict["mbIconsJPG"] = mb_icons_jpg
        if mb_icons_bmp is not UNSET:
            field_dict["mbIconsBMP"] = mb_icons_bmp
        if mb_icons_ico is not UNSET:
            field_dict["mbIconsICO"] = mb_icons_ico
        if mb_icons_png is not UNSET:
            field_dict["mbIconsPNG"] = mb_icons_png
        if mb_all_jpg is not UNSET:
            field_dict["mbAllJPG"] = mb_all_jpg
        if mb_all_bmp is not UNSET:
            field_dict["mbAllBMP"] = mb_all_bmp
        if mb_all_ico is not UNSET:
            field_dict["mbAllICO"] = mb_all_ico
        if mb_all_png is not UNSET:
            field_dict["mbAllPNG"] = mb_all_png
        if guid_sord_type_icons is not UNSET:
            field_dict["GUID_SORD_TYPE_ICONS"] = guid_sord_type_icons

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord_type_z import SordTypeZ

        d = src_dict.copy()
        max_folder_types = d.pop("MAX_FOLDER_TYPES", UNSET)

        max_document_types = d.pop("MAX_DOCUMENT_TYPES", UNSET)

        mb_id_name_ext = d.pop("mbIdNameExt", UNSET)

        mb_icon_member = d.pop("mbIconMember", UNSET)

        mb_workflow_icon_member = d.pop("mbWorkflowIconMember", UNSET)

        mb_disabled_icon_member = d.pop("mbDisabledIconMember", UNSET)

        mb_jpg = d.pop("mbJPG", UNSET)

        mb_bmp = d.pop("mbBMP", UNSET)

        mb_ico = d.pop("mbICO", UNSET)

        mb_png = d.pop("mbPNG", UNSET)

        _mb_no_icons = d.pop("mbNoIcons", UNSET)
        mb_no_icons: Union[Unset, SordTypeZ]
        if isinstance(_mb_no_icons, Unset):
            mb_no_icons = UNSET
        else:
            mb_no_icons = SordTypeZ.from_dict(_mb_no_icons)

        _mb_icon_jpg = d.pop("mbIconJPG", UNSET)
        mb_icon_jpg: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_jpg, Unset):
            mb_icon_jpg = UNSET
        else:
            mb_icon_jpg = SordTypeZ.from_dict(_mb_icon_jpg)

        _mb_icon_bmp = d.pop("mbIconBMP", UNSET)
        mb_icon_bmp: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_bmp, Unset):
            mb_icon_bmp = UNSET
        else:
            mb_icon_bmp = SordTypeZ.from_dict(_mb_icon_bmp)

        _mb_icon_ico = d.pop("mbIconICO", UNSET)
        mb_icon_ico: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_ico, Unset):
            mb_icon_ico = UNSET
        else:
            mb_icon_ico = SordTypeZ.from_dict(_mb_icon_ico)

        _mb_icon_png = d.pop("mbIconPNG", UNSET)
        mb_icon_png: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_png, Unset):
            mb_icon_png = UNSET
        else:
            mb_icon_png = SordTypeZ.from_dict(_mb_icon_png)

        _mb_icons_jpg = d.pop("mbIconsJPG", UNSET)
        mb_icons_jpg: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_jpg, Unset):
            mb_icons_jpg = UNSET
        else:
            mb_icons_jpg = SordTypeZ.from_dict(_mb_icons_jpg)

        _mb_icons_bmp = d.pop("mbIconsBMP", UNSET)
        mb_icons_bmp: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_bmp, Unset):
            mb_icons_bmp = UNSET
        else:
            mb_icons_bmp = SordTypeZ.from_dict(_mb_icons_bmp)

        _mb_icons_ico = d.pop("mbIconsICO", UNSET)
        mb_icons_ico: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_ico, Unset):
            mb_icons_ico = UNSET
        else:
            mb_icons_ico = SordTypeZ.from_dict(_mb_icons_ico)

        _mb_icons_png = d.pop("mbIconsPNG", UNSET)
        mb_icons_png: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_png, Unset):
            mb_icons_png = UNSET
        else:
            mb_icons_png = SordTypeZ.from_dict(_mb_icons_png)

        _mb_all_jpg = d.pop("mbAllJPG", UNSET)
        mb_all_jpg: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_jpg, Unset):
            mb_all_jpg = UNSET
        else:
            mb_all_jpg = SordTypeZ.from_dict(_mb_all_jpg)

        _mb_all_bmp = d.pop("mbAllBMP", UNSET)
        mb_all_bmp: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_bmp, Unset):
            mb_all_bmp = UNSET
        else:
            mb_all_bmp = SordTypeZ.from_dict(_mb_all_bmp)

        _mb_all_ico = d.pop("mbAllICO", UNSET)
        mb_all_ico: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_ico, Unset):
            mb_all_ico = UNSET
        else:
            mb_all_ico = SordTypeZ.from_dict(_mb_all_ico)

        _mb_all_png = d.pop("mbAllPNG", UNSET)
        mb_all_png: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_png, Unset):
            mb_all_png = UNSET
        else:
            mb_all_png = SordTypeZ.from_dict(_mb_all_png)

        guid_sord_type_icons = d.pop("GUID_SORD_TYPE_ICONS", UNSET)

        sord_type_c = cls(
            max_folder_types=max_folder_types,
            max_document_types=max_document_types,
            mb_id_name_ext=mb_id_name_ext,
            mb_icon_member=mb_icon_member,
            mb_workflow_icon_member=mb_workflow_icon_member,
            mb_disabled_icon_member=mb_disabled_icon_member,
            mb_jpg=mb_jpg,
            mb_bmp=mb_bmp,
            mb_ico=mb_ico,
            mb_png=mb_png,
            mb_no_icons=mb_no_icons,
            mb_icon_jpg=mb_icon_jpg,
            mb_icon_bmp=mb_icon_bmp,
            mb_icon_ico=mb_icon_ico,
            mb_icon_png=mb_icon_png,
            mb_icons_jpg=mb_icons_jpg,
            mb_icons_bmp=mb_icons_bmp,
            mb_icons_ico=mb_icons_ico,
            mb_icons_png=mb_icons_png,
            mb_all_jpg=mb_all_jpg,
            mb_all_bmp=mb_all_bmp,
            mb_all_ico=mb_all_ico,
            mb_all_png=mb_all_png,
            guid_sord_type_icons=guid_sord_type_icons,
        )

        sord_type_c.additional_properties = d
        return sord_type_c

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
