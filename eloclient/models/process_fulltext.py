from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessFulltext")


@_attrs_define
class ProcessFulltext:
    """Fulltext-Property to be added to/removed from an object.
    <p>
     Copyright: Copyright (c) 2008
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            add_to_fulltext (Union[Unset, bool]): Add to the fulltext-service
    """

    add_to_fulltext: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_to_fulltext = self.add_to_fulltext

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_to_fulltext is not UNSET:
            field_dict["addToFulltext"] = add_to_fulltext

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        add_to_fulltext = d.pop("addToFulltext", UNSET)

        process_fulltext = cls(
            add_to_fulltext=add_to_fulltext,
        )

        process_fulltext.additional_properties = d
        return process_fulltext

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
