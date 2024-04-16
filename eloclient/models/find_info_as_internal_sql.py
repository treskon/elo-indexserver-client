from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindInfoAsInternalSQL")


@_attrs_define
class FindInfoAsInternalSQL:
    """SQL command that is built from a FindInfo object.
    This class contains the elements of an internal
     SQL statement for finding Sord objects. Modifying this elements might cause errors or wrong
     results in subsequent versions of IX.

        Attributes:
            where_clause (Union[Unset, str]): SQL WHERE clause.
            group_by_clause (Union[Unset, str]): SQL GROUP BY clause.
            order_by_clause (Union[Unset, str]): SQL ORDER BY clause.
            from_tables (Union[Unset, str]): Comma separated list of table names.
    """

    where_clause: Union[Unset, str] = UNSET
    group_by_clause: Union[Unset, str] = UNSET
    order_by_clause: Union[Unset, str] = UNSET
    from_tables: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        where_clause = self.where_clause

        group_by_clause = self.group_by_clause

        order_by_clause = self.order_by_clause

        from_tables = self.from_tables

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if where_clause is not UNSET:
            field_dict["whereClause"] = where_clause
        if group_by_clause is not UNSET:
            field_dict["groupByClause"] = group_by_clause
        if order_by_clause is not UNSET:
            field_dict["orderByClause"] = order_by_clause
        if from_tables is not UNSET:
            field_dict["fromTables"] = from_tables

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        where_clause = d.pop("whereClause", UNSET)

        group_by_clause = d.pop("groupByClause", UNSET)

        order_by_clause = d.pop("orderByClause", UNSET)

        from_tables = d.pop("fromTables", UNSET)

        find_info_as_internal_sql = cls(
            where_clause=where_clause,
            group_by_clause=group_by_clause,
            order_by_clause=order_by_clause,
            from_tables=from_tables,
        )

        find_info_as_internal_sql.additional_properties = d
        return find_info_as_internal_sql

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
