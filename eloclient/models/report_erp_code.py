from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportErpCode")


@_attrs_define
class ReportErpCode:
    """This class describes an ERP code - a filter code number in the ELO report.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            id (Union[Unset, int]): ERP code
            limited (Union[Unset, bool]): This code is wirtten in limited report
            name (Union[Unset, str]): ERP name
            verbose (Union[Unset, bool]): This code is written in verbose report
    """

    id: Union[Unset, int] = UNSET
    limited: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    verbose: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        limited = self.limited
        name = self.name
        verbose = self.verbose

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if limited is not UNSET:
            field_dict["limited"] = limited
        if name is not UNSET:
            field_dict["name"] = name
        if verbose is not UNSET:
            field_dict["verbose"] = verbose

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        limited = d.pop("limited", UNSET)

        name = d.pop("name", UNSET)

        verbose = d.pop("verbose", UNSET)

        report_erp_code = cls(
            id=id,
            limited=limited,
            name=name,
            verbose=verbose,
        )

        report_erp_code.additional_properties = d
        return report_erp_code

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
