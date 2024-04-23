from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_filing_options import AutoFilingOptions
    from ..models.client_info import ClientInfo
    from ..models.sord import Sord


T = TypeVar("T", bound="BRequestIXServicePortIFEvalAutoFiling")


@_attrs_define
class BRequestIXServicePortIFEvalAutoFiling:
    """
    Attributes:
        opts (Union[Unset, AutoFilingOptions]): Options for function
            {@link IXServicePortIF#evalAutoFiling(ClientInfo, String, Sord, AutoFilingOptions)}
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
        mask_id (Union[Unset, str]):
        sord (Union[Unset, Sord]): <p>
            Indexing information of an archive entry.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    opts: Union[Unset, "AutoFilingOptions"] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    mask_id: Union[Unset, str] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        opts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.opts, Unset):
            opts = self.opts.to_dict()

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        mask_id = self.mask_id

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if opts is not UNSET:
            field_dict["opts"] = opts
        if ci is not UNSET:
            field_dict["ci"] = ci
        if mask_id is not UNSET:
            field_dict["maskId"] = mask_id
        if sord is not UNSET:
            field_dict["sord"] = sord

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.auto_filing_options import AutoFilingOptions
        from ..models.client_info import ClientInfo
        from ..models.sord import Sord

        d = src_dict.copy()
        _opts = d.pop("opts", UNSET)
        opts: Union[Unset, AutoFilingOptions]
        if isinstance(_opts, Unset):
            opts = UNSET
        else:
            opts = AutoFilingOptions.from_dict(_opts)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        mask_id = d.pop("maskId", UNSET)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        b_request_ix_service_port_if_eval_auto_filing = cls(
            opts=opts,
            ci=ci,
            mask_id=mask_id,
            sord=sord,
        )

        b_request_ix_service_port_if_eval_auto_filing.additional_properties = d
        return b_request_ix_service_port_if_eval_auto_filing

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
