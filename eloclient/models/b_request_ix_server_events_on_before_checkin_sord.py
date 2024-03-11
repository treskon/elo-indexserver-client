from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.lock_z import LockZ
    from ..models.sord import Sord
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="BRequestIXServerEventsOnBeforeCheckinSord")


@_attrs_define
class BRequestIXServerEventsOnBeforeCheckinSord:
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
        sord_db (Union[Unset, Sord]): <p>
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
        sord_z (Union[Unset, SordZ]): <p>
            This class encapsulates the constants of <code>SordC</code>
             </p>

             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    sord_db: Union[Unset, "Sord"] = UNSET
    parent_sord: Union[Unset, "Sord"] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        sord_db: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_db, Unset):
            sord_db = self.sord_db.to_dict()

        parent_sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_sord, Unset):
            parent_sord = self.parent_sord.to_dict()

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if sord is not UNSET:
            field_dict["sord"] = sord
        if sord_db is not UNSET:
            field_dict["sordDB"] = sord_db
        if parent_sord is not UNSET:
            field_dict["parentSord"] = parent_sord
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.lock_z import LockZ
        from ..models.sord import Sord
        from ..models.sord_z import SordZ

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

        _sord_db = d.pop("sordDB", UNSET)
        sord_db: Union[Unset, Sord]
        if isinstance(_sord_db, Unset):
            sord_db = UNSET
        else:
            sord_db = Sord.from_dict(_sord_db)

        _parent_sord = d.pop("parentSord", UNSET)
        parent_sord: Union[Unset, Sord]
        if isinstance(_parent_sord, Unset):
            parent_sord = UNSET
        else:
            parent_sord = Sord.from_dict(_parent_sord)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        b_request_ix_server_events_on_before_checkin_sord = cls(
            ec=ec,
            sord=sord,
            sord_db=sord_db,
            parent_sord=parent_sord,
            sord_z=sord_z,
            unlock_z=unlock_z,
        )

        b_request_ix_server_events_on_before_checkin_sord.additional_properties = d
        return b_request_ix_server_events_on_before_checkin_sord

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
