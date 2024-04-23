from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect import Aspect


T = TypeVar("T", bound="BResult8006547")


@_attrs_define
class BResult8006547:
    """
    Attributes:
        result (Union[Unset, List['Aspect']]):
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, List["Aspect"]] = UNSET
    exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for componentsschemas_list_of_aspect_item_data in self.result:
                componentsschemas_list_of_aspect_item = componentsschemas_list_of_aspect_item_data.to_dict()
                result.append(componentsschemas_list_of_aspect_item)

        exception = self.exception

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if exception is not UNSET:
            field_dict["exception"] = exception

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect import Aspect

        d = src_dict.copy()
        result = []
        _result = d.pop("result", UNSET)
        for componentsschemas_list_of_aspect_item_data in _result or []:
            componentsschemas_list_of_aspect_item = Aspect.from_dict(componentsschemas_list_of_aspect_item_data)

            result.append(componentsschemas_list_of_aspect_item)

        exception = d.pop("exception", UNSET)

        b_result_8006547 = cls(
            result=result,
            exception=exception,
        )

        b_result_8006547.additional_properties = d
        return b_result_8006547

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
