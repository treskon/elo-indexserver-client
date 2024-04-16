from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.archiv_value import ArchivValue


T = TypeVar("T", bound="ArchivReport")


@_attrs_define
class ArchivReport:
    """
    Attributes:
        objecte (Union[Unset, List['ArchivValue']]):
        archiv_guid (Union[Unset, str]):
        elodmdocs (Union[Unset, List['ArchivValue']]):
    """

    objecte: Union[Unset, List["ArchivValue"]] = UNSET
    archiv_guid: Union[Unset, str] = UNSET
    elodmdocs: Union[Unset, List["ArchivValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        objecte: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.objecte, Unset):
            objecte = []
            for componentsschemas_list_of_archiv_value_item_data in self.objecte:
                componentsschemas_list_of_archiv_value_item = componentsschemas_list_of_archiv_value_item_data.to_dict()
                objecte.append(componentsschemas_list_of_archiv_value_item)

        archiv_guid = self.archiv_guid

        elodmdocs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elodmdocs, Unset):
            elodmdocs = []
            for componentsschemas_list_of_archiv_value_item_data in self.elodmdocs:
                componentsschemas_list_of_archiv_value_item = componentsschemas_list_of_archiv_value_item_data.to_dict()
                elodmdocs.append(componentsschemas_list_of_archiv_value_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if objecte is not UNSET:
            field_dict["objecte"] = objecte
        if archiv_guid is not UNSET:
            field_dict["archivGUID"] = archiv_guid
        if elodmdocs is not UNSET:
            field_dict["elodmdocs"] = elodmdocs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.archiv_value import ArchivValue

        d = src_dict.copy()
        objecte = []
        _objecte = d.pop("objecte", UNSET)
        for componentsschemas_list_of_archiv_value_item_data in _objecte or []:
            componentsschemas_list_of_archiv_value_item = ArchivValue.from_dict(
                componentsschemas_list_of_archiv_value_item_data
            )

            objecte.append(componentsschemas_list_of_archiv_value_item)

        archiv_guid = d.pop("archivGUID", UNSET)

        elodmdocs = []
        _elodmdocs = d.pop("elodmdocs", UNSET)
        for componentsschemas_list_of_archiv_value_item_data in _elodmdocs or []:
            componentsschemas_list_of_archiv_value_item = ArchivValue.from_dict(
                componentsschemas_list_of_archiv_value_item_data
            )

            elodmdocs.append(componentsschemas_list_of_archiv_value_item)

        archiv_report = cls(
            objecte=objecte,
            archiv_guid=archiv_guid,
            elodmdocs=elodmdocs,
        )

        archiv_report.additional_properties = d
        return archiv_report

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
