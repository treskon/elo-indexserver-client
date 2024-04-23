from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_mode_z import ReportModeZ


T = TypeVar("T", bound="ReportModeC")


@_attrs_define
class ReportModeC:
    """
    Attributes:
        limited (Union[Unset, ReportModeZ]): <p>
            This class encapsulates the constants of <code>ReportModeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        no (Union[Unset, ReportModeZ]): <p>
            This class encapsulates the constants of <code>ReportModeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        bset_full (Union[Unset, str]):
        bset_limited (Union[Unset, str]):
        bset_verbose (Union[Unset, str]):
        verbose (Union[Unset, ReportModeZ]): <p>
            This class encapsulates the constants of <code>ReportModeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        bset_no (Union[Unset, str]):
        full (Union[Unset, ReportModeZ]): <p>
            This class encapsulates the constants of <code>ReportModeC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    limited: Union[Unset, "ReportModeZ"] = UNSET
    no: Union[Unset, "ReportModeZ"] = UNSET
    bset_full: Union[Unset, str] = UNSET
    bset_limited: Union[Unset, str] = UNSET
    bset_verbose: Union[Unset, str] = UNSET
    verbose: Union[Unset, "ReportModeZ"] = UNSET
    bset_no: Union[Unset, str] = UNSET
    full: Union[Unset, "ReportModeZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limited: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.limited, Unset):
            limited = self.limited.to_dict()

        no: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.no, Unset):
            no = self.no.to_dict()

        bset_full = self.bset_full

        bset_limited = self.bset_limited

        bset_verbose = self.bset_verbose

        verbose: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.verbose, Unset):
            verbose = self.verbose.to_dict()

        bset_no = self.bset_no

        full: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full, Unset):
            full = self.full.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limited is not UNSET:
            field_dict["LIMITED"] = limited
        if no is not UNSET:
            field_dict["NO"] = no
        if bset_full is not UNSET:
            field_dict["bsetFULL"] = bset_full
        if bset_limited is not UNSET:
            field_dict["bsetLIMITED"] = bset_limited
        if bset_verbose is not UNSET:
            field_dict["bsetVERBOSE"] = bset_verbose
        if verbose is not UNSET:
            field_dict["VERBOSE"] = verbose
        if bset_no is not UNSET:
            field_dict["bsetNO"] = bset_no
        if full is not UNSET:
            field_dict["FULL"] = full

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_mode_z import ReportModeZ

        d = src_dict.copy()
        _limited = d.pop("LIMITED", UNSET)
        limited: Union[Unset, ReportModeZ]
        if isinstance(_limited, Unset):
            limited = UNSET
        else:
            limited = ReportModeZ.from_dict(_limited)

        _no = d.pop("NO", UNSET)
        no: Union[Unset, ReportModeZ]
        if isinstance(_no, Unset):
            no = UNSET
        else:
            no = ReportModeZ.from_dict(_no)

        bset_full = d.pop("bsetFULL", UNSET)

        bset_limited = d.pop("bsetLIMITED", UNSET)

        bset_verbose = d.pop("bsetVERBOSE", UNSET)

        _verbose = d.pop("VERBOSE", UNSET)
        verbose: Union[Unset, ReportModeZ]
        if isinstance(_verbose, Unset):
            verbose = UNSET
        else:
            verbose = ReportModeZ.from_dict(_verbose)

        bset_no = d.pop("bsetNO", UNSET)

        _full = d.pop("FULL", UNSET)
        full: Union[Unset, ReportModeZ]
        if isinstance(_full, Unset):
            full = UNSET
        else:
            full = ReportModeZ.from_dict(_full)

        report_mode_c = cls(
            limited=limited,
            no=no,
            bset_full=bset_full,
            bset_limited=bset_limited,
            bset_verbose=bset_verbose,
            verbose=verbose,
            bset_no=bset_no,
            full=full,
        )

        report_mode_c.additional_properties = d
        return report_mode_c

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
