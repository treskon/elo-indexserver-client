from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sord_hist_key import SordHistKey


T = TypeVar("T", bound="SordHist")


@_attrs_define
class SordHist:
    """Version history for the keywording from an object.
    A version history is created for a sord object when the keywording
     is changed for the first time (a newly created sord has no version history). Once created only one SordHist object
     exist for the sord object and is assigned to the sord object via the Sord.guid = SordHist.objGuid relationship. The
     keywording properties that were altered in the change process are saved in an array of SordHistKey objects.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            hist_guid (Union[Unset, str]): GUID of the SordHist object.
            hist_source (Union[Unset, int]): Identifies the application with which changes were made to the keywording.
            obj_guid (Union[Unset, str]): GUID of the sord object.
            time_stamp_local (Union[Unset, str]): Timestamp of the change in the timezone of the client. The format is
                JJJJ.MM.DD.hh.mm.
                ss
            time_stamp_utc (Union[Unset, str]): Timestamp of the change in the timezone of the client, in UTC form. The
                format is JJJJ.MM.DD.hh.mm.
                ss
            user_name (Union[Unset, str]): The name of the user who carried out the changes.
            user_no (Union[Unset, int]): The user who carried out the changes.
            work_station (Union[Unset, str]): The name of the computer from which the change was carried out.
                This is the parameter clientComputer which is
                 provided by the ix.login function.
            hist_keys (Union[Unset, List['SordHistKey']]):
    """

    hist_guid: Union[Unset, str] = UNSET
    hist_source: Union[Unset, int] = UNSET
    obj_guid: Union[Unset, str] = UNSET
    time_stamp_local: Union[Unset, str] = UNSET
    time_stamp_utc: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_no: Union[Unset, int] = UNSET
    work_station: Union[Unset, str] = UNSET
    hist_keys: Union[Unset, List["SordHistKey"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hist_guid = self.hist_guid
        hist_source = self.hist_source
        obj_guid = self.obj_guid
        time_stamp_local = self.time_stamp_local
        time_stamp_utc = self.time_stamp_utc
        user_name = self.user_name
        user_no = self.user_no
        work_station = self.work_station
        hist_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.hist_keys, Unset):
            hist_keys = []
            for hist_keys_item_data in self.hist_keys:
                hist_keys_item = hist_keys_item_data.to_dict()

                hist_keys.append(hist_keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hist_guid is not UNSET:
            field_dict["histGuid"] = hist_guid
        if hist_source is not UNSET:
            field_dict["histSource"] = hist_source
        if obj_guid is not UNSET:
            field_dict["objGuid"] = obj_guid
        if time_stamp_local is not UNSET:
            field_dict["timeStampLocal"] = time_stamp_local
        if time_stamp_utc is not UNSET:
            field_dict["timeStampUTC"] = time_stamp_utc
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_no is not UNSET:
            field_dict["userNo"] = user_no
        if work_station is not UNSET:
            field_dict["workStation"] = work_station
        if hist_keys is not UNSET:
            field_dict["histKeys"] = hist_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sord_hist_key import SordHistKey

        d = src_dict.copy()
        hist_guid = d.pop("histGuid", UNSET)

        hist_source = d.pop("histSource", UNSET)

        obj_guid = d.pop("objGuid", UNSET)

        time_stamp_local = d.pop("timeStampLocal", UNSET)

        time_stamp_utc = d.pop("timeStampUTC", UNSET)

        user_name = d.pop("userName", UNSET)

        user_no = d.pop("userNo", UNSET)

        work_station = d.pop("workStation", UNSET)

        hist_keys = []
        _hist_keys = d.pop("histKeys", UNSET)
        for hist_keys_item_data in _hist_keys or []:
            hist_keys_item = SordHistKey.from_dict(hist_keys_item_data)

            hist_keys.append(hist_keys_item)

        sord_hist = cls(
            hist_guid=hist_guid,
            hist_source=hist_source,
            obj_guid=obj_guid,
            time_stamp_local=time_stamp_local,
            time_stamp_utc=time_stamp_utc,
            user_name=user_name,
            user_no=user_no,
            work_station=work_station,
            hist_keys=hist_keys,
        )

        sord_hist.additional_properties = d
        return sord_hist

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
