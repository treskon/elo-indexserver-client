from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFNodeHistory")


@_attrs_define
class WFNodeHistory:
    """Version history for a workflow node. A version history is created while leaving a workflow node.
    <p>
     Copyright: Copyright (c) 2015
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            succ_11 (Union[Unset, int]): DB column: wf_succ_11
            succ_10 (Union[Unset, int]): DB column: wf_succ_10
            succ_13 (Union[Unset, int]): DB column: wf_succ_13
            succ_12 (Union[Unset, int]): DB column: wf_succ_12
            enter_date_iso (Union[Unset, str]): The node was activated on this date. This member is valid for all node
                types.
            succ_9 (Union[Unset, int]): DB column: wf_succ_9
            hist_guid (Union[Unset, str]): GUID of the WorkflowHist object.
                DB column: wfhistguid
            succ_5 (Union[Unset, int]): DB column: wf_succ_5
            succ_6 (Union[Unset, int]): DB column: wf_succ_6
            flow_guid (Union[Unset, str]): GUID of the workflow.
                DB column: wfguid
            succ_7 (Union[Unset, int]): DB column: wf_succ_7
            succ_8 (Union[Unset, int]): DB column: wf_succ_8
            succ_1 (Union[Unset, int]): DB column: wf_succ_1
            succ_2 (Union[Unset, int]): DB column: wf_succ_2
            succ_3 (Union[Unset, int]): DB column: wf_succ_3
            succ_4 (Union[Unset, int]): DB column: wf_succ_4
            user_name (Union[Unset, str]): Name of user who has to process the node. Might be a group name too.
                Only valid for person
                 nodes. DB column: wf_username
            user_id (Union[Unset, int]): ID of user who has to process the node. Might be a group ID too. Only valid for
                person nodes.
                DB column: wf_userid
            succ_0 (Union[Unset, int]): Successor node(s) succ_0 ...
                Succ 19 DB column: wf_succ_0
            succ_19 (Union[Unset, int]): DB column: wf_succ_19
            succ_18 (Union[Unset, int]): DB column: wf_succ_18
            succ_15 (Union[Unset, int]): DB column: wf_succ_15
            succ_14 (Union[Unset, int]): DB column: wf_succ_14
            succ_17 (Union[Unset, int]): DB column: wf_succ_17
            succ_16 (Union[Unset, int]): DB column: wf_succ_16
            exit_date_iso (Union[Unset, str]): The node was exited/completed on this date. This member is valid for all node
                types.
            node_id (Union[Unset, int]): Node ID.
                DB column: wf_nodeid
    """

    succ_11: Union[Unset, int] = UNSET
    succ_10: Union[Unset, int] = UNSET
    succ_13: Union[Unset, int] = UNSET
    succ_12: Union[Unset, int] = UNSET
    enter_date_iso: Union[Unset, str] = UNSET
    succ_9: Union[Unset, int] = UNSET
    hist_guid: Union[Unset, str] = UNSET
    succ_5: Union[Unset, int] = UNSET
    succ_6: Union[Unset, int] = UNSET
    flow_guid: Union[Unset, str] = UNSET
    succ_7: Union[Unset, int] = UNSET
    succ_8: Union[Unset, int] = UNSET
    succ_1: Union[Unset, int] = UNSET
    succ_2: Union[Unset, int] = UNSET
    succ_3: Union[Unset, int] = UNSET
    succ_4: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    succ_0: Union[Unset, int] = UNSET
    succ_19: Union[Unset, int] = UNSET
    succ_18: Union[Unset, int] = UNSET
    succ_15: Union[Unset, int] = UNSET
    succ_14: Union[Unset, int] = UNSET
    succ_17: Union[Unset, int] = UNSET
    succ_16: Union[Unset, int] = UNSET
    exit_date_iso: Union[Unset, str] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        succ_11 = self.succ_11

        succ_10 = self.succ_10

        succ_13 = self.succ_13

        succ_12 = self.succ_12

        enter_date_iso = self.enter_date_iso

        succ_9 = self.succ_9

        hist_guid = self.hist_guid

        succ_5 = self.succ_5

        succ_6 = self.succ_6

        flow_guid = self.flow_guid

        succ_7 = self.succ_7

        succ_8 = self.succ_8

        succ_1 = self.succ_1

        succ_2 = self.succ_2

        succ_3 = self.succ_3

        succ_4 = self.succ_4

        user_name = self.user_name

        user_id = self.user_id

        succ_0 = self.succ_0

        succ_19 = self.succ_19

        succ_18 = self.succ_18

        succ_15 = self.succ_15

        succ_14 = self.succ_14

        succ_17 = self.succ_17

        succ_16 = self.succ_16

        exit_date_iso = self.exit_date_iso

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if succ_11 is not UNSET:
            field_dict["succ_11"] = succ_11
        if succ_10 is not UNSET:
            field_dict["succ_10"] = succ_10
        if succ_13 is not UNSET:
            field_dict["succ_13"] = succ_13
        if succ_12 is not UNSET:
            field_dict["succ_12"] = succ_12
        if enter_date_iso is not UNSET:
            field_dict["enterDateIso"] = enter_date_iso
        if succ_9 is not UNSET:
            field_dict["succ_9"] = succ_9
        if hist_guid is not UNSET:
            field_dict["histGuid"] = hist_guid
        if succ_5 is not UNSET:
            field_dict["succ_5"] = succ_5
        if succ_6 is not UNSET:
            field_dict["succ_6"] = succ_6
        if flow_guid is not UNSET:
            field_dict["flowGuid"] = flow_guid
        if succ_7 is not UNSET:
            field_dict["succ_7"] = succ_7
        if succ_8 is not UNSET:
            field_dict["succ_8"] = succ_8
        if succ_1 is not UNSET:
            field_dict["succ_1"] = succ_1
        if succ_2 is not UNSET:
            field_dict["succ_2"] = succ_2
        if succ_3 is not UNSET:
            field_dict["succ_3"] = succ_3
        if succ_4 is not UNSET:
            field_dict["succ_4"] = succ_4
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if succ_0 is not UNSET:
            field_dict["succ_0"] = succ_0
        if succ_19 is not UNSET:
            field_dict["succ_19"] = succ_19
        if succ_18 is not UNSET:
            field_dict["succ_18"] = succ_18
        if succ_15 is not UNSET:
            field_dict["succ_15"] = succ_15
        if succ_14 is not UNSET:
            field_dict["succ_14"] = succ_14
        if succ_17 is not UNSET:
            field_dict["succ_17"] = succ_17
        if succ_16 is not UNSET:
            field_dict["succ_16"] = succ_16
        if exit_date_iso is not UNSET:
            field_dict["exitDateIso"] = exit_date_iso
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        succ_11 = d.pop("succ_11", UNSET)

        succ_10 = d.pop("succ_10", UNSET)

        succ_13 = d.pop("succ_13", UNSET)

        succ_12 = d.pop("succ_12", UNSET)

        enter_date_iso = d.pop("enterDateIso", UNSET)

        succ_9 = d.pop("succ_9", UNSET)

        hist_guid = d.pop("histGuid", UNSET)

        succ_5 = d.pop("succ_5", UNSET)

        succ_6 = d.pop("succ_6", UNSET)

        flow_guid = d.pop("flowGuid", UNSET)

        succ_7 = d.pop("succ_7", UNSET)

        succ_8 = d.pop("succ_8", UNSET)

        succ_1 = d.pop("succ_1", UNSET)

        succ_2 = d.pop("succ_2", UNSET)

        succ_3 = d.pop("succ_3", UNSET)

        succ_4 = d.pop("succ_4", UNSET)

        user_name = d.pop("userName", UNSET)

        user_id = d.pop("userId", UNSET)

        succ_0 = d.pop("succ_0", UNSET)

        succ_19 = d.pop("succ_19", UNSET)

        succ_18 = d.pop("succ_18", UNSET)

        succ_15 = d.pop("succ_15", UNSET)

        succ_14 = d.pop("succ_14", UNSET)

        succ_17 = d.pop("succ_17", UNSET)

        succ_16 = d.pop("succ_16", UNSET)

        exit_date_iso = d.pop("exitDateIso", UNSET)

        node_id = d.pop("nodeId", UNSET)

        wf_node_history = cls(
            succ_11=succ_11,
            succ_10=succ_10,
            succ_13=succ_13,
            succ_12=succ_12,
            enter_date_iso=enter_date_iso,
            succ_9=succ_9,
            hist_guid=hist_guid,
            succ_5=succ_5,
            succ_6=succ_6,
            flow_guid=flow_guid,
            succ_7=succ_7,
            succ_8=succ_8,
            succ_1=succ_1,
            succ_2=succ_2,
            succ_3=succ_3,
            succ_4=succ_4,
            user_name=user_name,
            user_id=user_id,
            succ_0=succ_0,
            succ_19=succ_19,
            succ_18=succ_18,
            succ_15=succ_15,
            succ_14=succ_14,
            succ_17=succ_17,
            succ_16=succ_16,
            exit_date_iso=exit_date_iso,
            node_id=node_id,
        )

        wf_node_history.additional_properties = d
        return wf_node_history

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
