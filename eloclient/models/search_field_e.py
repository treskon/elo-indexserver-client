from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchFieldE")


@_attrs_define
class SearchFieldE:
    """<p>
    Use this class of constants to define in which field should be searched or aggregated.
     </p>
     <p>
     For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
     type is incorrect.
     </p>

        Attributes:
            feed_reference (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            i_date (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_author (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_text (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            sord_hash (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            owner_id (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            obj_id (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            mask_id (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_hashtag (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_date_updated (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            owner_name (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            version_number (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            timestamp (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_mention (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_type (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            extra_text (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            deleted_date (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            version_owner_id (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            filename (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            type (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            feed_date_created (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            file_extension (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            document_size (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            guid (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            parent_guid (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            x_date (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            version_comment (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            space_guids (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            fulltext (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            indexfield (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            title (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
            mask_name (Union[Unset, SearchFieldE]): <p>
                Use this class of constants to define in which field should be searched or aggregated.
                 </p>
                 <p>
                 For every option, allowed {@link FieldTypeE} is given which is also the fallback type if provided
                 type is incorrect.
                 </p>
    """

    feed_reference: Union[Unset, "SearchFieldE"] = UNSET
    i_date: Union[Unset, "SearchFieldE"] = UNSET
    feed_author: Union[Unset, "SearchFieldE"] = UNSET
    feed_text: Union[Unset, "SearchFieldE"] = UNSET
    sord_hash: Union[Unset, "SearchFieldE"] = UNSET
    owner_id: Union[Unset, "SearchFieldE"] = UNSET
    obj_id: Union[Unset, "SearchFieldE"] = UNSET
    mask_id: Union[Unset, "SearchFieldE"] = UNSET
    feed_hashtag: Union[Unset, "SearchFieldE"] = UNSET
    feed_date_updated: Union[Unset, "SearchFieldE"] = UNSET
    owner_name: Union[Unset, "SearchFieldE"] = UNSET
    version_number: Union[Unset, "SearchFieldE"] = UNSET
    timestamp: Union[Unset, "SearchFieldE"] = UNSET
    feed_mention: Union[Unset, "SearchFieldE"] = UNSET
    feed_type: Union[Unset, "SearchFieldE"] = UNSET
    extra_text: Union[Unset, "SearchFieldE"] = UNSET
    deleted_date: Union[Unset, "SearchFieldE"] = UNSET
    version_owner_id: Union[Unset, "SearchFieldE"] = UNSET
    filename: Union[Unset, "SearchFieldE"] = UNSET
    type: Union[Unset, "SearchFieldE"] = UNSET
    feed_date_created: Union[Unset, "SearchFieldE"] = UNSET
    file_extension: Union[Unset, "SearchFieldE"] = UNSET
    document_size: Union[Unset, "SearchFieldE"] = UNSET
    guid: Union[Unset, "SearchFieldE"] = UNSET
    parent_guid: Union[Unset, "SearchFieldE"] = UNSET
    x_date: Union[Unset, "SearchFieldE"] = UNSET
    version_comment: Union[Unset, "SearchFieldE"] = UNSET
    space_guids: Union[Unset, "SearchFieldE"] = UNSET
    fulltext: Union[Unset, "SearchFieldE"] = UNSET
    indexfield: Union[Unset, "SearchFieldE"] = UNSET
    title: Union[Unset, "SearchFieldE"] = UNSET
    mask_name: Union[Unset, "SearchFieldE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feed_reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_reference, Unset):
            feed_reference = self.feed_reference.to_dict()

        i_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.i_date, Unset):
            i_date = self.i_date.to_dict()

        feed_author: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_author, Unset):
            feed_author = self.feed_author.to_dict()

        feed_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_text, Unset):
            feed_text = self.feed_text.to_dict()

        sord_hash: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_hash, Unset):
            sord_hash = self.sord_hash.to_dict()

        owner_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_id, Unset):
            owner_id = self.owner_id.to_dict()

        obj_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.obj_id, Unset):
            obj_id = self.obj_id.to_dict()

        mask_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mask_id, Unset):
            mask_id = self.mask_id.to_dict()

        feed_hashtag: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_hashtag, Unset):
            feed_hashtag = self.feed_hashtag.to_dict()

        feed_date_updated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_date_updated, Unset):
            feed_date_updated = self.feed_date_updated.to_dict()

        owner_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner_name, Unset):
            owner_name = self.owner_name.to_dict()

        version_number: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version_number, Unset):
            version_number = self.version_number.to_dict()

        timestamp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.to_dict()

        feed_mention: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_mention, Unset):
            feed_mention = self.feed_mention.to_dict()

        feed_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_type, Unset):
            feed_type = self.feed_type.to_dict()

        extra_text: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.extra_text, Unset):
            extra_text = self.extra_text.to_dict()

        deleted_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.deleted_date, Unset):
            deleted_date = self.deleted_date.to_dict()

        version_owner_id: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version_owner_id, Unset):
            version_owner_id = self.version_owner_id.to_dict()

        filename: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filename, Unset):
            filename = self.filename.to_dict()

        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        feed_date_created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_date_created, Unset):
            feed_date_created = self.feed_date_created.to_dict()

        file_extension: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_extension, Unset):
            file_extension = self.file_extension.to_dict()

        document_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document_size, Unset):
            document_size = self.document_size.to_dict()

        guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guid, Unset):
            guid = self.guid.to_dict()

        parent_guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_guid, Unset):
            parent_guid = self.parent_guid.to_dict()

        x_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.x_date, Unset):
            x_date = self.x_date.to_dict()

        version_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version_comment, Unset):
            version_comment = self.version_comment.to_dict()

        space_guids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.space_guids, Unset):
            space_guids = self.space_guids.to_dict()

        fulltext: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fulltext, Unset):
            fulltext = self.fulltext.to_dict()

        indexfield: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indexfield, Unset):
            indexfield = self.indexfield.to_dict()

        title: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.title, Unset):
            title = self.title.to_dict()

        mask_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mask_name, Unset):
            mask_name = self.mask_name.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if feed_reference is not UNSET:
            field_dict["FEED_REFERENCE"] = feed_reference
        if i_date is not UNSET:
            field_dict["I_DATE"] = i_date
        if feed_author is not UNSET:
            field_dict["FEED_AUTHOR"] = feed_author
        if feed_text is not UNSET:
            field_dict["FEED_TEXT"] = feed_text
        if sord_hash is not UNSET:
            field_dict["SORD_HASH"] = sord_hash
        if owner_id is not UNSET:
            field_dict["OWNER_ID"] = owner_id
        if obj_id is not UNSET:
            field_dict["OBJ_ID"] = obj_id
        if mask_id is not UNSET:
            field_dict["MASK_ID"] = mask_id
        if feed_hashtag is not UNSET:
            field_dict["FEED_HASHTAG"] = feed_hashtag
        if feed_date_updated is not UNSET:
            field_dict["FEED_DATE_UPDATED"] = feed_date_updated
        if owner_name is not UNSET:
            field_dict["OWNER_NAME"] = owner_name
        if version_number is not UNSET:
            field_dict["VERSION_NUMBER"] = version_number
        if timestamp is not UNSET:
            field_dict["TIMESTAMP"] = timestamp
        if feed_mention is not UNSET:
            field_dict["FEED_MENTION"] = feed_mention
        if feed_type is not UNSET:
            field_dict["FEED_TYPE"] = feed_type
        if extra_text is not UNSET:
            field_dict["EXTRA_TEXT"] = extra_text
        if deleted_date is not UNSET:
            field_dict["DELETED_DATE"] = deleted_date
        if version_owner_id is not UNSET:
            field_dict["VERSION_OWNER_ID"] = version_owner_id
        if filename is not UNSET:
            field_dict["FILENAME"] = filename
        if type is not UNSET:
            field_dict["TYPE"] = type
        if feed_date_created is not UNSET:
            field_dict["FEED_DATE_CREATED"] = feed_date_created
        if file_extension is not UNSET:
            field_dict["FILE_EXTENSION"] = file_extension
        if document_size is not UNSET:
            field_dict["DOCUMENT_SIZE"] = document_size
        if guid is not UNSET:
            field_dict["GUID"] = guid
        if parent_guid is not UNSET:
            field_dict["PARENT_GUID"] = parent_guid
        if x_date is not UNSET:
            field_dict["X_DATE"] = x_date
        if version_comment is not UNSET:
            field_dict["VERSION_COMMENT"] = version_comment
        if space_guids is not UNSET:
            field_dict["SPACE_GUIDS"] = space_guids
        if fulltext is not UNSET:
            field_dict["FULLTEXT"] = fulltext
        if indexfield is not UNSET:
            field_dict["INDEXFIELD"] = indexfield
        if title is not UNSET:
            field_dict["TITLE"] = title
        if mask_name is not UNSET:
            field_dict["MASK_NAME"] = mask_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _feed_reference = d.pop("FEED_REFERENCE", UNSET)
        feed_reference: Union[Unset, SearchFieldE]
        if isinstance(_feed_reference, Unset):
            feed_reference = UNSET
        else:
            feed_reference = SearchFieldE.from_dict(_feed_reference)

        _i_date = d.pop("I_DATE", UNSET)
        i_date: Union[Unset, SearchFieldE]
        if isinstance(_i_date, Unset):
            i_date = UNSET
        else:
            i_date = SearchFieldE.from_dict(_i_date)

        _feed_author = d.pop("FEED_AUTHOR", UNSET)
        feed_author: Union[Unset, SearchFieldE]
        if isinstance(_feed_author, Unset):
            feed_author = UNSET
        else:
            feed_author = SearchFieldE.from_dict(_feed_author)

        _feed_text = d.pop("FEED_TEXT", UNSET)
        feed_text: Union[Unset, SearchFieldE]
        if isinstance(_feed_text, Unset):
            feed_text = UNSET
        else:
            feed_text = SearchFieldE.from_dict(_feed_text)

        _sord_hash = d.pop("SORD_HASH", UNSET)
        sord_hash: Union[Unset, SearchFieldE]
        if isinstance(_sord_hash, Unset):
            sord_hash = UNSET
        else:
            sord_hash = SearchFieldE.from_dict(_sord_hash)

        _owner_id = d.pop("OWNER_ID", UNSET)
        owner_id: Union[Unset, SearchFieldE]
        if isinstance(_owner_id, Unset):
            owner_id = UNSET
        else:
            owner_id = SearchFieldE.from_dict(_owner_id)

        _obj_id = d.pop("OBJ_ID", UNSET)
        obj_id: Union[Unset, SearchFieldE]
        if isinstance(_obj_id, Unset):
            obj_id = UNSET
        else:
            obj_id = SearchFieldE.from_dict(_obj_id)

        _mask_id = d.pop("MASK_ID", UNSET)
        mask_id: Union[Unset, SearchFieldE]
        if isinstance(_mask_id, Unset):
            mask_id = UNSET
        else:
            mask_id = SearchFieldE.from_dict(_mask_id)

        _feed_hashtag = d.pop("FEED_HASHTAG", UNSET)
        feed_hashtag: Union[Unset, SearchFieldE]
        if isinstance(_feed_hashtag, Unset):
            feed_hashtag = UNSET
        else:
            feed_hashtag = SearchFieldE.from_dict(_feed_hashtag)

        _feed_date_updated = d.pop("FEED_DATE_UPDATED", UNSET)
        feed_date_updated: Union[Unset, SearchFieldE]
        if isinstance(_feed_date_updated, Unset):
            feed_date_updated = UNSET
        else:
            feed_date_updated = SearchFieldE.from_dict(_feed_date_updated)

        _owner_name = d.pop("OWNER_NAME", UNSET)
        owner_name: Union[Unset, SearchFieldE]
        if isinstance(_owner_name, Unset):
            owner_name = UNSET
        else:
            owner_name = SearchFieldE.from_dict(_owner_name)

        _version_number = d.pop("VERSION_NUMBER", UNSET)
        version_number: Union[Unset, SearchFieldE]
        if isinstance(_version_number, Unset):
            version_number = UNSET
        else:
            version_number = SearchFieldE.from_dict(_version_number)

        _timestamp = d.pop("TIMESTAMP", UNSET)
        timestamp: Union[Unset, SearchFieldE]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = SearchFieldE.from_dict(_timestamp)

        _feed_mention = d.pop("FEED_MENTION", UNSET)
        feed_mention: Union[Unset, SearchFieldE]
        if isinstance(_feed_mention, Unset):
            feed_mention = UNSET
        else:
            feed_mention = SearchFieldE.from_dict(_feed_mention)

        _feed_type = d.pop("FEED_TYPE", UNSET)
        feed_type: Union[Unset, SearchFieldE]
        if isinstance(_feed_type, Unset):
            feed_type = UNSET
        else:
            feed_type = SearchFieldE.from_dict(_feed_type)

        _extra_text = d.pop("EXTRA_TEXT", UNSET)
        extra_text: Union[Unset, SearchFieldE]
        if isinstance(_extra_text, Unset):
            extra_text = UNSET
        else:
            extra_text = SearchFieldE.from_dict(_extra_text)

        _deleted_date = d.pop("DELETED_DATE", UNSET)
        deleted_date: Union[Unset, SearchFieldE]
        if isinstance(_deleted_date, Unset):
            deleted_date = UNSET
        else:
            deleted_date = SearchFieldE.from_dict(_deleted_date)

        _version_owner_id = d.pop("VERSION_OWNER_ID", UNSET)
        version_owner_id: Union[Unset, SearchFieldE]
        if isinstance(_version_owner_id, Unset):
            version_owner_id = UNSET
        else:
            version_owner_id = SearchFieldE.from_dict(_version_owner_id)

        _filename = d.pop("FILENAME", UNSET)
        filename: Union[Unset, SearchFieldE]
        if isinstance(_filename, Unset):
            filename = UNSET
        else:
            filename = SearchFieldE.from_dict(_filename)

        _type = d.pop("TYPE", UNSET)
        type: Union[Unset, SearchFieldE]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SearchFieldE.from_dict(_type)

        _feed_date_created = d.pop("FEED_DATE_CREATED", UNSET)
        feed_date_created: Union[Unset, SearchFieldE]
        if isinstance(_feed_date_created, Unset):
            feed_date_created = UNSET
        else:
            feed_date_created = SearchFieldE.from_dict(_feed_date_created)

        _file_extension = d.pop("FILE_EXTENSION", UNSET)
        file_extension: Union[Unset, SearchFieldE]
        if isinstance(_file_extension, Unset):
            file_extension = UNSET
        else:
            file_extension = SearchFieldE.from_dict(_file_extension)

        _document_size = d.pop("DOCUMENT_SIZE", UNSET)
        document_size: Union[Unset, SearchFieldE]
        if isinstance(_document_size, Unset):
            document_size = UNSET
        else:
            document_size = SearchFieldE.from_dict(_document_size)

        _guid = d.pop("GUID", UNSET)
        guid: Union[Unset, SearchFieldE]
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = SearchFieldE.from_dict(_guid)

        _parent_guid = d.pop("PARENT_GUID", UNSET)
        parent_guid: Union[Unset, SearchFieldE]
        if isinstance(_parent_guid, Unset):
            parent_guid = UNSET
        else:
            parent_guid = SearchFieldE.from_dict(_parent_guid)

        _x_date = d.pop("X_DATE", UNSET)
        x_date: Union[Unset, SearchFieldE]
        if isinstance(_x_date, Unset):
            x_date = UNSET
        else:
            x_date = SearchFieldE.from_dict(_x_date)

        _version_comment = d.pop("VERSION_COMMENT", UNSET)
        version_comment: Union[Unset, SearchFieldE]
        if isinstance(_version_comment, Unset):
            version_comment = UNSET
        else:
            version_comment = SearchFieldE.from_dict(_version_comment)

        _space_guids = d.pop("SPACE_GUIDS", UNSET)
        space_guids: Union[Unset, SearchFieldE]
        if isinstance(_space_guids, Unset):
            space_guids = UNSET
        else:
            space_guids = SearchFieldE.from_dict(_space_guids)

        _fulltext = d.pop("FULLTEXT", UNSET)
        fulltext: Union[Unset, SearchFieldE]
        if isinstance(_fulltext, Unset):
            fulltext = UNSET
        else:
            fulltext = SearchFieldE.from_dict(_fulltext)

        _indexfield = d.pop("INDEXFIELD", UNSET)
        indexfield: Union[Unset, SearchFieldE]
        if isinstance(_indexfield, Unset):
            indexfield = UNSET
        else:
            indexfield = SearchFieldE.from_dict(_indexfield)

        _title = d.pop("TITLE", UNSET)
        title: Union[Unset, SearchFieldE]
        if isinstance(_title, Unset):
            title = UNSET
        else:
            title = SearchFieldE.from_dict(_title)

        _mask_name = d.pop("MASK_NAME", UNSET)
        mask_name: Union[Unset, SearchFieldE]
        if isinstance(_mask_name, Unset):
            mask_name = UNSET
        else:
            mask_name = SearchFieldE.from_dict(_mask_name)

        search_field_e = cls(
            feed_reference=feed_reference,
            i_date=i_date,
            feed_author=feed_author,
            feed_text=feed_text,
            sord_hash=sord_hash,
            owner_id=owner_id,
            obj_id=obj_id,
            mask_id=mask_id,
            feed_hashtag=feed_hashtag,
            feed_date_updated=feed_date_updated,
            owner_name=owner_name,
            version_number=version_number,
            timestamp=timestamp,
            feed_mention=feed_mention,
            feed_type=feed_type,
            extra_text=extra_text,
            deleted_date=deleted_date,
            version_owner_id=version_owner_id,
            filename=filename,
            type=type,
            feed_date_created=feed_date_created,
            file_extension=file_extension,
            document_size=document_size,
            guid=guid,
            parent_guid=parent_guid,
            x_date=x_date,
            version_comment=version_comment,
            space_guids=space_guids,
            fulltext=fulltext,
            indexfield=indexfield,
            title=title,
            mask_name=mask_name,
        )

        search_field_e.additional_properties = d
        return search_field_e

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
