from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.es_node_obj import ESNodeObj


T = TypeVar("T", bound="ESInfoObj")


@_attrs_define
class ESInfoObj:
    """<b><i>Note: For internal use only. Might change in the near future.
    </i></b>

        Attributes:
            status_red (Union[Unset, int]):
            document_count (Union[Unset, int]):
            connection_count (Union[Unset, int]):
            langs_with_doc_count (Union[Unset, List[str]]):
            status_green (Union[Unset, int]):
            status_yellow (Union[Unset, int]):
            thesaurus_langs (Union[Unset, List[str]]):
            node_list (Union[Unset, List['ESNodeObj']]):
            installed_plugins (Union[Unset, List[str]]):
            arhive_status (Union[Unset, int]):
            thesaurus_status (Union[Unset, int]):
            last_update (Union[Unset, str]):
            installed_version (Union[Unset, str]):
    """

    status_red: Union[Unset, int] = UNSET
    document_count: Union[Unset, int] = UNSET
    connection_count: Union[Unset, int] = UNSET
    langs_with_doc_count: Union[Unset, List[str]] = UNSET
    status_green: Union[Unset, int] = UNSET
    status_yellow: Union[Unset, int] = UNSET
    thesaurus_langs: Union[Unset, List[str]] = UNSET
    node_list: Union[Unset, List["ESNodeObj"]] = UNSET
    installed_plugins: Union[Unset, List[str]] = UNSET
    arhive_status: Union[Unset, int] = UNSET
    thesaurus_status: Union[Unset, int] = UNSET
    last_update: Union[Unset, str] = UNSET
    installed_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_red = self.status_red

        document_count = self.document_count

        connection_count = self.connection_count

        langs_with_doc_count: Union[Unset, List[str]] = UNSET
        if not isinstance(self.langs_with_doc_count, Unset):
            langs_with_doc_count = self.langs_with_doc_count

        status_green = self.status_green

        status_yellow = self.status_yellow

        thesaurus_langs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.thesaurus_langs, Unset):
            thesaurus_langs = self.thesaurus_langs

        node_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.node_list, Unset):
            node_list = []
            for componentsschemas_list_of_es_node_obj_item_data in self.node_list:
                componentsschemas_list_of_es_node_obj_item = componentsschemas_list_of_es_node_obj_item_data.to_dict()
                node_list.append(componentsschemas_list_of_es_node_obj_item)

        installed_plugins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.installed_plugins, Unset):
            installed_plugins = self.installed_plugins

        arhive_status = self.arhive_status

        thesaurus_status = self.thesaurus_status

        last_update = self.last_update

        installed_version = self.installed_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_red is not UNSET:
            field_dict["STATUS_RED"] = status_red
        if document_count is not UNSET:
            field_dict["documentCount"] = document_count
        if connection_count is not UNSET:
            field_dict["connectionCount"] = connection_count
        if langs_with_doc_count is not UNSET:
            field_dict["langsWithDocCount"] = langs_with_doc_count
        if status_green is not UNSET:
            field_dict["STATUS_GREEN"] = status_green
        if status_yellow is not UNSET:
            field_dict["STATUS_YELLOW"] = status_yellow
        if thesaurus_langs is not UNSET:
            field_dict["thesaurusLangs"] = thesaurus_langs
        if node_list is not UNSET:
            field_dict["nodeList"] = node_list
        if installed_plugins is not UNSET:
            field_dict["installedPlugins"] = installed_plugins
        if arhive_status is not UNSET:
            field_dict["arhiveStatus"] = arhive_status
        if thesaurus_status is not UNSET:
            field_dict["thesaurusStatus"] = thesaurus_status
        if last_update is not UNSET:
            field_dict["lastUpdate"] = last_update
        if installed_version is not UNSET:
            field_dict["installedVersion"] = installed_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.es_node_obj import ESNodeObj

        d = src_dict.copy()
        status_red = d.pop("STATUS_RED", UNSET)

        document_count = d.pop("documentCount", UNSET)

        connection_count = d.pop("connectionCount", UNSET)

        langs_with_doc_count = cast(List[str], d.pop("langsWithDocCount", UNSET))

        status_green = d.pop("STATUS_GREEN", UNSET)

        status_yellow = d.pop("STATUS_YELLOW", UNSET)

        thesaurus_langs = cast(List[str], d.pop("thesaurusLangs", UNSET))

        node_list = []
        _node_list = d.pop("nodeList", UNSET)
        for componentsschemas_list_of_es_node_obj_item_data in _node_list or []:
            componentsschemas_list_of_es_node_obj_item = ESNodeObj.from_dict(
                componentsschemas_list_of_es_node_obj_item_data
            )

            node_list.append(componentsschemas_list_of_es_node_obj_item)

        installed_plugins = cast(List[str], d.pop("installedPlugins", UNSET))

        arhive_status = d.pop("arhiveStatus", UNSET)

        thesaurus_status = d.pop("thesaurusStatus", UNSET)

        last_update = d.pop("lastUpdate", UNSET)

        installed_version = d.pop("installedVersion", UNSET)

        es_info_obj = cls(
            status_red=status_red,
            document_count=document_count,
            connection_count=connection_count,
            langs_with_doc_count=langs_with_doc_count,
            status_green=status_green,
            status_yellow=status_yellow,
            thesaurus_langs=thesaurus_langs,
            node_list=node_list,
            installed_plugins=installed_plugins,
            arhive_status=arhive_status,
            thesaurus_status=thesaurus_status,
            last_update=last_update,
            installed_version=installed_version,
        )

        es_info_obj.additional_properties = d
        return es_info_obj

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
