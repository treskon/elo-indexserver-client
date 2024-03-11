from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.arc_path import ArcPath
    from ..models.doc_version import DocVersion
    from ..models.map_to_list_of_map_to_index_value import MapToListOfMapToIndexValue
    from ..models.obj_key import ObjKey
    from ..models.repl_set import ReplSet
    from ..models.repl_set_name import ReplSetName
    from ..models.sord_details import SordDetails
    from ..models.sord_link import SordLink


T = TypeVar("T", bound="Sord")


@_attrs_define
class Sord:
    """<p>
    Indexing information of an archive entry.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            s_reg (Union[Unset, str]): Version numer of the current work version.
            t_stamp (Union[Unset, str]): Timestamp of the last change. The format is JJJJ.MM.DD.hh.mm.
                ss
            acl (Union[Unset, str]): Access control language in coded form. The checkInSord method must set either acl or
                aclItems.
                aclItems has
                 priority.
            att (Union[Unset, int]): Id of the current attachment version. Read-only.
            child_count (Union[Unset, int]): Estimated sum of the sub-entries in a directory.
                This does not take account of any access rights assigned to the
                 entries. This property should only be used to determine whether the directory has additional entries. Read-
                only.
            doc (Union[Unset, int]): Read-only. Id of the current document version.
            guid (Union[Unset, str]): GUID.
            hist_count (Union[Unset, int]): Number of document versions.
            id (Union[Unset, int]): Numeric ID.
            info (Union[Unset, int]): RESERVED
            key (Union[Unset, int]): RESERVED
            kind (Union[Unset, int]): Colour
            lock_id (Union[Unset, int]): This is the id of the user who has a lock on the object.
                To know whether the Sord or the Document is locked, see
                 lockIdSord or lockIdDoc respectively. The object is locked using checkoutSord with the LOCK.YES, LOCK.SORD or
                 LOCK.DOC parameter. Read-only.
            mask (Union[Unset, int]): The id of the filing mask used to archive the sord. Read-only.
            name (Union[Unset, str]): The short description/name for the object.
            owner_id (Union[Unset, int]): The id of the owner of the object.
                Main-administrators can assign an owner ID for new Sords in
                 {@link IXServicePortIF#checkinSord(ClientInfo, Sord, SordZ, LockZ)} and
                 {@link IXServicePortIF#checkinSordPath(ClientInfo, String, Sord[], SordZ)}. This member is read-only for
                 Non-adminstrators or existing Sords.
            parent_id (Union[Unset, int]): Id of the parent object(archive heirachy) of the sord object.
                Read-only
            path (Union[Unset, int]): Filing path for the document manager. Only valid for documents. Read-only.
                <p>
                 If this Sord object is obtained by a call to checkoutSord or checkoutDoc with a database lock (e.g.
                LockC.IF_FREE),
                 this member contains the storage path specified in the associated keywording form (DocMask.DPath). If the
                 keywording form does not define a path, the default storage path is returned (ServerInfoDM.basisStoreIds[0]).
                 Hence, the current value of the database column objekte.objpath is not used as default for new versions
                anymore.
                 </p>
                 <p>
                 If this Sord object is obtained by a call without a lock, e.g. from findFirstSords, this value should not be
                used
                 anymore. The storage path of the work version should be used instead, which can be found in
                Sord.docVersion.pathId.
                 </p>
            type (Union[Unset, int]): The type of sord object.
                Folder objects: 0 &lt; type &lt; LBT_DOCUMENT Document objects: LBT_DOCUMENT &lt;= type
                 &lt; LBT_DOCUMENT_MAX
            vt_rep (Union[Unset, int]): RESERVED
            i_date_iso (Union[Unset, str]): ISO encoded internal (archive defined) date.
            x_date_iso (Union[Unset, str]): ISO encoded external (user defined) date.
            access (Union[Unset, int]): The current users access rights for this Sord. Returns a combination of AccessC.LUR_
                constants. Read-only.
                Is
                 returned when SordC.mbAcl is set in checkoutSord.
            acl_items (Union[Unset, List['AclItem']]):
            del_date_iso (Union[Unset, str]): ISO encoded expiry date. Only users having right AccessC.FLAG_EDITDUEDATE are
                allowed to set the expiry date.
                Once
                 the expiry date is set, it cannot be set to a date before the original expiry date.
            deleted (Union[Unset, bool]): Indicates whether the sord has been deleted or not.
            desc (Union[Unset, str]): The (visible) memo text. If the value starts with a "!" this member can define a
                dynamic folder.
                This is a folder
                 which contents are filled by an arbitrary SQL statement.
            details (Union[Unset, SordDetails]): Objects of this class are data elements and control the values assigned to
                certain boolean properties(yes/no
                attributes).

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            doc_version (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            hidden_text (Union[Unset, str]): Hidden text that must not be displayed to the user.
            links_come_in (Union[Unset, List['SordLink']]):
            links_go_out (Union[Unset, List['SordLink']]):
            lock_name (Union[Unset, str]): The name of the user who has locked the object. Read-only.
            obj_keys (Union[Unset, List['ObjKey']]):
            owner_name (Union[Unset, str]): Name of the owner (read-only).
            parent_ids (Union[Unset, List[str]]):
            ref_paths (Union[Unset, List['ArcPath']]):
            repl_names (Union[Unset, List['ReplSetName']]):
            repl_set (Union[Unset, ReplSet]): <p>
                Objects of this class store the replication information of archive entries.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mask_name (Union[Unset, str]): Name of keywording form. This value is translated into the language given by
                {@link ClientInfo#language}.
                It cannot
                 be used as a parameter in Indexserver API functions. Use {@link Sord#getMask()} to specify the Keywording form
                in
                 API functions. Read-only.
            att_version (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
            delete_date_iso (Union[Unset, str]): The Sord is deleted at this date. ClientInfo determines the Timezone.
                <p>
                 Is undefined if isDeleted() returns false.
                 </p>
            lock_id_sord (Union[Unset, int]): This is the id of the user who has a lock on the object (not the document).
                The object is locked using checkoutSord
                 with the LOCK.SORD parameter. Read-only.
            lock_id_doc (Union[Unset, int]): This is the id of the user who has a lock on the document (not the object).
                The object is locked using checkoutSord
                 with the LOCK.DOC parameter. Read-only.
            lock_name_sord (Union[Unset, str]): The name of the user who has locked the object. Read-only.
            lock_name_doc (Union[Unset, str]): The name of the user who has locked the document. Read-only.
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            t_stamp_acl (Union[Unset, str]): Timestamp of the last ACL change. The format is JJJJ.MM.DD.hh.mm.
                ss
            t_stamp_acl_sync (Union[Unset, str]): Timestamp of this object's ACLs last export by the replication.
            delete_user (Union[Unset, int]): The Sord is deleted at this user.
                <p>
                 Is undefined if isDeleted() returns false.
                 </p>
            aspects (Union[Unset, MapToListOfMapToIndexValue]):
            region_id (Union[Unset, int]): If the sord is contained in a region (i.e.
                lies below an object in archive tree that has an associated keywording
                 form which defines a region), this value contains the numeric Id of that region sord. This value is only valid,
                if
                 the associated keywording form {@link DocMask} is organized as {@link DocMask#dataOrganisation} =
                 {@link DocMaskC#DATA_ORGANISATION_ASPECT}.
    """

    s_reg: Union[Unset, str] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    att: Union[Unset, int] = UNSET
    child_count: Union[Unset, int] = UNSET
    doc: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    hist_count: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    info: Union[Unset, int] = UNSET
    key: Union[Unset, int] = UNSET
    kind: Union[Unset, int] = UNSET
    lock_id: Union[Unset, int] = UNSET
    mask: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    path: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    vt_rep: Union[Unset, int] = UNSET
    i_date_iso: Union[Unset, str] = UNSET
    x_date_iso: Union[Unset, str] = UNSET
    access: Union[Unset, int] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    del_date_iso: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    desc: Union[Unset, str] = UNSET
    details: Union[Unset, "SordDetails"] = UNSET
    doc_version: Union[Unset, "DocVersion"] = UNSET
    hidden_text: Union[Unset, str] = UNSET
    links_come_in: Union[Unset, List["SordLink"]] = UNSET
    links_go_out: Union[Unset, List["SordLink"]] = UNSET
    lock_name: Union[Unset, str] = UNSET
    obj_keys: Union[Unset, List["ObjKey"]] = UNSET
    owner_name: Union[Unset, str] = UNSET
    parent_ids: Union[Unset, List[str]] = UNSET
    ref_paths: Union[Unset, List["ArcPath"]] = UNSET
    repl_names: Union[Unset, List["ReplSetName"]] = UNSET
    repl_set: Union[Unset, "ReplSet"] = UNSET
    mask_name: Union[Unset, str] = UNSET
    att_version: Union[Unset, "DocVersion"] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    lock_id_sord: Union[Unset, int] = UNSET
    lock_id_doc: Union[Unset, int] = UNSET
    lock_name_sord: Union[Unset, str] = UNSET
    lock_name_doc: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    t_stamp_acl: Union[Unset, str] = UNSET
    t_stamp_acl_sync: Union[Unset, str] = UNSET
    delete_user: Union[Unset, int] = UNSET
    aspects: Union[Unset, "MapToListOfMapToIndexValue"] = UNSET
    region_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s_reg = self.s_reg
        t_stamp = self.t_stamp
        acl = self.acl
        att = self.att
        child_count = self.child_count
        doc = self.doc
        guid = self.guid
        hist_count = self.hist_count
        id = self.id
        info = self.info
        key = self.key
        kind = self.kind
        lock_id = self.lock_id
        mask = self.mask
        name = self.name
        owner_id = self.owner_id
        parent_id = self.parent_id
        path = self.path
        type = self.type
        vt_rep = self.vt_rep
        i_date_iso = self.i_date_iso
        x_date_iso = self.x_date_iso
        access = self.access
        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()

                acl_items.append(acl_items_item)

        del_date_iso = self.del_date_iso
        deleted = self.deleted
        desc = self.desc
        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        doc_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_version, Unset):
            doc_version = self.doc_version.to_dict()

        hidden_text = self.hidden_text
        links_come_in: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links_come_in, Unset):
            links_come_in = []
            for links_come_in_item_data in self.links_come_in:
                links_come_in_item = links_come_in_item_data.to_dict()

                links_come_in.append(links_come_in_item)

        links_go_out: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links_go_out, Unset):
            links_go_out = []
            for links_go_out_item_data in self.links_go_out:
                links_go_out_item = links_go_out_item_data.to_dict()

                links_go_out.append(links_go_out_item)

        lock_name = self.lock_name
        obj_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.obj_keys, Unset):
            obj_keys = []
            for obj_keys_item_data in self.obj_keys:
                obj_keys_item = obj_keys_item_data.to_dict()

                obj_keys.append(obj_keys_item)

        owner_name = self.owner_name
        parent_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_ids, Unset):
            parent_ids = self.parent_ids

        ref_paths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ref_paths, Unset):
            ref_paths = []
            for ref_paths_item_data in self.ref_paths:
                ref_paths_item = ref_paths_item_data.to_dict()

                ref_paths.append(ref_paths_item)

        repl_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.repl_names, Unset):
            repl_names = []
            for repl_names_item_data in self.repl_names:
                repl_names_item = repl_names_item_data.to_dict()

                repl_names.append(repl_names_item)

        repl_set: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repl_set, Unset):
            repl_set = self.repl_set.to_dict()

        mask_name = self.mask_name
        att_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.att_version, Unset):
            att_version = self.att_version.to_dict()

        delete_date_iso = self.delete_date_iso
        lock_id_sord = self.lock_id_sord
        lock_id_doc = self.lock_id_doc
        lock_name_sord = self.lock_name_sord
        lock_name_doc = self.lock_name_doc
        t_stamp_sync = self.t_stamp_sync
        t_stamp_acl = self.t_stamp_acl
        t_stamp_acl_sync = self.t_stamp_acl_sync
        delete_user = self.delete_user
        aspects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspects, Unset):
            aspects = self.aspects.to_dict()

        region_id = self.region_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if s_reg is not UNSET:
            field_dict["SReg"] = s_reg
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if acl is not UNSET:
            field_dict["acl"] = acl
        if att is not UNSET:
            field_dict["att"] = att
        if child_count is not UNSET:
            field_dict["childCount"] = child_count
        if doc is not UNSET:
            field_dict["doc"] = doc
        if guid is not UNSET:
            field_dict["guid"] = guid
        if hist_count is not UNSET:
            field_dict["histCount"] = hist_count
        if id is not UNSET:
            field_dict["id"] = id
        if info is not UNSET:
            field_dict["info"] = info
        if key is not UNSET:
            field_dict["key"] = key
        if kind is not UNSET:
            field_dict["kind"] = kind
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if mask is not UNSET:
            field_dict["mask"] = mask
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if type is not UNSET:
            field_dict["type"] = type
        if vt_rep is not UNSET:
            field_dict["vtRep"] = vt_rep
        if i_date_iso is not UNSET:
            field_dict["IDateIso"] = i_date_iso
        if x_date_iso is not UNSET:
            field_dict["XDateIso"] = x_date_iso
        if access is not UNSET:
            field_dict["access"] = access
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if del_date_iso is not UNSET:
            field_dict["delDateIso"] = del_date_iso
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if desc is not UNSET:
            field_dict["desc"] = desc
        if details is not UNSET:
            field_dict["details"] = details
        if doc_version is not UNSET:
            field_dict["docVersion"] = doc_version
        if hidden_text is not UNSET:
            field_dict["hiddenText"] = hidden_text
        if links_come_in is not UNSET:
            field_dict["linksComeIn"] = links_come_in
        if links_go_out is not UNSET:
            field_dict["linksGoOut"] = links_go_out
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if obj_keys is not UNSET:
            field_dict["objKeys"] = obj_keys
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if parent_ids is not UNSET:
            field_dict["parentIds"] = parent_ids
        if ref_paths is not UNSET:
            field_dict["refPaths"] = ref_paths
        if repl_names is not UNSET:
            field_dict["replNames"] = repl_names
        if repl_set is not UNSET:
            field_dict["replSet"] = repl_set
        if mask_name is not UNSET:
            field_dict["maskName"] = mask_name
        if att_version is not UNSET:
            field_dict["attVersion"] = att_version
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso
        if lock_id_sord is not UNSET:
            field_dict["lockIdSord"] = lock_id_sord
        if lock_id_doc is not UNSET:
            field_dict["lockIdDoc"] = lock_id_doc
        if lock_name_sord is not UNSET:
            field_dict["lockNameSord"] = lock_name_sord
        if lock_name_doc is not UNSET:
            field_dict["lockNameDoc"] = lock_name_doc
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if t_stamp_acl is not UNSET:
            field_dict["TStampAcl"] = t_stamp_acl
        if t_stamp_acl_sync is not UNSET:
            field_dict["TStampAclSync"] = t_stamp_acl_sync
        if delete_user is not UNSET:
            field_dict["deleteUser"] = delete_user
        if aspects is not UNSET:
            field_dict["aspects"] = aspects
        if region_id is not UNSET:
            field_dict["regionId"] = region_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.arc_path import ArcPath
        from ..models.doc_version import DocVersion
        from ..models.map_to_list_of_map_to_index_value import MapToListOfMapToIndexValue
        from ..models.obj_key import ObjKey
        from ..models.repl_set import ReplSet
        from ..models.repl_set_name import ReplSetName
        from ..models.sord_details import SordDetails
        from ..models.sord_link import SordLink

        d = src_dict.copy()
        s_reg = d.pop("SReg", UNSET)

        t_stamp = d.pop("TStamp", UNSET)

        acl = d.pop("acl", UNSET)

        att = d.pop("att", UNSET)

        child_count = d.pop("childCount", UNSET)

        doc = d.pop("doc", UNSET)

        guid = d.pop("guid", UNSET)

        hist_count = d.pop("histCount", UNSET)

        id = d.pop("id", UNSET)

        info = d.pop("info", UNSET)

        key = d.pop("key", UNSET)

        kind = d.pop("kind", UNSET)

        lock_id = d.pop("lockId", UNSET)

        mask = d.pop("mask", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        path = d.pop("path", UNSET)

        type = d.pop("type", UNSET)

        vt_rep = d.pop("vtRep", UNSET)

        i_date_iso = d.pop("IDateIso", UNSET)

        x_date_iso = d.pop("XDateIso", UNSET)

        access = d.pop("access", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        del_date_iso = d.pop("delDateIso", UNSET)

        deleted = d.pop("deleted", UNSET)

        desc = d.pop("desc", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, SordDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = SordDetails.from_dict(_details)

        _doc_version = d.pop("docVersion", UNSET)
        doc_version: Union[Unset, DocVersion]
        if isinstance(_doc_version, Unset):
            doc_version = UNSET
        else:
            doc_version = DocVersion.from_dict(_doc_version)

        hidden_text = d.pop("hiddenText", UNSET)

        links_come_in = []
        _links_come_in = d.pop("linksComeIn", UNSET)
        for links_come_in_item_data in _links_come_in or []:
            links_come_in_item = SordLink.from_dict(links_come_in_item_data)

            links_come_in.append(links_come_in_item)

        links_go_out = []
        _links_go_out = d.pop("linksGoOut", UNSET)
        for links_go_out_item_data in _links_go_out or []:
            links_go_out_item = SordLink.from_dict(links_go_out_item_data)

            links_go_out.append(links_go_out_item)

        lock_name = d.pop("lockName", UNSET)

        obj_keys = []
        _obj_keys = d.pop("objKeys", UNSET)
        for obj_keys_item_data in _obj_keys or []:
            obj_keys_item = ObjKey.from_dict(obj_keys_item_data)

            obj_keys.append(obj_keys_item)

        owner_name = d.pop("ownerName", UNSET)

        parent_ids = cast(List[str], d.pop("parentIds", UNSET))

        ref_paths = []
        _ref_paths = d.pop("refPaths", UNSET)
        for ref_paths_item_data in _ref_paths or []:
            ref_paths_item = ArcPath.from_dict(ref_paths_item_data)

            ref_paths.append(ref_paths_item)

        repl_names = []
        _repl_names = d.pop("replNames", UNSET)
        for repl_names_item_data in _repl_names or []:
            repl_names_item = ReplSetName.from_dict(repl_names_item_data)

            repl_names.append(repl_names_item)

        _repl_set = d.pop("replSet", UNSET)
        repl_set: Union[Unset, ReplSet]
        if isinstance(_repl_set, Unset):
            repl_set = UNSET
        else:
            repl_set = ReplSet.from_dict(_repl_set)

        mask_name = d.pop("maskName", UNSET)

        _att_version = d.pop("attVersion", UNSET)
        att_version: Union[Unset, DocVersion]
        if isinstance(_att_version, Unset):
            att_version = UNSET
        else:
            att_version = DocVersion.from_dict(_att_version)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        lock_id_sord = d.pop("lockIdSord", UNSET)

        lock_id_doc = d.pop("lockIdDoc", UNSET)

        lock_name_sord = d.pop("lockNameSord", UNSET)

        lock_name_doc = d.pop("lockNameDoc", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        t_stamp_acl = d.pop("TStampAcl", UNSET)

        t_stamp_acl_sync = d.pop("TStampAclSync", UNSET)

        delete_user = d.pop("deleteUser", UNSET)

        _aspects = d.pop("aspects", UNSET)
        aspects: Union[Unset, MapToListOfMapToIndexValue]
        if isinstance(_aspects, Unset):
            aspects = UNSET
        else:
            aspects = MapToListOfMapToIndexValue.from_dict(_aspects)

        region_id = d.pop("regionId", UNSET)

        sord = cls(
            s_reg=s_reg,
            t_stamp=t_stamp,
            acl=acl,
            att=att,
            child_count=child_count,
            doc=doc,
            guid=guid,
            hist_count=hist_count,
            id=id,
            info=info,
            key=key,
            kind=kind,
            lock_id=lock_id,
            mask=mask,
            name=name,
            owner_id=owner_id,
            parent_id=parent_id,
            path=path,
            type=type,
            vt_rep=vt_rep,
            i_date_iso=i_date_iso,
            x_date_iso=x_date_iso,
            access=access,
            acl_items=acl_items,
            del_date_iso=del_date_iso,
            deleted=deleted,
            desc=desc,
            details=details,
            doc_version=doc_version,
            hidden_text=hidden_text,
            links_come_in=links_come_in,
            links_go_out=links_go_out,
            lock_name=lock_name,
            obj_keys=obj_keys,
            owner_name=owner_name,
            parent_ids=parent_ids,
            ref_paths=ref_paths,
            repl_names=repl_names,
            repl_set=repl_set,
            mask_name=mask_name,
            att_version=att_version,
            delete_date_iso=delete_date_iso,
            lock_id_sord=lock_id_sord,
            lock_id_doc=lock_id_doc,
            lock_name_sord=lock_name_sord,
            lock_name_doc=lock_name_doc,
            t_stamp_sync=t_stamp_sync,
            t_stamp_acl=t_stamp_acl,
            t_stamp_acl_sync=t_stamp_acl_sync,
            delete_user=delete_user,
            aspects=aspects,
            region_id=region_id,
        )

        sord.additional_properties = d
        return sord

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
