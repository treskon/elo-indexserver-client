from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action import Action


T = TypeVar("T", bound="BResult2013723887")


@_attrs_define
class BResult2013723887:
    """
    Attributes:
        result (Union[Unset, List['Action']]):
        exception (Union[Unset, str]): Error message
    """

    result: Union[Unset, List["Action"]] = UNSET
    exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for componentsschemas_list_of_action_item_data in self.result:
                componentsschemas_list_of_action_item = componentsschemas_list_of_action_item_data.to_dict()
                result.append(componentsschemas_list_of_action_item)

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
        from ..models.action import Action

        d = src_dict.copy()
        result = []
        _result = d.pop("result", UNSET)
        for componentsschemas_list_of_action_item_data in _result or []:
            componentsschemas_list_of_action_item = Action.from_dict(componentsschemas_list_of_action_item_data)

            result.append(componentsschemas_list_of_action_item)

        exception = d.pop("exception", UNSET)

        b_result_2013723887 = cls(
            result=result,
            exception=exception,
        )

        b_result_2013723887.additional_properties = d
        return b_result_2013723887

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
