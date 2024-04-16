from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryJobProtocolC")


@_attrs_define
class QueryJobProtocolC:
    """<p>
    Constants for querying log messages of background jobs.
     </p>

        Attributes:
            log_level_warn (Union[Unset, int]): Return only warnings.
            log_level_error (Union[Unset, int]): Return only errors.
            log_level_info (Union[Unset, int]): Return only normal informations.
            objid_not_set (Union[Unset, int]): This value indicates that the object-ID is not set.
    """

    log_level_warn: Union[Unset, int] = UNSET
    log_level_error: Union[Unset, int] = UNSET
    log_level_info: Union[Unset, int] = UNSET
    objid_not_set: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        log_level_warn = self.log_level_warn

        log_level_error = self.log_level_error

        log_level_info = self.log_level_info

        objid_not_set = self.objid_not_set

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if log_level_warn is not UNSET:
            field_dict["LOG_LEVEL_WARN"] = log_level_warn
        if log_level_error is not UNSET:
            field_dict["LOG_LEVEL_ERROR"] = log_level_error
        if log_level_info is not UNSET:
            field_dict["LOG_LEVEL_INFO"] = log_level_info
        if objid_not_set is not UNSET:
            field_dict["OBJID_NOT_SET"] = objid_not_set

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        log_level_warn = d.pop("LOG_LEVEL_WARN", UNSET)

        log_level_error = d.pop("LOG_LEVEL_ERROR", UNSET)

        log_level_info = d.pop("LOG_LEVEL_INFO", UNSET)

        objid_not_set = d.pop("OBJID_NOT_SET", UNSET)

        query_job_protocol_c = cls(
            log_level_warn=log_level_warn,
            log_level_error=log_level_error,
            log_level_info=log_level_info,
            objid_not_set=objid_not_set,
        )

        query_job_protocol_c.additional_properties = d
        return query_job_protocol_c

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
