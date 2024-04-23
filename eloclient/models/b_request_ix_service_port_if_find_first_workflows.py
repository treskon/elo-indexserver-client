from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.find_workflow_info import FindWorkflowInfo
    from ..models.wf_diagram_z import WFDiagramZ


T = TypeVar("T", bound="BRequestIXServicePortIFFindFirstWorkflows")


@_attrs_define
class BRequestIXServicePortIFFindFirstWorkflows:
    """
    Attributes:
        max_ (Union[Unset, int]):
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
        find_info (Union[Unset, FindWorkflowInfo]): This class contains the search criteria for selecting workflows.
            <p>
             Copyright: Copyright (c) 2008, 2010
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        wf_diagram_z (Union[Unset, WFDiagramZ]): This class encapsulates the constants of the WFDiagramC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
    """

    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    find_info: Union[Unset, "FindWorkflowInfo"] = UNSET
    wf_diagram_z: Union[Unset, "WFDiagramZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        wf_diagram_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wf_diagram_z, Unset):
            wf_diagram_z = self.wf_diagram_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info
        if wf_diagram_z is not UNSET:
            field_dict["wfDiagramZ"] = wf_diagram_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.find_workflow_info import FindWorkflowInfo
        from ..models.wf_diagram_z import WFDiagramZ

        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindWorkflowInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindWorkflowInfo.from_dict(_find_info)

        _wf_diagram_z = d.pop("wfDiagramZ", UNSET)
        wf_diagram_z: Union[Unset, WFDiagramZ]
        if isinstance(_wf_diagram_z, Unset):
            wf_diagram_z = UNSET
        else:
            wf_diagram_z = WFDiagramZ.from_dict(_wf_diagram_z)

        b_request_ix_service_port_if_find_first_workflows = cls(
            max_=max_,
            ci=ci,
            find_info=find_info,
            wf_diagram_z=wf_diagram_z,
        )

        b_request_ix_service_port_if_find_first_workflows.additional_properties = d
        return b_request_ix_service_port_if_find_first_workflows

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
