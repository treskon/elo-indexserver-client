from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.es_settings_obj import ESSettingsObj


T = TypeVar("T", bound="BResult460462395")


@_attrs_define
class BResult460462395:
    """
    Attributes:
        result (Union[Unset, ESSettingsObj]): <p>
            <b>checkoutEsSettings</b> returns the current IX instance name, a list of all available IX
             instances as well as one EsInstanceSettings object for every IX instance of the archive and one
             for the setting "_ALL". If there is no entry for a setting in the database, the default value is
             returned as value.
             </p>

             <p>
             <b>checkinEsSettings</b> writes entries for every EsInstanceSettings to the database:
             </p>
             <ul>
             <li>If a EsSettingsProperty member is null, nothing is written or deleted.
             <li>To delete a setting, the EsSettingsProperty member must be set, but its member 'value' must
             be set to 'null'
             </ul>
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, "ESSettingsObj"] = UNSET
    exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        exception = self.exception

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.es_settings_obj import ESSettingsObj

        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, ESSettingsObj]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ESSettingsObj.from_dict(_result)

        exception = d.pop("exception", UNSET)

        b_result_460462395 = cls(
            result=result,
            exception=exception,
        )

        b_result_460462395.additional_properties = d
        return b_result_460462395

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
