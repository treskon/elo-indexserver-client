from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.values_of_obj_key_options import ValuesOfObjKeyOptions


T = TypeVar("T", bound="BRequestIXServicePortIFGetDistinctValuesOfObjKey")


@_attrs_define
class BRequestIXServicePortIFGetDistinctValuesOfObjKey:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface function, except the
             login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        okey_name (Union[Unset, str]):
        opts (Union[Unset, ValuesOfObjKeyOptions]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    okey_name: Union[Unset, str] = UNSET
    opts: Union[Unset, "ValuesOfObjKeyOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        okey_name = self.okey_name
        opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opts, Unset):
            opts = self.opts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if okey_name is not UNSET:
            field_dict["okeyName"] = okey_name
        if opts is not UNSET:
            field_dict["opts"] = opts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.values_of_obj_key_options import ValuesOfObjKeyOptions

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        okey_name = d.pop("okeyName", UNSET)

        _opts = d.pop("opts", UNSET)
        opts: Union[Unset, ValuesOfObjKeyOptions]
        if isinstance(_opts, Unset):
            opts = UNSET
        else:
            opts = ValuesOfObjKeyOptions.from_dict(_opts)

        b_request_ix_service_port_if_get_distinct_values_of_obj_key = cls(
            ci=ci,
            okey_name=okey_name,
            opts=opts,
        )

        b_request_ix_service_port_if_get_distinct_values_of_obj_key.additional_properties = d
        return b_request_ix_service_port_if_get_distinct_values_of_obj_key

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
