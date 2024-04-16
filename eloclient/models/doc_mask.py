from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.doc_mask_details import DocMaskDetails
    from ..models.doc_mask_inherit import DocMaskInherit
    from ..models.doc_mask_line import DocMaskLine
    from ..models.map_to_aspect_assoc import MapToAspectAssoc


T = TypeVar("T", bound="DocMask")


@_attrs_define
class DocMask:
    """<p>
    Contains the data for a storage mask.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            sord_type (Union[Unset, int]): Prepare this type for a new Sord object.
                <p>
                 If this value is 0, the Sord type is {@link SordC#LBT_DOCUMENT} for a new document. For a new
                 folder, the default sord type is set as the parent's sord type plus 1. If the parent is
                 undefined, the default type is 1.
                 </p>
                 <p>
                 If this value is not 0, it must be given between 1 and {@link SordC#LBT_DOCUMENT}-1 for folder
                 types and between {@link SordC#LBT_DOCUMENT} and {@link SordC#LBT_DOCUMENT_MAX} for document
                 types.
                 </p>
            data_organisation (Union[Unset, int]): This member specifies how the index values are stored in database.
            lifetime (Union[Unset, str]): New objects are valid for this length of time.
            acl (Union[Unset, str]): Access control for the mask line
            doc_acl_items (Union[Unset, List['AclItem']]):
            inherit_from_masks (Union[Unset, List['DocMaskInherit']]):
            t_stamp (Union[Unset, str]): Last update time of the storage mask data.
            transitive_children (Union[Unset, List[int]]):
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            d_kind (Union[Unset, int]): The marker color ID for new objects created with this mask.
            details (Union[Unset, DocMaskDetails]): This class contains a member of a <code>DocMask</code> object.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            id (Union[Unset, int]): Storage mask ID.
            text (Union[Unset, str]): Tab captions. List of tab captions separated by pipe char |.
            package_name (Union[Unset, str]): Package name of DocMask
            lines (Union[Unset, List['DocMaskLine']]):
            barcode (Union[Unset, str]): Barcode string.
            flow_id (Union[Unset, int]): The ID of a workflow that is started if a new object with this mask is created.
                If the
                 SessionOption START_DOCMASK_WORKFLOWS is set, the Indexserver starts this workflow, if an
                 associated document is created. Otherwise the client application is responsible for starting
                 the workflow.
            lock_name (Union[Unset, str]): Name of the user that has locked th storage mask. Read-only, ignored in
                checkinDocMask.
            text_translation_key (Union[Unset, str]): Translation-keyword for {@link DocMask#text}.
            index (Union[Unset, str]): This control string provides a way of storing new storage mask objects automatically
                in a
                particular archive path.
            local_aspect_assocs (Union[Unset, MapToAspectAssoc]):
            d_path (Union[Unset, int]): Document storage path name where the documents of this mask should be stored.
            lock_id (Union[Unset, int]): User ID of the user that has locked the storage mask. If -1, no lock is held.
            name_translation_key (Union[Unset, str]): Translation-keyword for {@link DocMask#name}.
            deleted (Union[Unset, bool]): Deleted status.
            flow_id_2 (Union[Unset, int]): The ID of a workflow that is to be started if a new version of an associated
                document is
                checked in. If the SessionOption START_DOCMASK_WORKFLOWS is set, the Indexserver starts this
                 workflow, if an associated document is checked in. Otherwise the client application is
                 responsible for starting the workflow.
            mask_ids_for_child_entries (Union[Unset, List[int]]):
            acl_items (Union[Unset, List['AclItem']]):
            name (Union[Unset, str]): Storage mask name. It can be translated into reps.
                from the users language: set
                 <code>SessionOptionsC.TRANSLATE_TERM</code>.
            d_acl (Union[Unset, str]): New objects are created with these ACL permission settings.
            guid (Union[Unset, str]): GUID
            aspect_assocs (Union[Unset, MapToAspectAssoc]):
            deletion_deadline (Union[Unset, str]): Deletion deadline for new objects.
    """

    sord_type: Union[Unset, int] = UNSET
    data_organisation: Union[Unset, int] = UNSET
    lifetime: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    doc_acl_items: Union[Unset, List["AclItem"]] = UNSET
    inherit_from_masks: Union[Unset, List["DocMaskInherit"]] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    transitive_children: Union[Unset, List[int]] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    d_kind: Union[Unset, int] = UNSET
    details: Union[Unset, "DocMaskDetails"] = UNSET
    id: Union[Unset, int] = UNSET
    text: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    lines: Union[Unset, List["DocMaskLine"]] = UNSET
    barcode: Union[Unset, str] = UNSET
    flow_id: Union[Unset, int] = UNSET
    lock_name: Union[Unset, str] = UNSET
    text_translation_key: Union[Unset, str] = UNSET
    index: Union[Unset, str] = UNSET
    local_aspect_assocs: Union[Unset, "MapToAspectAssoc"] = UNSET
    d_path: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    name_translation_key: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    flow_id_2: Union[Unset, int] = UNSET
    mask_ids_for_child_entries: Union[Unset, List[int]] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    d_acl: Union[Unset, str] = UNSET
    guid: Union[Unset, str] = UNSET
    aspect_assocs: Union[Unset, "MapToAspectAssoc"] = UNSET
    deletion_deadline: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sord_type = self.sord_type

        data_organisation = self.data_organisation

        lifetime = self.lifetime

        acl = self.acl

        doc_acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.doc_acl_items, Unset):
            doc_acl_items = []
            for doc_acl_items_item_data in self.doc_acl_items:
                doc_acl_items_item = doc_acl_items_item_data.to_dict()
                doc_acl_items.append(doc_acl_items_item)

        inherit_from_masks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inherit_from_masks, Unset):
            inherit_from_masks = []
            for componentsschemas_list_of_doc_mask_inherit_item_data in self.inherit_from_masks:
                componentsschemas_list_of_doc_mask_inherit_item = (
                    componentsschemas_list_of_doc_mask_inherit_item_data.to_dict()
                )
                inherit_from_masks.append(componentsschemas_list_of_doc_mask_inherit_item)

        t_stamp = self.t_stamp

        transitive_children: Union[Unset, List[int]] = UNSET
        if not isinstance(self.transitive_children, Unset):
            transitive_children = self.transitive_children

        t_stamp_sync = self.t_stamp_sync

        d_kind = self.d_kind

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        id = self.id

        text = self.text

        package_name = self.package_name

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        barcode = self.barcode

        flow_id = self.flow_id

        lock_name = self.lock_name

        text_translation_key = self.text_translation_key

        index = self.index

        local_aspect_assocs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.local_aspect_assocs, Unset):
            local_aspect_assocs = self.local_aspect_assocs.to_dict()

        d_path = self.d_path

        lock_id = self.lock_id

        name_translation_key = self.name_translation_key

        deleted = self.deleted

        flow_id_2 = self.flow_id_2

        mask_ids_for_child_entries: Union[Unset, List[int]] = UNSET
        if not isinstance(self.mask_ids_for_child_entries, Unset):
            mask_ids_for_child_entries = self.mask_ids_for_child_entries

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        name = self.name

        d_acl = self.d_acl

        guid = self.guid

        aspect_assocs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_assocs, Unset):
            aspect_assocs = self.aspect_assocs.to_dict()

        deletion_deadline = self.deletion_deadline

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sord_type is not UNSET:
            field_dict["sordType"] = sord_type
        if data_organisation is not UNSET:
            field_dict["dataOrganisation"] = data_organisation
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if acl is not UNSET:
            field_dict["acl"] = acl
        if doc_acl_items is not UNSET:
            field_dict["docAclItems"] = doc_acl_items
        if inherit_from_masks is not UNSET:
            field_dict["inheritFromMasks"] = inherit_from_masks
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if transitive_children is not UNSET:
            field_dict["transitiveChildren"] = transitive_children
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if d_kind is not UNSET:
            field_dict["DKind"] = d_kind
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if lines is not UNSET:
            field_dict["lines"] = lines
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if text_translation_key is not UNSET:
            field_dict["textTranslationKey"] = text_translation_key
        if index is not UNSET:
            field_dict["index"] = index
        if local_aspect_assocs is not UNSET:
            field_dict["localAspectAssocs"] = local_aspect_assocs
        if d_path is not UNSET:
            field_dict["DPath"] = d_path
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if name_translation_key is not UNSET:
            field_dict["nameTranslationKey"] = name_translation_key
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if flow_id_2 is not UNSET:
            field_dict["flowId2"] = flow_id_2
        if mask_ids_for_child_entries is not UNSET:
            field_dict["maskIdsForChildEntries"] = mask_ids_for_child_entries
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if name is not UNSET:
            field_dict["name"] = name
        if d_acl is not UNSET:
            field_dict["DAcl"] = d_acl
        if guid is not UNSET:
            field_dict["guid"] = guid
        if aspect_assocs is not UNSET:
            field_dict["aspectAssocs"] = aspect_assocs
        if deletion_deadline is not UNSET:
            field_dict["deletionDeadline"] = deletion_deadline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.doc_mask_details import DocMaskDetails
        from ..models.doc_mask_inherit import DocMaskInherit
        from ..models.doc_mask_line import DocMaskLine
        from ..models.map_to_aspect_assoc import MapToAspectAssoc

        d = src_dict.copy()
        sord_type = d.pop("sordType", UNSET)

        data_organisation = d.pop("dataOrganisation", UNSET)

        lifetime = d.pop("lifetime", UNSET)

        acl = d.pop("acl", UNSET)

        doc_acl_items = []
        _doc_acl_items = d.pop("docAclItems", UNSET)
        for doc_acl_items_item_data in _doc_acl_items or []:
            doc_acl_items_item = AclItem.from_dict(doc_acl_items_item_data)

            doc_acl_items.append(doc_acl_items_item)

        inherit_from_masks = []
        _inherit_from_masks = d.pop("inheritFromMasks", UNSET)
        for componentsschemas_list_of_doc_mask_inherit_item_data in _inherit_from_masks or []:
            componentsschemas_list_of_doc_mask_inherit_item = DocMaskInherit.from_dict(
                componentsschemas_list_of_doc_mask_inherit_item_data
            )

            inherit_from_masks.append(componentsschemas_list_of_doc_mask_inherit_item)

        t_stamp = d.pop("TStamp", UNSET)

        transitive_children = cast(List[int], d.pop("transitiveChildren", UNSET))

        t_stamp_sync = d.pop("TStampSync", UNSET)

        d_kind = d.pop("DKind", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, DocMaskDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = DocMaskDetails.from_dict(_details)

        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        package_name = d.pop("packageName", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = DocMaskLine.from_dict(lines_item_data)

            lines.append(lines_item)

        barcode = d.pop("barcode", UNSET)

        flow_id = d.pop("flowId", UNSET)

        lock_name = d.pop("lockName", UNSET)

        text_translation_key = d.pop("textTranslationKey", UNSET)

        index = d.pop("index", UNSET)

        _local_aspect_assocs = d.pop("localAspectAssocs", UNSET)
        local_aspect_assocs: Union[Unset, MapToAspectAssoc]
        if isinstance(_local_aspect_assocs, Unset):
            local_aspect_assocs = UNSET
        else:
            local_aspect_assocs = MapToAspectAssoc.from_dict(_local_aspect_assocs)

        d_path = d.pop("DPath", UNSET)

        lock_id = d.pop("lockId", UNSET)

        name_translation_key = d.pop("nameTranslationKey", UNSET)

        deleted = d.pop("deleted", UNSET)

        flow_id_2 = d.pop("flowId2", UNSET)

        mask_ids_for_child_entries = cast(List[int], d.pop("maskIdsForChildEntries", UNSET))

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        name = d.pop("name", UNSET)

        d_acl = d.pop("DAcl", UNSET)

        guid = d.pop("guid", UNSET)

        _aspect_assocs = d.pop("aspectAssocs", UNSET)
        aspect_assocs: Union[Unset, MapToAspectAssoc]
        if isinstance(_aspect_assocs, Unset):
            aspect_assocs = UNSET
        else:
            aspect_assocs = MapToAspectAssoc.from_dict(_aspect_assocs)

        deletion_deadline = d.pop("deletionDeadline", UNSET)

        doc_mask = cls(
            sord_type=sord_type,
            data_organisation=data_organisation,
            lifetime=lifetime,
            acl=acl,
            doc_acl_items=doc_acl_items,
            inherit_from_masks=inherit_from_masks,
            t_stamp=t_stamp,
            transitive_children=transitive_children,
            t_stamp_sync=t_stamp_sync,
            d_kind=d_kind,
            details=details,
            id=id,
            text=text,
            package_name=package_name,
            lines=lines,
            barcode=barcode,
            flow_id=flow_id,
            lock_name=lock_name,
            text_translation_key=text_translation_key,
            index=index,
            local_aspect_assocs=local_aspect_assocs,
            d_path=d_path,
            lock_id=lock_id,
            name_translation_key=name_translation_key,
            deleted=deleted,
            flow_id_2=flow_id_2,
            mask_ids_for_child_entries=mask_ids_for_child_entries,
            acl_items=acl_items,
            name=name,
            d_acl=d_acl,
            guid=guid,
            aspect_assocs=aspect_assocs,
            deletion_deadline=deletion_deadline,
        )

        doc_mask.additional_properties = d
        return doc_mask

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
