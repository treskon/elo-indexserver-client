from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityOptionC")


@_attrs_define
class ActivityOptionC:
    """Constants for class ActivityOption

    Attributes:
        id_status (Union[Unset, int]): Option ID for receiving status.
        id_receiver (Union[Unset, int]): Option ID for receiver.
        id_value (Union[Unset, int]): Application defined IDs must be greater or equal to this value.
            Up to 10 application defined
             IDs can be defined. Their values have to be in the range from ID_VALUE+0 to ID_VALUE+9.
        id_trans (Union[Unset, int]): Option ID for transmission number.
        id_type (Union[Unset, int]): Option ID for shipping type.
    """

    id_status: Union[Unset, int] = UNSET
    id_receiver: Union[Unset, int] = UNSET
    id_value: Union[Unset, int] = UNSET
    id_trans: Union[Unset, int] = UNSET
    id_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_status = self.id_status

        id_receiver = self.id_receiver

        id_value = self.id_value

        id_trans = self.id_trans

        id_type = self.id_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id_status is not UNSET:
            field_dict["ID_STATUS"] = id_status
        if id_receiver is not UNSET:
            field_dict["ID_RECEIVER"] = id_receiver
        if id_value is not UNSET:
            field_dict["ID_VALUE"] = id_value
        if id_trans is not UNSET:
            field_dict["ID_TRANS"] = id_trans
        if id_type is not UNSET:
            field_dict["ID_TYPE"] = id_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_status = d.pop("ID_STATUS", UNSET)

        id_receiver = d.pop("ID_RECEIVER", UNSET)

        id_value = d.pop("ID_VALUE", UNSET)

        id_trans = d.pop("ID_TRANS", UNSET)

        id_type = d.pop("ID_TYPE", UNSET)

        activity_option_c = cls(
            id_status=id_status,
            id_receiver=id_receiver,
            id_value=id_value,
            id_trans=id_trans,
            id_type=id_type,
        )

        activity_option_c.additional_properties = d
        return activity_option_c

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
