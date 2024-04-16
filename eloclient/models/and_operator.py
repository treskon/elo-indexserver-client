from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_object import QueryObject


T = TypeVar("T", bound="AndOperator")


@_attrs_define
class AndOperator:
    """This operator contains a list of QueryObjects and concatenates them with an "AND" operation.
    This
     means, a document is returned if all of the QueryObjects are present in the document. For REST
     calls, use class QueryOperator and set the operator type in {@link QueryOperator#operatorType}.

        Attributes:
            query_object_list (Union[Unset, List['QueryObject']]):
    """

    query_object_list: Union[Unset, List["QueryObject"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        query_object_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.query_object_list, Unset):
            query_object_list = []
            for componentsschemas_list_of_query_object_item_data in self.query_object_list:
                componentsschemas_list_of_query_object_item = componentsschemas_list_of_query_object_item_data.to_dict()
                query_object_list.append(componentsschemas_list_of_query_object_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query_object_list is not UNSET:
            field_dict["queryObjectList"] = query_object_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.query_object import QueryObject

        d = src_dict.copy()
        query_object_list = []
        _query_object_list = d.pop("queryObjectList", UNSET)
        for componentsschemas_list_of_query_object_item_data in _query_object_list or []:
            componentsschemas_list_of_query_object_item = QueryObject.from_dict(
                componentsschemas_list_of_query_object_item_data
            )

            query_object_list.append(componentsschemas_list_of_query_object_item)

        and_operator = cls(
            query_object_list=query_object_list,
        )

        and_operator.additional_properties = d
        return and_operator

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
