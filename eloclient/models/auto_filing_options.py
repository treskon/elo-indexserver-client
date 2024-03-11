from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoFilingOptions")


@_attrs_define
class AutoFilingOptions:
    """Options for function
    {@link IXServicePortIF#evalAutoFiling(ClientInfo, String, Sord, AutoFilingOptions)}

        Attributes:
            auto_filing_definition (Union[Unset, str]): Auto filing index string.
                If this option is set, paramter <code>maskId</code> in
                 {@link IXServicePortIF#evalAutoFiling(ClientInfo, String, Sord, AutoFilingOptions)} is ignored.
    """

    auto_filing_definition: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_filing_definition = self.auto_filing_definition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_filing_definition is not UNSET:
            field_dict["autoFilingDefinition"] = auto_filing_definition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_filing_definition = d.pop("autoFilingDefinition", UNSET)

        auto_filing_options = cls(
            auto_filing_definition=auto_filing_definition,
        )

        auto_filing_options.additional_properties = d
        return auto_filing_options

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
