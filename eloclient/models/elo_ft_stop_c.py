from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EloFtStopC")


@_attrs_define
class EloFtStopC:
    """<p>Bit constants for members of EloFtStop</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_stopword (Union[Unset, str]): DB column: stopword
            ln_stopword (Union[Unset, int]): DB column: stopword
    """

    mb_all_members: Union[Unset, str] = UNSET
    mb_stopword: Union[Unset, str] = UNSET
    ln_stopword: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all_members = self.mb_all_members

        mb_stopword = self.mb_stopword

        ln_stopword = self.ln_stopword

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_stopword is not UNSET:
            field_dict["mbStopword"] = mb_stopword
        if ln_stopword is not UNSET:
            field_dict["lnStopword"] = ln_stopword

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_stopword = d.pop("mbStopword", UNSET)

        ln_stopword = d.pop("lnStopword", UNSET)

        elo_ft_stop_c = cls(
            mb_all_members=mb_all_members,
            mb_stopword=mb_stopword,
            ln_stopword=ln_stopword,
        )

        elo_ft_stop_c.additional_properties = d
        return elo_ft_stop_c

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
