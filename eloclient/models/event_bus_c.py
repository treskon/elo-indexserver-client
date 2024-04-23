from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventBusC")


@_attrs_define
class EventBusC:
    """Constants related to the event bus API.

    Attributes:
        event_ocr_request (Union[Unset, str]): OCR Request Event.
            OCR Worker Processes listen to this event and process OCR on the supplied
             image data. In order to listen for this event, the session user must have the permission
             FLAG_ADMIN.
        event_ocr_result (Union[Unset, str]): OCR Finished Event. OCR Worker Process sends this event if the OCR
            processing is finished.
            The
             client application initiates a OCR request by calling API function processOCR. It receives an
             Event ID
        busid_max_system (Union[Unset, str]): Reserved.
        watch_delete (Union[Unset, int]): An object was deleted.
        busid_broadcast (Union[Unset, str]): Broadcast bus ID. The EventBusC.
            BUSID_BROADCAST refers to a public communication channel that
             can used by all applications and users. Any user can send events to this bus and is allowed to
             listen to it.
        event_type_watch_folder (Union[Unset, str]): Watch folder event.
            An event of this type is sent, if the contents of a given folder have been
             changed.
             <p>
             In order to register a listener for such events, the folder to be watched has to be specified
             with an object ID expression in <code>EventFilter.param2</code>(see checkoutSord):

             <pre>
             <code>
             IXConnection conn = ...

             // Folder to be watched
             int folderId = ...

             // Register listener
             conn.getEventBusApi().getBroadcastBus().addListener(
               EventBusC.EVENT_TYPE_WATCH_FOLDER,
               Integer.toString(folderId) );
             </code>
             </pre>
             </p>
             <p>
             For each modified Sord object in the watched folder, the client application receives one
             <code>Event</code>, whereby the data members are set as follows:

             <pre>
             <code>
             Event ev = ...

             // Folder being watched
             int folderId = Integer.parseInt(ev.getParam2());

             // Arguments
             Object[] args = (Object[])AnyToObject.toObject(ev.getAny());

             // Inserted, updated (e.g. locked) or deleted Sord
             Sord sord = (Sord)args[0];

             // Valid members of args[0]
             SordZ sordMembersZ = (SordZ)args[1];

             // What has happened: EventBusC.WATCH_INSERT, EventBusC.WATCH_UPDATE, EventBusC.WATCH_DELETE
             int what = (Integer)args[2];
             </code>
             </pre>
             </p>
             <p>
             Watch folder events are sent to every current acitve connection, provided that a listener was
             registered for it and the associated user has at least read access to the changed object. It is
             also sent to the connection that fires this event.
             </p>
        event_type_chat (Union[Unset, str]): Chat event type. Events of this type contain chat text.
        watch_insert (Union[Unset, int]): An object was inserted.
        busid_user (Union[Unset, str]): User related bus ID. For each user, an event bus exists with the bus ID
            EventBusC.
            BUSID_USER +
             user-ID. Any user can send events to this bus but only the owning user can listen to it.
        watch_update (Union[Unset, int]): An object was updated, locked or unlocked.
        event_type_max_system (Union[Unset, str]): User defined events must have a higher type value than this limit.
        event_type_close_chat (Union[Unset, str]): Close chat event type.
            An event of this type is sent to notify the subscribers that the chat
             channel (resp. event bus) will be closed shortly.
        event_type_open_chat (Union[Unset, str]): Open chat event type.
            Events of this type are used to invite subscribers to open a public final
             static chat channel.
        event_fulltext_indexing_status_update (Union[Unset, str]): Notify about status change in fulltext indexing.
    """

    event_ocr_request: Union[Unset, str] = UNSET
    event_ocr_result: Union[Unset, str] = UNSET
    busid_max_system: Union[Unset, str] = UNSET
    watch_delete: Union[Unset, int] = UNSET
    busid_broadcast: Union[Unset, str] = UNSET
    event_type_watch_folder: Union[Unset, str] = UNSET
    event_type_chat: Union[Unset, str] = UNSET
    watch_insert: Union[Unset, int] = UNSET
    busid_user: Union[Unset, str] = UNSET
    watch_update: Union[Unset, int] = UNSET
    event_type_max_system: Union[Unset, str] = UNSET
    event_type_close_chat: Union[Unset, str] = UNSET
    event_type_open_chat: Union[Unset, str] = UNSET
    event_fulltext_indexing_status_update: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_ocr_request = self.event_ocr_request

        event_ocr_result = self.event_ocr_result

        busid_max_system = self.busid_max_system

        watch_delete = self.watch_delete

        busid_broadcast = self.busid_broadcast

        event_type_watch_folder = self.event_type_watch_folder

        event_type_chat = self.event_type_chat

        watch_insert = self.watch_insert

        busid_user = self.busid_user

        watch_update = self.watch_update

        event_type_max_system = self.event_type_max_system

        event_type_close_chat = self.event_type_close_chat

        event_type_open_chat = self.event_type_open_chat

        event_fulltext_indexing_status_update = self.event_fulltext_indexing_status_update

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_ocr_request is not UNSET:
            field_dict["EVENT_OCR_REQUEST"] = event_ocr_request
        if event_ocr_result is not UNSET:
            field_dict["EVENT_OCR_RESULT"] = event_ocr_result
        if busid_max_system is not UNSET:
            field_dict["BUSID_MAX_SYSTEM"] = busid_max_system
        if watch_delete is not UNSET:
            field_dict["WATCH_DELETE"] = watch_delete
        if busid_broadcast is not UNSET:
            field_dict["BUSID_BROADCAST"] = busid_broadcast
        if event_type_watch_folder is not UNSET:
            field_dict["EVENT_TYPE_WATCH_FOLDER"] = event_type_watch_folder
        if event_type_chat is not UNSET:
            field_dict["EVENT_TYPE_CHAT"] = event_type_chat
        if watch_insert is not UNSET:
            field_dict["WATCH_INSERT"] = watch_insert
        if busid_user is not UNSET:
            field_dict["BUSID_USER"] = busid_user
        if watch_update is not UNSET:
            field_dict["WATCH_UPDATE"] = watch_update
        if event_type_max_system is not UNSET:
            field_dict["EVENT_TYPE_MAX_SYSTEM"] = event_type_max_system
        if event_type_close_chat is not UNSET:
            field_dict["EVENT_TYPE_CLOSE_CHAT"] = event_type_close_chat
        if event_type_open_chat is not UNSET:
            field_dict["EVENT_TYPE_OPEN_CHAT"] = event_type_open_chat
        if event_fulltext_indexing_status_update is not UNSET:
            field_dict["EVENT_FULLTEXT_INDEXING_STATUS_UPDATE"] = event_fulltext_indexing_status_update

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_ocr_request = d.pop("EVENT_OCR_REQUEST", UNSET)

        event_ocr_result = d.pop("EVENT_OCR_RESULT", UNSET)

        busid_max_system = d.pop("BUSID_MAX_SYSTEM", UNSET)

        watch_delete = d.pop("WATCH_DELETE", UNSET)

        busid_broadcast = d.pop("BUSID_BROADCAST", UNSET)

        event_type_watch_folder = d.pop("EVENT_TYPE_WATCH_FOLDER", UNSET)

        event_type_chat = d.pop("EVENT_TYPE_CHAT", UNSET)

        watch_insert = d.pop("WATCH_INSERT", UNSET)

        busid_user = d.pop("BUSID_USER", UNSET)

        watch_update = d.pop("WATCH_UPDATE", UNSET)

        event_type_max_system = d.pop("EVENT_TYPE_MAX_SYSTEM", UNSET)

        event_type_close_chat = d.pop("EVENT_TYPE_CLOSE_CHAT", UNSET)

        event_type_open_chat = d.pop("EVENT_TYPE_OPEN_CHAT", UNSET)

        event_fulltext_indexing_status_update = d.pop("EVENT_FULLTEXT_INDEXING_STATUS_UPDATE", UNSET)

        event_bus_c = cls(
            event_ocr_request=event_ocr_request,
            event_ocr_result=event_ocr_result,
            busid_max_system=busid_max_system,
            watch_delete=watch_delete,
            busid_broadcast=busid_broadcast,
            event_type_watch_folder=event_type_watch_folder,
            event_type_chat=event_type_chat,
            watch_insert=watch_insert,
            busid_user=busid_user,
            watch_update=watch_update,
            event_type_max_system=event_type_max_system,
            event_type_close_chat=event_type_close_chat,
            event_type_open_chat=event_type_open_chat,
            event_fulltext_indexing_status_update=event_fulltext_indexing_status_update,
        )

        event_bus_c.additional_properties = d
        return event_bus_c

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
