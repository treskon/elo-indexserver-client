from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString


T = TypeVar("T", bound="KeywordsDynamicResult")


@_attrs_define
class KeywordsDynamicResult:
    """<p>
    The class KeywordsDynamicResult defines the return value of the IX call
     {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)} .
     </p>

        Attributes:
            table (Union[Unset, List[List[str]]]):
            header (Union[Unset, List[str]]):
            key_names (Union[Unset, List[str]]):
            message (Union[Unset, str]): <p>
                The executed script may provide additional informations to the client such as "Please fill field XYZ". Such
                 informations are stored in the value <code>message</code>. The script has to provide the translation to the
                 client's language.
                 </p>
            more_results (Union[Unset, bool]): <p>
                Is true if there are more results.
                 </p>
            title (Union[Unset, str]): <p>
                A brief and succinctly description about the represented data. The script developer must provide a title,
                otherwise
                 an exception is thrown.
                 </p>
            column_properties (Union[Unset, List['MapToString']]):
    """

    table: Union[Unset, List[List[str]]] = UNSET
    header: Union[Unset, List[str]] = UNSET
    key_names: Union[Unset, List[str]] = UNSET
    message: Union[Unset, str] = UNSET
    more_results: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    column_properties: Union[Unset, List["MapToString"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        table: Union[Unset, List[List[str]]] = UNSET
        if not isinstance(self.table, Unset):
            table = []
            for componentsschemas_list_of_list_of_string_item_data in self.table:
                componentsschemas_list_of_list_of_string_item = componentsschemas_list_of_list_of_string_item_data

                table.append(componentsschemas_list_of_list_of_string_item)

        header: Union[Unset, List[str]] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header

        key_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.key_names, Unset):
            key_names = self.key_names

        message = self.message
        more_results = self.more_results
        title = self.title
        column_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.column_properties, Unset):
            column_properties = []
            for componentsschemas_list_of_map_to_string_item_data in self.column_properties:
                componentsschemas_list_of_map_to_string_item = (
                    componentsschemas_list_of_map_to_string_item_data.to_dict()
                )

                column_properties.append(componentsschemas_list_of_map_to_string_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if table is not UNSET:
            field_dict["table"] = table
        if header is not UNSET:
            field_dict["header"] = header
        if key_names is not UNSET:
            field_dict["keyNames"] = key_names
        if message is not UNSET:
            field_dict["message"] = message
        if more_results is not UNSET:
            field_dict["moreResults"] = more_results
        if title is not UNSET:
            field_dict["title"] = title
        if column_properties is not UNSET:
            field_dict["columnProperties"] = column_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        table = []
        _table = d.pop("table", UNSET)
        for componentsschemas_list_of_list_of_string_item_data in _table or []:
            componentsschemas_list_of_list_of_string_item = cast(
                List[str], componentsschemas_list_of_list_of_string_item_data
            )

            table.append(componentsschemas_list_of_list_of_string_item)

        header = cast(List[str], d.pop("header", UNSET))

        key_names = cast(List[str], d.pop("keyNames", UNSET))

        message = d.pop("message", UNSET)

        more_results = d.pop("moreResults", UNSET)

        title = d.pop("title", UNSET)

        column_properties = []
        _column_properties = d.pop("columnProperties", UNSET)
        for componentsschemas_list_of_map_to_string_item_data in _column_properties or []:
            componentsschemas_list_of_map_to_string_item = MapToString.from_dict(
                componentsschemas_list_of_map_to_string_item_data
            )

            column_properties.append(componentsschemas_list_of_map_to_string_item)

        keywords_dynamic_result = cls(
            table=table,
            header=header,
            key_names=key_names,
            message=message,
            more_results=more_results,
            title=title,
            column_properties=column_properties,
        )

        keywords_dynamic_result.additional_properties = d
        return keywords_dynamic_result

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
