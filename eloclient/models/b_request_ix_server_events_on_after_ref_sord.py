from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServerEventsOnAfterRefSord")


@_attrs_define
class BRequestIXServerEventsOnAfterRefSord:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        parent_sord_old (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        parent_sord_new (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        man_sort_index (Union[Unset, int]):
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    parent_sord_old: Union[Unset, "Sord"] = UNSET
    parent_sord_new: Union[Unset, "Sord"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    man_sort_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        parent_sord_old: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_sord_old, Unset):
            parent_sord_old = self.parent_sord_old.to_dict()

        parent_sord_new: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_sord_new, Unset):
            parent_sord_new = self.parent_sord_new.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        man_sort_index = self.man_sort_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if parent_sord_old is not UNSET:
            field_dict["parentSordOld"] = parent_sord_old
        if parent_sord_new is not UNSET:
            field_dict["parentSordNew"] = parent_sord_new
        if sord is not UNSET:
            field_dict["sord"] = sord
        if man_sort_index is not UNSET:
            field_dict["manSortIndex"] = man_sort_index

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

        _parent_sord_old = d.pop("parentSordOld", UNSET)
        parent_sord_old: Union[Unset, Sord]
        if isinstance(_parent_sord_old, Unset):
            parent_sord_old = UNSET
        else:
            parent_sord_old = Sord.from_dict(_parent_sord_old)

        _parent_sord_new = d.pop("parentSordNew", UNSET)
        parent_sord_new: Union[Unset, Sord]
        if isinstance(_parent_sord_new, Unset):
            parent_sord_new = UNSET
        else:
            parent_sord_new = Sord.from_dict(_parent_sord_new)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        man_sort_index = d.pop("manSortIndex", UNSET)

        b_request_ix_server_events_on_after_ref_sord = cls(
            ec=ec,
            parent_sord_old=parent_sord_old,
            parent_sord_new=parent_sord_new,
            sord=sord,
            man_sort_index=man_sort_index,
        )

        b_request_ix_server_events_on_after_ref_sord.additional_properties = d
        return b_request_ix_server_events_on_after_ref_sord

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
