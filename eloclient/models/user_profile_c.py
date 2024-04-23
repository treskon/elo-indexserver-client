from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfileC")


@_attrs_define
class UserProfileC:
    """The constants in this class exist due to compatibility requirements with older Index Server
    versions, which gave back formatted data (Sord.xDataDispl).

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            sord_date_format (Union[Unset, str]):
            sord_xdate_format (Union[Unset, str]):
            date_format (Union[Unset, str]):
            doc_version_create_format (Union[Unset, str]):
            key_feed_subscribe_newversion (Union[Unset, str]): Automatically subscribe Feed if the User creates a new
                Version of a Document
            key_feed_subscribe_mydoc (Union[Unset, str]): Automatically subscribe Feed if the User creates a new Document
            key_prefix_system_encryption_password (Union[Unset, str]): Prefix for system encryption password options.
            key_prefix_fulltext_search_options (Union[Unset, str]): Prefix for fulltext search options.
            key_server_id (Union[Unset, str]): Server-ID for WF-Replication
            key_password_valid_days (Union[Unset, str]): The password has to be changed after this number of days.
                The value corresponds to
                 UserInfo.userProps[UserInfoC.PROP_ACTION].
            key_default_docmask_doc (Union[Unset, str]): Default mask for new document.
            sord_deldate_format (Union[Unset, str]):
            userid_all (Union[Unset, str]): Read/write user profile options for all users.
            ln_key (Union[Unset, int]): Maximum length of key
            doc_version_access_format (Union[Unset, str]):
            doc_version_update_format (Union[Unset, str]):
            key_archive_language (Union[Unset, str]): Give the archive's language (set by a new installation since Server
                Setup 9.00.004).
            key_feed_subscribe_myfolder (Union[Unset, str]): Automatically subscribe Feed if the User creates a new Folder
            doc_version_date_format (Union[Unset, str]):
            key_extend_document_access_in_workflow (Union[Unset, str]): Extended access control for documents or folders
                used in workflows.
                <p>
                 There are two concepts of extending access control for folders and documents routed though a
                 workflow. The rules are only applied if (a) the current user has an active workflow task for
                 the folder or document and (b) the right AccessC.FLAG2_EXTEND_WORKFLOW_RIGHTS is assigned to
                 the current user.
                 </p>
                 <p>
                 1. Overlay additional access rights over the objects ACL: the lower 8 bits of the keys value
                 specify a combination of AccessC.LUR_* constants that are added to the ACL access rights when
                 access checking is performed. The objects ACL is not modified, this rule only changes the
                 internal program logic.
                 </p>
                 <p>
                 2. Permanently add additional access to the ACL: the higher 8 bits of the keys value specify a
                 combination of AccessC.LUR_* constants for a new ACL entry to be added for the current user.
                 The ACL is only extended, if checkoutSord or checkoutDoc detects less access for the current
                 user.
            sord_idate_format (Union[Unset, str]):
            key_password_rules (Union[Unset, str]): Password rules. The password rules are stored as a comma separated list
                of 5 Integers, e.g.
                "7,1,1,0,0". 1. Minimum password length 2. Is != 0, if password must contain at least one
                 letter. 3. Is != 0, if password must contain at least one special character (not letter and not
                 digit). 4. Is != 0, if password must contain at least one lower case and one upper case letter.
                 5. Is != 0, if password must contain at least one digit.
            key_feed_subscribe_newcomment (Union[Unset, str]): Automatically subscribe Feed if the User adds a comment to a
                Feed
            ln_value (Union[Unset, int]): Maximum length of value
            key_default_docmask_folder (Union[Unset, str]): Default mask for new structure element.
    """

    sord_date_format: Union[Unset, str] = UNSET
    sord_xdate_format: Union[Unset, str] = UNSET
    date_format: Union[Unset, str] = UNSET
    doc_version_create_format: Union[Unset, str] = UNSET
    key_feed_subscribe_newversion: Union[Unset, str] = UNSET
    key_feed_subscribe_mydoc: Union[Unset, str] = UNSET
    key_prefix_system_encryption_password: Union[Unset, str] = UNSET
    key_prefix_fulltext_search_options: Union[Unset, str] = UNSET
    key_server_id: Union[Unset, str] = UNSET
    key_password_valid_days: Union[Unset, str] = UNSET
    key_default_docmask_doc: Union[Unset, str] = UNSET
    sord_deldate_format: Union[Unset, str] = UNSET
    userid_all: Union[Unset, str] = UNSET
    ln_key: Union[Unset, int] = UNSET
    doc_version_access_format: Union[Unset, str] = UNSET
    doc_version_update_format: Union[Unset, str] = UNSET
    key_archive_language: Union[Unset, str] = UNSET
    key_feed_subscribe_myfolder: Union[Unset, str] = UNSET
    doc_version_date_format: Union[Unset, str] = UNSET
    key_extend_document_access_in_workflow: Union[Unset, str] = UNSET
    sord_idate_format: Union[Unset, str] = UNSET
    key_password_rules: Union[Unset, str] = UNSET
    key_feed_subscribe_newcomment: Union[Unset, str] = UNSET
    ln_value: Union[Unset, int] = UNSET
    key_default_docmask_folder: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sord_date_format = self.sord_date_format

        sord_xdate_format = self.sord_xdate_format

        date_format = self.date_format

        doc_version_create_format = self.doc_version_create_format

        key_feed_subscribe_newversion = self.key_feed_subscribe_newversion

        key_feed_subscribe_mydoc = self.key_feed_subscribe_mydoc

        key_prefix_system_encryption_password = self.key_prefix_system_encryption_password

        key_prefix_fulltext_search_options = self.key_prefix_fulltext_search_options

        key_server_id = self.key_server_id

        key_password_valid_days = self.key_password_valid_days

        key_default_docmask_doc = self.key_default_docmask_doc

        sord_deldate_format = self.sord_deldate_format

        userid_all = self.userid_all

        ln_key = self.ln_key

        doc_version_access_format = self.doc_version_access_format

        doc_version_update_format = self.doc_version_update_format

        key_archive_language = self.key_archive_language

        key_feed_subscribe_myfolder = self.key_feed_subscribe_myfolder

        doc_version_date_format = self.doc_version_date_format

        key_extend_document_access_in_workflow = self.key_extend_document_access_in_workflow

        sord_idate_format = self.sord_idate_format

        key_password_rules = self.key_password_rules

        key_feed_subscribe_newcomment = self.key_feed_subscribe_newcomment

        ln_value = self.ln_value

        key_default_docmask_folder = self.key_default_docmask_folder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sord_date_format is not UNSET:
            field_dict["SORD_DATE_FORMAT"] = sord_date_format
        if sord_xdate_format is not UNSET:
            field_dict["SORD_XDATE_FORMAT"] = sord_xdate_format
        if date_format is not UNSET:
            field_dict["DATE_FORMAT"] = date_format
        if doc_version_create_format is not UNSET:
            field_dict["DOC_VERSION_CREATE_FORMAT"] = doc_version_create_format
        if key_feed_subscribe_newversion is not UNSET:
            field_dict["KEY_FEED_SUBSCRIBE_NEWVERSION"] = key_feed_subscribe_newversion
        if key_feed_subscribe_mydoc is not UNSET:
            field_dict["KEY_FEED_SUBSCRIBE_MYDOC"] = key_feed_subscribe_mydoc
        if key_prefix_system_encryption_password is not UNSET:
            field_dict["KEY_PREFIX_SYSTEM_ENCRYPTION_PASSWORD"] = key_prefix_system_encryption_password
        if key_prefix_fulltext_search_options is not UNSET:
            field_dict["KEY_PREFIX_FULLTEXT_SEARCH_OPTIONS"] = key_prefix_fulltext_search_options
        if key_server_id is not UNSET:
            field_dict["KEY_SERVER_ID"] = key_server_id
        if key_password_valid_days is not UNSET:
            field_dict["KEY_PASSWORD_VALID_DAYS"] = key_password_valid_days
        if key_default_docmask_doc is not UNSET:
            field_dict["KEY_DEFAULT_DOCMASK_DOC"] = key_default_docmask_doc
        if sord_deldate_format is not UNSET:
            field_dict["SORD_DELDATE_FORMAT"] = sord_deldate_format
        if userid_all is not UNSET:
            field_dict["USERID_ALL"] = userid_all
        if ln_key is not UNSET:
            field_dict["lnKey"] = ln_key
        if doc_version_access_format is not UNSET:
            field_dict["DOC_VERSION_ACCESS_FORMAT"] = doc_version_access_format
        if doc_version_update_format is not UNSET:
            field_dict["DOC_VERSION_UPDATE_FORMAT"] = doc_version_update_format
        if key_archive_language is not UNSET:
            field_dict["KEY_ARCHIVE_LANGUAGE"] = key_archive_language
        if key_feed_subscribe_myfolder is not UNSET:
            field_dict["KEY_FEED_SUBSCRIBE_MYFOLDER"] = key_feed_subscribe_myfolder
        if doc_version_date_format is not UNSET:
            field_dict["DOC_VERSION_DATE_FORMAT"] = doc_version_date_format
        if key_extend_document_access_in_workflow is not UNSET:
            field_dict["KEY_EXTEND_DOCUMENT_ACCESS_IN_WORKFLOW"] = key_extend_document_access_in_workflow
        if sord_idate_format is not UNSET:
            field_dict["SORD_IDATE_FORMAT"] = sord_idate_format
        if key_password_rules is not UNSET:
            field_dict["KEY_PASSWORD_RULES"] = key_password_rules
        if key_feed_subscribe_newcomment is not UNSET:
            field_dict["KEY_FEED_SUBSCRIBE_NEWCOMMENT"] = key_feed_subscribe_newcomment
        if ln_value is not UNSET:
            field_dict["lnValue"] = ln_value
        if key_default_docmask_folder is not UNSET:
            field_dict["KEY_DEFAULT_DOCMASK_FOLDER"] = key_default_docmask_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sord_date_format = d.pop("SORD_DATE_FORMAT", UNSET)

        sord_xdate_format = d.pop("SORD_XDATE_FORMAT", UNSET)

        date_format = d.pop("DATE_FORMAT", UNSET)

        doc_version_create_format = d.pop("DOC_VERSION_CREATE_FORMAT", UNSET)

        key_feed_subscribe_newversion = d.pop("KEY_FEED_SUBSCRIBE_NEWVERSION", UNSET)

        key_feed_subscribe_mydoc = d.pop("KEY_FEED_SUBSCRIBE_MYDOC", UNSET)

        key_prefix_system_encryption_password = d.pop("KEY_PREFIX_SYSTEM_ENCRYPTION_PASSWORD", UNSET)

        key_prefix_fulltext_search_options = d.pop("KEY_PREFIX_FULLTEXT_SEARCH_OPTIONS", UNSET)

        key_server_id = d.pop("KEY_SERVER_ID", UNSET)

        key_password_valid_days = d.pop("KEY_PASSWORD_VALID_DAYS", UNSET)

        key_default_docmask_doc = d.pop("KEY_DEFAULT_DOCMASK_DOC", UNSET)

        sord_deldate_format = d.pop("SORD_DELDATE_FORMAT", UNSET)

        userid_all = d.pop("USERID_ALL", UNSET)

        ln_key = d.pop("lnKey", UNSET)

        doc_version_access_format = d.pop("DOC_VERSION_ACCESS_FORMAT", UNSET)

        doc_version_update_format = d.pop("DOC_VERSION_UPDATE_FORMAT", UNSET)

        key_archive_language = d.pop("KEY_ARCHIVE_LANGUAGE", UNSET)

        key_feed_subscribe_myfolder = d.pop("KEY_FEED_SUBSCRIBE_MYFOLDER", UNSET)

        doc_version_date_format = d.pop("DOC_VERSION_DATE_FORMAT", UNSET)

        key_extend_document_access_in_workflow = d.pop("KEY_EXTEND_DOCUMENT_ACCESS_IN_WORKFLOW", UNSET)

        sord_idate_format = d.pop("SORD_IDATE_FORMAT", UNSET)

        key_password_rules = d.pop("KEY_PASSWORD_RULES", UNSET)

        key_feed_subscribe_newcomment = d.pop("KEY_FEED_SUBSCRIBE_NEWCOMMENT", UNSET)

        ln_value = d.pop("lnValue", UNSET)

        key_default_docmask_folder = d.pop("KEY_DEFAULT_DOCMASK_FOLDER", UNSET)

        user_profile_c = cls(
            sord_date_format=sord_date_format,
            sord_xdate_format=sord_xdate_format,
            date_format=date_format,
            doc_version_create_format=doc_version_create_format,
            key_feed_subscribe_newversion=key_feed_subscribe_newversion,
            key_feed_subscribe_mydoc=key_feed_subscribe_mydoc,
            key_prefix_system_encryption_password=key_prefix_system_encryption_password,
            key_prefix_fulltext_search_options=key_prefix_fulltext_search_options,
            key_server_id=key_server_id,
            key_password_valid_days=key_password_valid_days,
            key_default_docmask_doc=key_default_docmask_doc,
            sord_deldate_format=sord_deldate_format,
            userid_all=userid_all,
            ln_key=ln_key,
            doc_version_access_format=doc_version_access_format,
            doc_version_update_format=doc_version_update_format,
            key_archive_language=key_archive_language,
            key_feed_subscribe_myfolder=key_feed_subscribe_myfolder,
            doc_version_date_format=doc_version_date_format,
            key_extend_document_access_in_workflow=key_extend_document_access_in_workflow,
            sord_idate_format=sord_idate_format,
            key_password_rules=key_password_rules,
            key_feed_subscribe_newcomment=key_feed_subscribe_newcomment,
            ln_value=ln_value,
            key_default_docmask_folder=key_default_docmask_folder,
        )

        user_profile_c.additional_properties = d
        return user_profile_c

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
