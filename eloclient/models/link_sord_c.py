from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_sord_z import LinkSordZ


T = TypeVar("T", bound="LinkSordC")


@_attrs_define
class LinkSordC:
    """Constants for linkSord(...).
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            nothing (Union[Unset, LinkSordZ]): This class encapsulates the constants of LinkSordC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            pair (Union[Unset, LinkSordZ]): This class encapsulates the constants of LinkSordC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            cross_link (Union[Unset, LinkSordZ]): This class encapsulates the constants of LinkSordC.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    nothing: Union[Unset, "LinkSordZ"] = UNSET
    pair: Union[Unset, "LinkSordZ"] = UNSET
    cross_link: Union[Unset, "LinkSordZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nothing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nothing, Unset):
            nothing = self.nothing.to_dict()

        pair: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pair, Unset):
            pair = self.pair.to_dict()

        cross_link: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cross_link, Unset):
            cross_link = self.cross_link.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nothing is not UNSET:
            field_dict["NOTHING"] = nothing
        if pair is not UNSET:
            field_dict["PAIR"] = pair
        if cross_link is not UNSET:
            field_dict["CROSS_LINK"] = cross_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_sord_z import LinkSordZ

        d = src_dict.copy()
        _nothing = d.pop("NOTHING", UNSET)
        nothing: Union[Unset, LinkSordZ]
        if isinstance(_nothing, Unset):
            nothing = UNSET
        else:
            nothing = LinkSordZ.from_dict(_nothing)

        _pair = d.pop("PAIR", UNSET)
        pair: Union[Unset, LinkSordZ]
        if isinstance(_pair, Unset):
            pair = UNSET
        else:
            pair = LinkSordZ.from_dict(_pair)

        _cross_link = d.pop("CROSS_LINK", UNSET)
        cross_link: Union[Unset, LinkSordZ]
        if isinstance(_cross_link, Unset):
            cross_link = UNSET
        else:
            cross_link = LinkSordZ.from_dict(_cross_link)

        link_sord_c = cls(
            nothing=nothing,
            pair=pair,
            cross_link=cross_link,
        )

        link_sord_c.additional_properties = d
        return link_sord_c

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
