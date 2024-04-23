from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloIxOptOld")


@_attrs_define
class EloIxOptOld:
    """Internal class.

    Attributes:
        opt_no (Union[Unset, int]): DB column: optno
        opt_val (Union[Unset, str]): DB column: optval
        remark (Union[Unset, str]): DB column: remark
    """

    opt_no: Union[Unset, int] = UNSET
    opt_val: Union[Unset, str] = UNSET
    remark: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opt_no = self.opt_no

        opt_val = self.opt_val

        remark = self.remark

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opt_no is not UNSET:
            field_dict["optNo"] = opt_no
        if opt_val is not UNSET:
            field_dict["optVal"] = opt_val
        if remark is not UNSET:
            field_dict["remark"] = remark

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        opt_no = d.pop("optNo", UNSET)

        opt_val = d.pop("optVal", UNSET)

        remark = d.pop("remark", UNSET)

        elo_ix_opt_old = cls(
            opt_no=opt_no,
            opt_val=opt_val,
            remark=remark,
        )

        elo_ix_opt_old.additional_properties = d
        return elo_ix_opt_old

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
