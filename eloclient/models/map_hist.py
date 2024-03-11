from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_hist_item import MapHistItem


T = TypeVar("T", bound="MapHist")


@_attrs_define
class MapHist:
    """Version history for maps.

    Attributes:
        hist_guid (Union[Unset, str]): GUID of the SordHist object.
        hist_source (Union[Unset, int]): Identifies the application with which changes were made to the keywording.
        map_guid (Union[Unset, str]): GUID of the map object.
        time_stamp_local (Union[Unset, str]): Timestamp of the change in the timezone of the client. The format is
            JJJJ.MM.DD.hh.mm.
            ss
        time_stamp_utc (Union[Unset, str]): Timestamp of the change in the timezone of the client, in UTC form. The
            format is JJJJ.MM.DD.hh.mm.
            ss
        user_name (Union[Unset, str]): The name of the user who carried out the changes.
        user_id (Union[Unset, int]): The user who carried out the changes.
        work_station (Union[Unset, str]): The name of the computer from which the change was carried out.
            This is the parameter clientComputer which is
             provided by the ix.login function.
        hist_items (Union[Unset, List['MapHistItem']]):
        map_id (Union[Unset, str]): ID of the map object.
    """

    hist_guid: Union[Unset, str] = UNSET
    hist_source: Union[Unset, int] = UNSET
    map_guid: Union[Unset, str] = UNSET
    time_stamp_local: Union[Unset, str] = UNSET
    time_stamp_utc: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    work_station: Union[Unset, str] = UNSET
    hist_items: Union[Unset, List["MapHistItem"]] = UNSET
    map_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hist_guid = self.hist_guid
        hist_source = self.hist_source
        map_guid = self.map_guid
        time_stamp_local = self.time_stamp_local
        time_stamp_utc = self.time_stamp_utc
        user_name = self.user_name
        user_id = self.user_id
        work_station = self.work_station
        hist_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hist_items, Unset):
            hist_items = []
            for hist_items_item_data in self.hist_items:
                hist_items_item = hist_items_item_data.to_dict()

                hist_items.append(hist_items_item)

        map_id = self.map_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hist_guid is not UNSET:
            field_dict["histGuid"] = hist_guid
        if hist_source is not UNSET:
            field_dict["histSource"] = hist_source
        if map_guid is not UNSET:
            field_dict["mapGuid"] = map_guid
        if time_stamp_local is not UNSET:
            field_dict["timeStampLocal"] = time_stamp_local
        if time_stamp_utc is not UNSET:
            field_dict["timeStampUTC"] = time_stamp_utc
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if work_station is not UNSET:
            field_dict["workStation"] = work_station
        if hist_items is not UNSET:
            field_dict["histItems"] = hist_items
        if map_id is not UNSET:
            field_dict["mapId"] = map_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_hist_item import MapHistItem

        d = src_dict.copy()
        hist_guid = d.pop("histGuid", UNSET)

        hist_source = d.pop("histSource", UNSET)

        map_guid = d.pop("mapGuid", UNSET)

        time_stamp_local = d.pop("timeStampLocal", UNSET)

        time_stamp_utc = d.pop("timeStampUTC", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        work_station = d.pop("workStation", UNSET)

        hist_items = []
        _hist_items = d.pop("histItems", UNSET)
        for hist_items_item_data in _hist_items or []:
            hist_items_item = MapHistItem.from_dict(hist_items_item_data)

            hist_items.append(hist_items_item)

        map_id = d.pop("mapId", UNSET)

        map_hist = cls(
            hist_guid=hist_guid,
            hist_source=hist_source,
            map_guid=map_guid,
            time_stamp_local=time_stamp_local,
            time_stamp_utc=time_stamp_utc,
            user_name=user_name,
            user_id=user_id,
            work_station=work_station,
            hist_items=hist_items,
            map_id=map_id,
        )

        map_hist.additional_properties = d
        return map_hist

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
