from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SordLink")


@_attrs_define
class SordLink:
    """This class represents a link to an archive entry.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            id (Union[Unset, str]): Numerical ID or GUID of referenced Sord.
            link_id (Union[Unset, str]): Link ID.
            permanent (Union[Unset, bool]): True, if this SordLink is permanent. Permanent links between Sords cannot be
                deleted.
    """

    id: Union[Unset, str] = UNSET
    link_id: Union[Unset, str] = UNSET
    permanent: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        link_id = self.link_id
        permanent = self.permanent

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if link_id is not UNSET:
            field_dict["linkId"] = link_id
        if permanent is not UNSET:
            field_dict["permanent"] = permanent

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        link_id = d.pop("linkId", UNSET)

        permanent = d.pop("permanent", UNSET)

        sord_link = cls(
            id=id,
            link_id=link_id,
            permanent=permanent,
        )

        sord_link.additional_properties = d
        return sord_link

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
