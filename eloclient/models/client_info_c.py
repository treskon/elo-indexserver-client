from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientInfoC")


@_attrs_define
class ClientInfoC:
    """Constants for ClientInfo. These constanse are only for internal usage.

    Attributes:
        option_avoid_event_cascading (Union[Unset, int]): Can be used to check if an operation is called from a client
            or not
            (initially requested by FLOWS to avoid event recursion).
             Constant has to be evaluated in scripts accordingly.
             IX does not evaluate this constant.
        option_replication_request (Union[Unset, int]): Replication requests are marked with this bit.
        option_do_not_translate_terms (Union[Unset, int]): Do not translate terms into the language given by {@link
            ClientInfo#language}.
            Session option
             {@link SessionOptionsC#TRANSLATE_TERMS} is ignored.
    """

    option_avoid_event_cascading: Union[Unset, int] = UNSET
    option_replication_request: Union[Unset, int] = UNSET
    option_do_not_translate_terms: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        option_avoid_event_cascading = self.option_avoid_event_cascading

        option_replication_request = self.option_replication_request

        option_do_not_translate_terms = self.option_do_not_translate_terms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if option_avoid_event_cascading is not UNSET:
            field_dict["OPTION_AVOID_EVENT_CASCADING"] = option_avoid_event_cascading
        if option_replication_request is not UNSET:
            field_dict["OPTION_REPLICATION_REQUEST"] = option_replication_request
        if option_do_not_translate_terms is not UNSET:
            field_dict["OPTION_DO_NOT_TRANSLATE_TERMS"] = option_do_not_translate_terms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        option_avoid_event_cascading = d.pop("OPTION_AVOID_EVENT_CASCADING", UNSET)

        option_replication_request = d.pop("OPTION_REPLICATION_REQUEST", UNSET)

        option_do_not_translate_terms = d.pop("OPTION_DO_NOT_TRANSLATE_TERMS", UNSET)

        client_info_c = cls(
            option_avoid_event_cascading=option_avoid_event_cascading,
            option_replication_request=option_replication_request,
            option_do_not_translate_terms=option_do_not_translate_terms,
        )

        client_info_c.additional_properties = d
        return client_info_c

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
