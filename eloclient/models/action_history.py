from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionHistory")


@_attrs_define
class ActionHistory:
    """
    Attributes:
        action_guid (Union[Unset, str]): Action GUID. Unique identifier.
        create_date_iso (Union[Unset, str]): Create date.
            This element is the ISO formatted create date of the action in the time zone of
             the client application. In order to convert this value into a date object, invoke function
             {@link de.elo.ix.client.IXConnection#isoToDate}.
        text (Union[Unset, str]): Comment text.
            This element is only valid for {@link EActionType#UserComment}, and
             {@link EActionType#AutoComment}.
    """

    action_guid: Union[Unset, str] = UNSET
    create_date_iso: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action_guid = self.action_guid

        create_date_iso = self.create_date_iso

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action_guid is not UNSET:
            field_dict["actionGuid"] = action_guid
        if create_date_iso is not UNSET:
            field_dict["createDateIso"] = create_date_iso
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action_guid = d.pop("actionGuid", UNSET)

        create_date_iso = d.pop("createDateIso", UNSET)

        text = d.pop("text", UNSET)

        action_history = cls(
            action_guid=action_guid,
            create_date_iso=create_date_iso,
            text=text,
        )

        action_history.additional_properties = d
        return action_history

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
