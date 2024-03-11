from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ix_server_events_context import IXServerEventsContext
    from ..models.sord import Sord
    from ..models.sord_z import SordZ
    from ..models.wf_diagram import WFDiagram


T = TypeVar("T", bound="BRequestIXServerEventsOnAfterEndEditWorkFlowNode")


@_attrs_define
class BRequestIXServerEventsOnAfterEndEditWorkFlowNode:
    """
    Attributes:
        ec (Union[Unset, IXServerEventsContext]): Execution context of server events. An object of this class is passed
            to every server event and registered function.
            On the server side, it can be casted to IObjectFactory to retrieve helper objects for access checking,
            conversion of
             date values and numeric values, etc.
        workflow (Union[Unset, WFDiagram]): This class represents an active or finished workflow or a workflow template
        node_id (Union[Unset, int]):
        sord (Union[Unset, Sord]): <p>
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
    """

    ec: Union[Unset, "IXServerEventsContext"] = UNSET
    workflow: Union[Unset, "WFDiagram"] = UNSET
    node_id: Union[Unset, int] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    sord_z: Union[Unset, "SordZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ec, Unset):
            ec = self.ec.to_dict()

        workflow: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.workflow, Unset):
            workflow = self.workflow.to_dict()

        node_id = self.node_id
        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        sord_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_z, Unset):
            sord_z = self.sord_z.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ec is not UNSET:
            field_dict["ec"] = ec
        if workflow is not UNSET:
            field_dict["workflow"] = workflow
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if sord is not UNSET:
            field_dict["sord"] = sord
        if sord_z is not UNSET:
            field_dict["sordZ"] = sord_z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ix_server_events_context import IXServerEventsContext
        from ..models.sord import Sord
        from ..models.sord_z import SordZ
        from ..models.wf_diagram import WFDiagram

        d = src_dict.copy()
        _ec = d.pop("ec", UNSET)
        ec: Union[Unset, IXServerEventsContext]
        if isinstance(_ec, Unset):
            ec = UNSET
        else:
            ec = IXServerEventsContext.from_dict(_ec)

        _workflow = d.pop("workflow", UNSET)
        workflow: Union[Unset, WFDiagram]
        if isinstance(_workflow, Unset):
            workflow = UNSET
        else:
            workflow = WFDiagram.from_dict(_workflow)

        node_id = d.pop("nodeId", UNSET)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        _sord_z = d.pop("sordZ", UNSET)
        sord_z: Union[Unset, SordZ]
        if isinstance(_sord_z, Unset):
            sord_z = UNSET
        else:
            sord_z = SordZ.from_dict(_sord_z)

        b_request_ix_server_events_on_after_end_edit_work_flow_node = cls(
            ec=ec,
            workflow=workflow,
            node_id=node_id,
            sord=sord,
            sord_z=sord_z,
        )

        b_request_ix_server_events_on_after_end_edit_work_flow_node.additional_properties = d
        return b_request_ix_server_events_on_after_end_edit_work_flow_node

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
