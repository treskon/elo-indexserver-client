from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteOptions")


@_attrs_define
class DeleteOptions:
    """This class contains options for deleting archive SORDs using the deleteSord function.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            folder_must_be_empty (Union[Unset, bool]): Delete a folder only if it is empty.
                Set this member to true, if deleteSord should delete only
                 empty folders. If the parameters to deleteSord specify the original location of a non-empty
                 folder, the exception IXExceptionC.ACCESS_DENIED is thrown. This option is ignored, if
                 deleteSord is invokded with a reference.
            delete_expired_folders (Union[Unset, bool]): Delete only expired folders and documents. Only expired empty
                folders can be deleted.
                Only
                 supported in function <code>cleanupStart</code>. This option can be combined with
                 <code>deleteFinally</code>.
                 <table border="2" summary="">
                 <tr>
                 <td><code>deleteFinally</code></td>
                 <td>Action</td>
                 </tr>
                 <tr>
                 <td><code>false</code></td>
                 <td>All expired objects will be marked as deleted (but not finally deleted). The objects ACL is
                 checked before it is deleted. LockC.FORCE is applied when deleting an object.</td>
                 </tr>
                 <tr>
                 <td><code>true</code></td>
                 <td>Objects that are expired and marked are deleted finally.</td>
                 </tr>
                 </table>
            max_i_date (Union[Unset, str]): maxIDate ist the ISO representation of the local date used to mark the upper
                limit for
                deleting.
            delete_residue_free (Union[Unset, bool]): Delete all references to the objects in the database.
                This includes reporting, replication
                 control information, fulltext, etc. This option is ignroed, if deleteFinally is false.
            delete_document_versions_only (Union[Unset, bool]): Delete the document versions of the objects but keep
                keywording information.
                In order to delete
                 only the document versions, call deleteSord on an maybe undeleted object and set
                 DeleteOptions.deleteFinally=true and DeleteOptions.deleteDocumentVersionsOnly=true.
            delete_finally (Union[Unset, bool]): deleteFinally=true causes the objects to be removed physically.
                When used together with
                 <code>cleanupStart</code>, this option is always true. Exception: see
                 {@link #deleteExpiredOnly}
            delete_expired_only (Union[Unset, bool]): Delete only expired objects. Only supported in function
                <code>cleanupStart</code>.
                This option
                 can be combined with <code>deleteFinally</code>.
                 <table border="2" summary="">
                 <tr>
                 <td><code>deleteFinally</code></td>
                 <td>Action</td>
                 </tr>
                 <tr>
                 <td><code>false</code></td>
                 <td>All expired objects will be marked as deleted (but not finally deleted). The objects ACL is
                 checked before it is deleted. LockC.FORCE is applied when deleting an object.</td>
                 </tr>
                 <tr>
                 <td><code>true</code></td>
                 <td>Objects that are expired and marked are deleted finally.</td>
                 </tr>
                 </table>
            delete_certain_document_versions_only (Union[Unset, bool]): Delete physically certain document versions of the
                objects.
                In order to delete physically
                 certain document versions, first mark document versions as deleted (using
                 DocVersion.setDeleted, followed by checkinDocEnd). Then call deleteSord after having set
                 DeleteOptions.deleteFinally=true and DeleteOptions.deleteCertainDocumentVersionsOnly=true. (In
                 order to delete all document versions, use field deleteDocumentVersionsOnly)
            max_t_stamp (Union[Unset, str]): Delete objects modified last time before this date.
                Only supported in function
                 <code>cleanupStart</code>. If deleteFinally is true and this member is set, ony those objects
                 are deleted finally, which were deleted logically before the given time. It must be an ISO
                 value in the local time zone.
    """

    folder_must_be_empty: Union[Unset, bool] = UNSET
    delete_expired_folders: Union[Unset, bool] = UNSET
    max_i_date: Union[Unset, str] = UNSET
    delete_residue_free: Union[Unset, bool] = UNSET
    delete_document_versions_only: Union[Unset, bool] = UNSET
    delete_finally: Union[Unset, bool] = UNSET
    delete_expired_only: Union[Unset, bool] = UNSET
    delete_certain_document_versions_only: Union[Unset, bool] = UNSET
    max_t_stamp: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        folder_must_be_empty = self.folder_must_be_empty

        delete_expired_folders = self.delete_expired_folders

        max_i_date = self.max_i_date

        delete_residue_free = self.delete_residue_free

        delete_document_versions_only = self.delete_document_versions_only

        delete_finally = self.delete_finally

        delete_expired_only = self.delete_expired_only

        delete_certain_document_versions_only = self.delete_certain_document_versions_only

        max_t_stamp = self.max_t_stamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folder_must_be_empty is not UNSET:
            field_dict["folderMustBeEmpty"] = folder_must_be_empty
        if delete_expired_folders is not UNSET:
            field_dict["deleteExpiredFolders"] = delete_expired_folders
        if max_i_date is not UNSET:
            field_dict["maxIDate"] = max_i_date
        if delete_residue_free is not UNSET:
            field_dict["deleteResidueFree"] = delete_residue_free
        if delete_document_versions_only is not UNSET:
            field_dict["deleteDocumentVersionsOnly"] = delete_document_versions_only
        if delete_finally is not UNSET:
            field_dict["deleteFinally"] = delete_finally
        if delete_expired_only is not UNSET:
            field_dict["deleteExpiredOnly"] = delete_expired_only
        if delete_certain_document_versions_only is not UNSET:
            field_dict["deleteCertainDocumentVersionsOnly"] = delete_certain_document_versions_only
        if max_t_stamp is not UNSET:
            field_dict["maxTStamp"] = max_t_stamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        folder_must_be_empty = d.pop("folderMustBeEmpty", UNSET)

        delete_expired_folders = d.pop("deleteExpiredFolders", UNSET)

        max_i_date = d.pop("maxIDate", UNSET)

        delete_residue_free = d.pop("deleteResidueFree", UNSET)

        delete_document_versions_only = d.pop("deleteDocumentVersionsOnly", UNSET)

        delete_finally = d.pop("deleteFinally", UNSET)

        delete_expired_only = d.pop("deleteExpiredOnly", UNSET)

        delete_certain_document_versions_only = d.pop("deleteCertainDocumentVersionsOnly", UNSET)

        max_t_stamp = d.pop("maxTStamp", UNSET)

        delete_options = cls(
            folder_must_be_empty=folder_must_be_empty,
            delete_expired_folders=delete_expired_folders,
            max_i_date=max_i_date,
            delete_residue_free=delete_residue_free,
            delete_document_versions_only=delete_document_versions_only,
            delete_finally=delete_finally,
            delete_expired_only=delete_expired_only,
            delete_certain_document_versions_only=delete_certain_document_versions_only,
            max_t_stamp=max_t_stamp,
        )

        delete_options.additional_properties = d
        return delete_options

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
