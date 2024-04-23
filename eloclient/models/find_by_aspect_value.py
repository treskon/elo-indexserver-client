from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_search_value import IndexSearchValue


T = TypeVar("T", bound="FindByAspectValue")


@_attrs_define
class FindByAspectValue:
    """This class contains disjunct conditions to search for aspect data in the database.
    Used as value
     in {@link FindByIndex#aspects}.

        Attributes:
            condition (Union[Unset, IndexSearchValue]): This class is used to search for index values in aspect objects.
                Regardless of whether the
                 search-mode is set to {@link SearchModeC#OR}, all of the conditions defined in this class must be
                 met. In other words, the server will evaluate all the conditions in this class in a
                 "<tt>???</tt>" manner.<br>
                 Please not that you must use the correct field according to the aspect's line type. The
                 Indexserver will not evaluate other fields. That means that if the aspect's line type is
                 {@link AspectLineC#TYPE_DOUBLE}, the Indexserver will look at {@link #doubleValue} and
                 {@link #doubleValues} only.
            disjunct_conditions (Union[Unset, List['IndexSearchValue']]):
    """

    condition: Union[Unset, "IndexSearchValue"] = UNSET
    disjunct_conditions: Union[Unset, List["IndexSearchValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        disjunct_conditions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.disjunct_conditions, Unset):
            disjunct_conditions = []
            for componentsschemas_list_of_index_search_value_item_data in self.disjunct_conditions:
                componentsschemas_list_of_index_search_value_item = (
                    componentsschemas_list_of_index_search_value_item_data.to_dict()
                )
                disjunct_conditions.append(componentsschemas_list_of_index_search_value_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition is not UNSET:
            field_dict["condition"] = condition
        if disjunct_conditions is not UNSET:
            field_dict["disjunctConditions"] = disjunct_conditions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.index_search_value import IndexSearchValue

        d = src_dict.copy()
        _condition = d.pop("condition", UNSET)
        condition: Union[Unset, IndexSearchValue]
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = IndexSearchValue.from_dict(_condition)

        disjunct_conditions = []
        _disjunct_conditions = d.pop("disjunctConditions", UNSET)
        for componentsschemas_list_of_index_search_value_item_data in _disjunct_conditions or []:
            componentsschemas_list_of_index_search_value_item = IndexSearchValue.from_dict(
                componentsschemas_list_of_index_search_value_item_data
            )

            disjunct_conditions.append(componentsschemas_list_of_index_search_value_item)

        find_by_aspect_value = cls(
            condition=condition,
            disjunct_conditions=disjunct_conditions,
        )

        find_by_aspect_value.additional_properties = d
        return find_by_aspect_value

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
