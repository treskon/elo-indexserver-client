from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocInfoDM")


@_attrs_define
class DocInfoDM:
    """<p>
    Document information table of DM. For performance reason directly read by IX
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            id (Union[Unset, int]): Document version ID.
                DB column: docid
            guid (Union[Unset, str]): Document GUID.
                DB column: docguid
            size (Union[Unset, int]): File size.
                DB column: docsize
            md5 (Union[Unset, str]): MD5 hash.
                DB column: md5
            path_id (Union[Unset, int]): Storage path ID DB column: pathid
            path_id_2 (Union[Unset, int]): reserved DB column: pathid2
            create_date_iso (Union[Unset, str]): Create date ISO.
                DB column: createdate
            last_access_iso (Union[Unset, str]): Last access date ISO.
                DB column: lastaccess
            last_update_iso (Union[Unset, str]): Last update date ISO.
                DB column: lastupdate
            owner (Union[Unset, int]): User ID.
                DB column: owner
            ext (Union[Unset, str]): File extension DB column: ext
            fclip (Union[Unset, str]): reserved DB column: fclip
            ext_orig (Union[Unset, str]): Original file extension for encrypted documents
            size_orig (Union[Unset, int]): Original file size for encrypted documents
            encr_set (Union[Unset, int]): Encryption set.
            preview_size (Union[Unset, int]): Size of preview file. Is 0, if there is no preview file assigned. Is -1, if
                preview creation has failed.
            preview_ext (Union[Unset, str]): Preview file extension.
            fulltext_content_t_stamp (Union[Unset, str]): Fulltext content timestamp
            fulltext_content_size (Union[Unset, int]): Fulltext content file size.
                Since the fulltext content file is usually stored in UTF-8 encoding, the file size
                 might be different from the number of characters.
            size_l (Union[Unset, str]): Document file size.
            size_orig_l (Union[Unset, str]): Original file extension for encrypted documents
            preview_size_l (Union[Unset, str]): Size of preview file. Is 0, if there is no preview file assigned. Is -1, if
                preview creation has failed.
            rel_file_path (Union[Unset, str]): Relative file path
            ft_ext (Union[Unset, str]): Fulltext file extension.
            preview_ext_orig (Union[Unset, str]): Original preview file extension for encrypted previews.
    """

    id: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    md5: Union[Unset, str] = UNSET
    path_id: Union[Unset, int] = UNSET
    path_id_2: Union[Unset, int] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    last_access_iso: Union[Unset, str] = UNSET
    last_update_iso: Union[Unset, str] = UNSET
    owner: Union[Unset, int] = UNSET
    ext: Union[Unset, str] = UNSET
    fclip: Union[Unset, str] = UNSET
    ext_orig: Union[Unset, str] = UNSET
    size_orig: Union[Unset, int] = UNSET
    encr_set: Union[Unset, int] = UNSET
    preview_size: Union[Unset, int] = UNSET
    preview_ext: Union[Unset, str] = UNSET
    fulltext_content_t_stamp: Union[Unset, str] = UNSET
    fulltext_content_size: Union[Unset, int] = UNSET
    size_l: Union[Unset, str] = UNSET
    size_orig_l: Union[Unset, str] = UNSET
    preview_size_l: Union[Unset, str] = UNSET
    rel_file_path: Union[Unset, str] = UNSET
    ft_ext: Union[Unset, str] = UNSET
    preview_ext_orig: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        guid = self.guid
        size = self.size
        md5 = self.md5
        path_id = self.path_id
        path_id_2 = self.path_id_2
        create_date_iso = self.create_date_iso
        last_access_iso = self.last_access_iso
        last_update_iso = self.last_update_iso
        owner = self.owner
        ext = self.ext
        fclip = self.fclip
        ext_orig = self.ext_orig
        size_orig = self.size_orig
        encr_set = self.encr_set
        preview_size = self.preview_size
        preview_ext = self.preview_ext
        fulltext_content_t_stamp = self.fulltext_content_t_stamp
        fulltext_content_size = self.fulltext_content_size
        size_l = self.size_l
        size_orig_l = self.size_orig_l
        preview_size_l = self.preview_size_l
        rel_file_path = self.rel_file_path
        ft_ext = self.ft_ext
        preview_ext_orig = self.preview_ext_orig

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if guid is not UNSET:
            field_dict["guid"] = guid
        if size is not UNSET:
            field_dict["size"] = size
        if md5 is not UNSET:
            field_dict["md5"] = md5
        if path_id is not UNSET:
            field_dict["pathId"] = path_id
        if path_id_2 is not UNSET:
            field_dict["pathId2"] = path_id_2
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if last_access_iso is not UNSET:
            field_dict["lastAccessIso"] = last_access_iso
        if last_update_iso is not UNSET:
            field_dict["lastUpdateIso"] = last_update_iso
        if owner is not UNSET:
            field_dict["owner"] = owner
        if ext is not UNSET:
            field_dict["ext"] = ext
        if fclip is not UNSET:
            field_dict["fclip"] = fclip
        if ext_orig is not UNSET:
            field_dict["extOrig"] = ext_orig
        if size_orig is not UNSET:
            field_dict["sizeOrig"] = size_orig
        if encr_set is not UNSET:
            field_dict["encrSet"] = encr_set
        if preview_size is not UNSET:
            field_dict["previewSize"] = preview_size
        if preview_ext is not UNSET:
            field_dict["previewExt"] = preview_ext
        if fulltext_content_t_stamp is not UNSET:
            field_dict["fulltextContentTStamp"] = fulltext_content_t_stamp
        if fulltext_content_size is not UNSET:
            field_dict["fulltextContentSize"] = fulltext_content_size
        if size_l is not UNSET:
            field_dict["sizeL"] = size_l
        if size_orig_l is not UNSET:
            field_dict["sizeOrigL"] = size_orig_l
        if preview_size_l is not UNSET:
            field_dict["previewSizeL"] = preview_size_l
        if rel_file_path is not UNSET:
            field_dict["relFilePath"] = rel_file_path
        if ft_ext is not UNSET:
            field_dict["ftExt"] = ft_ext
        if preview_ext_orig is not UNSET:
            field_dict["previewExtOrig"] = preview_ext_orig

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        guid = d.pop("guid", UNSET)

        size = d.pop("size", UNSET)

        md5 = d.pop("md5", UNSET)

        path_id = d.pop("pathId", UNSET)

        path_id_2 = d.pop("pathId2", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        last_access_iso = d.pop("lastAccessIso", UNSET)

        last_update_iso = d.pop("lastUpdateIso", UNSET)

        owner = d.pop("owner", UNSET)

        ext = d.pop("ext", UNSET)

        fclip = d.pop("fclip", UNSET)

        ext_orig = d.pop("extOrig", UNSET)

        size_orig = d.pop("sizeOrig", UNSET)

        encr_set = d.pop("encrSet", UNSET)

        preview_size = d.pop("previewSize", UNSET)

        preview_ext = d.pop("previewExt", UNSET)

        fulltext_content_t_stamp = d.pop("fulltextContentTStamp", UNSET)

        fulltext_content_size = d.pop("fulltextContentSize", UNSET)

        size_l = d.pop("sizeL", UNSET)

        size_orig_l = d.pop("sizeOrigL", UNSET)

        preview_size_l = d.pop("previewSizeL", UNSET)

        rel_file_path = d.pop("relFilePath", UNSET)

        ft_ext = d.pop("ftExt", UNSET)

        preview_ext_orig = d.pop("previewExtOrig", UNSET)

        doc_info_dm = cls(
            id=id,
            guid=guid,
            size=size,
            md5=md5,
            path_id=path_id,
            path_id_2=path_id_2,
            create_date_iso=create_date_iso,
            last_access_iso=last_access_iso,
            last_update_iso=last_update_iso,
            owner=owner,
            ext=ext,
            fclip=fclip,
            ext_orig=ext_orig,
            size_orig=size_orig,
            encr_set=encr_set,
            preview_size=preview_size,
            preview_ext=preview_ext,
            fulltext_content_t_stamp=fulltext_content_t_stamp,
            fulltext_content_size=fulltext_content_size,
            size_l=size_l,
            size_orig_l=size_orig_l,
            preview_size_l=preview_size_l,
            rel_file_path=rel_file_path,
            ft_ext=ft_ext,
            preview_ext_orig=preview_ext_orig,
        )

        doc_info_dm.additional_properties = d
        return doc_info_dm

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
