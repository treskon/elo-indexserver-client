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
        guid_calc (Union[Unset, str]): calc
        guid_firma (Union[Unset, str]): firma
        mb_icons_png (Union[Unset, SordTypeZ]): <p>
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
        max_folder_types (Union[Unset, int]): Maximum number of folder types (=253).
        guid_einzelperson (Union[Unset, str]): einzelperson
        guid_gif (Union[Unset, str]): gif
        guid_web_dokument (Union[Unset, str]): web_dokument
        guid_dokument (Union[Unset, str]): dokument
        guid_access (Union[Unset, str]): access
        guid_ordner (Union[Unset, str]): ordner
        guid_schrank (Union[Unset, str]): schrank
        guid_register_gelb (Union[Unset, str]): register_gelb
        guid_autocad_dxf (Union[Unset, str]): autocad_dxf
        guid_workflowordner (Union[Unset, str]): workflowordner
        mb_bmp (Union[Unset, str]):
        mb_no_icons (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_register_rot (Union[Unset, str]): register_rot
        guid_visio (Union[Unset, str]): visio
        guid_xml (Union[Unset, str]): xml
        mb_jpg (Union[Unset, str]):
        guid_ordner_gelb (Union[Unset, str]): ordner_gelb
        mb_icons_bmp (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        mb_workflow_icon_member (Union[Unset, str]): Return file data of workflow icon in <code>checkoutSordType</code>.
        mb_icon_member (Union[Unset, str]): Return icon file data in <code>checkoutSordType</code>.
        mb_icon_png (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_akten_schublade (Union[Unset, str]): akten_schublade
        guid_powerpoint (Union[Unset, str]): powerpoint
        guid_sord_type_icons (Union[Unset, str]): GUID for folder "/Administration/Sord Type Icons"
        guid_zip (Union[Unset, str]): zip
        mb_all_png (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_ordner_blau (Union[Unset, str]): ordner_blau
        guid_ebene_32 (Union[Unset, str]): ebene_32
        guid_png (Union[Unset, str]): png
        mb_icons_ico (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_auftragsbearbeitung (Union[Unset, str]): auftragsbearbeitung
        guid_ordner_gruen (Union[Unset, str]): ordner_gruen
        guid_impress (Union[Unset, str]): impress
        mb_id_name_ext (Union[Unset, str]): ID, name, extension.
        mb_all_ico (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_aktivitaeten (Union[Unset, str]): aktivitaeten
        guid_web_archiv (Union[Unset, str]): web_archiv
        mb_icon_ico (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_bild (Union[Unset, str]): bild
        guid_ebene_5 (Union[Unset, str]): ebene_5
        guid_ebene_4 (Union[Unset, str]): ebene_4
        guid_akten_schublade_rot (Union[Unset, str]): akten_schublade_rot
        guid_ebene_6 (Union[Unset, str]): ebene_6
        mb_package_name (Union[Unset, str]):
        guid_writer (Union[Unset, str]): writer
        guid_email (Union[Unset, str]): EMAIL
        guid_video (Union[Unset, str]): video
        mb_icon_bmp (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_audio (Union[Unset, str]): audio
        guid_register_gruen (Union[Unset, str]): register_gruen
        guid_bmp (Union[Unset, str]): bmp
        guid_register_blau (Union[Unset, str]): register_blau
        guid_word (Union[Unset, str]): word
        mb_all_members (Union[Unset, str]):
        guid_support (Union[Unset, str]): support
        guid_scan_dokument (Union[Unset, str]): scan_dokument
        guid_adresse (Union[Unset, str]): adresse
        guid_besuchsberichte (Union[Unset, str]): besuchsberichte
        guid_kunden (Union[Unset, str]): kunden
        guid_kundengruppe (Union[Unset, str]): kundengruppe
        guid_chm_hilfe (Union[Unset, str]): chm_hilfe
        mb_all_jpg (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_excel (Union[Unset, str]): excel
        guid_register (Union[Unset, str]): register
        guid_ordner_rot (Union[Unset, str]): ordner_rot
        mb_ico (Union[Unset, str]):
        guid_projektarbeit (Union[Unset, str]): projektarbeit
        mb_icon_jpg (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_aktenkoffer (Union[Unset, str]): aktenkoffer
        guid_draw (Union[Unset, str]): draw
        guid_javascript (Union[Unset, str]): javascript
        mb_disabled_icon_member (Union[Unset, str]): Return file data of disabled icon in <code>checkoutSordType</code>.
        guid_autocad_dwg (Union[Unset, str]): autocad_dwg
        guid_autocad_dwf (Union[Unset, str]): autocad_dwf
        mb_png (Union[Unset, str]):
        guid_txt (Union[Unset, str]): txt
        guid_pdf (Union[Unset, str]): pdf
        guid_telefon (Union[Unset, str]): telefon
        guid_schriftverkehr (Union[Unset, str]): schriftverkehr
        max_document_types (Union[Unset, int]): Maximum number of document types (=746).
        mb_icons_jpg (Union[Unset, SordTypeZ]): <p>
            This class encapsulates the constants of <code>SordTypeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        guid_formularordner (Union[Unset, str]): formularordner
    """

    guid_calc: Union[Unset, str] = UNSET
    guid_firma: Union[Unset, str] = UNSET
    mb_icons_png: Union[Unset, "SordTypeZ"] = UNSET
    mb_all_bmp: Union[Unset, "SordTypeZ"] = UNSET
    max_folder_types: Union[Unset, int] = UNSET
    guid_einzelperson: Union[Unset, str] = UNSET
    guid_gif: Union[Unset, str] = UNSET
    guid_web_dokument: Union[Unset, str] = UNSET
    guid_dokument: Union[Unset, str] = UNSET
    guid_access: Union[Unset, str] = UNSET
    guid_ordner: Union[Unset, str] = UNSET
    guid_schrank: Union[Unset, str] = UNSET
    guid_register_gelb: Union[Unset, str] = UNSET
    guid_autocad_dxf: Union[Unset, str] = UNSET
    guid_workflowordner: Union[Unset, str] = UNSET
    mb_bmp: Union[Unset, str] = UNSET
    mb_no_icons: Union[Unset, "SordTypeZ"] = UNSET
    guid_register_rot: Union[Unset, str] = UNSET
    guid_visio: Union[Unset, str] = UNSET
    guid_xml: Union[Unset, str] = UNSET
    mb_jpg: Union[Unset, str] = UNSET
    guid_ordner_gelb: Union[Unset, str] = UNSET
    mb_icons_bmp: Union[Unset, "SordTypeZ"] = UNSET
    mb_workflow_icon_member: Union[Unset, str] = UNSET
    mb_icon_member: Union[Unset, str] = UNSET
    mb_icon_png: Union[Unset, "SordTypeZ"] = UNSET
    guid_akten_schublade: Union[Unset, str] = UNSET
    guid_powerpoint: Union[Unset, str] = UNSET
    guid_sord_type_icons: Union[Unset, str] = UNSET
    guid_zip: Union[Unset, str] = UNSET
    mb_all_png: Union[Unset, "SordTypeZ"] = UNSET
    guid_ordner_blau: Union[Unset, str] = UNSET
    guid_ebene_32: Union[Unset, str] = UNSET
    guid_png: Union[Unset, str] = UNSET
    mb_icons_ico: Union[Unset, "SordTypeZ"] = UNSET
    guid_auftragsbearbeitung: Union[Unset, str] = UNSET
    guid_ordner_gruen: Union[Unset, str] = UNSET
    guid_impress: Union[Unset, str] = UNSET
    mb_id_name_ext: Union[Unset, str] = UNSET
    mb_all_ico: Union[Unset, "SordTypeZ"] = UNSET
    guid_aktivitaeten: Union[Unset, str] = UNSET
    guid_web_archiv: Union[Unset, str] = UNSET
    mb_icon_ico: Union[Unset, "SordTypeZ"] = UNSET
    guid_bild: Union[Unset, str] = UNSET
    guid_ebene_5: Union[Unset, str] = UNSET
    guid_ebene_4: Union[Unset, str] = UNSET
    guid_akten_schublade_rot: Union[Unset, str] = UNSET
    guid_ebene_6: Union[Unset, str] = UNSET
    mb_package_name: Union[Unset, str] = UNSET
    guid_writer: Union[Unset, str] = UNSET
    guid_email: Union[Unset, str] = UNSET
    guid_video: Union[Unset, str] = UNSET
    mb_icon_bmp: Union[Unset, "SordTypeZ"] = UNSET
    guid_audio: Union[Unset, str] = UNSET
    guid_register_gruen: Union[Unset, str] = UNSET
    guid_bmp: Union[Unset, str] = UNSET
    guid_register_blau: Union[Unset, str] = UNSET
    guid_word: Union[Unset, str] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    guid_support: Union[Unset, str] = UNSET
    guid_scan_dokument: Union[Unset, str] = UNSET
    guid_adresse: Union[Unset, str] = UNSET
    guid_besuchsberichte: Union[Unset, str] = UNSET
    guid_kunden: Union[Unset, str] = UNSET
    guid_kundengruppe: Union[Unset, str] = UNSET
    guid_chm_hilfe: Union[Unset, str] = UNSET
    mb_all_jpg: Union[Unset, "SordTypeZ"] = UNSET
    guid_excel: Union[Unset, str] = UNSET
    guid_register: Union[Unset, str] = UNSET
    guid_ordner_rot: Union[Unset, str] = UNSET
    mb_ico: Union[Unset, str] = UNSET
    guid_projektarbeit: Union[Unset, str] = UNSET
    mb_icon_jpg: Union[Unset, "SordTypeZ"] = UNSET
    guid_aktenkoffer: Union[Unset, str] = UNSET
    guid_draw: Union[Unset, str] = UNSET
    guid_javascript: Union[Unset, str] = UNSET
    mb_disabled_icon_member: Union[Unset, str] = UNSET
    guid_autocad_dwg: Union[Unset, str] = UNSET
    guid_autocad_dwf: Union[Unset, str] = UNSET
    mb_png: Union[Unset, str] = UNSET
    guid_txt: Union[Unset, str] = UNSET
    guid_pdf: Union[Unset, str] = UNSET
    guid_telefon: Union[Unset, str] = UNSET
    guid_schriftverkehr: Union[Unset, str] = UNSET
    max_document_types: Union[Unset, int] = UNSET
    mb_icons_jpg: Union[Unset, "SordTypeZ"] = UNSET
    guid_formularordner: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guid_calc = self.guid_calc

        guid_firma = self.guid_firma

        mb_icons_png: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_png, Unset):
            mb_icons_png = self.mb_icons_png.to_dict()

        mb_all_bmp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_bmp, Unset):
            mb_all_bmp = self.mb_all_bmp.to_dict()

        max_folder_types = self.max_folder_types

        guid_einzelperson = self.guid_einzelperson

        guid_gif = self.guid_gif

        guid_web_dokument = self.guid_web_dokument

        guid_dokument = self.guid_dokument

        guid_access = self.guid_access

        guid_ordner = self.guid_ordner

        guid_schrank = self.guid_schrank

        guid_register_gelb = self.guid_register_gelb

        guid_autocad_dxf = self.guid_autocad_dxf

        guid_workflowordner = self.guid_workflowordner

        mb_bmp = self.mb_bmp

        mb_no_icons: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_no_icons, Unset):
            mb_no_icons = self.mb_no_icons.to_dict()

        guid_register_rot = self.guid_register_rot

        guid_visio = self.guid_visio

        guid_xml = self.guid_xml

        mb_jpg = self.mb_jpg

        guid_ordner_gelb = self.guid_ordner_gelb

        mb_icons_bmp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_bmp, Unset):
            mb_icons_bmp = self.mb_icons_bmp.to_dict()

        mb_workflow_icon_member = self.mb_workflow_icon_member

        mb_icon_member = self.mb_icon_member

        mb_icon_png: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_png, Unset):
            mb_icon_png = self.mb_icon_png.to_dict()

        guid_akten_schublade = self.guid_akten_schublade

        guid_powerpoint = self.guid_powerpoint

        guid_sord_type_icons = self.guid_sord_type_icons

        guid_zip = self.guid_zip

        mb_all_png: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_png, Unset):
            mb_all_png = self.mb_all_png.to_dict()

        guid_ordner_blau = self.guid_ordner_blau

        guid_ebene_32 = self.guid_ebene_32

        guid_png = self.guid_png

        mb_icons_ico: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_ico, Unset):
            mb_icons_ico = self.mb_icons_ico.to_dict()

        guid_auftragsbearbeitung = self.guid_auftragsbearbeitung

        guid_ordner_gruen = self.guid_ordner_gruen

        guid_impress = self.guid_impress

        mb_id_name_ext = self.mb_id_name_ext

        mb_all_ico: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_ico, Unset):
            mb_all_ico = self.mb_all_ico.to_dict()

        guid_aktivitaeten = self.guid_aktivitaeten

        guid_web_archiv = self.guid_web_archiv

        mb_icon_ico: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_ico, Unset):
            mb_icon_ico = self.mb_icon_ico.to_dict()

        guid_bild = self.guid_bild

        guid_ebene_5 = self.guid_ebene_5

        guid_ebene_4 = self.guid_ebene_4

        guid_akten_schublade_rot = self.guid_akten_schublade_rot

        guid_ebene_6 = self.guid_ebene_6

        mb_package_name = self.mb_package_name

        guid_writer = self.guid_writer

        guid_email = self.guid_email

        guid_video = self.guid_video

        mb_icon_bmp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_bmp, Unset):
            mb_icon_bmp = self.mb_icon_bmp.to_dict()

        guid_audio = self.guid_audio

        guid_register_gruen = self.guid_register_gruen

        guid_bmp = self.guid_bmp

        guid_register_blau = self.guid_register_blau

        guid_word = self.guid_word

        mb_all_members = self.mb_all_members

        guid_support = self.guid_support

        guid_scan_dokument = self.guid_scan_dokument

        guid_adresse = self.guid_adresse

        guid_besuchsberichte = self.guid_besuchsberichte

        guid_kunden = self.guid_kunden

        guid_kundengruppe = self.guid_kundengruppe

        guid_chm_hilfe = self.guid_chm_hilfe

        mb_all_jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all_jpg, Unset):
            mb_all_jpg = self.mb_all_jpg.to_dict()

        guid_excel = self.guid_excel

        guid_register = self.guid_register

        guid_ordner_rot = self.guid_ordner_rot

        mb_ico = self.mb_ico

        guid_projektarbeit = self.guid_projektarbeit

        mb_icon_jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icon_jpg, Unset):
            mb_icon_jpg = self.mb_icon_jpg.to_dict()

        guid_aktenkoffer = self.guid_aktenkoffer

        guid_draw = self.guid_draw

        guid_javascript = self.guid_javascript

        mb_disabled_icon_member = self.mb_disabled_icon_member

        guid_autocad_dwg = self.guid_autocad_dwg

        guid_autocad_dwf = self.guid_autocad_dwf

        mb_png = self.mb_png

        guid_txt = self.guid_txt

        guid_pdf = self.guid_pdf

        guid_telefon = self.guid_telefon

        guid_schriftverkehr = self.guid_schriftverkehr

        max_document_types = self.max_document_types

        mb_icons_jpg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_icons_jpg, Unset):
            mb_icons_jpg = self.mb_icons_jpg.to_dict()

        guid_formularordner = self.guid_formularordner

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guid_calc is not UNSET:
            field_dict["GUID_CALC"] = guid_calc
        if guid_firma is not UNSET:
            field_dict["GUID_FIRMA"] = guid_firma
        if mb_icons_png is not UNSET:
            field_dict["mbIconsPNG"] = mb_icons_png
        if mb_all_bmp is not UNSET:
            field_dict["mbAllBMP"] = mb_all_bmp
        if max_folder_types is not UNSET:
            field_dict["MAX_FOLDER_TYPES"] = max_folder_types
        if guid_einzelperson is not UNSET:
            field_dict["GUID_EINZELPERSON"] = guid_einzelperson
        if guid_gif is not UNSET:
            field_dict["GUID_GIF"] = guid_gif
        if guid_web_dokument is not UNSET:
            field_dict["GUID_WEB_DOKUMENT"] = guid_web_dokument
        if guid_dokument is not UNSET:
            field_dict["GUID_DOKUMENT"] = guid_dokument
        if guid_access is not UNSET:
            field_dict["GUID_ACCESS"] = guid_access
        if guid_ordner is not UNSET:
            field_dict["GUID_ORDNER"] = guid_ordner
        if guid_schrank is not UNSET:
            field_dict["GUID_SCHRANK"] = guid_schrank
        if guid_register_gelb is not UNSET:
            field_dict["GUID_REGISTER_GELB"] = guid_register_gelb
        if guid_autocad_dxf is not UNSET:
            field_dict["GUID_AUTOCAD_DXF"] = guid_autocad_dxf
        if guid_workflowordner is not UNSET:
            field_dict["GUID_WORKFLOWORDNER"] = guid_workflowordner
        if mb_bmp is not UNSET:
            field_dict["mbBMP"] = mb_bmp
        if mb_no_icons is not UNSET:
            field_dict["mbNoIcons"] = mb_no_icons
        if guid_register_rot is not UNSET:
            field_dict["GUID_REGISTER_ROT"] = guid_register_rot
        if guid_visio is not UNSET:
            field_dict["GUID_VISIO"] = guid_visio
        if guid_xml is not UNSET:
            field_dict["GUID_XML"] = guid_xml
        if mb_jpg is not UNSET:
            field_dict["mbJPG"] = mb_jpg
        if guid_ordner_gelb is not UNSET:
            field_dict["GUID_ORDNER_GELB"] = guid_ordner_gelb
        if mb_icons_bmp is not UNSET:
            field_dict["mbIconsBMP"] = mb_icons_bmp
        if mb_workflow_icon_member is not UNSET:
            field_dict["mbWorkflowIconMember"] = mb_workflow_icon_member
        if mb_icon_member is not UNSET:
            field_dict["mbIconMember"] = mb_icon_member
        if mb_icon_png is not UNSET:
            field_dict["mbIconPNG"] = mb_icon_png
        if guid_akten_schublade is not UNSET:
            field_dict["GUID_AKTEN_SCHUBLADE"] = guid_akten_schublade
        if guid_powerpoint is not UNSET:
            field_dict["GUID_POWERPOINT"] = guid_powerpoint
        if guid_sord_type_icons is not UNSET:
            field_dict["GUID_SORD_TYPE_ICONS"] = guid_sord_type_icons
        if guid_zip is not UNSET:
            field_dict["GUID_ZIP"] = guid_zip
        if mb_all_png is not UNSET:
            field_dict["mbAllPNG"] = mb_all_png
        if guid_ordner_blau is not UNSET:
            field_dict["GUID_ORDNER_BLAU"] = guid_ordner_blau
        if guid_ebene_32 is not UNSET:
            field_dict["GUID_EBENE_32"] = guid_ebene_32
        if guid_png is not UNSET:
            field_dict["GUID_PNG"] = guid_png
        if mb_icons_ico is not UNSET:
            field_dict["mbIconsICO"] = mb_icons_ico
        if guid_auftragsbearbeitung is not UNSET:
            field_dict["GUID_AUFTRAGSBEARBEITUNG"] = guid_auftragsbearbeitung
        if guid_ordner_gruen is not UNSET:
            field_dict["GUID_ORDNER_GRUEN"] = guid_ordner_gruen
        if guid_impress is not UNSET:
            field_dict["GUID_IMPRESS"] = guid_impress
        if mb_id_name_ext is not UNSET:
            field_dict["mbIdNameExt"] = mb_id_name_ext
        if mb_all_ico is not UNSET:
            field_dict["mbAllICO"] = mb_all_ico
        if guid_aktivitaeten is not UNSET:
            field_dict["GUID_AKTIVITAETEN"] = guid_aktivitaeten
        if guid_web_archiv is not UNSET:
            field_dict["GUID_WEB_ARCHIV"] = guid_web_archiv
        if mb_icon_ico is not UNSET:
            field_dict["mbIconICO"] = mb_icon_ico
        if guid_bild is not UNSET:
            field_dict["GUID_BILD"] = guid_bild
        if guid_ebene_5 is not UNSET:
            field_dict["GUID_EBENE_5"] = guid_ebene_5
        if guid_ebene_4 is not UNSET:
            field_dict["GUID_EBENE_4"] = guid_ebene_4
        if guid_akten_schublade_rot is not UNSET:
            field_dict["GUID_AKTEN_SCHUBLADE_ROT"] = guid_akten_schublade_rot
        if guid_ebene_6 is not UNSET:
            field_dict["GUID_EBENE_6"] = guid_ebene_6
        if mb_package_name is not UNSET:
            field_dict["mbPackageName"] = mb_package_name
        if guid_writer is not UNSET:
            field_dict["GUID_WRITER"] = guid_writer
        if guid_email is not UNSET:
            field_dict["GUID_EMAIL"] = guid_email
        if guid_video is not UNSET:
            field_dict["GUID_VIDEO"] = guid_video
        if mb_icon_bmp is not UNSET:
            field_dict["mbIconBMP"] = mb_icon_bmp
        if guid_audio is not UNSET:
            field_dict["GUID_AUDIO"] = guid_audio
        if guid_register_gruen is not UNSET:
            field_dict["GUID_REGISTER_GRUEN"] = guid_register_gruen
        if guid_bmp is not UNSET:
            field_dict["GUID_BMP"] = guid_bmp
        if guid_register_blau is not UNSET:
            field_dict["GUID_REGISTER_BLAU"] = guid_register_blau
        if guid_word is not UNSET:
            field_dict["GUID_WORD"] = guid_word
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if guid_support is not UNSET:
            field_dict["GUID_SUPPORT"] = guid_support
        if guid_scan_dokument is not UNSET:
            field_dict["GUID_SCAN_DOKUMENT"] = guid_scan_dokument
        if guid_adresse is not UNSET:
            field_dict["GUID_ADRESSE"] = guid_adresse
        if guid_besuchsberichte is not UNSET:
            field_dict["GUID_BESUCHSBERICHTE"] = guid_besuchsberichte
        if guid_kunden is not UNSET:
            field_dict["GUID_KUNDEN"] = guid_kunden
        if guid_kundengruppe is not UNSET:
            field_dict["GUID_KUNDENGRUPPE"] = guid_kundengruppe
        if guid_chm_hilfe is not UNSET:
            field_dict["GUID_CHM_HILFE"] = guid_chm_hilfe
        if mb_all_jpg is not UNSET:
            field_dict["mbAllJPG"] = mb_all_jpg
        if guid_excel is not UNSET:
            field_dict["GUID_EXCEL"] = guid_excel
        if guid_register is not UNSET:
            field_dict["GUID_REGISTER"] = guid_register
        if guid_ordner_rot is not UNSET:
            field_dict["GUID_ORDNER_ROT"] = guid_ordner_rot
        if mb_ico is not UNSET:
            field_dict["mbICO"] = mb_ico
        if guid_projektarbeit is not UNSET:
            field_dict["GUID_PROJEKTARBEIT"] = guid_projektarbeit
        if mb_icon_jpg is not UNSET:
            field_dict["mbIconJPG"] = mb_icon_jpg
        if guid_aktenkoffer is not UNSET:
            field_dict["GUID_AKTENKOFFER"] = guid_aktenkoffer
        if guid_draw is not UNSET:
            field_dict["GUID_DRAW"] = guid_draw
        if guid_javascript is not UNSET:
            field_dict["GUID_JAVASCRIPT"] = guid_javascript
        if mb_disabled_icon_member is not UNSET:
            field_dict["mbDisabledIconMember"] = mb_disabled_icon_member
        if guid_autocad_dwg is not UNSET:
            field_dict["GUID_AUTOCAD_DWG"] = guid_autocad_dwg
        if guid_autocad_dwf is not UNSET:
            field_dict["GUID_AUTOCAD_DWF"] = guid_autocad_dwf
        if mb_png is not UNSET:
            field_dict["mbPNG"] = mb_png
        if guid_txt is not UNSET:
            field_dict["GUID_TXT"] = guid_txt
        if guid_pdf is not UNSET:
            field_dict["GUID_PDF"] = guid_pdf
        if guid_telefon is not UNSET:
            field_dict["GUID_TELEFON"] = guid_telefon
        if guid_schriftverkehr is not UNSET:
            field_dict["GUID_SCHRIFTVERKEHR"] = guid_schriftverkehr
        if max_document_types is not UNSET:
            field_dict["MAX_DOCUMENT_TYPES"] = max_document_types
        if mb_icons_jpg is not UNSET:
            field_dict["mbIconsJPG"] = mb_icons_jpg
        if guid_formularordner is not UNSET:
            field_dict["GUID_FORMULARORDNER"] = guid_formularordner

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord_type_z import SordTypeZ

        d = src_dict.copy()
        guid_calc = d.pop("GUID_CALC", UNSET)

        guid_firma = d.pop("GUID_FIRMA", UNSET)

        _mb_icons_png = d.pop("mbIconsPNG", UNSET)
        mb_icons_png: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_png, Unset):
            mb_icons_png = UNSET
        else:
            mb_icons_png = SordTypeZ.from_dict(_mb_icons_png)

        _mb_all_bmp = d.pop("mbAllBMP", UNSET)
        mb_all_bmp: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_bmp, Unset):
            mb_all_bmp = UNSET
        else:
            mb_all_bmp = SordTypeZ.from_dict(_mb_all_bmp)

        max_folder_types = d.pop("MAX_FOLDER_TYPES", UNSET)

        guid_einzelperson = d.pop("GUID_EINZELPERSON", UNSET)

        guid_gif = d.pop("GUID_GIF", UNSET)

        guid_web_dokument = d.pop("GUID_WEB_DOKUMENT", UNSET)

        guid_dokument = d.pop("GUID_DOKUMENT", UNSET)

        guid_access = d.pop("GUID_ACCESS", UNSET)

        guid_ordner = d.pop("GUID_ORDNER", UNSET)

        guid_schrank = d.pop("GUID_SCHRANK", UNSET)

        guid_register_gelb = d.pop("GUID_REGISTER_GELB", UNSET)

        guid_autocad_dxf = d.pop("GUID_AUTOCAD_DXF", UNSET)

        guid_workflowordner = d.pop("GUID_WORKFLOWORDNER", UNSET)

        mb_bmp = d.pop("mbBMP", UNSET)

        _mb_no_icons = d.pop("mbNoIcons", UNSET)
        mb_no_icons: Union[Unset, SordTypeZ]
        if isinstance(_mb_no_icons, Unset):
            mb_no_icons = UNSET
        else:
            mb_no_icons = SordTypeZ.from_dict(_mb_no_icons)

        guid_register_rot = d.pop("GUID_REGISTER_ROT", UNSET)

        guid_visio = d.pop("GUID_VISIO", UNSET)

        guid_xml = d.pop("GUID_XML", UNSET)

        mb_jpg = d.pop("mbJPG", UNSET)

        guid_ordner_gelb = d.pop("GUID_ORDNER_GELB", UNSET)

        _mb_icons_bmp = d.pop("mbIconsBMP", UNSET)
        mb_icons_bmp: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_bmp, Unset):
            mb_icons_bmp = UNSET
        else:
            mb_icons_bmp = SordTypeZ.from_dict(_mb_icons_bmp)

        mb_workflow_icon_member = d.pop("mbWorkflowIconMember", UNSET)

        mb_icon_member = d.pop("mbIconMember", UNSET)

        _mb_icon_png = d.pop("mbIconPNG", UNSET)
        mb_icon_png: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_png, Unset):
            mb_icon_png = UNSET
        else:
            mb_icon_png = SordTypeZ.from_dict(_mb_icon_png)

        guid_akten_schublade = d.pop("GUID_AKTEN_SCHUBLADE", UNSET)

        guid_powerpoint = d.pop("GUID_POWERPOINT", UNSET)

        guid_sord_type_icons = d.pop("GUID_SORD_TYPE_ICONS", UNSET)

        guid_zip = d.pop("GUID_ZIP", UNSET)

        _mb_all_png = d.pop("mbAllPNG", UNSET)
        mb_all_png: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_png, Unset):
            mb_all_png = UNSET
        else:
            mb_all_png = SordTypeZ.from_dict(_mb_all_png)

        guid_ordner_blau = d.pop("GUID_ORDNER_BLAU", UNSET)

        guid_ebene_32 = d.pop("GUID_EBENE_32", UNSET)

        guid_png = d.pop("GUID_PNG", UNSET)

        _mb_icons_ico = d.pop("mbIconsICO", UNSET)
        mb_icons_ico: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_ico, Unset):
            mb_icons_ico = UNSET
        else:
            mb_icons_ico = SordTypeZ.from_dict(_mb_icons_ico)

        guid_auftragsbearbeitung = d.pop("GUID_AUFTRAGSBEARBEITUNG", UNSET)

        guid_ordner_gruen = d.pop("GUID_ORDNER_GRUEN", UNSET)

        guid_impress = d.pop("GUID_IMPRESS", UNSET)

        mb_id_name_ext = d.pop("mbIdNameExt", UNSET)

        _mb_all_ico = d.pop("mbAllICO", UNSET)
        mb_all_ico: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_ico, Unset):
            mb_all_ico = UNSET
        else:
            mb_all_ico = SordTypeZ.from_dict(_mb_all_ico)

        guid_aktivitaeten = d.pop("GUID_AKTIVITAETEN", UNSET)

        guid_web_archiv = d.pop("GUID_WEB_ARCHIV", UNSET)

        _mb_icon_ico = d.pop("mbIconICO", UNSET)
        mb_icon_ico: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_ico, Unset):
            mb_icon_ico = UNSET
        else:
            mb_icon_ico = SordTypeZ.from_dict(_mb_icon_ico)

        guid_bild = d.pop("GUID_BILD", UNSET)

        guid_ebene_5 = d.pop("GUID_EBENE_5", UNSET)

        guid_ebene_4 = d.pop("GUID_EBENE_4", UNSET)

        guid_akten_schublade_rot = d.pop("GUID_AKTEN_SCHUBLADE_ROT", UNSET)

        guid_ebene_6 = d.pop("GUID_EBENE_6", UNSET)

        mb_package_name = d.pop("mbPackageName", UNSET)

        guid_writer = d.pop("GUID_WRITER", UNSET)

        guid_email = d.pop("GUID_EMAIL", UNSET)

        guid_video = d.pop("GUID_VIDEO", UNSET)

        _mb_icon_bmp = d.pop("mbIconBMP", UNSET)
        mb_icon_bmp: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_bmp, Unset):
            mb_icon_bmp = UNSET
        else:
            mb_icon_bmp = SordTypeZ.from_dict(_mb_icon_bmp)

        guid_audio = d.pop("GUID_AUDIO", UNSET)

        guid_register_gruen = d.pop("GUID_REGISTER_GRUEN", UNSET)

        guid_bmp = d.pop("GUID_BMP", UNSET)

        guid_register_blau = d.pop("GUID_REGISTER_BLAU", UNSET)

        guid_word = d.pop("GUID_WORD", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        guid_support = d.pop("GUID_SUPPORT", UNSET)

        guid_scan_dokument = d.pop("GUID_SCAN_DOKUMENT", UNSET)

        guid_adresse = d.pop("GUID_ADRESSE", UNSET)

        guid_besuchsberichte = d.pop("GUID_BESUCHSBERICHTE", UNSET)

        guid_kunden = d.pop("GUID_KUNDEN", UNSET)

        guid_kundengruppe = d.pop("GUID_KUNDENGRUPPE", UNSET)

        guid_chm_hilfe = d.pop("GUID_CHM_HILFE", UNSET)

        _mb_all_jpg = d.pop("mbAllJPG", UNSET)
        mb_all_jpg: Union[Unset, SordTypeZ]
        if isinstance(_mb_all_jpg, Unset):
            mb_all_jpg = UNSET
        else:
            mb_all_jpg = SordTypeZ.from_dict(_mb_all_jpg)

        guid_excel = d.pop("GUID_EXCEL", UNSET)

        guid_register = d.pop("GUID_REGISTER", UNSET)

        guid_ordner_rot = d.pop("GUID_ORDNER_ROT", UNSET)

        mb_ico = d.pop("mbICO", UNSET)

        guid_projektarbeit = d.pop("GUID_PROJEKTARBEIT", UNSET)

        _mb_icon_jpg = d.pop("mbIconJPG", UNSET)
        mb_icon_jpg: Union[Unset, SordTypeZ]
        if isinstance(_mb_icon_jpg, Unset):
            mb_icon_jpg = UNSET
        else:
            mb_icon_jpg = SordTypeZ.from_dict(_mb_icon_jpg)

        guid_aktenkoffer = d.pop("GUID_AKTENKOFFER", UNSET)

        guid_draw = d.pop("GUID_DRAW", UNSET)

        guid_javascript = d.pop("GUID_JAVASCRIPT", UNSET)

        mb_disabled_icon_member = d.pop("mbDisabledIconMember", UNSET)

        guid_autocad_dwg = d.pop("GUID_AUTOCAD_DWG", UNSET)

        guid_autocad_dwf = d.pop("GUID_AUTOCAD_DWF", UNSET)

        mb_png = d.pop("mbPNG", UNSET)

        guid_txt = d.pop("GUID_TXT", UNSET)

        guid_pdf = d.pop("GUID_PDF", UNSET)

        guid_telefon = d.pop("GUID_TELEFON", UNSET)

        guid_schriftverkehr = d.pop("GUID_SCHRIFTVERKEHR", UNSET)

        max_document_types = d.pop("MAX_DOCUMENT_TYPES", UNSET)

        _mb_icons_jpg = d.pop("mbIconsJPG", UNSET)
        mb_icons_jpg: Union[Unset, SordTypeZ]
        if isinstance(_mb_icons_jpg, Unset):
            mb_icons_jpg = UNSET
        else:
            mb_icons_jpg = SordTypeZ.from_dict(_mb_icons_jpg)

        guid_formularordner = d.pop("GUID_FORMULARORDNER", UNSET)

        sord_type_c = cls(
            guid_calc=guid_calc,
            guid_firma=guid_firma,
            mb_icons_png=mb_icons_png,
            mb_all_bmp=mb_all_bmp,
            max_folder_types=max_folder_types,
            guid_einzelperson=guid_einzelperson,
            guid_gif=guid_gif,
            guid_web_dokument=guid_web_dokument,
            guid_dokument=guid_dokument,
            guid_access=guid_access,
            guid_ordner=guid_ordner,
            guid_schrank=guid_schrank,
            guid_register_gelb=guid_register_gelb,
            guid_autocad_dxf=guid_autocad_dxf,
            guid_workflowordner=guid_workflowordner,
            mb_bmp=mb_bmp,
            mb_no_icons=mb_no_icons,
            guid_register_rot=guid_register_rot,
            guid_visio=guid_visio,
            guid_xml=guid_xml,
            mb_jpg=mb_jpg,
            guid_ordner_gelb=guid_ordner_gelb,
            mb_icons_bmp=mb_icons_bmp,
            mb_workflow_icon_member=mb_workflow_icon_member,
            mb_icon_member=mb_icon_member,
            mb_icon_png=mb_icon_png,
            guid_akten_schublade=guid_akten_schublade,
            guid_powerpoint=guid_powerpoint,
            guid_sord_type_icons=guid_sord_type_icons,
            guid_zip=guid_zip,
            mb_all_png=mb_all_png,
            guid_ordner_blau=guid_ordner_blau,
            guid_ebene_32=guid_ebene_32,
            guid_png=guid_png,
            mb_icons_ico=mb_icons_ico,
            guid_auftragsbearbeitung=guid_auftragsbearbeitung,
            guid_ordner_gruen=guid_ordner_gruen,
            guid_impress=guid_impress,
            mb_id_name_ext=mb_id_name_ext,
            mb_all_ico=mb_all_ico,
            guid_aktivitaeten=guid_aktivitaeten,
            guid_web_archiv=guid_web_archiv,
            mb_icon_ico=mb_icon_ico,
            guid_bild=guid_bild,
            guid_ebene_5=guid_ebene_5,
            guid_ebene_4=guid_ebene_4,
            guid_akten_schublade_rot=guid_akten_schublade_rot,
            guid_ebene_6=guid_ebene_6,
            mb_package_name=mb_package_name,
            guid_writer=guid_writer,
            guid_email=guid_email,
            guid_video=guid_video,
            mb_icon_bmp=mb_icon_bmp,
            guid_audio=guid_audio,
            guid_register_gruen=guid_register_gruen,
            guid_bmp=guid_bmp,
            guid_register_blau=guid_register_blau,
            guid_word=guid_word,
            mb_all_members=mb_all_members,
            guid_support=guid_support,
            guid_scan_dokument=guid_scan_dokument,
            guid_adresse=guid_adresse,
            guid_besuchsberichte=guid_besuchsberichte,
            guid_kunden=guid_kunden,
            guid_kundengruppe=guid_kundengruppe,
            guid_chm_hilfe=guid_chm_hilfe,
            mb_all_jpg=mb_all_jpg,
            guid_excel=guid_excel,
            guid_register=guid_register,
            guid_ordner_rot=guid_ordner_rot,
            mb_ico=mb_ico,
            guid_projektarbeit=guid_projektarbeit,
            mb_icon_jpg=mb_icon_jpg,
            guid_aktenkoffer=guid_aktenkoffer,
            guid_draw=guid_draw,
            guid_javascript=guid_javascript,
            mb_disabled_icon_member=mb_disabled_icon_member,
            guid_autocad_dwg=guid_autocad_dwg,
            guid_autocad_dwf=guid_autocad_dwf,
            mb_png=mb_png,
            guid_txt=guid_txt,
            guid_pdf=guid_pdf,
            guid_telefon=guid_telefon,
            guid_schriftverkehr=guid_schriftverkehr,
            max_document_types=max_document_types,
            mb_icons_jpg=mb_icons_jpg,
            guid_formularordner=guid_formularordner,
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
