from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect_z import AspectZ


T = TypeVar("T", bound="AspectC")


@_attrs_define
class AspectC:
    """<p>
    Constants related to class <code>Aspect</code>.

        Attributes:
            mb_all (Union[Unset, AspectZ]): This class encapsulates the constants of the AspectC class.
                <p>
                 Copyright: Copyright (c) 2019
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_only_lock (Union[Unset, AspectZ]): This class encapsulates the constants of the AspectC class.
                <p>
                 Copyright: Copyright (c) 2019
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mb_all_members (Union[Unset, str]): Member bit: read or write all elements.
            mb_aspect_lines (Union[Unset, str]): Member bit: read or write index lines.
    """

    mb_all: Union[Unset, "AspectZ"] = UNSET
    mb_only_lock: Union[Unset, "AspectZ"] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_aspect_lines: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mb_all: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_all, Unset):
            mb_all = self.mb_all.to_dict()

        mb_only_lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mb_only_lock, Unset):
            mb_only_lock = self.mb_only_lock.to_dict()

        mb_all_members = self.mb_all_members

        mb_aspect_lines = self.mb_aspect_lines

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mb_all is not UNSET:
            field_dict["mbAll"] = mb_all
        if mb_only_lock is not UNSET:
            field_dict["mbOnlyLock"] = mb_only_lock
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_aspect_lines is not UNSET:
            field_dict["mbAspectLines"] = mb_aspect_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect_z import AspectZ

        d = src_dict.copy()
        _mb_all = d.pop("mbAll", UNSET)
        mb_all: Union[Unset, AspectZ]
        if isinstance(_mb_all, Unset):
            mb_all = UNSET
        else:
            mb_all = AspectZ.from_dict(_mb_all)

        _mb_only_lock = d.pop("mbOnlyLock", UNSET)
        mb_only_lock: Union[Unset, AspectZ]
        if isinstance(_mb_only_lock, Unset):
            mb_only_lock = UNSET
        else:
            mb_only_lock = AspectZ.from_dict(_mb_only_lock)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_aspect_lines = d.pop("mbAspectLines", UNSET)

        aspect_c = cls(
            mb_all=mb_all,
            mb_only_lock=mb_only_lock,
            mb_all_members=mb_all_members,
            mb_aspect_lines=mb_aspect_lines,
        )

        aspect_c.additional_properties = d
        return aspect_c

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
