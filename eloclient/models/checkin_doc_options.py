from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckinDocOptions")


@_attrs_define
class CheckinDocOptions:
    """This class defines options for the API function checkinDocBegin2.

    Attributes:
        keep_ids (Union[Unset, bool]): If <tt>true</tt>, the DocVersion to check-in will use the ID and GUID you
            specify.
            In order to
             only set the GUID, set the ID to 0.
    """

    keep_ids: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keep_ids = self.keep_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keep_ids is not UNSET:
            field_dict["keepIds"] = keep_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        keep_ids = d.pop("keepIds", UNSET)

        checkin_doc_options = cls(
            keep_ids=keep_ids,
        )

        checkin_doc_options.additional_properties = d
        return checkin_doc_options

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
