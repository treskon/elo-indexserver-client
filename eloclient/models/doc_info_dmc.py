from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocInfoDMC")


@_attrs_define
class DocInfoDMC:
    """<p>Bit constants for members of DocInfoDM</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_rel_file_path (Union[Unset, str]): Member bit: Relative file path
                DB column: relfilepath
            ln_fulltext_content_t_stamp (Union[Unset, int]): Column length: Fulltext content timestamp
                DB column: fttstamp
            mb_md_5 (Union[Unset, str]): DB column: md5
            mb_preview_size_l (Union[Unset, str]): Member bit: Size of preview file. Is 0, if there is no preview file
                assigned.
                Is -1, if preview creation
                 DB column: previewsize
            mb_path_id (Union[Unset, str]): DB column: pathid
            ln_fclip (Union[Unset, int]): DB column: fclip
            mb_ft_ext (Union[Unset, str]): Member bit: Fulltext file extension.
                DB column: ftext
            mb_owner (Union[Unset, str]): DB column: owner
            ln_guid (Union[Unset, int]): DB column: docguid
            ln_size_l (Union[Unset, int]): Column length: Document file size.
                DB column: docsize
            ln_create_date_iso (Union[Unset, int]): DB column: createdate
            mb_size_l (Union[Unset, str]): Member bit: Document file size.
                DB column: docsize
            mb_encr_set (Union[Unset, str]): Member bit: Encryption set.
                DB column: cryptno
            ln_preview_ext (Union[Unset, int]): Column length: Preview file extension.
                DB column: previewext
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_last_access_iso (Union[Unset, str]): DB column: lastaccess
            ln_ext (Union[Unset, int]): DB column: ext
            ln_ext_orig (Union[Unset, int]): Column length: Original file extension for encrypted documents
                DB column: extorig
            mb_size_orig (Union[Unset, str]): DB column: null
            ln_preview_ext_orig (Union[Unset, int]): Column length: Original preview file extension for encrypted previews.
                DB column: previewextorig
            ln_last_access_iso (Union[Unset, int]): DB column: lastaccess
            mb_path_id_2 (Union[Unset, str]): DB column: pathid2
            mb_ext_orig (Union[Unset, str]): Member bit: Original file extension for encrypted documents
                DB column: extorig
            mb_ext (Union[Unset, str]): DB column: ext
            mb_fulltext_content_t_stamp (Union[Unset, str]): Member bit: Fulltext content timestamp
                DB column: fttstamp
            mb_id (Union[Unset, str]): DB column: docid
            mb_create_date_iso (Union[Unset, str]): DB column: createdate
            mb_preview_ext_orig (Union[Unset, str]): Member bit: Original preview file extension for encrypted previews.
                DB column: previewextorig
            ln_preview_size_l (Union[Unset, int]): Column length: Size of preview file. Is 0, if there is no preview file
                assigned.
                Is -1, if preview creation
                 DB column: previewsize
            mb_preview_size (Union[Unset, str]): DB column: null
            mb_fclip (Union[Unset, str]): DB column: fclip
            mb_preview_ext (Union[Unset, str]): Member bit: Preview file extension.
                DB column: previewext
            ln_rel_file_path (Union[Unset, int]): Column length: Relative file path
                DB column: relfilepath
            mb_fulltext_content_size (Union[Unset, str]): Member bit: Fulltext content file size.
                Since the fulltext content file is usually stored in UTF-8
                 DB column: ftsize
            ln_ft_ext (Union[Unset, int]): Column length: Fulltext file extension.
                DB column: ftext
            mb_guid (Union[Unset, str]): DB column: docguid
            ln_md_5 (Union[Unset, int]): DB column: md5
            mb_size (Union[Unset, str]): DB column: null
            mb_size_orig_l (Union[Unset, str]): Member bit: Original file extension for encrypted documents
                DB column: docsizeorig
            ln_size_orig_l (Union[Unset, int]): Column length: Original file extension for encrypted documents
                DB column: docsizeorig
            mb_last_update_iso (Union[Unset, str]): DB column: lastupdate
            ln_last_update_iso (Union[Unset, int]): DB column: lastupdate
    """

    mb_rel_file_path: Union[Unset, str] = UNSET
    ln_fulltext_content_t_stamp: Union[Unset, int] = UNSET
    mb_md_5: Union[Unset, str] = UNSET
    mb_preview_size_l: Union[Unset, str] = UNSET
    mb_path_id: Union[Unset, str] = UNSET
    ln_fclip: Union[Unset, int] = UNSET
    mb_ft_ext: Union[Unset, str] = UNSET
    mb_owner: Union[Unset, str] = UNSET
    ln_guid: Union[Unset, int] = UNSET
    ln_size_l: Union[Unset, int] = UNSET
    ln_create_date_iso: Union[Unset, int] = UNSET
    mb_size_l: Union[Unset, str] = UNSET
    mb_encr_set: Union[Unset, str] = UNSET
    ln_preview_ext: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_last_access_iso: Union[Unset, str] = UNSET
    ln_ext: Union[Unset, int] = UNSET
    ln_ext_orig: Union[Unset, int] = UNSET
    mb_size_orig: Union[Unset, str] = UNSET
    ln_preview_ext_orig: Union[Unset, int] = UNSET
    ln_last_access_iso: Union[Unset, int] = UNSET
    mb_path_id_2: Union[Unset, str] = UNSET
    mb_ext_orig: Union[Unset, str] = UNSET
    mb_ext: Union[Unset, str] = UNSET
    mb_fulltext_content_t_stamp: Union[Unset, str] = UNSET
    mb_id: Union[Unset, str] = UNSET
    mb_create_date_iso: Union[Unset, str] = UNSET
    mb_preview_ext_orig: Union[Unset, str] = UNSET
    ln_preview_size_l: Union[Unset, int] = UNSET
    mb_preview_size: Union[Unset, str] = UNSET
    mb_fclip: Union[Unset, str] = UNSET
    mb_preview_ext: Union[Unset, str] = UNSET
    ln_rel_file_path: Union[Unset, int] = UNSET
    mb_fulltext_content_size: Union[Unset, str] = UNSET
    ln_ft_ext: Union[Unset, int] = UNSET
    mb_guid: Union[Unset, str] = UNSET
    ln_md_5: Union[Unset, int] = UNSET
    mb_size: Union[Unset, str] = UNSET
    mb_size_orig_l: Union[Unset, str] = UNSET
    ln_size_orig_l: Union[Unset, int] = UNSET
    mb_last_update_iso: Union[Unset, str] = UNSET
    ln_last_update_iso: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_rel_file_path = self.mb_rel_file_path

        ln_fulltext_content_t_stamp = self.ln_fulltext_content_t_stamp

        mb_md_5 = self.mb_md_5

        mb_preview_size_l = self.mb_preview_size_l

        mb_path_id = self.mb_path_id

        ln_fclip = self.ln_fclip

        mb_ft_ext = self.mb_ft_ext

        mb_owner = self.mb_owner

        ln_guid = self.ln_guid

        ln_size_l = self.ln_size_l

        ln_create_date_iso = self.ln_create_date_iso

        mb_size_l = self.mb_size_l

        mb_encr_set = self.mb_encr_set

        ln_preview_ext = self.ln_preview_ext

        mb_all_members = self.mb_all_members

        mb_last_access_iso = self.mb_last_access_iso

        ln_ext = self.ln_ext

        ln_ext_orig = self.ln_ext_orig

        mb_size_orig = self.mb_size_orig

        ln_preview_ext_orig = self.ln_preview_ext_orig

        ln_last_access_iso = self.ln_last_access_iso

        mb_path_id_2 = self.mb_path_id_2

        mb_ext_orig = self.mb_ext_orig

        mb_ext = self.mb_ext

        mb_fulltext_content_t_stamp = self.mb_fulltext_content_t_stamp

        mb_id = self.mb_id

        mb_create_date_iso = self.mb_create_date_iso

        mb_preview_ext_orig = self.mb_preview_ext_orig

        ln_preview_size_l = self.ln_preview_size_l

        mb_preview_size = self.mb_preview_size

        mb_fclip = self.mb_fclip

        mb_preview_ext = self.mb_preview_ext

        ln_rel_file_path = self.ln_rel_file_path

        mb_fulltext_content_size = self.mb_fulltext_content_size

        ln_ft_ext = self.ln_ft_ext

        mb_guid = self.mb_guid

        ln_md_5 = self.ln_md_5

        mb_size = self.mb_size

        mb_size_orig_l = self.mb_size_orig_l

        ln_size_orig_l = self.ln_size_orig_l

        mb_last_update_iso = self.mb_last_update_iso

        ln_last_update_iso = self.ln_last_update_iso

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_rel_file_path is not UNSET:
            field_dict["mbRelFilePath"] = mb_rel_file_path
        if ln_fulltext_content_t_stamp is not UNSET:
            field_dict["lnFulltextContentTStamp"] = ln_fulltext_content_t_stamp
        if mb_md_5 is not UNSET:
            field_dict["mbMd5"] = mb_md_5
        if mb_preview_size_l is not UNSET:
            field_dict["mbPreviewSizeL"] = mb_preview_size_l
        if mb_path_id is not UNSET:
            field_dict["mbPathId"] = mb_path_id
        if ln_fclip is not UNSET:
            field_dict["lnFclip"] = ln_fclip
        if mb_ft_ext is not UNSET:
            field_dict["mbFtExt"] = mb_ft_ext
        if mb_owner is not UNSET:
            field_dict["mbOwner"] = mb_owner
        if ln_guid is not UNSET:
            field_dict["lnGuid"] = ln_guid
        if ln_size_l is not UNSET:
            field_dict["lnSizeL"] = ln_size_l
        if ln_create_date_iso is not UNSET:
            field_dict["lnCreateDateIso"] = ln_create_date_iso
        if mb_size_l is not UNSET:
            field_dict["mbSizeL"] = mb_size_l
        if mb_encr_set is not UNSET:
            field_dict["mbEncrSet"] = mb_encr_set
        if ln_preview_ext is not UNSET:
            field_dict["lnPreviewExt"] = ln_preview_ext
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_last_access_iso is not UNSET:
            field_dict["mbLastAccessIso"] = mb_last_access_iso
        if ln_ext is not UNSET:
            field_dict["lnExt"] = ln_ext
        if ln_ext_orig is not UNSET:
            field_dict["lnExtOrig"] = ln_ext_orig
        if mb_size_orig is not UNSET:
            field_dict["mbSizeOrig"] = mb_size_orig
        if ln_preview_ext_orig is not UNSET:
            field_dict["lnPreviewExtOrig"] = ln_preview_ext_orig
        if ln_last_access_iso is not UNSET:
            field_dict["lnLastAccessIso"] = ln_last_access_iso
        if mb_path_id_2 is not UNSET:
            field_dict["mbPathId2"] = mb_path_id_2
        if mb_ext_orig is not UNSET:
            field_dict["mbExtOrig"] = mb_ext_orig
        if mb_ext is not UNSET:
            field_dict["mbExt"] = mb_ext
        if mb_fulltext_content_t_stamp is not UNSET:
            field_dict["mbFulltextContentTStamp"] = mb_fulltext_content_t_stamp
        if mb_id is not UNSET:
            field_dict["mbId"] = mb_id
        if mb_create_date_iso is not UNSET:
            field_dict["mbCreateDateIso"] = mb_create_date_iso
        if mb_preview_ext_orig is not UNSET:
            field_dict["mbPreviewExtOrig"] = mb_preview_ext_orig
        if ln_preview_size_l is not UNSET:
            field_dict["lnPreviewSizeL"] = ln_preview_size_l
        if mb_preview_size is not UNSET:
            field_dict["mbPreviewSize"] = mb_preview_size
        if mb_fclip is not UNSET:
            field_dict["mbFclip"] = mb_fclip
        if mb_preview_ext is not UNSET:
            field_dict["mbPreviewExt"] = mb_preview_ext
        if ln_rel_file_path is not UNSET:
            field_dict["lnRelFilePath"] = ln_rel_file_path
        if mb_fulltext_content_size is not UNSET:
            field_dict["mbFulltextContentSize"] = mb_fulltext_content_size
        if ln_ft_ext is not UNSET:
            field_dict["lnFtExt"] = ln_ft_ext
        if mb_guid is not UNSET:
            field_dict["mbGuid"] = mb_guid
        if ln_md_5 is not UNSET:
            field_dict["lnMd5"] = ln_md_5
        if mb_size is not UNSET:
            field_dict["mbSize"] = mb_size
        if mb_size_orig_l is not UNSET:
            field_dict["mbSizeOrigL"] = mb_size_orig_l
        if ln_size_orig_l is not UNSET:
            field_dict["lnSizeOrigL"] = ln_size_orig_l
        if mb_last_update_iso is not UNSET:
            field_dict["mbLastUpdateIso"] = mb_last_update_iso
        if ln_last_update_iso is not UNSET:
            field_dict["lnLastUpdateIso"] = ln_last_update_iso

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_rel_file_path = d.pop("mbRelFilePath", UNSET)

        ln_fulltext_content_t_stamp = d.pop("lnFulltextContentTStamp", UNSET)

        mb_md_5 = d.pop("mbMd5", UNSET)

        mb_preview_size_l = d.pop("mbPreviewSizeL", UNSET)

        mb_path_id = d.pop("mbPathId", UNSET)

        ln_fclip = d.pop("lnFclip", UNSET)

        mb_ft_ext = d.pop("mbFtExt", UNSET)

        mb_owner = d.pop("mbOwner", UNSET)

        ln_guid = d.pop("lnGuid", UNSET)

        ln_size_l = d.pop("lnSizeL", UNSET)

        ln_create_date_iso = d.pop("lnCreateDateIso", UNSET)

        mb_size_l = d.pop("mbSizeL", UNSET)

        mb_encr_set = d.pop("mbEncrSet", UNSET)

        ln_preview_ext = d.pop("lnPreviewExt", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_last_access_iso = d.pop("mbLastAccessIso", UNSET)

        ln_ext = d.pop("lnExt", UNSET)

        ln_ext_orig = d.pop("lnExtOrig", UNSET)

        mb_size_orig = d.pop("mbSizeOrig", UNSET)

        ln_preview_ext_orig = d.pop("lnPreviewExtOrig", UNSET)

        ln_last_access_iso = d.pop("lnLastAccessIso", UNSET)

        mb_path_id_2 = d.pop("mbPathId2", UNSET)

        mb_ext_orig = d.pop("mbExtOrig", UNSET)

        mb_ext = d.pop("mbExt", UNSET)

        mb_fulltext_content_t_stamp = d.pop("mbFulltextContentTStamp", UNSET)

        mb_id = d.pop("mbId", UNSET)

        mb_create_date_iso = d.pop("mbCreateDateIso", UNSET)

        mb_preview_ext_orig = d.pop("mbPreviewExtOrig", UNSET)

        ln_preview_size_l = d.pop("lnPreviewSizeL", UNSET)

        mb_preview_size = d.pop("mbPreviewSize", UNSET)

        mb_fclip = d.pop("mbFclip", UNSET)

        mb_preview_ext = d.pop("mbPreviewExt", UNSET)

        ln_rel_file_path = d.pop("lnRelFilePath", UNSET)

        mb_fulltext_content_size = d.pop("mbFulltextContentSize", UNSET)

        ln_ft_ext = d.pop("lnFtExt", UNSET)

        mb_guid = d.pop("mbGuid", UNSET)

        ln_md_5 = d.pop("lnMd5", UNSET)

        mb_size = d.pop("mbSize", UNSET)

        mb_size_orig_l = d.pop("mbSizeOrigL", UNSET)

        ln_size_orig_l = d.pop("lnSizeOrigL", UNSET)

        mb_last_update_iso = d.pop("mbLastUpdateIso", UNSET)

        ln_last_update_iso = d.pop("lnLastUpdateIso", UNSET)

        doc_info_dmc = cls(
            mb_rel_file_path=mb_rel_file_path,
            ln_fulltext_content_t_stamp=ln_fulltext_content_t_stamp,
            mb_md_5=mb_md_5,
            mb_preview_size_l=mb_preview_size_l,
            mb_path_id=mb_path_id,
            ln_fclip=ln_fclip,
            mb_ft_ext=mb_ft_ext,
            mb_owner=mb_owner,
            ln_guid=ln_guid,
            ln_size_l=ln_size_l,
            ln_create_date_iso=ln_create_date_iso,
            mb_size_l=mb_size_l,
            mb_encr_set=mb_encr_set,
            ln_preview_ext=ln_preview_ext,
            mb_all_members=mb_all_members,
            mb_last_access_iso=mb_last_access_iso,
            ln_ext=ln_ext,
            ln_ext_orig=ln_ext_orig,
            mb_size_orig=mb_size_orig,
            ln_preview_ext_orig=ln_preview_ext_orig,
            ln_last_access_iso=ln_last_access_iso,
            mb_path_id_2=mb_path_id_2,
            mb_ext_orig=mb_ext_orig,
            mb_ext=mb_ext,
            mb_fulltext_content_t_stamp=mb_fulltext_content_t_stamp,
            mb_id=mb_id,
            mb_create_date_iso=mb_create_date_iso,
            mb_preview_ext_orig=mb_preview_ext_orig,
            ln_preview_size_l=ln_preview_size_l,
            mb_preview_size=mb_preview_size,
            mb_fclip=mb_fclip,
            mb_preview_ext=mb_preview_ext,
            ln_rel_file_path=ln_rel_file_path,
            mb_fulltext_content_size=mb_fulltext_content_size,
            ln_ft_ext=ln_ft_ext,
            mb_guid=mb_guid,
            ln_md_5=ln_md_5,
            mb_size=mb_size,
            mb_size_orig_l=mb_size_orig_l,
            ln_size_orig_l=ln_size_orig_l,
            mb_last_update_iso=mb_last_update_iso,
            ln_last_update_iso=ln_last_update_iso,
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
