from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndexSearchOperator")


@_attrs_define
class IndexSearchOperator:
    """The constants in this class define the supported operations for conditions when searching for
    aspect objects in the database.

        Attributes:
            lower_than (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            equals (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            like (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            lower (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            greater_than (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations
                for conditions when searching for
                aspect objects in the database.
            greater (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            isnull (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
            isempty (Union[Unset, IndexSearchOperator]): The constants in this class define the supported operations for
                conditions when searching for
                aspect objects in the database.
    """

    lower_than: Union[Unset, "IndexSearchOperator"] = UNSET
    equals: Union[Unset, "IndexSearchOperator"] = UNSET
    like: Union[Unset, "IndexSearchOperator"] = UNSET
    lower: Union[Unset, "IndexSearchOperator"] = UNSET
    greater_than: Union[Unset, "IndexSearchOperator"] = UNSET
    greater: Union[Unset, "IndexSearchOperator"] = UNSET
    isnull: Union[Unset, "IndexSearchOperator"] = UNSET
    isempty: Union[Unset, "IndexSearchOperator"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        lower_than: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lower_than, Unset):
            lower_than = self.lower_than.to_dict()

        equals: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.equals, Unset):
            equals = self.equals.to_dict()

        like: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.like, Unset):
            like = self.like.to_dict()

        lower: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lower, Unset):
            lower = self.lower.to_dict()

        greater_than: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.greater_than, Unset):
            greater_than = self.greater_than.to_dict()

        greater: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.greater, Unset):
            greater = self.greater.to_dict()

        isnull: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.isnull, Unset):
            isnull = self.isnull.to_dict()

        isempty: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.isempty, Unset):
            isempty = self.isempty.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lower_than is not UNSET:
            field_dict["LOWER_THAN"] = lower_than
        if equals is not UNSET:
            field_dict["EQUALS"] = equals
        if like is not UNSET:
            field_dict["LIKE"] = like
        if lower is not UNSET:
            field_dict["LOWER"] = lower
        if greater_than is not UNSET:
            field_dict["GREATER_THAN"] = greater_than
        if greater is not UNSET:
            field_dict["GREATER"] = greater
        if isnull is not UNSET:
            field_dict["ISNULL"] = isnull
        if isempty is not UNSET:
            field_dict["ISEMPTY"] = isempty

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _lower_than = d.pop("LOWER_THAN", UNSET)
        lower_than: Union[Unset, IndexSearchOperator]
        if isinstance(_lower_than, Unset):
            lower_than = UNSET
        else:
            lower_than = IndexSearchOperator.from_dict(_lower_than)

        _equals = d.pop("EQUALS", UNSET)
        equals: Union[Unset, IndexSearchOperator]
        if isinstance(_equals, Unset):
            equals = UNSET
        else:
            equals = IndexSearchOperator.from_dict(_equals)

        _like = d.pop("LIKE", UNSET)
        like: Union[Unset, IndexSearchOperator]
        if isinstance(_like, Unset):
            like = UNSET
        else:
            like = IndexSearchOperator.from_dict(_like)

        _lower = d.pop("LOWER", UNSET)
        lower: Union[Unset, IndexSearchOperator]
        if isinstance(_lower, Unset):
            lower = UNSET
        else:
            lower = IndexSearchOperator.from_dict(_lower)

        _greater_than = d.pop("GREATER_THAN", UNSET)
        greater_than: Union[Unset, IndexSearchOperator]
        if isinstance(_greater_than, Unset):
            greater_than = UNSET
        else:
            greater_than = IndexSearchOperator.from_dict(_greater_than)

        _greater = d.pop("GREATER", UNSET)
        greater: Union[Unset, IndexSearchOperator]
        if isinstance(_greater, Unset):
            greater = UNSET
        else:
            greater = IndexSearchOperator.from_dict(_greater)

        _isnull = d.pop("ISNULL", UNSET)
        isnull: Union[Unset, IndexSearchOperator]
        if isinstance(_isnull, Unset):
            isnull = UNSET
        else:
            isnull = IndexSearchOperator.from_dict(_isnull)

        _isempty = d.pop("ISEMPTY", UNSET)
        isempty: Union[Unset, IndexSearchOperator]
        if isinstance(_isempty, Unset):
            isempty = UNSET
        else:
            isempty = IndexSearchOperator.from_dict(_isempty)

        index_search_operator = cls(
            lower_than=lower_than,
            equals=equals,
            like=like,
            lower=lower,
            greater_than=greater_than,
            greater=greater,
            isnull=isnull,
            isempty=isempty,
        )

        index_search_operator.additional_properties = d
        return index_search_operator

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
