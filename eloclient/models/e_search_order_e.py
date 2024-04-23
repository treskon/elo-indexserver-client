from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ESearchOrderE")


@_attrs_define
class ESearchOrderE:
    """Sort options for ElasticSearch.

    Attributes:
        idate_asc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        xdate_asc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        idate_desc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        relevance (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        xdate_desc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        tstamp_desc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        tstamp_asc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        alpha_desc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
        alpha_asc (Union[Unset, ESearchOrderE]): Sort options for ElasticSearch.
    """

    idate_asc: Union[Unset, "ESearchOrderE"] = UNSET
    xdate_asc: Union[Unset, "ESearchOrderE"] = UNSET
    idate_desc: Union[Unset, "ESearchOrderE"] = UNSET
    relevance: Union[Unset, "ESearchOrderE"] = UNSET
    xdate_desc: Union[Unset, "ESearchOrderE"] = UNSET
    tstamp_desc: Union[Unset, "ESearchOrderE"] = UNSET
    tstamp_asc: Union[Unset, "ESearchOrderE"] = UNSET
    alpha_desc: Union[Unset, "ESearchOrderE"] = UNSET
    alpha_asc: Union[Unset, "ESearchOrderE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idate_asc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.idate_asc, Unset):
            idate_asc = self.idate_asc.to_dict()

        xdate_asc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xdate_asc, Unset):
            xdate_asc = self.xdate_asc.to_dict()

        idate_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.idate_desc, Unset):
            idate_desc = self.idate_desc.to_dict()

        relevance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relevance, Unset):
            relevance = self.relevance.to_dict()

        xdate_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.xdate_desc, Unset):
            xdate_desc = self.xdate_desc.to_dict()

        tstamp_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tstamp_desc, Unset):
            tstamp_desc = self.tstamp_desc.to_dict()

        tstamp_asc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tstamp_asc, Unset):
            tstamp_asc = self.tstamp_asc.to_dict()

        alpha_desc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alpha_desc, Unset):
            alpha_desc = self.alpha_desc.to_dict()

        alpha_asc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alpha_asc, Unset):
            alpha_asc = self.alpha_asc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idate_asc is not UNSET:
            field_dict["IDATE_ASC"] = idate_asc
        if xdate_asc is not UNSET:
            field_dict["XDATE_ASC"] = xdate_asc
        if idate_desc is not UNSET:
            field_dict["IDATE_DESC"] = idate_desc
        if relevance is not UNSET:
            field_dict["RELEVANCE"] = relevance
        if xdate_desc is not UNSET:
            field_dict["XDATE_DESC"] = xdate_desc
        if tstamp_desc is not UNSET:
            field_dict["TSTAMP_DESC"] = tstamp_desc
        if tstamp_asc is not UNSET:
            field_dict["TSTAMP_ASC"] = tstamp_asc
        if alpha_desc is not UNSET:
            field_dict["ALPHA_DESC"] = alpha_desc
        if alpha_asc is not UNSET:
            field_dict["ALPHA_ASC"] = alpha_asc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _idate_asc = d.pop("IDATE_ASC", UNSET)
        idate_asc: Union[Unset, ESearchOrderE]
        if isinstance(_idate_asc, Unset):
            idate_asc = UNSET
        else:
            idate_asc = ESearchOrderE.from_dict(_idate_asc)

        _xdate_asc = d.pop("XDATE_ASC", UNSET)
        xdate_asc: Union[Unset, ESearchOrderE]
        if isinstance(_xdate_asc, Unset):
            xdate_asc = UNSET
        else:
            xdate_asc = ESearchOrderE.from_dict(_xdate_asc)

        _idate_desc = d.pop("IDATE_DESC", UNSET)
        idate_desc: Union[Unset, ESearchOrderE]
        if isinstance(_idate_desc, Unset):
            idate_desc = UNSET
        else:
            idate_desc = ESearchOrderE.from_dict(_idate_desc)

        _relevance = d.pop("RELEVANCE", UNSET)
        relevance: Union[Unset, ESearchOrderE]
        if isinstance(_relevance, Unset):
            relevance = UNSET
        else:
            relevance = ESearchOrderE.from_dict(_relevance)

        _xdate_desc = d.pop("XDATE_DESC", UNSET)
        xdate_desc: Union[Unset, ESearchOrderE]
        if isinstance(_xdate_desc, Unset):
            xdate_desc = UNSET
        else:
            xdate_desc = ESearchOrderE.from_dict(_xdate_desc)

        _tstamp_desc = d.pop("TSTAMP_DESC", UNSET)
        tstamp_desc: Union[Unset, ESearchOrderE]
        if isinstance(_tstamp_desc, Unset):
            tstamp_desc = UNSET
        else:
            tstamp_desc = ESearchOrderE.from_dict(_tstamp_desc)

        _tstamp_asc = d.pop("TSTAMP_ASC", UNSET)
        tstamp_asc: Union[Unset, ESearchOrderE]
        if isinstance(_tstamp_asc, Unset):
            tstamp_asc = UNSET
        else:
            tstamp_asc = ESearchOrderE.from_dict(_tstamp_asc)

        _alpha_desc = d.pop("ALPHA_DESC", UNSET)
        alpha_desc: Union[Unset, ESearchOrderE]
        if isinstance(_alpha_desc, Unset):
            alpha_desc = UNSET
        else:
            alpha_desc = ESearchOrderE.from_dict(_alpha_desc)

        _alpha_asc = d.pop("ALPHA_ASC", UNSET)
        alpha_asc: Union[Unset, ESearchOrderE]
        if isinstance(_alpha_asc, Unset):
            alpha_asc = UNSET
        else:
            alpha_asc = ESearchOrderE.from_dict(_alpha_asc)

        e_search_order_e = cls(
            idate_asc=idate_asc,
            xdate_asc=xdate_asc,
            idate_desc=idate_desc,
            relevance=relevance,
            xdate_desc=xdate_desc,
            tstamp_desc=tstamp_desc,
            tstamp_asc=tstamp_asc,
            alpha_desc=alpha_desc,
            alpha_asc=alpha_asc,
        )

        e_search_order_e.additional_properties = d
        return e_search_order_e

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
