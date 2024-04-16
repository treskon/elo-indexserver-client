from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidateCacheC")


@_attrs_define
class InvalidateCacheC:
    """Constants for cache invalidation.
    This constans can be used as bit combination in function
     invalidateCache.

        Attributes:
            all_ (Union[Unset, int]): Flag used to specify that all cached objects are invalid.
            workflows (Union[Unset, int]): Flag used to specify that the workflow cache is invalid.
            subscriptions (Union[Unset, int]): Flag used to specify that the subscription cache is invalid.
            aspects (Union[Unset, int]): Flag used to specify that the cached Aspect objects are invalid.
            markers (Union[Unset, int]): Flag used to specify that the cached ColorData objects are invalid.
            paths (Union[Unset, int]): Flag used to specify that the cached Path objects are invalid.
            hashtagcount (Union[Unset, int]): Flag used to specify that the hashtag count cache is invalid.
            session (Union[Unset, int]): Notify about modified session options or permissions. Reserved for internal usage.
            crypt_info (Union[Unset, int]): Flag used to specify that the cached crypt keys are invalid.
            note_and_cold_images (Union[Unset, int]): Flag used to specify that the note and cold background images are
                invalid.
            repl_names (Union[Unset, int]): Flag used to specify that the cached ReplName objects are invalid.
            keyword_lists (Union[Unset, int]): Notify about modified keyword lists.
            sord_types (Union[Unset, int]): Flag used to specify that the cached SordType objects are invalid.
            indexfield_display_data (Union[Unset, int]): Flag used to specify that the display data of references in index
                fields of type relation have
                changed.
            keys (Union[Unset, int]): Flag used to specify that the cached keys are invalid.
            objkey_display_data (Union[Unset, int]): Flag used to specify that the display data of references in ObjKeys
                have changed.
                Note: there
                 is a newer name for this constant flag: INDEXFIELD_DISPLAY_DATA. Please use the newer version
                 see below.
            translate_terms (Union[Unset, int]): Flag used to specify that the translate terms are invalid.
            document (Union[Unset, int]): Flag used to specify that a cached document (script) has changed.
            masks (Union[Unset, int]): Flag used to specify that the cached DocMask objects are invalid.
            users (Union[Unset, int]): Flag used to specify that the cached users are invalid.
            workspace_acls (Union[Unset, int]): Invalidate cache of workspace/teamspace ACLs.
            no_forward_to_other_ixs (Union[Unset, int]): Do not invalidate the caches of the other servers.
    """

    all_: Union[Unset, int] = UNSET
    workflows: Union[Unset, int] = UNSET
    subscriptions: Union[Unset, int] = UNSET
    aspects: Union[Unset, int] = UNSET
    markers: Union[Unset, int] = UNSET
    paths: Union[Unset, int] = UNSET
    hashtagcount: Union[Unset, int] = UNSET
    session: Union[Unset, int] = UNSET
    crypt_info: Union[Unset, int] = UNSET
    note_and_cold_images: Union[Unset, int] = UNSET
    repl_names: Union[Unset, int] = UNSET
    keyword_lists: Union[Unset, int] = UNSET
    sord_types: Union[Unset, int] = UNSET
    indexfield_display_data: Union[Unset, int] = UNSET
    keys: Union[Unset, int] = UNSET
    objkey_display_data: Union[Unset, int] = UNSET
    translate_terms: Union[Unset, int] = UNSET
    document: Union[Unset, int] = UNSET
    masks: Union[Unset, int] = UNSET
    users: Union[Unset, int] = UNSET
    workspace_acls: Union[Unset, int] = UNSET
    no_forward_to_other_ixs: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        all_ = self.all_

        workflows = self.workflows

        subscriptions = self.subscriptions

        aspects = self.aspects

        markers = self.markers

        paths = self.paths

        hashtagcount = self.hashtagcount

        session = self.session

        crypt_info = self.crypt_info

        note_and_cold_images = self.note_and_cold_images

        repl_names = self.repl_names

        keyword_lists = self.keyword_lists

        sord_types = self.sord_types

        indexfield_display_data = self.indexfield_display_data

        keys = self.keys

        objkey_display_data = self.objkey_display_data

        translate_terms = self.translate_terms

        document = self.document

        masks = self.masks

        users = self.users

        workspace_acls = self.workspace_acls

        no_forward_to_other_ixs = self.no_forward_to_other_ixs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["ALL"] = all_
        if workflows is not UNSET:
            field_dict["WORKFLOWS"] = workflows
        if subscriptions is not UNSET:
            field_dict["SUBSCRIPTIONS"] = subscriptions
        if aspects is not UNSET:
            field_dict["ASPECTS"] = aspects
        if markers is not UNSET:
            field_dict["MARKERS"] = markers
        if paths is not UNSET:
            field_dict["PATHS"] = paths
        if hashtagcount is not UNSET:
            field_dict["HASHTAGCOUNT"] = hashtagcount
        if session is not UNSET:
            field_dict["SESSION"] = session
        if crypt_info is not UNSET:
            field_dict["CRYPT_INFO"] = crypt_info
        if note_and_cold_images is not UNSET:
            field_dict["NOTE_AND_COLD_IMAGES"] = note_and_cold_images
        if repl_names is not UNSET:
            field_dict["REPL_NAMES"] = repl_names
        if keyword_lists is not UNSET:
            field_dict["KEYWORD_LISTS"] = keyword_lists
        if sord_types is not UNSET:
            field_dict["SORD_TYPES"] = sord_types
        if indexfield_display_data is not UNSET:
            field_dict["INDEXFIELD_DISPLAY_DATA"] = indexfield_display_data
        if keys is not UNSET:
            field_dict["KEYS"] = keys
        if objkey_display_data is not UNSET:
            field_dict["OBJKEY_DISPLAY_DATA"] = objkey_display_data
        if translate_terms is not UNSET:
            field_dict["TRANSLATE_TERMS"] = translate_terms
        if document is not UNSET:
            field_dict["DOCUMENT"] = document
        if masks is not UNSET:
            field_dict["MASKS"] = masks
        if users is not UNSET:
            field_dict["USERS"] = users
        if workspace_acls is not UNSET:
            field_dict["WORKSPACE_ACLS"] = workspace_acls
        if no_forward_to_other_ixs is not UNSET:
            field_dict["NO_FORWARD_TO_OTHER_IXS"] = no_forward_to_other_ixs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        all_ = d.pop("ALL", UNSET)

        workflows = d.pop("WORKFLOWS", UNSET)

        subscriptions = d.pop("SUBSCRIPTIONS", UNSET)

        aspects = d.pop("ASPECTS", UNSET)

        markers = d.pop("MARKERS", UNSET)

        paths = d.pop("PATHS", UNSET)

        hashtagcount = d.pop("HASHTAGCOUNT", UNSET)

        session = d.pop("SESSION", UNSET)

        crypt_info = d.pop("CRYPT_INFO", UNSET)

        note_and_cold_images = d.pop("NOTE_AND_COLD_IMAGES", UNSET)

        repl_names = d.pop("REPL_NAMES", UNSET)

        keyword_lists = d.pop("KEYWORD_LISTS", UNSET)

        sord_types = d.pop("SORD_TYPES", UNSET)

        indexfield_display_data = d.pop("INDEXFIELD_DISPLAY_DATA", UNSET)

        keys = d.pop("KEYS", UNSET)

        objkey_display_data = d.pop("OBJKEY_DISPLAY_DATA", UNSET)

        translate_terms = d.pop("TRANSLATE_TERMS", UNSET)

        document = d.pop("DOCUMENT", UNSET)

        masks = d.pop("MASKS", UNSET)

        users = d.pop("USERS", UNSET)

        workspace_acls = d.pop("WORKSPACE_ACLS", UNSET)

        no_forward_to_other_ixs = d.pop("NO_FORWARD_TO_OTHER_IXS", UNSET)

        invalidate_cache_c = cls(
            all_=all_,
            workflows=workflows,
            subscriptions=subscriptions,
            aspects=aspects,
            markers=markers,
            paths=paths,
            hashtagcount=hashtagcount,
            session=session,
            crypt_info=crypt_info,
            note_and_cold_images=note_and_cold_images,
            repl_names=repl_names,
            keyword_lists=keyword_lists,
            sord_types=sord_types,
            indexfield_display_data=indexfield_display_data,
            keys=keys,
            objkey_display_data=objkey_display_data,
            translate_terms=translate_terms,
            document=document,
            masks=masks,
            users=users,
            workspace_acls=workspace_acls,
            no_forward_to_other_ixs=no_forward_to_other_ixs,
        )

        invalidate_cache_c.additional_properties = d
        return invalidate_cache_c

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
