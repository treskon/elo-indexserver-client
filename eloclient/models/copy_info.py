from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CopyInfo")


@_attrs_define
class CopyInfo:
    """Controls the options of de.elo.ix.IXServicePortIF.copySord().
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            adjust_acl_overwrite (Union[Unset, bool]): Set the permissions of the moved object equal to the permissions of
                the new parent.
            depth (Union[Unset, int]): Depth up to which the structure is to be copied.
                THIS FUNCTION IS NOT CURRENTLY SUPPORTED!
            adjust_acl_ignore_documents (Union[Unset, bool]): Recursivly adjust the permissions of the child-documents of
                the moved object too.
            name (Union[Unset, str]): COPY-Mode: Name of the destination archive entry.
                THIS FUNCTION IS NOT CURRENTLY SUPPORTED!
            man_sort_idx (Union[Unset, int]): Manually determine the position. Use 0 to insert at the beginning of the child
                list.
                Use -1 to insert at the end of
                 the child list ( this is the fastest mode). A value n greater then 0 inserts the object at the position n.
            old_parent_id (Union[Unset, str]): Parent ID for move operation.
                Set this element to the old parent ID when a reference has to be
                 moved. If an original entry has to be moved, set the main parent ID or leave the value empty.
            adjust_acl_in_background (Union[Unset, bool]): Recursivly adjust the permissions of the child-elements in the
                background.
            adjust_acl_difference (Union[Unset, bool]): The permissions of the moved object are modified.
                The permissions inherited from the old parent are substracted and
                 the permissions of the new parent are added to the object.
            adjust_acl_ignore_folders (Union[Unset, bool]): Recursivly adjust the permissions of the sub-folders of the
                moved object too.
            check_recursion (Union[Unset, bool]): Check for recursion.
                If this member is set, the function
                 {@link IXServicePortIF#copySord(ClientInfo, String, String, CopyInfo, CopySordZ)} checks
                 whether the copy or move operation causes a recursion in the archive hierarchy. If so, the
                 function throws an exception with {@link IXExceptionC#ACCESS_DENIED}.
    """

    adjust_acl_overwrite: Union[Unset, bool] = UNSET
    depth: Union[Unset, int] = UNSET
    adjust_acl_ignore_documents: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    man_sort_idx: Union[Unset, int] = UNSET
    old_parent_id: Union[Unset, str] = UNSET
    adjust_acl_in_background: Union[Unset, bool] = UNSET
    adjust_acl_difference: Union[Unset, bool] = UNSET
    adjust_acl_ignore_folders: Union[Unset, bool] = UNSET
    check_recursion: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adjust_acl_overwrite = self.adjust_acl_overwrite

        depth = self.depth

        adjust_acl_ignore_documents = self.adjust_acl_ignore_documents

        name = self.name

        man_sort_idx = self.man_sort_idx

        old_parent_id = self.old_parent_id

        adjust_acl_in_background = self.adjust_acl_in_background

        adjust_acl_difference = self.adjust_acl_difference

        adjust_acl_ignore_folders = self.adjust_acl_ignore_folders

        check_recursion = self.check_recursion

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjust_acl_overwrite is not UNSET:
            field_dict["adjustAclOverwrite"] = adjust_acl_overwrite
        if depth is not UNSET:
            field_dict["depth"] = depth
        if adjust_acl_ignore_documents is not UNSET:
            field_dict["adjustAclIgnoreDocuments"] = adjust_acl_ignore_documents
        if name is not UNSET:
            field_dict["name"] = name
        if man_sort_idx is not UNSET:
            field_dict["manSortIdx"] = man_sort_idx
        if old_parent_id is not UNSET:
            field_dict["oldParentId"] = old_parent_id
        if adjust_acl_in_background is not UNSET:
            field_dict["adjustAclInBackground"] = adjust_acl_in_background
        if adjust_acl_difference is not UNSET:
            field_dict["adjustAclDifference"] = adjust_acl_difference
        if adjust_acl_ignore_folders is not UNSET:
            field_dict["adjustAclIgnoreFolders"] = adjust_acl_ignore_folders
        if check_recursion is not UNSET:
            field_dict["checkRecursion"] = check_recursion

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        adjust_acl_overwrite = d.pop("adjustAclOverwrite", UNSET)

        depth = d.pop("depth", UNSET)

        adjust_acl_ignore_documents = d.pop("adjustAclIgnoreDocuments", UNSET)

        name = d.pop("name", UNSET)

        man_sort_idx = d.pop("manSortIdx", UNSET)

        old_parent_id = d.pop("oldParentId", UNSET)

        adjust_acl_in_background = d.pop("adjustAclInBackground", UNSET)

        adjust_acl_difference = d.pop("adjustAclDifference", UNSET)

        adjust_acl_ignore_folders = d.pop("adjustAclIgnoreFolders", UNSET)

        check_recursion = d.pop("checkRecursion", UNSET)

        copy_info = cls(
            adjust_acl_overwrite=adjust_acl_overwrite,
            depth=depth,
            adjust_acl_ignore_documents=adjust_acl_ignore_documents,
            name=name,
            man_sort_idx=man_sort_idx,
            old_parent_id=old_parent_id,
            adjust_acl_in_background=adjust_acl_in_background,
            adjust_acl_difference=adjust_acl_difference,
            adjust_acl_ignore_folders=adjust_acl_ignore_folders,
            check_recursion=check_recursion,
        )

        copy_info.additional_properties = d
        return copy_info

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
