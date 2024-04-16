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
            del_date_iso (Union[Unset, str]): ISO encoded expiry date. Only users having right AccessC.
                FLAG_EDITDUEDATE are allowed to set
                 the expiry date. Once the expiry date is set, it cannot be set to a date before the original
                 expiry date.
            acl (Union[Unset, str]): Access control language in coded form. The checkInSord method must set either acl or
                aclItems.
                aclItems has priority.
            owner_id (Union[Unset, int]): The id of the owner of the object.
                Main-administrators can assign an owner ID for new Sords in
                 {@link IXServicePortIF#checkinSord(ClientInfo, Sord, SordZ, LockZ)} and
                 {@link IXServicePortIF#checkinSordPath(ClientInfo, String, Sord[], SordZ)}. This member is
                 read-only for Non-adminstrators or existing Sords.
            type (Union[Unset, int]): The type of sord object.
                Folder objects: 0 &lt; type &lt; LBT_DOCUMENT Document objects:
                 LBT_DOCUMENT &lt;= type &lt; LBT_DOCUMENT_MAX
            obj_keys (Union[Unset, List['ObjKey']]):
            path (Union[Unset, int]): Filing path for the document manager. Only valid for documents. Read-only.
                <p>
                 If this Sord object is obtained by a call to checkoutSord or checkoutDoc with a database lock
                 (e.g. LockC.IF_FREE), this member contains the storage path specified in the associated
                 keywording form (DocMask.DPath). If the keywording form does not define a path, the default
                 storage path is returned (ServerInfoDM.basisStoreIds[0]). Hence, the current value of the
                 database column objekte.objpath is not used as default for new versions anymore.
                 </p>
                 <p>
                 If this Sord object is obtained by a call without a lock, e.g. from findFirstSords, this value
                 should not be used anymore. The storage path of the work version should be used instead, which
                 can be found in Sord.docVersion.pathId.
                 </p>
            details (Union[Unset, SordDetails]): Objects of this class are data elements and control the values assigned to
                certain boolean
                properties(yes/no attributes).

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            id (Union[Unset, int]): Numeric ID.
            i_date_iso (Union[Unset, str]): ISO encoded internal (archive defined) date.
            lock_name (Union[Unset, str]): The name of the user who has locked the object. Read-only.
            doc_version (Union[Unset, DocVersion]): <p>
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
            info (Union[Unset, int]): RESERVED
            att (Union[Unset, int]): Id of the current attachment version. Read-only.
            ref_paths (Union[Unset, List['ArcPath']]):
            kind (Union[Unset, int]): Colour
            hidden_text (Union[Unset, str]): Hidden text that must not be displayed to the user.
            lock_name_sord (Union[Unset, str]): The name of the user who has locked the object. Read-only.
            lock_id (Union[Unset, int]): This is the id of the user who has a lock on the object.
                To know whether the Sord or the
                 Document is locked, see lockIdSord or lockIdDoc respectively. The object is locked using
                 checkoutSord with the LOCK.YES, LOCK.SORD or LOCK.DOC parameter. Read-only.
            space_guid (Union[Unset, str]): If the sord belongs to a workspace, this value contains the GUID of that
                workspace.
            acl_items (Union[Unset, List['AclItem']]):
            name (Union[Unset, str]): The short description/name for the object.
            delete_user (Union[Unset, int]): The Sord is deleted at this user.
                <p>
                 Is undefined if isDeleted() returns false.
                 </p>
            doc (Union[Unset, int]): Read-only. Id of the current document version.
            guid (Union[Unset, str]): GUID.
            t_stamp_acl (Union[Unset, str]): Timestamp of the last ACL change. The format is JJJJ.MM.DD.hh.mm.
                ss
            desc (Union[Unset, str]): The (visible) memo text.
                If the value starts with a "!" this member can define a dynamic
                 folder. This is a folder which contents are filled by an arbitrary SQL statement.
            lock_name_doc (Union[Unset, str]): The name of the user who has locked the document. Read-only.
            access (Union[Unset, int]): The current users access rights for this Sord. Returns a combination of AccessC.LUR_
                constants. Read-only.
                Is
                 returned when SordC.mbAcl is set in checkoutSord.
            t_stamp_acl_sync (Union[Unset, str]): Timestamp of this object's ACLs last export by the replication.
            parent_ids (Union[Unset, List[str]]):
            aspects (Union[Unset, MapToListOfMapToIndexValue]):
            vt_rep (Union[Unset, int]): RESERVED
            repl_set (Union[Unset, ReplSet]): <p>
                Objects of this class store the replication information of archive entries.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            t_stamp (Union[Unset, str]): Timestamp of the last change. The format is JJJJ.MM.DD.hh.mm.
                ss
            links_come_in (Union[Unset, List['SordLink']]):
            owner_name (Union[Unset, str]): Name of the owner (read-only).
            t_stamp_sync (Union[Unset, str]): Timestamp of this object's last export by the replication.
            repl_names (Union[Unset, List['ReplSetName']]):
            x_date_iso (Union[Unset, str]): ISO encoded external (user defined) date.
            package_name (Union[Unset, str]): Package name of sord
            key (Union[Unset, int]): RESERVED
            mask (Union[Unset, int]): The id of the filing mask used to archive the sord. Read-only.
            lock_id_doc (Union[Unset, int]): This is the id of the user who has a lock on the document (not the object).
                The object is
                 locked using checkoutSord with the LOCK.DOC parameter. Read-only.
            lock_id_sord (Union[Unset, int]): This is the id of the user who has a lock on the object (not the document).
                The object is
                 locked using checkoutSord with the LOCK.SORD parameter. Read-only.
            hist_count (Union[Unset, int]): Number of document versions.
            space_guids (Union[Unset, List[str]]):
            s_reg (Union[Unset, str]): Version numer of the current work version.
            child_count (Union[Unset, int]): Estimated sum of the sub-entries in a directory.
                This does not take account of any access
                 rights assigned to the entries. This property should only be used to determine whether the
                 directory has additional entries. Read-only.
            t_stamp_local (Union[Unset, str]): Timestamp that indicates the next iSearch Index run The format is
                JJJJ.MM.DD.hh.mm.
                ss
            parent_id (Union[Unset, int]): Id of the parent object(archive heirachy) of the sord object.
                Read-only
            links_go_out (Union[Unset, List['SordLink']]):
            deleted (Union[Unset, bool]): Indicates whether the sord has been deleted or not.
            mask_name (Union[Unset, str]): Name of keywording form.
                This value is translated into the language given by
                 {@link ClientInfo#language}. It cannot be used as a parameter in Indexserver API functions. Use
                 {@link Sord#getMask()} to specify the Keywording form in API functions. Read-only.
            region_id (Union[Unset, int]): This is a RESERVED field for future use. Do not use.
                <br>
                 If the sord is contained in a region (i.e. lies below an object in archive tree that has an
                 associated keywording form which defines a region), this value contains the numeric Id of that
                 region sord. This value is only valid, if the associated keywording form {@link DocMask} is
                 organized as {@link DocMask#dataOrganisation} = {@link DocMaskC#DATA_ORGANISATION_ASPECT}.
            att_version (Union[Unset, DocVersion]): <p>
                Description: This class describes a document version, a document preview or a signature.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2002
                 </p>
                 <p>
                 Organisation: ELO DIgital Office GmbH
                 </p>
    """

    del_date_iso: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    type: Union[Unset, int] = UNSET
    obj_keys: Union[Unset, List["ObjKey"]] = UNSET
    path: Union[Unset, int] = UNSET
    details: Union[Unset, "SordDetails"] = UNSET
    id: Union[Unset, int] = UNSET
    i_date_iso: Union[Unset, str] = UNSET
    lock_name: Union[Unset, str] = UNSET
    doc_version: Union[Unset, "DocVersion"] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    info: Union[Unset, int] = UNSET
    att: Union[Unset, int] = UNSET
    ref_paths: Union[Unset, List["ArcPath"]] = UNSET
    kind: Union[Unset, int] = UNSET
    hidden_text: Union[Unset, str] = UNSET
    lock_name_sord: Union[Unset, str] = UNSET
    lock_id: Union[Unset, int] = UNSET
    space_guid: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    delete_user: Union[Unset, int] = UNSET
    doc: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    t_stamp_acl: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    lock_name_doc: Union[Unset, str] = UNSET
    access: Union[Unset, int] = UNSET
    t_stamp_acl_sync: Union[Unset, str] = UNSET
    parent_ids: Union[Unset, List[str]] = UNSET
    aspects: Union[Unset, "MapToListOfMapToIndexValue"] = UNSET
    vt_rep: Union[Unset, int] = UNSET
    repl_set: Union[Unset, "ReplSet"] = UNSET
    t_stamp: Union[Unset, str] = UNSET
    links_come_in: Union[Unset, List["SordLink"]] = UNSET
    owner_name: Union[Unset, str] = UNSET
    t_stamp_sync: Union[Unset, str] = UNSET
    repl_names: Union[Unset, List["ReplSetName"]] = UNSET
    x_date_iso: Union[Unset, str] = UNSET
    package_name: Union[Unset, str] = UNSET
    key: Union[Unset, int] = UNSET
    mask: Union[Unset, int] = UNSET
    lock_id_doc: Union[Unset, int] = UNSET
    lock_id_sord: Union[Unset, int] = UNSET
    hist_count: Union[Unset, int] = UNSET
    space_guids: Union[Unset, List[str]] = UNSET
    s_reg: Union[Unset, str] = UNSET
    child_count: Union[Unset, int] = UNSET
    t_stamp_local: Union[Unset, str] = UNSET
    parent_id: Union[Unset, int] = UNSET
    links_go_out: Union[Unset, List["SordLink"]] = UNSET
    deleted: Union[Unset, bool] = UNSET
    mask_name: Union[Unset, str] = UNSET
    region_id: Union[Unset, int] = UNSET
    att_version: Union[Unset, "DocVersion"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        del_date_iso = self.del_date_iso

        acl = self.acl

        owner_id = self.owner_id

        type = self.type

        obj_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.obj_keys, Unset):
            obj_keys = []
            for obj_keys_item_data in self.obj_keys:
                obj_keys_item = obj_keys_item_data.to_dict()
                obj_keys.append(obj_keys_item)

        path = self.path

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        id = self.id

        i_date_iso = self.i_date_iso

        lock_name = self.lock_name

        doc_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_version, Unset):
            doc_version = self.doc_version.to_dict()

        delete_date_iso = self.delete_date_iso

        info = self.info

        att = self.att

        ref_paths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ref_paths, Unset):
            ref_paths = []
            for ref_paths_item_data in self.ref_paths:
                ref_paths_item = ref_paths_item_data.to_dict()
                ref_paths.append(ref_paths_item)

        kind = self.kind

        hidden_text = self.hidden_text

        lock_name_sord = self.lock_name_sord

        lock_id = self.lock_id

        space_guid = self.space_guid

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        name = self.name

        delete_user = self.delete_user

        doc = self.doc

        guid = self.guid

        t_stamp_acl = self.t_stamp_acl

        desc = self.desc

        lock_name_doc = self.lock_name_doc

        access = self.access

        t_stamp_acl_sync = self.t_stamp_acl_sync

        parent_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parent_ids, Unset):
            parent_ids = self.parent_ids

        aspects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspects, Unset):
            aspects = self.aspects.to_dict()

        vt_rep = self.vt_rep

        repl_set: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repl_set, Unset):
            repl_set = self.repl_set.to_dict()

        t_stamp = self.t_stamp

        links_come_in: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links_come_in, Unset):
            links_come_in = []
            for links_come_in_item_data in self.links_come_in:
                links_come_in_item = links_come_in_item_data.to_dict()
                links_come_in.append(links_come_in_item)

        owner_name = self.owner_name

        t_stamp_sync = self.t_stamp_sync

        repl_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.repl_names, Unset):
            repl_names = []
            for repl_names_item_data in self.repl_names:
                repl_names_item = repl_names_item_data.to_dict()
                repl_names.append(repl_names_item)

        x_date_iso = self.x_date_iso

        package_name = self.package_name

        key = self.key

        mask = self.mask

        lock_id_doc = self.lock_id_doc

        lock_id_sord = self.lock_id_sord

        hist_count = self.hist_count

        space_guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.space_guids, Unset):
            space_guids = self.space_guids

        s_reg = self.s_reg

        child_count = self.child_count

        t_stamp_local = self.t_stamp_local

        parent_id = self.parent_id

        links_go_out: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links_go_out, Unset):
            links_go_out = []
            for links_go_out_item_data in self.links_go_out:
                links_go_out_item = links_go_out_item_data.to_dict()
                links_go_out.append(links_go_out_item)

        deleted = self.deleted

        mask_name = self.mask_name

        region_id = self.region_id

        att_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.att_version, Unset):
            att_version = self.att_version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if del_date_iso is not UNSET:
            field_dict["delDateIso"] = del_date_iso
        if acl is not UNSET:
            field_dict["acl"] = acl
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if type is not UNSET:
            field_dict["type"] = type
        if obj_keys is not UNSET:
            field_dict["objKeys"] = obj_keys
        if path is not UNSET:
            field_dict["path"] = path
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if i_date_iso is not UNSET:
            field_dict["IDateIso"] = i_date_iso
        if lock_name is not UNSET:
            field_dict["lockName"] = lock_name
        if doc_version is not UNSET:
            field_dict["docVersion"] = doc_version
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso
        if info is not UNSET:
            field_dict["info"] = info
        if att is not UNSET:
            field_dict["att"] = att
        if ref_paths is not UNSET:
            field_dict["refPaths"] = ref_paths
        if kind is not UNSET:
            field_dict["kind"] = kind
        if hidden_text is not UNSET:
            field_dict["hiddenText"] = hidden_text
        if lock_name_sord is not UNSET:
            field_dict["lockNameSord"] = lock_name_sord
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if space_guid is not UNSET:
            field_dict["spaceGuid"] = space_guid
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if name is not UNSET:
            field_dict["name"] = name
        if delete_user is not UNSET:
            field_dict["deleteUser"] = delete_user
        if doc is not UNSET:
            field_dict["doc"] = doc
        if guid is not UNSET:
            field_dict["guid"] = guid
        if t_stamp_acl is not UNSET:
            field_dict["TStampAcl"] = t_stamp_acl
        if desc is not UNSET:
            field_dict["desc"] = desc
        if lock_name_doc is not UNSET:
            field_dict["lockNameDoc"] = lock_name_doc
        if access is not UNSET:
            field_dict["access"] = access
        if t_stamp_acl_sync is not UNSET:
            field_dict["TStampAclSync"] = t_stamp_acl_sync
        if parent_ids is not UNSET:
            field_dict["parentIds"] = parent_ids
        if aspects is not UNSET:
            field_dict["aspects"] = aspects
        if vt_rep is not UNSET:
            field_dict["vtRep"] = vt_rep
        if repl_set is not UNSET:
            field_dict["replSet"] = repl_set
        if t_stamp is not UNSET:
            field_dict["TStamp"] = t_stamp
        if links_come_in is not UNSET:
            field_dict["linksComeIn"] = links_come_in
        if owner_name is not UNSET:
            field_dict["ownerName"] = owner_name
        if t_stamp_sync is not UNSET:
            field_dict["TStampSync"] = t_stamp_sync
        if repl_names is not UNSET:
            field_dict["replNames"] = repl_names
        if x_date_iso is not UNSET:
            field_dict["XDateIso"] = x_date_iso
        if package_name is not UNSET:
            field_dict["packageName"] = package_name
        if key is not UNSET:
            field_dict["key"] = key
        if mask is not UNSET:
            field_dict["mask"] = mask
        if lock_id_doc is not UNSET:
            field_dict["lockIdDoc"] = lock_id_doc
        if lock_id_sord is not UNSET:
            field_dict["lockIdSord"] = lock_id_sord
        if hist_count is not UNSET:
            field_dict["histCount"] = hist_count
        if space_guids is not UNSET:
            field_dict["spaceGuids"] = space_guids
        if s_reg is not UNSET:
            field_dict["SReg"] = s_reg
        if child_count is not UNSET:
            field_dict["childCount"] = child_count
        if t_stamp_local is not UNSET:
            field_dict["TStampLocal"] = t_stamp_local
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if links_go_out is not UNSET:
            field_dict["linksGoOut"] = links_go_out
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if mask_name is not UNSET:
            field_dict["maskName"] = mask_name
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if att_version is not UNSET:
            field_dict["attVersion"] = att_version

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
        del_date_iso = d.pop("delDateIso", UNSET)

        acl = d.pop("acl", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        type = d.pop("type", UNSET)

        obj_keys = []
        _obj_keys = d.pop("objKeys", UNSET)
        for obj_keys_item_data in _obj_keys or []:
            obj_keys_item = ObjKey.from_dict(obj_keys_item_data)

            obj_keys.append(obj_keys_item)

        path = d.pop("path", UNSET)

        _details = d.pop("details", UNSET)
        details: Union[Unset, SordDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = SordDetails.from_dict(_details)

        id = d.pop("id", UNSET)

        i_date_iso = d.pop("IDateIso", UNSET)

        lock_name = d.pop("lockName", UNSET)

        _doc_version = d.pop("docVersion", UNSET)
        doc_version: Union[Unset, DocVersion]
        if isinstance(_doc_version, Unset):
            doc_version = UNSET
        else:
            doc_version = DocVersion.from_dict(_doc_version)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        info = d.pop("info", UNSET)

        att = d.pop("att", UNSET)

        ref_paths = []
        _ref_paths = d.pop("refPaths", UNSET)
        for ref_paths_item_data in _ref_paths or []:
            ref_paths_item = ArcPath.from_dict(ref_paths_item_data)

            ref_paths.append(ref_paths_item)

        kind = d.pop("kind", UNSET)

        hidden_text = d.pop("hiddenText", UNSET)

        lock_name_sord = d.pop("lockNameSord", UNSET)

        lock_id = d.pop("lockId", UNSET)

        space_guid = d.pop("spaceGuid", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        name = d.pop("name", UNSET)

        delete_user = d.pop("deleteUser", UNSET)

        doc = d.pop("doc", UNSET)

        guid = d.pop("guid", UNSET)

        t_stamp_acl = d.pop("TStampAcl", UNSET)

        desc = d.pop("desc", UNSET)

        lock_name_doc = d.pop("lockNameDoc", UNSET)

        access = d.pop("access", UNSET)

        t_stamp_acl_sync = d.pop("TStampAclSync", UNSET)

        parent_ids = cast(List[str], d.pop("parentIds", UNSET))

        _aspects = d.pop("aspects", UNSET)
        aspects: Union[Unset, MapToListOfMapToIndexValue]
        if isinstance(_aspects, Unset):
            aspects = UNSET
        else:
            aspects = MapToListOfMapToIndexValue.from_dict(_aspects)

        vt_rep = d.pop("vtRep", UNSET)

        _repl_set = d.pop("replSet", UNSET)
        repl_set: Union[Unset, ReplSet]
        if isinstance(_repl_set, Unset):
            repl_set = UNSET
        else:
            repl_set = ReplSet.from_dict(_repl_set)

        t_stamp = d.pop("TStamp", UNSET)

        links_come_in = []
        _links_come_in = d.pop("linksComeIn", UNSET)
        for links_come_in_item_data in _links_come_in or []:
            links_come_in_item = SordLink.from_dict(links_come_in_item_data)

            links_come_in.append(links_come_in_item)

        owner_name = d.pop("ownerName", UNSET)

        t_stamp_sync = d.pop("TStampSync", UNSET)

        repl_names = []
        _repl_names = d.pop("replNames", UNSET)
        for repl_names_item_data in _repl_names or []:
            repl_names_item = ReplSetName.from_dict(repl_names_item_data)

            repl_names.append(repl_names_item)

        x_date_iso = d.pop("XDateIso", UNSET)

        package_name = d.pop("packageName", UNSET)

        key = d.pop("key", UNSET)

        mask = d.pop("mask", UNSET)

        lock_id_doc = d.pop("lockIdDoc", UNSET)

        lock_id_sord = d.pop("lockIdSord", UNSET)

        hist_count = d.pop("histCount", UNSET)

        space_guids = cast(List[str], d.pop("spaceGuids", UNSET))

        s_reg = d.pop("SReg", UNSET)

        child_count = d.pop("childCount", UNSET)

        t_stamp_local = d.pop("TStampLocal", UNSET)

        parent_id = d.pop("parentId", UNSET)

        links_go_out = []
        _links_go_out = d.pop("linksGoOut", UNSET)
        for links_go_out_item_data in _links_go_out or []:
            links_go_out_item = SordLink.from_dict(links_go_out_item_data)

            links_go_out.append(links_go_out_item)

        deleted = d.pop("deleted", UNSET)

        mask_name = d.pop("maskName", UNSET)

        region_id = d.pop("regionId", UNSET)

        _att_version = d.pop("attVersion", UNSET)
        att_version: Union[Unset, DocVersion]
        if isinstance(_att_version, Unset):
            att_version = UNSET
        else:
            att_version = DocVersion.from_dict(_att_version)

        sord = cls(
            del_date_iso=del_date_iso,
            acl=acl,
            owner_id=owner_id,
            type=type,
            obj_keys=obj_keys,
            path=path,
            details=details,
            id=id,
            i_date_iso=i_date_iso,
            lock_name=lock_name,
            doc_version=doc_version,
            delete_date_iso=delete_date_iso,
            info=info,
            att=att,
            ref_paths=ref_paths,
            kind=kind,
            hidden_text=hidden_text,
            lock_name_sord=lock_name_sord,
            lock_id=lock_id,
            space_guid=space_guid,
            acl_items=acl_items,
            name=name,
            delete_user=delete_user,
            doc=doc,
            guid=guid,
            t_stamp_acl=t_stamp_acl,
            desc=desc,
            lock_name_doc=lock_name_doc,
            access=access,
            t_stamp_acl_sync=t_stamp_acl_sync,
            parent_ids=parent_ids,
            aspects=aspects,
            vt_rep=vt_rep,
            repl_set=repl_set,
            t_stamp=t_stamp,
            links_come_in=links_come_in,
            owner_name=owner_name,
            t_stamp_sync=t_stamp_sync,
            repl_names=repl_names,
            x_date_iso=x_date_iso,
            package_name=package_name,
            key=key,
            mask=mask,
            lock_id_doc=lock_id_doc,
            lock_id_sord=lock_id_sord,
            hist_count=hist_count,
            space_guids=space_guids,
            s_reg=s_reg,
            child_count=child_count,
            t_stamp_local=t_stamp_local,
            parent_id=parent_id,
            links_go_out=links_go_out,
            deleted=deleted,
            mask_name=mask_name,
            region_id=region_id,
            att_version=att_version,
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
