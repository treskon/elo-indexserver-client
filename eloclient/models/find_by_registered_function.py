from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.any_ import Any


T = TypeVar("T", bound="FindByRegisteredFunction")


@_attrs_define
class FindByRegisteredFunction:
    """
    Attributes:
        args (Union[Unset, Any]): This class is a container for one value of a serializable type.
        function_name (Union[Unset, str]):
    """

    args: Union[Unset, "Any"] = UNSET
    function_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.any_ import Any

        args: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.args, Unset):
            args = self.args.to_dict()

        function_name = self.function_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if args is not UNSET:
            field_dict["args"] = args
        if function_name is not UNSET:
            field_dict["functionName"] = function_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.any_ import Any

        d = src_dict.copy()
        _args = d.pop("args", UNSET)
        args: Union[Unset, Any]
        if isinstance(_args, Unset):
            args = UNSET
        else:
            args = Any.from_dict(_args)

        function_name = d.pop("functionName", UNSET)

        find_by_registered_function = cls(
            args=args,
            function_name=function_name,
        )

        find_by_registered_function.additional_properties = d
        return find_by_registered_function

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
