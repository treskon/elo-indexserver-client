from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityOption")


@_attrs_define
class ActivityOption:
    """This class represents an option for an activity project.

    Attributes:
        sorted_ (Union[Unset, bool]): The value has to be displayed in an appropriate order.
            This option has to be checked by the
             client application. It is not checked by Indexserver.
        keywords (Union[Unset, List[str]]):
        name (Union[Unset, str]): Activity option name.
            The name must not contain one of this characters: ! $ - + *
        stamp (Union[Unset, bool]): This option is a stamp field. This option has to be checked by the client
            application.
            It is
             not checked by Indexserver.
        read_only (Union[Unset, bool]): The value can not be edited in the user interface.
            This option has to be checked by the client
             application. It is not checked by Indexserver.
        id (Union[Unset, int]): Option ID. This value can be one of the predefined option IDs in ActivityOptionC.
            Or you can
             use an application defined value greater or equal to ActivityOptionC.ID_VALUE.
        mandatory (Union[Unset, bool]): A value must be defined for this option.
            This option has to be checked by the client
             application. It is not checked by Indexserver.
        only_keyword (Union[Unset, bool]): The value can only be selected from the associated keyword list.
            This option has to be checked
             by the client application. It is not checked by Indexserver.
    """

    sorted_: Union[Unset, bool] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    name: Union[Unset, str] = UNSET
    stamp: Union[Unset, bool] = UNSET
    read_only: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    only_keyword: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sorted_ = self.sorted_

        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        name = self.name

        stamp = self.stamp

        read_only = self.read_only

        id = self.id

        mandatory = self.mandatory

        only_keyword = self.only_keyword

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sorted_ is not UNSET:
            field_dict["sorted"] = sorted_
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if name is not UNSET:
            field_dict["name"] = name
        if stamp is not UNSET:
            field_dict["stamp"] = stamp
        if read_only is not UNSET:
            field_dict["readOnly"] = read_only
        if id is not UNSET:
            field_dict["id"] = id
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if only_keyword is not UNSET:
            field_dict["onlyKeyword"] = only_keyword

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sorted_ = d.pop("sorted", UNSET)

        keywords = cast(List[str], d.pop("keywords", UNSET))

        name = d.pop("name", UNSET)

        stamp = d.pop("stamp", UNSET)

        read_only = d.pop("readOnly", UNSET)

        id = d.pop("id", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        only_keyword = d.pop("onlyKeyword", UNSET)

        activity_option = cls(
            sorted_=sorted_,
            keywords=keywords,
            name=name,
            stamp=stamp,
            read_only=read_only,
            id=id,
            mandatory=mandatory,
            only_keyword=only_keyword,
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
