from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_options import DeleteOptions
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.lock_z import LockZ
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServerEventsOnAfterDeleteSord")


@_attrs_define
class BRequestIXServerEventsOnAfterDeleteSord:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        parent_sord (Union[Unset, Sord]): <p>
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
        unlock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        del_opts (Union[Unset, DeleteOptions]): This class contains options for deleting archive SORDs using the
            deleteSord function.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        ret (Union[Unset, bool]):
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    parent_sord: Union[Unset, "Sord"] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    unlock_z: Union[Unset, "LockZ"] = UNSET
    del_opts: Union[Unset, "DeleteOptions"] = UNSET
    ret: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        parent_sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parent_sord, Unset):
            parent_sord = self.parent_sord.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        unlock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unlock_z, Unset):
            unlock_z = self.unlock_z.to_dict()

        del_opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.del_opts, Unset):
            del_opts = self.del_opts.to_dict()

        ret = self.ret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if parent_sord is not UNSET:
            field_dict["parentSord"] = parent_sord
        if sord is not UNSET:
            field_dict["sord"] = sord
        if unlock_z is not UNSET:
            field_dict["unlockZ"] = unlock_z
        if del_opts is not UNSET:
            field_dict["delOpts"] = del_opts
        if ret is not UNSET:
            field_dict["ret"] = ret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.delete_options import DeleteOptions
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.lock_z import LockZ
        from ..models.sord import Sord

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _parent_sord = d.pop("parentSord", UNSET)
        parent_sord: Union[Unset, Sord]
        if isinstance(_parent_sord, Unset):
            parent_sord = UNSET
        else:
            parent_sord = Sord.from_dict(_parent_sord)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        _unlock_z = d.pop("unlockZ", UNSET)
        unlock_z: Union[Unset, LockZ]
        if isinstance(_unlock_z, Unset):
            unlock_z = UNSET
        else:
            unlock_z = LockZ.from_dict(_unlock_z)

        _del_opts = d.pop("delOpts", UNSET)
        del_opts: Union[Unset, DeleteOptions]
        if isinstance(_del_opts, Unset):
            del_opts = UNSET
        else:
            del_opts = DeleteOptions.from_dict(_del_opts)

        ret = d.pop("ret", UNSET)

        b_request_ix_server_events_on_after_delete_sord = cls(
            ec=ec,
            parent_sord=parent_sord,
            sord=sord,
            unlock_z=unlock_z,
            del_opts=del_opts,
            ret=ret,
        )

        b_request_ix_server_events_on_after_delete_sord.additional_properties = d
        return b_request_ix_server_events_on_after_delete_sord

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
