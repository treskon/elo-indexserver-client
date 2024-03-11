from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityOption")


@_attrs_define
class ActivityOption:
    """This class represents an option for an activity project.

    Attributes:
        id (Union[Unset, int]): Option ID. This value can be one of the predefined option IDs in ActivityOptionC.
            Or you can use an application
             defined value greater or equal to ActivityOptionC.ID_VALUE.
        name (Union[Unset, str]): Activity option name.
            The name must not contain one of this characters: ! $ - + *
        only_keyword (Union[Unset, bool]): The value can only be selected from the associated keyword list.
            This option has to be checked by the client
             application. It is not checked by Indexserver.
        read_only (Union[Unset, bool]): The value can not be edited in the user interface. This option has to be checked
            by the client application.
            It is
             not checked by Indexserver.
        sorted_ (Union[Unset, bool]): The value has to be displayed in an appropriate order. This option has to be
            checked by the client application.
            It
             is not checked by Indexserver.
        stamp (Union[Unset, bool]): This option is a stamp field. This option has to be checked by the client
            application.
            It is not checked by
             Indexserver.
        mandatory (Union[Unset, bool]): A value must be defined for this option. This option has to be checked by the
            client application.
            It is not checked
             by Indexserver.
        keywords (Union[Unset, List[str]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    only_keyword: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    sorted_: Union[Unset, bool] = UNSET
    stamp: Union[Unset, bool] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        only_keyword = self.only_keyword
        read_only = self.read_only
        sorted_ = self.sorted_
        stamp = self.stamp
        mandatory = self.mandatory
        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if only_keyword is not UNSET:
            field_dict["onlyKeyword"] = only_keyword
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if sorted_ is not UNSET:
            field_dict["sorted"] = sorted_
        if stamp is not UNSET:
            field_dict["stamp"] = stamp
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        only_keyword = d.pop("onlyKeyword", UNSET)

        read_only = d.pop("readOnly", UNSET)

        sorted_ = d.pop("sorted", UNSET)

        stamp = d.pop("stamp", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        keywords = cast(List[str], d.pop("keywords", UNSET))

        activity_option = cls(
            id=id,
            name=name,
            only_keyword=only_keyword,
            read_only=read_only,
            sorted_=sorted_,
            stamp=stamp,
            mandatory=mandatory,
            keywords=keywords,
        )

        activity_option.additional_properties = d
        return activity_option

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
