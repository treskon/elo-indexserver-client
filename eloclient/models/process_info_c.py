from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessInfoC")


@_attrs_define
class ProcessInfoC:
    """Constants class for the ProcessInfo class.
    Errors: The error modes are ordered by increasing failure tolerance. In most cases a tree walk
     will traverse nodes in prefix mode except scripts, that may have an user defined processing
     position, so the operational success of a given node directly influences further processing.
     ERRORMODE_ALL, the zero failure tolerance, stops the job (nearly) immediately, while
     ERRORMODE_SKIP_SUBTREE just skips subtree traversals, but continues with lists or siblings. If
     you pass ERRORMODE_SKIP_PROCINFO the sequence of ProcessInfo members will be executed completely,
     whether errors occur or not. The most tolerant mode is ERRORMODE_SKIP_PROCINFO where only errors
     impeding further traversing stop the job.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            delstatus_deleted (Union[Unset, int]): filter ony deleted SORDs.
            errormode_skip_subtree (Union[Unset, int]): Stop the subtree processing (processTrees only), but continue with
                list elements respectively
                siblings.
            delstatus_all (Union[Unset, int]): Do not filter by SORD status.
            errormode_critical_only (Union[Unset, int]): Stop only on non-recoverable errors.
            errormode_skip_procinfo (Union[Unset, int]): Stop the ProcessInfo sequence for the current Node.
            delstatus_valid (Union[Unset, int]): Filter only undeleted SORDs.
            errormode_all (Union[Unset, int]): Processing will be stopped when an error occurs, regardless of the error
                type.
            procmsgmax (Union[Unset, int]): Maximum allowed amount of error messages.
    """

    delstatus_deleted: Union[Unset, int] = UNSET
    errormode_skip_subtree: Union[Unset, int] = UNSET
    delstatus_all: Union[Unset, int] = UNSET
    errormode_critical_only: Union[Unset, int] = UNSET
    errormode_skip_procinfo: Union[Unset, int] = UNSET
    delstatus_valid: Union[Unset, int] = UNSET
    errormode_all: Union[Unset, int] = UNSET
    procmsgmax: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delstatus_deleted = self.delstatus_deleted

        errormode_skip_subtree = self.errormode_skip_subtree

        delstatus_all = self.delstatus_all

        errormode_critical_only = self.errormode_critical_only

        errormode_skip_procinfo = self.errormode_skip_procinfo

        delstatus_valid = self.delstatus_valid

        errormode_all = self.errormode_all

        procmsgmax = self.procmsgmax

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delstatus_deleted is not UNSET:
            field_dict["DELSTATUS_DELETED"] = delstatus_deleted
        if errormode_skip_subtree is not UNSET:
            field_dict["ERRORMODE_SKIP_SUBTREE"] = errormode_skip_subtree
        if delstatus_all is not UNSET:
            field_dict["DELSTATUS_ALL"] = delstatus_all
        if errormode_critical_only is not UNSET:
            field_dict["ERRORMODE_CRITICAL_ONLY"] = errormode_critical_only
        if errormode_skip_procinfo is not UNSET:
            field_dict["ERRORMODE_SKIP_PROCINFO"] = errormode_skip_procinfo
        if delstatus_valid is not UNSET:
            field_dict["DELSTATUS_VALID"] = delstatus_valid
        if errormode_all is not UNSET:
            field_dict["ERRORMODE_ALL"] = errormode_all
        if procmsgmax is not UNSET:
            field_dict["PROCMSGMAX"] = procmsgmax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delstatus_deleted = d.pop("DELSTATUS_DELETED", UNSET)

        errormode_skip_subtree = d.pop("ERRORMODE_SKIP_SUBTREE", UNSET)

        delstatus_all = d.pop("DELSTATUS_ALL", UNSET)

        errormode_critical_only = d.pop("ERRORMODE_CRITICAL_ONLY", UNSET)

        errormode_skip_procinfo = d.pop("ERRORMODE_SKIP_PROCINFO", UNSET)

        delstatus_valid = d.pop("DELSTATUS_VALID", UNSET)

        errormode_all = d.pop("ERRORMODE_ALL", UNSET)

        procmsgmax = d.pop("PROCMSGMAX", UNSET)

        process_info_c = cls(
            delstatus_deleted=delstatus_deleted,
            errormode_skip_subtree=errormode_skip_subtree,
            delstatus_all=delstatus_all,
            errormode_critical_only=errormode_critical_only,
            errormode_skip_procinfo=errormode_skip_procinfo,
            delstatus_valid=delstatus_valid,
            errormode_all=errormode_all,
            procmsgmax=procmsgmax,
        )

        process_info_c.additional_properties = d
        return process_info_c

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
