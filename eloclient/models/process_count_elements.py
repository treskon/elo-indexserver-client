from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.count_result import CountResult


T = TypeVar("T", bound="ProcessCountElements")


@_attrs_define
class ProcessCountElements:
    """This class make possible the count of the archive elements.
    <p>
     Copyright: Copyright (c) 2008
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            count_result (Union[Unset, CountResult]): Class for the results of one count process.
    """

    count_result: Union[Unset, "CountResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.count_result, Unset):
            count_result = self.count_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_result is not UNSET:
            field_dict["countResult"] = count_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.count_result import CountResult

        d = src_dict.copy()
        _count_result = d.pop("countResult", UNSET)
        count_result: Union[Unset, CountResult]
        if isinstance(_count_result, Unset):
            count_result = UNSET
        else:
            count_result = CountResult.from_dict(_count_result)

        process_count_elements = cls(
            count_result=count_result,
        )

        process_count_elements.additional_properties = d
        return process_count_elements

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
