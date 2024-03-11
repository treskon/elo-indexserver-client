from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServerEventsOnInheritKeywording")


@_attrs_define
class BRequestIXServerEventsOnInheritKeywording:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        parent_sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        okey_names (Union[Unset, List[str]]):
        reserved (Union[Unset, str]):
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    parent_sord: Union[Unset, "Sord"] = UNSET
    okey_names: Union[Unset, List[str]] = UNSET
    reserved: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        parent_sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_sord, Unset):
            parent_sord = self.parent_sord.to_dict()

        okey_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.okey_names, Unset):
            okey_names = self.okey_names

        reserved = self.reserved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if sord is not UNSET:
            field_dict["sord"] = sord
        if parent_sord is not UNSET:
            field_dict["parentSord"] = parent_sord
        if okey_names is not UNSET:
            field_dict["okeyNames"] = okey_names
        if reserved is not UNSET:
            field_dict["reserved"] = reserved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.sord import Sord

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        _parent_sord = d.pop("parentSord", UNSET)
        parent_sord: Union[Unset, Sord]
        if isinstance(_parent_sord, Unset):
            parent_sord = UNSET
        else:
            parent_sord = Sord.from_dict(_parent_sord)

        okey_names = cast(List[str], d.pop("okeyNames", UNSET))

        reserved = d.pop("reserved", UNSET)

        b_request_ix_server_events_on_inherit_keywording = cls(
            ec=ec,
            sord=sord,
            parent_sord=parent_sord,
            okey_names=okey_names,
            reserved=reserved,
        )

        b_request_ix_server_events_on_inherit_keywording.additional_properties = d
        return b_request_ix_server_events_on_inherit_keywording

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
