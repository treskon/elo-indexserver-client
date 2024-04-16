from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemReport")


@_attrs_define
class SystemReport:
    """
    Attributes:
        doccount (Union[Unset, str]):
        ftsize (Union[Unset, str]):
        docsize (Union[Unset, str]):
        previewsize (Union[Unset, str]):
    """

    doccount: Union[Unset, str] = UNSET
    ftsize: Union[Unset, str] = UNSET
    docsize: Union[Unset, str] = UNSET
    previewsize: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doccount = self.doccount

        ftsize = self.ftsize

        docsize = self.docsize

        previewsize = self.previewsize

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doccount is not UNSET:
            field_dict["doccount"] = doccount
        if ftsize is not UNSET:
            field_dict["ftsize"] = ftsize
        if docsize is not UNSET:
            field_dict["docsize"] = docsize
        if previewsize is not UNSET:
            field_dict["previewsize"] = previewsize

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doccount = d.pop("doccount", UNSET)

        ftsize = d.pop("ftsize", UNSET)

        docsize = d.pop("docsize", UNSET)

        previewsize = d.pop("previewsize", UNSET)

        system_report = cls(
            doccount=doccount,
            ftsize=ftsize,
            docsize=docsize,
            previewsize=previewsize,
        )

        system_report.additional_properties = d
        return system_report

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
