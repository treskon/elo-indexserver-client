from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lock_z import LockZ
    from ..models.process_acl import ProcessAcl
    from ..models.process_copy_elements import ProcessCopyElements
    from ..models.process_count_elements import ProcessCountElements
    from ..models.process_fulltext import ProcessFulltext
    from ..models.process_inherit_keywording import ProcessInheritKeywording
    from ..models.process_move_documents_to_storage_path import ProcessMoveDocumentsToStoragePath
    from ..models.process_region import ProcessRegion
    from ..models.process_release_lock import ProcessReleaseLock
    from ..models.process_repl_set import ProcessReplSet
    from ..models.process_script import ProcessScript
    from ..models.process_space_guid import ProcessSpaceGuid


T = TypeVar("T", bound="ProcessInfo")


@_attrs_define
class ProcessInfo:
    """Specific processing information for each node of processTrees(...) or processFindResults(...).
    The operations will be for existence (not null) in order of their appearance in ProcessInfo. Some
     of the underlying structures may allow toggling between prefix and postfix processing when used
     with processTrees.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            proc_move_documents_to_storage_path (Union[Unset, ProcessMoveDocumentsToStoragePath]): This class specifies the
                options for moving a document into another storage path.
                It is used as
                 member in <code>ProcessInfo</code> and is interpreted in the functions
                 <code>processFindResult</code> and <code>processTrees</code>.
            proc_msgs (Union[Unset, List[str]]):
            proc_repl_set (Union[Unset, ProcessReplSet]): Replication sets to be added to/removed from an object.
                The replication set parameter must refer
                 to existing objects that may contain empty lists. Null values are not allowed.

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            incl_references (Union[Unset, bool]): Process references (logical copies) too.
            ignore_documents (Union[Unset, bool]): processing flag for documents.
            proc_inherit_keywording (Union[Unset, ProcessInheritKeywording]): This class of keywording.
            proc_msg_max (Union[Unset, int]): Maximum amount of recorded errors in procMsgs; from ProcessInfoC: PROCMSGMAX.
            error_mode (Union[Unset, int]): From ProcessInfoC: ERRORMODE_ALL, ERRORMODE_SKIP_SUBTREE,
                ERRORMODE_SKIP_PROCINFO or
                ERRORMODE_CRITICAL_ONLY.
            lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            proc_fulltext (Union[Unset, ProcessFulltext]): Fulltext-Property to be added to/removed from an object.
                <p>
                 Copyright: Copyright (c) 2008
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            proc_script (Union[Unset, ProcessScript]): NOT CURRENTLY SUPPORTED
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            proc_count_elem (Union[Unset, ProcessCountElements]): This class make possible the count of the archive
                elements.
                <p>
                 Copyright: Copyright (c) 2008
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            proc_space_guid (Union[Unset, ProcessSpaceGuid]): This class specifies the options for setting a sord's
                spaceGuid (i.e.
                GUID of the workspace it
                 belongs to). It is used as member in <code>ProcessInfo</code> and is interpreted in the functions
                 <code>processFindResult</code> and <code>processTrees</code>.
            del_status (Union[Unset, int]): pass 0 for valid (undeleted) nodes, &gt;0 otherwise.
            proc_acl (Union[Unset, ProcessAcl]): This class is used to assign or remove ACLs to an object.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            proc_region (Union[Unset, ProcessRegion]): This class specifies the options for setting a sord's {@link
                Sord#regionId} (i.e.
                ID of the
                 region it belongs to) for sub-trees of sords. It is used as member in {@link ProcessInfo} and
                 defines a respective operation.

                 <p>
                 Copyright: Copyright (c) 2022
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            ignore_structures (Union[Unset, bool]): processing flag for structure elements.
            proc_copy_elements (Union[Unset, ProcessCopyElements]): Copy archive elements in other position in the archive.
                <p>
                 Copyright: Copyright (c) 2009
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            force_operation (Union[Unset, bool]): Defines, if the data allways have to be written
            proc_release_lock (Union[Unset, ProcessReleaseLock]): Releases the locks on archive elements.
            desc (Union[Unset, str]): Holds the user defined description of a specific call. This member must not be null or
                empty.
    """

    proc_move_documents_to_storage_path: Union[Unset, "ProcessMoveDocumentsToStoragePath"] = UNSET
    proc_msgs: Union[Unset, List[str]] = UNSET
    proc_repl_set: Union[Unset, "ProcessReplSet"] = UNSET
    incl_references: Union[Unset, bool] = UNSET
    ignore_documents: Union[Unset, bool] = UNSET
    proc_inherit_keywording: Union[Unset, "ProcessInheritKeywording"] = UNSET
    proc_msg_max: Union[Unset, int] = UNSET
    error_mode: Union[Unset, int] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    proc_fulltext: Union[Unset, "ProcessFulltext"] = UNSET
    proc_script: Union[Unset, "ProcessScript"] = UNSET
    proc_count_elem: Union[Unset, "ProcessCountElements"] = UNSET
    proc_space_guid: Union[Unset, "ProcessSpaceGuid"] = UNSET
    del_status: Union[Unset, int] = UNSET
    proc_acl: Union[Unset, "ProcessAcl"] = UNSET
    proc_region: Union[Unset, "ProcessRegion"] = UNSET
    ignore_structures: Union[Unset, bool] = UNSET
    proc_copy_elements: Union[Unset, "ProcessCopyElements"] = UNSET
    force_operation: Union[Unset, bool] = UNSET
    proc_release_lock: Union[Unset, "ProcessReleaseLock"] = UNSET
    desc: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proc_move_documents_to_storage_path: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_move_documents_to_storage_path, Unset):
            proc_move_documents_to_storage_path = self.proc_move_documents_to_storage_path.to_dict()

        proc_msgs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.proc_msgs, Unset):
            proc_msgs = self.proc_msgs

        proc_repl_set: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_repl_set, Unset):
            proc_repl_set = self.proc_repl_set.to_dict()

        incl_references = self.incl_references

        ignore_documents = self.ignore_documents

        proc_inherit_keywording: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_inherit_keywording, Unset):
            proc_inherit_keywording = self.proc_inherit_keywording.to_dict()

        proc_msg_max = self.proc_msg_max

        error_mode = self.error_mode

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        proc_fulltext: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_fulltext, Unset):
            proc_fulltext = self.proc_fulltext.to_dict()

        proc_script: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_script, Unset):
            proc_script = self.proc_script.to_dict()

        proc_count_elem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_count_elem, Unset):
            proc_count_elem = self.proc_count_elem.to_dict()

        proc_space_guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_space_guid, Unset):
            proc_space_guid = self.proc_space_guid.to_dict()

        del_status = self.del_status

        proc_acl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_acl, Unset):
            proc_acl = self.proc_acl.to_dict()

        proc_region: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_region, Unset):
            proc_region = self.proc_region.to_dict()

        ignore_structures = self.ignore_structures

        proc_copy_elements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_copy_elements, Unset):
            proc_copy_elements = self.proc_copy_elements.to_dict()

        force_operation = self.force_operation

        proc_release_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proc_release_lock, Unset):
            proc_release_lock = self.proc_release_lock.to_dict()

        desc = self.desc

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proc_move_documents_to_storage_path is not UNSET:
            field_dict["procMoveDocumentsToStoragePath"] = proc_move_documents_to_storage_path
        if proc_msgs is not UNSET:
            field_dict["procMsgs"] = proc_msgs
        if proc_repl_set is not UNSET:
            field_dict["procReplSet"] = proc_repl_set
        if incl_references is not UNSET:
            field_dict["inclReferences"] = incl_references
        if ignore_documents is not UNSET:
            field_dict["ignoreDocuments"] = ignore_documents
        if proc_inherit_keywording is not UNSET:
            field_dict["procInheritKeywording"] = proc_inherit_keywording
        if proc_msg_max is not UNSET:
            field_dict["procMsgMax"] = proc_msg_max
        if error_mode is not UNSET:
            field_dict["errorMode"] = error_mode
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if proc_fulltext is not UNSET:
            field_dict["procFulltext"] = proc_fulltext
        if proc_script is not UNSET:
            field_dict["procScript"] = proc_script
        if proc_count_elem is not UNSET:
            field_dict["procCountElem"] = proc_count_elem
        if proc_space_guid is not UNSET:
            field_dict["procSpaceGuid"] = proc_space_guid
        if del_status is not UNSET:
            field_dict["delStatus"] = del_status
        if proc_acl is not UNSET:
            field_dict["procAcl"] = proc_acl
        if proc_region is not UNSET:
            field_dict["procRegion"] = proc_region
        if ignore_structures is not UNSET:
            field_dict["ignoreStructures"] = ignore_structures
        if proc_copy_elements is not UNSET:
            field_dict["procCopyElements"] = proc_copy_elements
        if force_operation is not UNSET:
            field_dict["forceOperation"] = force_operation
        if proc_release_lock is not UNSET:
            field_dict["procReleaseLock"] = proc_release_lock
        if desc is not UNSET:
            field_dict["desc"] = desc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lock_z import LockZ
        from ..models.process_acl import ProcessAcl
        from ..models.process_copy_elements import ProcessCopyElements
        from ..models.process_count_elements import ProcessCountElements
        from ..models.process_fulltext import ProcessFulltext
        from ..models.process_inherit_keywording import ProcessInheritKeywording
        from ..models.process_move_documents_to_storage_path import ProcessMoveDocumentsToStoragePath
        from ..models.process_region import ProcessRegion
        from ..models.process_release_lock import ProcessReleaseLock
        from ..models.process_repl_set import ProcessReplSet
        from ..models.process_script import ProcessScript
        from ..models.process_space_guid import ProcessSpaceGuid

        d = src_dict.copy()
        _proc_move_documents_to_storage_path = d.pop("procMoveDocumentsToStoragePath", UNSET)
        proc_move_documents_to_storage_path: Union[Unset, ProcessMoveDocumentsToStoragePath]
        if isinstance(_proc_move_documents_to_storage_path, Unset):
            proc_move_documents_to_storage_path = UNSET
        else:
            proc_move_documents_to_storage_path = ProcessMoveDocumentsToStoragePath.from_dict(
                _proc_move_documents_to_storage_path
            )

        proc_msgs = cast(List[str], d.pop("procMsgs", UNSET))

        _proc_repl_set = d.pop("procReplSet", UNSET)
        proc_repl_set: Union[Unset, ProcessReplSet]
        if isinstance(_proc_repl_set, Unset):
            proc_repl_set = UNSET
        else:
            proc_repl_set = ProcessReplSet.from_dict(_proc_repl_set)

        incl_references = d.pop("inclReferences", UNSET)

        ignore_documents = d.pop("ignoreDocuments", UNSET)

        _proc_inherit_keywording = d.pop("procInheritKeywording", UNSET)
        proc_inherit_keywording: Union[Unset, ProcessInheritKeywording]
        if isinstance(_proc_inherit_keywording, Unset):
            proc_inherit_keywording = UNSET
        else:
            proc_inherit_keywording = ProcessInheritKeywording.from_dict(_proc_inherit_keywording)

        proc_msg_max = d.pop("procMsgMax", UNSET)

        error_mode = d.pop("errorMode", UNSET)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        _proc_fulltext = d.pop("procFulltext", UNSET)
        proc_fulltext: Union[Unset, ProcessFulltext]
        if isinstance(_proc_fulltext, Unset):
            proc_fulltext = UNSET
        else:
            proc_fulltext = ProcessFulltext.from_dict(_proc_fulltext)

        _proc_script = d.pop("procScript", UNSET)
        proc_script: Union[Unset, ProcessScript]
        if isinstance(_proc_script, Unset):
            proc_script = UNSET
        else:
            proc_script = ProcessScript.from_dict(_proc_script)

        _proc_count_elem = d.pop("procCountElem", UNSET)
        proc_count_elem: Union[Unset, ProcessCountElements]
        if isinstance(_proc_count_elem, Unset):
            proc_count_elem = UNSET
        else:
            proc_count_elem = ProcessCountElements.from_dict(_proc_count_elem)

        _proc_space_guid = d.pop("procSpaceGuid", UNSET)
        proc_space_guid: Union[Unset, ProcessSpaceGuid]
        if isinstance(_proc_space_guid, Unset):
            proc_space_guid = UNSET
        else:
            proc_space_guid = ProcessSpaceGuid.from_dict(_proc_space_guid)

        del_status = d.pop("delStatus", UNSET)

        _proc_acl = d.pop("procAcl", UNSET)
        proc_acl: Union[Unset, ProcessAcl]
        if isinstance(_proc_acl, Unset):
            proc_acl = UNSET
        else:
            proc_acl = ProcessAcl.from_dict(_proc_acl)

        _proc_region = d.pop("procRegion", UNSET)
        proc_region: Union[Unset, ProcessRegion]
        if isinstance(_proc_region, Unset):
            proc_region = UNSET
        else:
            proc_region = ProcessRegion.from_dict(_proc_region)

        ignore_structures = d.pop("ignoreStructures", UNSET)

        _proc_copy_elements = d.pop("procCopyElements", UNSET)
        proc_copy_elements: Union[Unset, ProcessCopyElements]
        if isinstance(_proc_copy_elements, Unset):
            proc_copy_elements = UNSET
        else:
            proc_copy_elements = ProcessCopyElements.from_dict(_proc_copy_elements)

        force_operation = d.pop("forceOperation", UNSET)

        _proc_release_lock = d.pop("procReleaseLock", UNSET)
        proc_release_lock: Union[Unset, ProcessReleaseLock]
        if isinstance(_proc_release_lock, Unset):
            proc_release_lock = UNSET
        else:
            proc_release_lock = ProcessReleaseLock.from_dict(_proc_release_lock)

        desc = d.pop("desc", UNSET)

        process_info = cls(
            proc_move_documents_to_storage_path=proc_move_documents_to_storage_path,
            proc_msgs=proc_msgs,
            proc_repl_set=proc_repl_set,
            incl_references=incl_references,
            ignore_documents=ignore_documents,
            proc_inherit_keywording=proc_inherit_keywording,
            proc_msg_max=proc_msg_max,
            error_mode=error_mode,
            lock_z=lock_z,
            proc_fulltext=proc_fulltext,
            proc_script=proc_script,
            proc_count_elem=proc_count_elem,
            proc_space_guid=proc_space_guid,
            del_status=del_status,
            proc_acl=proc_acl,
            proc_region=proc_region,
            ignore_structures=ignore_structures,
            proc_copy_elements=proc_copy_elements,
            force_operation=force_operation,
            proc_release_lock=proc_release_lock,
            desc=desc,
        )

        process_info.additional_properties = d
        return process_info

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
