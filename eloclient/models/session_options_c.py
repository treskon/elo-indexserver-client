from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionOptionsC")


@_attrs_define
class SessionOptionsC:
    """Constants of SessionOptions.

    Attributes:
        iso_date_with_delims (Union[Unset, str]): Format ISO date values with delimiter characters defined in ISO 8601.
        ticket_from_cookie (Union[Unset, str]): This value can be used as {@link ClientInfo#ticket} or in
            IXConnFactory#createFromTicket() if
            the server should use the session cookie as authentication token. EIX-393
        client_app_version (Union[Unset, str]): Client application version. Optional.
        client_app_name (Union[Unset, str]): Client application name. Optional.
        direct_dm_access (Union[Unset, str]): This option specifies which application is addressed in URLs to upload and
            download documents.
            If direct access is true, the URLs address the DM directly. Otherwise the documents are routed
             though the IX.
        download_url_type (Union[Unset, str]): Define the download URL type. IX can generate several types of URLs to
            download documents.
            Possible values are the constants DOWNLOAD_URL_TYPE_*. The default value is
             DOWNLOAD_URL_TYPE_TEMPORARY.
        apply_all_blackenings (Union[Unset, str]): Apply all blackenings on documents regardless of their ACL.
            ELOtr sets this option as "true" to
             receive documents with all blackenings. This ensures that blackened parts cannot be retrieved
             by a fulltext search. TTS003793
        public_download_expiredtime (Union[Unset, str]): Define the expired time of public downloads.
        handle_ix_server_events (Union[Unset, str]): This session option declares that the IXConnection handles server
            events declared in
            {@link IXServerEvents}.
        copy_objkeys_in_background (Union[Unset, str]): Control the synchronicity of copying objkeys to child entries.
        client_app_type (Union[Unset, str]): Client application type. Mandatory.
            The appropriate value for partner applications is
             TYPE_PARTNER_APPLICATION unless a special type is arranged.
        translate_terms (Union[Unset, str]): Translate keywording forms names, index names, index values and keyword
            lists into resp.
            from
             the language given in <code>ClientInfo.language</code>.
        download_url_type_public_version (Union[Unset, str]): Generate public download URLs for the document version,
            that expire after a given time..
            Only a
             given number of downloads is allowed. IX generates URLs that can be used by non ELO users. The
             URL includes a strongly encrypted ID of the document or attachment version. AES is used to
             encrypt the URL parameters. The AES key is read from the IX option AESEncryptionKey.

             <br/>
             <b>ATTENTION: If the key AESEncryptionKey is changed, all URLs generated before become
             invalid!</b>

             <br/>
             <b>ATTENTION: No access checking is performed, when the document is downloaded from the URL!
             Everyone who knows the URL and has access to ELOix can download the document. This option
             cannot not be used for documents with blackening. No URL is generated for those documents.</b>

             <br/>
             Authentication is not required or performed.
        http_session_ticket (Union[Unset, str]): Attribute name to which Indexserver maps a Ticket in the HTTP Session
        http_session_ix_connection (Union[Unset, str]): Attribute name to which Indexserver maps an IXConnection in the
            HTTP Session
        disable_logging_api_calls (Union[Unset, str]): Disable logging of API calls for this session.
            EIX-3303
        decrypt_documents (Union[Unset, str]): Set this option to decrypt documents on checkout.
            A secure connection (HTTPS) is required to
             use this option.
        db_escape_char (Union[Unset, str]): This character is used in the SQL statement, if the search criterias contain
            one of the SQL
            wildcard characters: &quot;%&quot;, &quot;_&quot;. It defaults to &quot;¶&quot; which is a
             reserved character in ELO and a valid escape character for the most SQL servers and
             configurations. Unless a search kritera contains &quot;¶&quot; or the SQL server does not allow
             the use of this character (e. g. ORACLE, UTF-8) the value has to be changed. Hint:
             Indexserver-API uses &quot;*&quot; as the only valid wildcard. The escape character must not be
             used in the search criterias.
        doc_url_base (Union[Unset, str]): Define the first part of the document URLs generated from Indexserver.
            See configuration option
             documentUrlBase on the Indexserver option page.
        db_wildcards (Union[Unset, str]): This characters are used as wildcards in search terms.
            The first wildcard is used for zero or
             more characters. The second wildcard is used for exactly one character. By default (if this
             member is null or empty), only the first wildcard is defined: *
        session_add (Union[Unset, int]): Function getSessionFromTicket: used in combination with SESSION_FROM_AM.
            Add the session into
             the internal session management.
        public_download_count (Union[Unset, str]): Define the allowed number of public downloads.
        download_url_type_public (Union[Unset, str]): Generate public download URLs for the actual working version, that
            expire after a given time.
            Only a given number of downloads is allowed. IX generates URLs that can be used by non ELO
             users. The URL includes a strongly encrypted ID of the document or attachment version. AES is
             used to encrypt the URL parameters. The AES key is read from the IX option AESEncryptionKey.

             <br/>
             <b>ATTENTION: If the key AESEncryptionKey is changed, all URLs generated before become
             invalid!</b>

             <br/>
             <b>ATTENTION: No access checking is performed, when the document is downloaded from the URL!
             Everyone who knows the URL and has access to ELOix can download the document. This option
             cannot not be used for documents with blackening. No URL is generated for those documents.</b>

             <br/>
             Authentication is not required or performed.
        app_type_mini_client (Union[Unset, str]): Reserved. This value is reserved for ELO applications.
            Unauthorized usage violates the ELO
             licensing terms.
        active_roles (Union[Unset, str]): Comma separated list of active role IDs.
        session_from_am_add (Union[Unset, int]): Function getSessionFromTicket: any active session can be requested and
            is inserted into the
            session management of this Indexserver instance. If the session is not known by this
             Indexserver instance, it is assumed to be a Windows CLIENT session (relevant to license model).
             The ticket lifetime is extended. This value is the same as SESSION_FROM_AM | SESSION_ADD.
        disable_change_info_protection (Union[Unset, str]): If set, this option disables the protection of change
            information.
            <p>
             Disabling the writing of changes information causes the Indexserver to not update the *tstamp*
             database columns. Then, the client has to ensure that the time stamps of objects are set
             correctly. Setting this option without reason causes the loss of traceability of objects in the
             archive! Only the replication module should use this option.
             </p>
             <p>
             The replication searches the database for changes since the last replication run. The gathered
             changes will be transported to other sites and imported into the database there. Such an import
             must not trigger the writing of change informations as further this would trigger the export of
             these changes again, claiming the changes would have been made at the site importing the
             changes.
             </p>
        session_from_am (Union[Unset, int]): Function getSessionFromTicket: any active session known by the
            AccessManager can be requested.
            The session is not inserted into the session management of this Indexserver instance. Thus the
             session cannot be used to make Indexserver function calls. The ticket lifetime is not extended.
        session_from_ix (Union[Unset, int]): Function getSessionFromTicket: session must be known by this Indexserver
            instance.
            An exception
             is thrown, if the session is not known by this Indexserver instance. The ticket lifetime is
             extended.
        download_url_type_temporary (Union[Unset, str]): Generate URLs that expire after a given time.
            The lifetime can be specified with the option
             "documentUrlLifetimeSeconds". By default, all URLs are created with a constrained lifetime.
        type_partner_application (Union[Unset, str]): This option value has to be used for option CLIENT_APP_TYPE if a
            partner application connects
            to IX.
        start_docmask_workflows (Union[Unset, str]): If this option is set to "true", the Indexserver starts the
            workflow defined in DocMask.
            flowId
             and DocMask.flowId2 when an associated document is created or checked in.
        ix_url_base (Union[Unset, str]): Define the first part of the URLs generated from Indexserver.
            See configuration option
             ixUrlBase on the Indexserver option page.
        download_url_type_persistent (Union[Unset, str]): Generate URLs that do not expire. IX generates URLs that can
            be used without time limitation.
            The URL includes a strongly encrypted ID of the document or attachment version. AES is used to
             encrypt the URL parameters. The AES key is read from the IX option AESEncryptionKey.

             <br/>
             <b>ATTENTION: If the key AESEncryptionKey is changed, all URLs generated before become
             invalid!</b>

             <br/>
             <b>ATTENTION: No access checking is performed, when the document is downloaded from the URL!
             Everyone who knows the URL and has access to ELOix can download the document. This option
             cannot not be used for documents with blackening. No URL is generated for those documents.</b>

             <br/>
             Only main administrators can use this option. The document is accessed by the IX account.
             Authentication is not required or performed.
        encrypt_documents (Union[Unset, str]): Set this option to encrypt documents on checkin.
            A secure connection (HTTPS) is required to use
             this option.
    """

    iso_date_with_delims: Union[Unset, str] = UNSET
    ticket_from_cookie: Union[Unset, str] = UNSET
    client_app_version: Union[Unset, str] = UNSET
    client_app_name: Union[Unset, str] = UNSET
    direct_dm_access: Union[Unset, str] = UNSET
    download_url_type: Union[Unset, str] = UNSET
    apply_all_blackenings: Union[Unset, str] = UNSET
    public_download_expiredtime: Union[Unset, str] = UNSET
    handle_ix_server_events: Union[Unset, str] = UNSET
    copy_objkeys_in_background: Union[Unset, str] = UNSET
    client_app_type: Union[Unset, str] = UNSET
    translate_terms: Union[Unset, str] = UNSET
    download_url_type_public_version: Union[Unset, str] = UNSET
    http_session_ticket: Union[Unset, str] = UNSET
    http_session_ix_connection: Union[Unset, str] = UNSET
    disable_logging_api_calls: Union[Unset, str] = UNSET
    decrypt_documents: Union[Unset, str] = UNSET
    db_escape_char: Union[Unset, str] = UNSET
    doc_url_base: Union[Unset, str] = UNSET
    db_wildcards: Union[Unset, str] = UNSET
    session_add: Union[Unset, int] = UNSET
    public_download_count: Union[Unset, str] = UNSET
    download_url_type_public: Union[Unset, str] = UNSET
    app_type_mini_client: Union[Unset, str] = UNSET
    active_roles: Union[Unset, str] = UNSET
    session_from_am_add: Union[Unset, int] = UNSET
    disable_change_info_protection: Union[Unset, str] = UNSET
    session_from_am: Union[Unset, int] = UNSET
    session_from_ix: Union[Unset, int] = UNSET
    download_url_type_temporary: Union[Unset, str] = UNSET
    type_partner_application: Union[Unset, str] = UNSET
    start_docmask_workflows: Union[Unset, str] = UNSET
    ix_url_base: Union[Unset, str] = UNSET
    download_url_type_persistent: Union[Unset, str] = UNSET
    encrypt_documents: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        iso_date_with_delims = self.iso_date_with_delims

        ticket_from_cookie = self.ticket_from_cookie

        client_app_version = self.client_app_version

        client_app_name = self.client_app_name

        direct_dm_access = self.direct_dm_access

        download_url_type = self.download_url_type

        apply_all_blackenings = self.apply_all_blackenings

        public_download_expiredtime = self.public_download_expiredtime

        handle_ix_server_events = self.handle_ix_server_events

        copy_objkeys_in_background = self.copy_objkeys_in_background

        client_app_type = self.client_app_type

        translate_terms = self.translate_terms

        download_url_type_public_version = self.download_url_type_public_version

        http_session_ticket = self.http_session_ticket

        http_session_ix_connection = self.http_session_ix_connection

        disable_logging_api_calls = self.disable_logging_api_calls

        decrypt_documents = self.decrypt_documents

        db_escape_char = self.db_escape_char

        doc_url_base = self.doc_url_base

        db_wildcards = self.db_wildcards

        session_add = self.session_add

        public_download_count = self.public_download_count

        download_url_type_public = self.download_url_type_public

        app_type_mini_client = self.app_type_mini_client

        active_roles = self.active_roles

        session_from_am_add = self.session_from_am_add

        disable_change_info_protection = self.disable_change_info_protection

        session_from_am = self.session_from_am

        session_from_ix = self.session_from_ix

        download_url_type_temporary = self.download_url_type_temporary

        type_partner_application = self.type_partner_application

        start_docmask_workflows = self.start_docmask_workflows

        ix_url_base = self.ix_url_base

        download_url_type_persistent = self.download_url_type_persistent

        encrypt_documents = self.encrypt_documents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if iso_date_with_delims is not UNSET:
            field_dict["ISO_DATE_WITH_DELIMS"] = iso_date_with_delims
        if ticket_from_cookie is not UNSET:
            field_dict["TICKET_FROM_COOKIE"] = ticket_from_cookie
        if client_app_version is not UNSET:
            field_dict["CLIENT_APP_VERSION"] = client_app_version
        if client_app_name is not UNSET:
            field_dict["CLIENT_APP_NAME"] = client_app_name
        if direct_dm_access is not UNSET:
            field_dict["DIRECT_DM_ACCESS"] = direct_dm_access
        if download_url_type is not UNSET:
            field_dict["DOWNLOAD_URL_TYPE"] = download_url_type
        if apply_all_blackenings is not UNSET:
            field_dict["APPLY_ALL_BLACKENINGS"] = apply_all_blackenings
        if public_download_expiredtime is not UNSET:
            field_dict["PUBLIC_DOWNLOAD_EXPIREDTIME"] = public_download_expiredtime
        if handle_ix_server_events is not UNSET:
            field_dict["HANDLE_IX_SERVER_EVENTS"] = handle_ix_server_events
        if copy_objkeys_in_background is not UNSET:
            field_dict["COPY_OBJKEYS_IN_BACKGROUND"] = copy_objkeys_in_background
        if client_app_type is not UNSET:
            field_dict["CLIENT_APP_TYPE"] = client_app_type
        if translate_terms is not UNSET:
            field_dict["TRANSLATE_TERMS"] = translate_terms
        if download_url_type_public_version is not UNSET:
            field_dict["DOWNLOAD_URL_TYPE_PUBLIC_VERSION"] = download_url_type_public_version
        if http_session_ticket is not UNSET:
            field_dict["HTTP_SESSION_TICKET"] = http_session_ticket
        if http_session_ix_connection is not UNSET:
            field_dict["HTTP_SESSION_IX_CONNECTION"] = http_session_ix_connection
        if disable_logging_api_calls is not UNSET:
            field_dict["DISABLE_LOGGING_API_CALLS"] = disable_logging_api_calls
        if decrypt_documents is not UNSET:
            field_dict["DECRYPT_DOCUMENTS"] = decrypt_documents
        if db_escape_char is not UNSET:
            field_dict["DB_ESCAPE_CHAR"] = db_escape_char
        if doc_url_base is not UNSET:
            field_dict["DOC_URL_BASE"] = doc_url_base
        if db_wildcards is not UNSET:
            field_dict["DB_WILDCARDS"] = db_wildcards
        if session_add is not UNSET:
            field_dict["SESSION_ADD"] = session_add
        if public_download_count is not UNSET:
            field_dict["PUBLIC_DOWNLOAD_COUNT"] = public_download_count
        if download_url_type_public is not UNSET:
            field_dict["DOWNLOAD_URL_TYPE_PUBLIC"] = download_url_type_public
        if app_type_mini_client is not UNSET:
            field_dict["APP_TYPE_MINI_CLIENT"] = app_type_mini_client
        if active_roles is not UNSET:
            field_dict["ACTIVE_ROLES"] = active_roles
        if session_from_am_add is not UNSET:
            field_dict["SESSION_FROM_AM_ADD"] = session_from_am_add
        if disable_change_info_protection is not UNSET:
            field_dict["DISABLE_CHANGE_INFO_PROTECTION"] = disable_change_info_protection
        if session_from_am is not UNSET:
            field_dict["SESSION_FROM_AM"] = session_from_am
        if session_from_ix is not UNSET:
            field_dict["SESSION_FROM_IX"] = session_from_ix
        if download_url_type_temporary is not UNSET:
            field_dict["DOWNLOAD_URL_TYPE_TEMPORARY"] = download_url_type_temporary
        if type_partner_application is not UNSET:
            field_dict["TYPE_PARTNER_APPLICATION"] = type_partner_application
        if start_docmask_workflows is not UNSET:
            field_dict["START_DOCMASK_WORKFLOWS"] = start_docmask_workflows
        if ix_url_base is not UNSET:
            field_dict["IX_URL_BASE"] = ix_url_base
        if download_url_type_persistent is not UNSET:
            field_dict["DOWNLOAD_URL_TYPE_PERSISTENT"] = download_url_type_persistent
        if encrypt_documents is not UNSET:
            field_dict["ENCRYPT_DOCUMENTS"] = encrypt_documents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        iso_date_with_delims = d.pop("ISO_DATE_WITH_DELIMS", UNSET)

        ticket_from_cookie = d.pop("TICKET_FROM_COOKIE", UNSET)

        client_app_version = d.pop("CLIENT_APP_VERSION", UNSET)

        client_app_name = d.pop("CLIENT_APP_NAME", UNSET)

        direct_dm_access = d.pop("DIRECT_DM_ACCESS", UNSET)

        download_url_type = d.pop("DOWNLOAD_URL_TYPE", UNSET)

        apply_all_blackenings = d.pop("APPLY_ALL_BLACKENINGS", UNSET)

        public_download_expiredtime = d.pop("PUBLIC_DOWNLOAD_EXPIREDTIME", UNSET)

        handle_ix_server_events = d.pop("HANDLE_IX_SERVER_EVENTS", UNSET)

        copy_objkeys_in_background = d.pop("COPY_OBJKEYS_IN_BACKGROUND", UNSET)

        client_app_type = d.pop("CLIENT_APP_TYPE", UNSET)

        translate_terms = d.pop("TRANSLATE_TERMS", UNSET)

        download_url_type_public_version = d.pop("DOWNLOAD_URL_TYPE_PUBLIC_VERSION", UNSET)

        http_session_ticket = d.pop("HTTP_SESSION_TICKET", UNSET)

        http_session_ix_connection = d.pop("HTTP_SESSION_IX_CONNECTION", UNSET)

        disable_logging_api_calls = d.pop("DISABLE_LOGGING_API_CALLS", UNSET)

        decrypt_documents = d.pop("DECRYPT_DOCUMENTS", UNSET)

        db_escape_char = d.pop("DB_ESCAPE_CHAR", UNSET)

        doc_url_base = d.pop("DOC_URL_BASE", UNSET)

        db_wildcards = d.pop("DB_WILDCARDS", UNSET)

        session_add = d.pop("SESSION_ADD", UNSET)

        public_download_count = d.pop("PUBLIC_DOWNLOAD_COUNT", UNSET)

        download_url_type_public = d.pop("DOWNLOAD_URL_TYPE_PUBLIC", UNSET)

        app_type_mini_client = d.pop("APP_TYPE_MINI_CLIENT", UNSET)

        active_roles = d.pop("ACTIVE_ROLES", UNSET)

        session_from_am_add = d.pop("SESSION_FROM_AM_ADD", UNSET)

        disable_change_info_protection = d.pop("DISABLE_CHANGE_INFO_PROTECTION", UNSET)

        session_from_am = d.pop("SESSION_FROM_AM", UNSET)

        session_from_ix = d.pop("SESSION_FROM_IX", UNSET)

        download_url_type_temporary = d.pop("DOWNLOAD_URL_TYPE_TEMPORARY", UNSET)

        type_partner_application = d.pop("TYPE_PARTNER_APPLICATION", UNSET)

        start_docmask_workflows = d.pop("START_DOCMASK_WORKFLOWS", UNSET)

        ix_url_base = d.pop("IX_URL_BASE", UNSET)

        download_url_type_persistent = d.pop("DOWNLOAD_URL_TYPE_PERSISTENT", UNSET)

        encrypt_documents = d.pop("ENCRYPT_DOCUMENTS", UNSET)

        session_options_c = cls(
            iso_date_with_delims=iso_date_with_delims,
            ticket_from_cookie=ticket_from_cookie,
            client_app_version=client_app_version,
            client_app_name=client_app_name,
            direct_dm_access=direct_dm_access,
            download_url_type=download_url_type,
            apply_all_blackenings=apply_all_blackenings,
            public_download_expiredtime=public_download_expiredtime,
            handle_ix_server_events=handle_ix_server_events,
            copy_objkeys_in_background=copy_objkeys_in_background,
            client_app_type=client_app_type,
            translate_terms=translate_terms,
            download_url_type_public_version=download_url_type_public_version,
            http_session_ticket=http_session_ticket,
            http_session_ix_connection=http_session_ix_connection,
            disable_logging_api_calls=disable_logging_api_calls,
            decrypt_documents=decrypt_documents,
            db_escape_char=db_escape_char,
            doc_url_base=doc_url_base,
            db_wildcards=db_wildcards,
            session_add=session_add,
            public_download_count=public_download_count,
            download_url_type_public=download_url_type_public,
            app_type_mini_client=app_type_mini_client,
            active_roles=active_roles,
            session_from_am_add=session_from_am_add,
            disable_change_info_protection=disable_change_info_protection,
            session_from_am=session_from_am,
            session_from_ix=session_from_ix,
            download_url_type_temporary=download_url_type_temporary,
            type_partner_application=type_partner_application,
            start_docmask_workflows=start_docmask_workflows,
            ix_url_base=ix_url_base,
            download_url_type_persistent=download_url_type_persistent,
            encrypt_documents=encrypt_documents,
        )

        session_options_c.additional_properties = d
        return session_options_c

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
