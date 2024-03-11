from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidateCacheC")


@_attrs_define
class InvalidateCacheC:
    """Constants for cache invalidation. This constans can be used as bit combination in function invalidateCache.

    Attributes:
        masks (Union[Unset, int]): Flag used to specify that the cached DocMask objects are invalid.
        markers (Union[Unset, int]): Flag used to specify that the cached ColorData objects are invalid.
        paths (Union[Unset, int]): Flag used to specify that the cached Path objects are invalid.
        sord_types (Union[Unset, int]): Flag used to specify that the cached SordType objects are invalid.
        repl_names (Union[Unset, int]): Flag used to specify that the cached ReplName objects are invalid.
        crypt_info (Union[Unset, int]): Flag used to specify that the cached crypt keys are invalid.
        users (Union[Unset, int]): Flag used to specify that the cached users are invalid.
        keys (Union[Unset, int]): Flag used to specify that the cached keys are invalid.
        translate_terms (Union[Unset, int]): Flag used to specify that the translate terms are invalid.
        note_and_cold_images (Union[Unset, int]): Flag used to specify that the note and cold background images are
            invalid.
        workflows (Union[Unset, int]): Flag used to specify that the workflow cache is invalid.
        subscriptions (Union[Unset, int]): Flag used to specify that the subscription cache is invalid.
        hashtagcount (Union[Unset, int]): Flag used to specify that the hashtag count cache is invalid.
        objkey_display_data (Union[Unset, int]): Flag used to specify that the display data of references in ObjKeys
            have changed.
        document (Union[Unset, int]): Flag used to specify that a cached document (script) has changed.
        aspects (Union[Unset, int]): Flag used to specify that the cached Aspect objects are invalid.
        no_forward_to_other_ixs (Union[Unset, int]): Do not invalidate the caches of the other servers.
        session (Union[Unset, int]): Notify about modified session options or permissions. Reserved for internal usage.
        all_ (Union[Unset, int]): Flag used to specify that all cached objects are invalid.
    """

    masks: Union[Unset, int] = UNSET
    markers: Union[Unset, int] = UNSET
    paths: Union[Unset, int] = UNSET
    sord_types: Union[Unset, int] = UNSET
    repl_names: Union[Unset, int] = UNSET
    crypt_info: Union[Unset, int] = UNSET
    users: Union[Unset, int] = UNSET
    keys: Union[Unset, int] = UNSET
    translate_terms: Union[Unset, int] = UNSET
    note_and_cold_images: Union[Unset, int] = UNSET
    workflows: Union[Unset, int] = UNSET
    subscriptions: Union[Unset, int] = UNSET
    hashtagcount: Union[Unset, int] = UNSET
    objkey_display_data: Union[Unset, int] = UNSET
    document: Union[Unset, int] = UNSET
    aspects: Union[Unset, int] = UNSET
    no_forward_to_other_ixs: Union[Unset, int] = UNSET
    session: Union[Unset, int] = UNSET
    all_: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        masks = self.masks
        markers = self.markers
        paths = self.paths
        sord_types = self.sord_types
        repl_names = self.repl_names
        crypt_info = self.crypt_info
        users = self.users
        keys = self.keys
        translate_terms = self.translate_terms
        note_and_cold_images = self.note_and_cold_images
        workflows = self.workflows
        subscriptions = self.subscriptions
        hashtagcount = self.hashtagcount
        objkey_display_data = self.objkey_display_data
        document = self.document
        aspects = self.aspects
        no_forward_to_other_ixs = self.no_forward_to_other_ixs
        session = self.session
        all_ = self.all_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if masks is not UNSET:
            field_dict["MASKS"] = masks
        if markers is not UNSET:
            field_dict["MARKERS"] = markers
        if paths is not UNSET:
            field_dict["PATHS"] = paths
        if sord_types is not UNSET:
            field_dict["SORD_TYPES"] = sord_types
        if repl_names is not UNSET:
            field_dict["REPL_NAMES"] = repl_names
        if crypt_info is not UNSET:
            field_dict["CRYPT_INFO"] = crypt_info
        if users is not UNSET:
            field_dict["USERS"] = users
        if keys is not UNSET:
            field_dict["KEYS"] = keys
        if translate_terms is not UNSET:
            field_dict["TRANSLATE_TERMS"] = translate_terms
        if note_and_cold_images is not UNSET:
            field_dict["NOTE_AND_COLD_IMAGES"] = note_and_cold_images
        if workflows is not UNSET:
            field_dict["WORKFLOWS"] = workflows
        if subscriptions is not UNSET:
            field_dict["SUBSCRIPTIONS"] = subscriptions
        if hashtagcount is not UNSET:
            field_dict["HASHTAGCOUNT"] = hashtagcount
        if objkey_display_data is not UNSET:
            field_dict["OBJKEY_DISPLAY_DATA"] = objkey_display_data
        if document is not UNSET:
            field_dict["DOCUMENT"] = document
        if aspects is not UNSET:
            field_dict["ASPECTS"] = aspects
        if no_forward_to_other_ixs is not UNSET:
            field_dict["NO_FORWARD_TO_OTHER_IXS"] = no_forward_to_other_ixs
        if session is not UNSET:
            field_dict["SESSION"] = session
        if all_ is not UNSET:
            field_dict["ALL"] = all_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        masks = d.pop("MASKS", UNSET)

        markers = d.pop("MARKERS", UNSET)

        paths = d.pop("PATHS", UNSET)

        sord_types = d.pop("SORD_TYPES", UNSET)

        repl_names = d.pop("REPL_NAMES", UNSET)

        crypt_info = d.pop("CRYPT_INFO", UNSET)

        users = d.pop("USERS", UNSET)

        keys = d.pop("KEYS", UNSET)

        translate_terms = d.pop("TRANSLATE_TERMS", UNSET)

        note_and_cold_images = d.pop("NOTE_AND_COLD_IMAGES", UNSET)

        workflows = d.pop("WORKFLOWS", UNSET)

        subscriptions = d.pop("SUBSCRIPTIONS", UNSET)

        hashtagcount = d.pop("HASHTAGCOUNT", UNSET)

        objkey_display_data = d.pop("OBJKEY_DISPLAY_DATA", UNSET)

        document = d.pop("DOCUMENT", UNSET)

        aspects = d.pop("ASPECTS", UNSET)

        no_forward_to_other_ixs = d.pop("NO_FORWARD_TO_OTHER_IXS", UNSET)

        session = d.pop("SESSION", UNSET)

        all_ = d.pop("ALL", UNSET)

        invalidate_cache_c = cls(
            masks=masks,
            markers=markers,
            paths=paths,
            sord_types=sord_types,
            repl_names=repl_names,
            crypt_info=crypt_info,
            users=users,
            keys=keys,
            translate_terms=translate_terms,
            note_and_cold_images=note_and_cold_images,
            workflows=workflows,
            subscriptions=subscriptions,
            hashtagcount=hashtagcount,
            objkey_display_data=objkey_display_data,
            document=document,
            aspects=aspects,
            no_forward_to_other_ixs=no_forward_to_other_ixs,
            session=session,
            all_=all_,
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
