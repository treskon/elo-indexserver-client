from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_info import FindInfo
    from ..models.find_result import FindResult
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.sord_z import SordZ


T = TypeVar("T", bound="BRequestIXServerEventsOnFindSordsResult")


@_attrs_define
class BRequestIXServerEventsOnFindSordsResult:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        find_info (Union[Unset, FindInfo]): This class controls the search function findFirstSords.
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
        find_result (Union[Unset, FindResult]): <p>
            This class contains the search results of a call to <code>IXServicePortIF.findFirstSords</code>
             </p>
             or <code>IXServicePortIF.findNextSords</code>.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    find_info: Union[Unset, "FindInfo"] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    find_result: Union[Unset, "FindResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        find_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_result, Unset):
            find_result = self.find_result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z
        if find_result is not UNSET:
            field_dict["findResult"] = find_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_info import FindInfo
        from ..models.find_result import FindResult
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.sord_z import SordZ

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindInfo.from_dict(_find_info)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        _find_result = d.pop("findResult", UNSET)
        find_result: Union[Unset, FindResult]
        if isinstance(_find_result, Unset):
            find_result = UNSET
        else:
            find_result = FindResult.from_dict(_find_result)

        b_request_ix_server_events_on_find_sords_result = cls(
            ec=ec,
            find_info=find_info,
            sord_z=sord_z,
            find_result=find_result,
        )

        b_request_ix_server_events_on_find_sords_result.additional_properties = d
        return b_request_ix_server_events_on_find_sords_result

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
