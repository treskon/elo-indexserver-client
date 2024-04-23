from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.keywords_dynamic_info import KeywordsDynamicInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCheckoutKeywordsDynamic")


@_attrs_define
class BRequestIXServicePortIFCheckoutKeywordsDynamic:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        keywords_dynamic_info (Union[Unset, KeywordsDynamicInfo]): This Class contains parameters for the IX call
            {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)} .
             <p>
             There are two ways to execute the script for dynamic keyword lists. According to the parameter in
             this class, the one way or the other is chosen. The first way is to specify
             {@link KeywordsDynamicInfo#sord} and {@link KeywordsDynamicInfo#maskLineFocus}. Then, the IX
             passes these parameters to the script via the script-function open(ec, sord, fieldName). The
             other parameters will be overwritten by <code>null</code> and completely ignored. The other way
             is to set the fields {@link KeywordsDynamicInfo#mapData},
             {@link KeywordsDynamicInfo#mapLineFocus} and {@link KeywordsDynamicInfo#mapScriptName}. In this
             case, the IX passes these parameters to the scripting function openMap(ec, data, fieldName). To
             achieve this, <code>sord</code> as well as <code>maskLineFocus</code> must be <code>null</code>.
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    keywords_dynamic_info: Union[Unset, "KeywordsDynamicInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        keywords_dynamic_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.keywords_dynamic_info, Unset):
            keywords_dynamic_info = self.keywords_dynamic_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if keywords_dynamic_info is not UNSET:
            field_dict["keywordsDynamicInfo"] = keywords_dynamic_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.keywords_dynamic_info import KeywordsDynamicInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _keywords_dynamic_info = d.pop("keywordsDynamicInfo", UNSET)
        keywords_dynamic_info: Union[Unset, KeywordsDynamicInfo]
        if isinstance(_keywords_dynamic_info, Unset):
            keywords_dynamic_info = UNSET
        else:
            keywords_dynamic_info = KeywordsDynamicInfo.from_dict(_keywords_dynamic_info)

        b_request_ix_service_port_if_checkout_keywords_dynamic = cls(
            ci=ci,
            keywords_dynamic_info=keywords_dynamic_info,
        )

        b_request_ix_service_port_if_checkout_keywords_dynamic.additional_properties = d
        return b_request_ix_service_port_if_checkout_keywords_dynamic

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
