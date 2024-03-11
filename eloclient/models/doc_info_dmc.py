from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocInfoDMC")


@_attrs_define
class DocInfoDMC:
    """<p>
    Bit constants for members of DocInfoDM
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mb_id (Union[Unset, str]): DB column: docid
            mb_guid (Union[Unset, str]): DB column: docguid
            ln_guid (Union[Unset, int]): DB column: docguid
            mb_md_5 (Union[Unset, str]): DB column: md5
            ln_md_5 (Union[Unset, int]): DB column: md5
            mb_path_id (Union[Unset, str]): DB column: pathid
            mb_path_id_2 (Union[Unset, str]): DB column: pathid2
            mb_create_date_iso (Union[Unset, str]): DB column: createdate
            ln_create_date_iso (Union[Unset, int]): DB column: createdate
            mb_last_access_iso (Union[Unset, str]): DB column: lastaccess
            ln_last_access_iso (Union[Unset, int]): DB column: lastaccess
            mb_last_update_iso (Union[Unset, str]): DB column: lastupdate
            ln_last_update_iso (Union[Unset, int]): DB column: lastupdate
            mb_owner (Union[Unset, str]): DB column: owner
            mb_ext (Union[Unset, str]): DB column: ext
            ln_ext (Union[Unset, int]): DB column: ext
            mb_fclip (Union[Unset, str]): DB column: fclip
            ln_fclip (Union[Unset, int]): DB column: fclip
            mb_size (Union[Unset, str]): DB column: null
            mb_preview_size (Union[Unset, str]): DB column: null
            mb_size_orig (Union[Unset, str]): DB column: null
            mb_ext_orig (Union[Unset, str]): Member bit: Original file extension for encrypted documents DB column: extorig
            ln_ext_orig (Union[Unset, int]): Column length: Original file extension for encrypted documents DB column:
                extorig
            mb_encr_set (Union[Unset, str]): Member bit: Encryption set.
                DB column: cryptno
            mb_preview_ext (Union[Unset, str]): Member bit: Preview file extension.
                DB column: previewext
            ln_preview_ext (Union[Unset, int]): Column length: Preview file extension.
                DB column: previewext
            mb_fulltext_content_t_stamp (Union[Unset, str]): Member bit: Fulltext content timestamp DB column: fttstamp
            ln_fulltext_content_t_stamp (Union[Unset, int]): Column length: Fulltext content timestamp DB column: fttstamp
            mb_fulltext_content_size (Union[Unset, str]): Member bit: Fulltext content file size.
                DB column: ftsize
            mb_size_l (Union[Unset, str]): Member bit: Document file size.
                DB column: docsize
            ln_size_l (Union[Unset, int]): Column length: Document file size.
                DB column: docsize
            mb_size_orig_l (Union[Unset, str]): Member bit: Original file extension for encrypted documents DB column:
                docsizeorig
            ln_size_orig_l (Union[Unset, int]): Column length: Original file extension for encrypted documents DB column:
                docsizeorig
            mb_preview_size_l (Union[Unset, str]): Member bit: Size of preview file.
                DB column: previewsize
            ln_preview_size_l (Union[Unset, int]): Column length: Size of preview file.
                DB column: previewsize
            mb_rel_file_path (Union[Unset, str]): Member bit: Relative file path DB column: relfilepath
            ln_rel_file_path (Union[Unset, int]): Column length: Relative file path DB column: relfilepath
            mb_ft_ext (Union[Unset, str]): Member bit: Fulltext file extension.
                DB column: ftext
            ln_ft_ext (Union[Unset, int]): Column length: Fulltext file extension.
                DB column: ftext
            mb_preview_ext_orig (Union[Unset, str]): Member bit: Original preview file extension for encrypted previews.
                DB column: previewextorig
            ln_preview_ext_orig (Union[Unset, int]): Column length: Original preview file extension for encrypted previews.
                DB column: previewextorig
            mb_all_members (Union[Unset, str]): All valid member bits.
    """

    mb_id: Union[Unset, str] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    mb_md_5: Union[Unset, str] = UNSET
    ln_md_5: Union[Unset, int] = UNSET
    mb_path_id: Union[Unset, str] = UNSET
    mb_path_id_2: Union[Unset, str] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_last_access_iso: Union[Unset, str] = UNSET
    ln_last_access_iso: Union[Unset, int] = UNSET
    mb_last_update_iso: Union[Unset, str] = UNSET
    ln_last_update_iso: Union[Unset, int] = UNSET
    mb_owner: Union[Unset, str] = UNSET
    mb_ext: Union[Unset, str] = UNSET
    ln_ext: Union[Unset, int] = UNSET
    mb_fclip: Union[Unset, str] = UNSET
    ln_fclip: Union[Unset, int] = UNSET
    mb_size: Union[Unset, str] = UNSET
    mb_preview_size: Union[Unset, str] = UNSET
    mb_size_orig: Union[Unset, str] = UNSET
    mb_ext_orig: Union[Unset, str] = UNSET
    ln_ext_orig: Union[Unset, int] = UNSET
    mb_encr_set: Union[Unset, str] = UNSET
    mb_preview_ext: Union[Unset, str] = UNSET
    ln_preview_ext: Union[Unset, int] = UNSET
    mb_fulltext_content_t_stamp: Union[Unset, str] = UNSET
    ln_fulltext_content_t_stamp: Union[Unset, int] = UNSET
    mb_fulltext_content_size: Union[Unset, str] = UNSET
    mb_size_l: Union[Unset, str] = UNSET
    ln_size_l: Union[Unset, int] = UNSET
    mb_size_orig_l: Union[Unset, str] = UNSET
    ln_size_orig_l: Union[Unset, int] = UNSET
    mb_preview_size_l: Union[Unset, str] = UNSET
    ln_preview_size_l: Union[Unset, int] = UNSET
    mb_rel_file_path: Union[Unset, str] = UNSET
    ln_rel_file_path: Union[Unset, int] = UNSET
    mb_ft_ext: Union[Unset, str] = UNSET
    ln_ft_ext: Union[Unset, int] = UNSET
    mb_preview_ext_orig: Union[Unset, str] = UNSET
    ln_preview_ext_orig: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_id = self.mb_id
        mb_guid = self.mb_guid
        ln_guid = self.ln_guid
        mb_md_5 = self.mb_md_5
        ln_md_5 = self.ln_md_5
        mb_path_id = self.mb_path_id
        mb_path_id_2 = self.mb_path_id_2
        mb_create_date_iso = self.mb_create_date_iso
        ln_create_date_iso = self.ln_create_date_iso
        mb_last_access_iso = self.mb_last_access_iso
        ln_last_access_iso = self.ln_last_access_iso
        mb_last_update_iso = self.mb_last_update_iso
        ln_last_update_iso = self.ln_last_update_iso
        mb_owner = self.mb_owner
        mb_ext = self.mb_ext
        ln_ext = self.ln_ext
        mb_fclip = self.mb_fclip
        ln_fclip = self.ln_fclip
        mb_size = self.mb_size
        mb_preview_size = self.mb_preview_size
        mb_size_orig = self.mb_size_orig
        mb_ext_orig = self.mb_ext_orig
        ln_ext_orig = self.ln_ext_orig
        mb_encr_set = self.mb_encr_set
        mb_preview_ext = self.mb_preview_ext
        ln_preview_ext = self.ln_preview_ext
        mb_fulltext_content_t_stamp = self.mb_fulltext_content_t_stamp
        ln_fulltext_content_t_stamp = self.ln_fulltext_content_t_stamp
        mb_fulltext_content_size = self.mb_fulltext_content_size
        mb_size_l = self.mb_size_l
        ln_size_l = self.ln_size_l
        mb_size_orig_l = self.mb_size_orig_l
        ln_size_orig_l = self.ln_size_orig_l
        mb_preview_size_l = self.mb_preview_size_l
        ln_preview_size_l = self.ln_preview_size_l
        mb_rel_file_path = self.mb_rel_file_path
        ln_rel_file_path = self.ln_rel_file_path
        mb_ft_ext = self.mb_ft_ext
        ln_ft_ext = self.ln_ft_ext
        mb_preview_ext_orig = self.mb_preview_ext_orig
        ln_preview_ext_orig = self.ln_preview_ext_orig
        mb_all_members = self.mb_all_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if mb_md_5 is not UNSET:
            field_dict["mbMd5"] = mb_md_5
        if ln_md_5 is not UNSET:
            field_dict["lnMd5"] = ln_md_5
        if mb_path_id is not UNSET:
            field_dict["mbPathId"] = mb_path_id
        if mb_path_id_2 is not UNSET:
            field_dict["mbPathId2"] = mb_path_id_2
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_last_access_iso is not UNSET:
            field_dict["mbLastAccessIso"] = mb_last_access_iso
        if ln_last_access_iso is not UNSET:
            field_dict["lnLastAccessIso"] = ln_last_access_iso
        if mb_last_update_iso is not UNSET:
            field_dict["mbLastUpdateIso"] = mb_last_update_iso
        if ln_last_update_iso is not UNSET:
            field_dict["lnLastUpdateIso"] = ln_last_update_iso
        if mb_owner is not UNSET:
            field_dict["mbOwner"] = mb_owner
        if mb_ext is not UNSET:
            field_dict["mbExt"] = mb_ext
        if ln_ext is not UNSET:
            field_dict["lnExt"] = ln_ext
        if mb_fclip is not UNSET:
            field_dict["mbFclip"] = mb_fclip
        if ln_fclip is not UNSET:
            field_dict["lnFclip"] = ln_fclip
        if mb_size is not UNSET:
            field_dict["mbSize"] = mb_size
        if mb_preview_size is not UNSET:
            field_dict["mbPreviewSize"] = mb_preview_size
        if mb_size_orig is not UNSET:
            field_dict["mbSizeOrig"] = mb_size_orig
        if mb_ext_orig is not UNSET:
            field_dict["mbExtOrig"] = mb_ext_orig
        if ln_ext_orig is not UNSET:
            field_dict["lnExtOrig"] = ln_ext_orig
        if mb_encr_set is not UNSET:
            field_dict["mbEncrSet"] = mb_encr_set
        if mb_preview_ext is not UNSET:
            field_dict["mbPreviewExt"] = mb_preview_ext
        if ln_preview_ext is not UNSET:
            field_dict["lnPreviewExt"] = ln_preview_ext
        if mb_fulltext_content_t_stamp is not UNSET:
            field_dict["mbFulltextContentTStamp"] = mb_fulltext_content_t_stamp
        if ln_fulltext_content_t_stamp is not UNSET:
            field_dict["lnFulltextContentTStamp"] = ln_fulltext_content_t_stamp
        if mb_fulltext_content_size is not UNSET:
            field_dict["mbFulltextContentSize"] = mb_fulltext_content_size
        if mb_size_l is not UNSET:
            field_dict["mbSizeL"] = mb_size_l
        if ln_size_l is not UNSET:
            field_dict["lnSizeL"] = ln_size_l
        if mb_size_orig_l is not UNSET:
            field_dict["mbSizeOrigL"] = mb_size_orig_l
        if ln_size_orig_l is not UNSET:
            field_dict["lnSizeOrigL"] = ln_size_orig_l
        if mb_preview_size_l is not UNSET:
            field_dict["mbPreviewSizeL"] = mb_preview_size_l
        if ln_preview_size_l is not UNSET:
            field_dict["lnPreviewSizeL"] = ln_preview_size_l
        if mb_rel_file_path is not UNSET:
            field_dict["mbRelFilePath"] = mb_rel_file_path
        if ln_rel_file_path is not UNSET:
            field_dict["lnRelFilePath"] = ln_rel_file_path
        if mb_ft_ext is not UNSET:
            field_dict["mbFtExt"] = mb_ft_ext
        if ln_ft_ext is not UNSET:
            field_dict["lnFtExt"] = ln_ft_ext
        if mb_preview_ext_orig is not UNSET:
            field_dict["mbPreviewExtOrig"] = mb_preview_ext_orig
        if ln_preview_ext_orig is not UNSET:
            field_dict["lnPreviewExtOrig"] = ln_preview_ext_orig
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_id = d.pop("mbId", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        mb_md_5 = d.pop("mbMd5", UNSET)

        ln_md_5 = d.pop("lnMd5", UNSET)

        mb_path_id = d.pop("mbPathId", UNSET)

        mb_path_id_2 = d.pop("mbPathId2", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_last_access_iso = d.pop("mbLastAccessIso", UNSET)

        ln_last_access_iso = d.pop("lnLastAccessIso", UNSET)

        mb_last_update_iso = d.pop("mbLastUpdateIso", UNSET)

        ln_last_update_iso = d.pop("lnLastUpdateIso", UNSET)

        mb_owner = d.pop("mbOwner", UNSET)

        mb_ext = d.pop("mbExt", UNSET)

        ln_ext = d.pop("lnExt", UNSET)

        mb_fclip = d.pop("mbFclip", UNSET)

        ln_fclip = d.pop("lnFclip", UNSET)

        mb_size = d.pop("mbSize", UNSET)

        mb_preview_size = d.pop("mbPreviewSize", UNSET)

        mb_size_orig = d.pop("mbSizeOrig", UNSET)

        mb_ext_orig = d.pop("mbExtOrig", UNSET)

        ln_ext_orig = d.pop("lnExtOrig", UNSET)

        mb_encr_set = d.pop("mbEncrSet", UNSET)

        mb_preview_ext = d.pop("mbPreviewExt", UNSET)

        ln_preview_ext = d.pop("lnPreviewExt", UNSET)

        mb_fulltext_content_t_stamp = d.pop("mbFulltextContentTStamp", UNSET)

        ln_fulltext_content_t_stamp = d.pop("lnFulltextContentTStamp", UNSET)

        mb_fulltext_content_size = d.pop("mbFulltextContentSize", UNSET)

        mb_size_l = d.pop("mbSizeL", UNSET)

        ln_size_l = d.pop("lnSizeL", UNSET)

        mb_size_orig_l = d.pop("mbSizeOrigL", UNSET)

        ln_size_orig_l = d.pop("lnSizeOrigL", UNSET)

        mb_preview_size_l = d.pop("mbPreviewSizeL", UNSET)

        ln_preview_size_l = d.pop("lnPreviewSizeL", UNSET)

        mb_rel_file_path = d.pop("mbRelFilePath", UNSET)

        ln_rel_file_path = d.pop("lnRelFilePath", UNSET)

        mb_ft_ext = d.pop("mbFtExt", UNSET)

        ln_ft_ext = d.pop("lnFtExt", UNSET)

        mb_preview_ext_orig = d.pop("mbPreviewExtOrig", UNSET)

        ln_preview_ext_orig = d.pop("lnPreviewExtOrig", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        doc_info_dmc = cls(
            mb_id=mb_id,
            mb_guid=mb_guid,
            ln_guid=ln_guid,
            mb_md_5=mb_md_5,
            ln_md_5=ln_md_5,
            mb_path_id=mb_path_id,
            mb_path_id_2=mb_path_id_2,
            mb_create_date_iso=mb_create_date_iso,
            ln_create_date_iso=ln_create_date_iso,
            mb_last_access_iso=mb_last_access_iso,
            ln_last_access_iso=ln_last_access_iso,
            mb_last_update_iso=mb_last_update_iso,
            ln_last_update_iso=ln_last_update_iso,
            mb_owner=mb_owner,
            mb_ext=mb_ext,
            ln_ext=ln_ext,
            mb_fclip=mb_fclip,
            ln_fclip=ln_fclip,
            mb_size=mb_size,
            mb_preview_size=mb_preview_size,
            mb_size_orig=mb_size_orig,
            mb_ext_orig=mb_ext_orig,
            ln_ext_orig=ln_ext_orig,
            mb_encr_set=mb_encr_set,
            mb_preview_ext=mb_preview_ext,
            ln_preview_ext=ln_preview_ext,
            mb_fulltext_content_t_stamp=mb_fulltext_content_t_stamp,
            ln_fulltext_content_t_stamp=ln_fulltext_content_t_stamp,
            mb_fulltext_content_size=mb_fulltext_content_size,
            mb_size_l=mb_size_l,
            ln_size_l=ln_size_l,
            mb_size_orig_l=mb_size_orig_l,
            ln_size_orig_l=ln_size_orig_l,
            mb_preview_size_l=mb_preview_size_l,
            ln_preview_size_l=ln_preview_size_l,
            mb_rel_file_path=mb_rel_file_path,
            ln_rel_file_path=ln_rel_file_path,
            mb_ft_ext=mb_ft_ext,
            ln_ft_ext=ln_ft_ext,
            mb_preview_ext_orig=mb_preview_ext_orig,
            ln_preview_ext_orig=ln_preview_ext_orig,
            mb_all_members=mb_all_members,
        )

        doc_info_dmc.additional_properties = d
        return doc_info_dmc

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
