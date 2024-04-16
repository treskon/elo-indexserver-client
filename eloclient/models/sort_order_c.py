from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SortOrderC")


@_attrs_define
class SortOrderC:
    """This class contains constants for sorting of archive entries and search results.

    Attributes:
        dummy (Union[Unset, int]):
        xdate (Union[Unset, int]): Subitems are sorted by external date.
        idate (Union[Unset, int]): Subitems are sorted by internal date.
        ixdate (Union[Unset, int]): Subitems are sorted by external date descending.
        iidate (Union[Unset, int]): Subitems are sorted by internal date descending.
        alpha (Union[Unset, int]): Subitems are sorted by name.
        username (Union[Unset, int]): Used for the ascending ordering of threads by username.
            This value can be used for
             {@link FindBackgroundThreadOptions#sortOrder}.
        manual (Union[Unset, int]): Subitems are sorted manually.
        ialpha (Union[Unset, int]): Subitems are sorted by name descending.
        none (Union[Unset, int]):
        iusername (Union[Unset, int]): Used for the descending ordering of threads by username.
            This value can be used for
             {@link FindBackgroundThreadOptions#sortOrder}.
        default (Union[Unset, int]):
    """

    dummy: Union[Unset, int] = UNSET
    xdate: Union[Unset, int] = UNSET
    idate: Union[Unset, int] = UNSET
    ixdate: Union[Unset, int] = UNSET
    iidate: Union[Unset, int] = UNSET
    alpha: Union[Unset, int] = UNSET
    username: Union[Unset, int] = UNSET
    manual: Union[Unset, int] = UNSET
    ialpha: Union[Unset, int] = UNSET
    none: Union[Unset, int] = UNSET
    iusername: Union[Unset, int] = UNSET
    default: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dummy = self.dummy

        xdate = self.xdate

        idate = self.idate

        ixdate = self.ixdate

        iidate = self.iidate

        alpha = self.alpha

        username = self.username

        manual = self.manual

        ialpha = self.ialpha

        none = self.none

        iusername = self.iusername

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dummy is not UNSET:
            field_dict["dummy"] = dummy
        if xdate is not UNSET:
            field_dict["XDATE"] = xdate
        if idate is not UNSET:
            field_dict["IDATE"] = idate
        if ixdate is not UNSET:
            field_dict["IXDATE"] = ixdate
        if iidate is not UNSET:
            field_dict["IIDATE"] = iidate
        if alpha is not UNSET:
            field_dict["ALPHA"] = alpha
        if username is not UNSET:
            field_dict["USERNAME"] = username
        if manual is not UNSET:
            field_dict["MANUAL"] = manual
        if ialpha is not UNSET:
            field_dict["IALPHA"] = ialpha
        if none is not UNSET:
            field_dict["NONE"] = none
        if iusername is not UNSET:
            field_dict["IUSERNAME"] = iusername
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dummy = d.pop("dummy", UNSET)

        xdate = d.pop("XDATE", UNSET)

        idate = d.pop("IDATE", UNSET)

        ixdate = d.pop("IXDATE", UNSET)

        iidate = d.pop("IIDATE", UNSET)

        alpha = d.pop("ALPHA", UNSET)

        username = d.pop("USERNAME", UNSET)

        manual = d.pop("MANUAL", UNSET)

        ialpha = d.pop("IALPHA", UNSET)

        none = d.pop("NONE", UNSET)

        iusername = d.pop("IUSERNAME", UNSET)

        default = d.pop("DEFAULT", UNSET)

        sort_order_c = cls(
            dummy=dummy,
            xdate=xdate,
            idate=idate,
            ixdate=ixdate,
            iidate=iidate,
            alpha=alpha,
            username=username,
            manual=manual,
            ialpha=ialpha,
            none=none,
            iusername=iusername,
            default=default,
        )

        sort_order_c.additional_properties = d
        return sort_order_c

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
