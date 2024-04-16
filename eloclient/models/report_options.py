from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_erp_code import ReportErpCode
    from ..models.report_mode_z import ReportModeZ


T = TypeVar("T", bound="ReportOptions")


@_attrs_define
class ReportOptions:
    """This class contains the codes for the activities/processes that are to be protocolled in a
    report.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            mode (Union[Unset, ReportModeZ]): <p>
                This class encapsulates the constants of <code>ReportModeC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            erp_codes (Union[Unset, List['ReportErpCode']]):
    """

    mode: Union[Unset, "ReportModeZ"] = UNSET
    erp_codes: Union[Unset, List["ReportErpCode"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.to_dict()

        erp_codes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.erp_codes, Unset):
            erp_codes = []
            for erp_codes_item_data in self.erp_codes:
                erp_codes_item = erp_codes_item_data.to_dict()
                erp_codes.append(erp_codes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if erp_codes is not UNSET:
            field_dict["erpCodes"] = erp_codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_erp_code import ReportErpCode
        from ..models.report_mode_z import ReportModeZ

        d = src_dict.copy()
        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, ReportModeZ]
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = ReportModeZ.from_dict(_mode)

        erp_codes = []
        _erp_codes = d.pop("erpCodes", UNSET)
        for erp_codes_item_data in _erp_codes or []:
            erp_codes_item = ReportErpCode.from_dict(erp_codes_item_data)

            erp_codes.append(erp_codes_item)

        report_options = cls(
            mode=mode,
            erp_codes=erp_codes,
        )

        report_options.additional_properties = d
        return report_options

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
