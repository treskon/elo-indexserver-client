from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WFNodeHistoryC")


@_attrs_define
class WFNodeHistoryC:
    """<p>Bit constants for members of WFNodeHistory</p>
    <p>Copyright: Copyright (c) 2003</p>
     <p>Organisation: ELO Digital Office GmbH</p>

        Attributes:
            ln_user_name (Union[Unset, int]): DB column: wf_username
            ln_hist_guid (Union[Unset, int]): DB column: wfhistguid
            mb_terminate (Union[Unset, str]): DB column: wf_terminate
            mb_user_name (Union[Unset, str]): DB column: wf_username
            mb_flow_guid (Union[Unset, str]): DB column: wfguid
            mb_node_id (Union[Unset, str]): DB column: wf_nodeid
            ln_flow_guid (Union[Unset, int]): DB column: wfguid
            mb_all_members (Union[Unset, str]): All valid member bits.
            mb_succ_10 (Union[Unset, str]): DB column: wf_succ_10
            mb_succ_4 (Union[Unset, str]): DB column: wf_succ_4
            mb_succ_15 (Union[Unset, str]): DB column: wf_succ_15
            mb_user_id (Union[Unset, str]): DB column: wf_user
            mb_succ_5 (Union[Unset, str]): DB column: wf_succ_5
            mb_succ_16 (Union[Unset, str]): DB column: wf_succ_16
            mb_succ_6 (Union[Unset, str]): DB column: wf_succ_6
            mb_succ_17 (Union[Unset, str]): DB column: wf_succ_17
            mb_succ_7 (Union[Unset, str]): DB column: wf_succ_7
            mb_succ_18 (Union[Unset, str]): DB column: wf_succ_18
            mb_succ_0 (Union[Unset, str]): DB column: wf_succ_0
            mb_succ_11 (Union[Unset, str]): DB column: wf_succ_11
            mb_succ_1 (Union[Unset, str]): DB column: wf_succ_1
            mb_succ_12 (Union[Unset, str]): DB column: wf_succ_12
            mb_succ_2 (Union[Unset, str]): DB column: wf_succ_2
            mb_succ_13 (Union[Unset, str]): DB column: wf_succ_13
            mb_succ_3 (Union[Unset, str]): DB column: wf_succ_3
            mb_succ_14 (Union[Unset, str]): DB column: wf_succ_14
            mb_succ_8 (Union[Unset, str]): DB column: wf_succ_8
            mb_succ_19 (Union[Unset, str]): DB column: wf_succ_19
            mb_activate (Union[Unset, str]): DB column: wf_activate
            mb_succ_9 (Union[Unset, str]): DB column: wf_succ_9
            mb_hist_guid (Union[Unset, str]): DB column: wfhistguid
    """

    ln_user_name: Union[Unset, int] = UNSET
    ln_hist_guid: Union[Unset, int] = UNSET
    mb_terminate: Union[Unset, str] = UNSET
    mb_user_name: Union[Unset, str] = UNSET
    mb_flow_guid: Union[Unset, str] = UNSET
    mb_node_id: Union[Unset, str] = UNSET
    ln_flow_guid: Union[Unset, int] = UNSET
    mb_all_members: Union[Unset, str] = UNSET
    mb_succ_10: Union[Unset, str] = UNSET
    mb_succ_4: Union[Unset, str] = UNSET
    mb_succ_15: Union[Unset, str] = UNSET
    mb_user_id: Union[Unset, str] = UNSET
    mb_succ_5: Union[Unset, str] = UNSET
    mb_succ_16: Union[Unset, str] = UNSET
    mb_succ_6: Union[Unset, str] = UNSET
    mb_succ_17: Union[Unset, str] = UNSET
    mb_succ_7: Union[Unset, str] = UNSET
    mb_succ_18: Union[Unset, str] = UNSET
    mb_succ_0: Union[Unset, str] = UNSET
    mb_succ_11: Union[Unset, str] = UNSET
    mb_succ_1: Union[Unset, str] = UNSET
    mb_succ_12: Union[Unset, str] = UNSET
    mb_succ_2: Union[Unset, str] = UNSET
    mb_succ_13: Union[Unset, str] = UNSET
    mb_succ_3: Union[Unset, str] = UNSET
    mb_succ_14: Union[Unset, str] = UNSET
    mb_succ_8: Union[Unset, str] = UNSET
    mb_succ_19: Union[Unset, str] = UNSET
    mb_activate: Union[Unset, str] = UNSET
    mb_succ_9: Union[Unset, str] = UNSET
    mb_hist_guid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ln_user_name = self.ln_user_name

        ln_hist_guid = self.ln_hist_guid

        mb_terminate = self.mb_terminate

        mb_user_name = self.mb_user_name

        mb_flow_guid = self.mb_flow_guid

        mb_node_id = self.mb_node_id

        ln_flow_guid = self.ln_flow_guid

        mb_all_members = self.mb_all_members

        mb_succ_10 = self.mb_succ_10

        mb_succ_4 = self.mb_succ_4

        mb_succ_15 = self.mb_succ_15

        mb_user_id = self.mb_user_id

        mb_succ_5 = self.mb_succ_5

        mb_succ_16 = self.mb_succ_16

        mb_succ_6 = self.mb_succ_6

        mb_succ_17 = self.mb_succ_17

        mb_succ_7 = self.mb_succ_7

        mb_succ_18 = self.mb_succ_18

        mb_succ_0 = self.mb_succ_0

        mb_succ_11 = self.mb_succ_11

        mb_succ_1 = self.mb_succ_1

        mb_succ_12 = self.mb_succ_12

        mb_succ_2 = self.mb_succ_2

        mb_succ_13 = self.mb_succ_13

        mb_succ_3 = self.mb_succ_3

        mb_succ_14 = self.mb_succ_14

        mb_succ_8 = self.mb_succ_8

        mb_succ_19 = self.mb_succ_19

        mb_activate = self.mb_activate

        mb_succ_9 = self.mb_succ_9

        mb_hist_guid = self.mb_hist_guid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ln_user_name is not UNSET:
            field_dict["lnUserName"] = ln_user_name
        if ln_hist_guid is not UNSET:
            field_dict["lnHistGuid"] = ln_hist_guid
        if mb_terminate is not UNSET:
            field_dict["mbTerminate"] = mb_terminate
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if mb_flow_guid is not UNSET:
            field_dict["mbFlowGuid"] = mb_flow_guid
        if mb_node_id is not UNSET:
            field_dict["mbNodeId"] = mb_node_id
        if ln_flow_guid is not UNSET:
            field_dict["lnFlowGuid"] = ln_flow_guid
        if mb_all_members is not UNSET:
            field_dict["mbAllMembers"] = mb_all_members
        if mb_succ_10 is not UNSET:
            field_dict["mbSucc_10"] = mb_succ_10
        if mb_succ_4 is not UNSET:
            field_dict["mbSucc_4"] = mb_succ_4
        if mb_succ_15 is not UNSET:
            field_dict["mbSucc_15"] = mb_succ_15
        if mb_user_id is not UNSET:
            field_dict["mbUserId"] = mb_user_id
        if mb_succ_5 is not UNSET:
            field_dict["mbSucc_5"] = mb_succ_5
        if mb_succ_16 is not UNSET:
            field_dict["mbSucc_16"] = mb_succ_16
        if mb_succ_6 is not UNSET:
            field_dict["mbSucc_6"] = mb_succ_6
        if mb_succ_17 is not UNSET:
            field_dict["mbSucc_17"] = mb_succ_17
        if mb_succ_7 is not UNSET:
            field_dict["mbSucc_7"] = mb_succ_7
        if mb_succ_18 is not UNSET:
            field_dict["mbSucc_18"] = mb_succ_18
        if mb_succ_0 is not UNSET:
            field_dict["mbSucc_0"] = mb_succ_0
        if mb_succ_11 is not UNSET:
            field_dict["mbSucc_11"] = mb_succ_11
        if mb_succ_1 is not UNSET:
            field_dict["mbSucc_1"] = mb_succ_1
        if mb_succ_12 is not UNSET:
            field_dict["mbSucc_12"] = mb_succ_12
        if mb_succ_2 is not UNSET:
            field_dict["mbSucc_2"] = mb_succ_2
        if mb_succ_13 is not UNSET:
            field_dict["mbSucc_13"] = mb_succ_13
        if mb_succ_3 is not UNSET:
            field_dict["mbSucc_3"] = mb_succ_3
        if mb_succ_14 is not UNSET:
            field_dict["mbSucc_14"] = mb_succ_14
        if mb_succ_8 is not UNSET:
            field_dict["mbSucc_8"] = mb_succ_8
        if mb_succ_19 is not UNSET:
            field_dict["mbSucc_19"] = mb_succ_19
        if mb_activate is not UNSET:
            field_dict["mbActivate"] = mb_activate
        if mb_succ_9 is not UNSET:
            field_dict["mbSucc_9"] = mb_succ_9
        if mb_hist_guid is not UNSET:
            field_dict["mbHistGuid"] = mb_hist_guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ln_user_name = d.pop("lnUserName", UNSET)

        ln_hist_guid = d.pop("lnHistGuid", UNSET)

        mb_terminate = d.pop("mbTerminate", UNSET)

        mb_user_name = d.pop("mbUserName", UNSET)

        mb_flow_guid = d.pop("mbFlowGuid", UNSET)

        mb_node_id = d.pop("mbNodeId", UNSET)

        ln_flow_guid = d.pop("lnFlowGuid", UNSET)

        mb_all_members = d.pop("mbAllMembers", UNSET)

        mb_succ_10 = d.pop("mbSucc_10", UNSET)

        mb_succ_4 = d.pop("mbSucc_4", UNSET)

        mb_succ_15 = d.pop("mbSucc_15", UNSET)

        mb_user_id = d.pop("mbUserId", UNSET)

        mb_succ_5 = d.pop("mbSucc_5", UNSET)

        mb_succ_16 = d.pop("mbSucc_16", UNSET)

        mb_succ_6 = d.pop("mbSucc_6", UNSET)

        mb_succ_17 = d.pop("mbSucc_17", UNSET)

        mb_succ_7 = d.pop("mbSucc_7", UNSET)

        mb_succ_18 = d.pop("mbSucc_18", UNSET)

        mb_succ_0 = d.pop("mbSucc_0", UNSET)

        mb_succ_11 = d.pop("mbSucc_11", UNSET)

        mb_succ_1 = d.pop("mbSucc_1", UNSET)

        mb_succ_12 = d.pop("mbSucc_12", UNSET)

        mb_succ_2 = d.pop("mbSucc_2", UNSET)

        mb_succ_13 = d.pop("mbSucc_13", UNSET)

        mb_succ_3 = d.pop("mbSucc_3", UNSET)

        mb_succ_14 = d.pop("mbSucc_14", UNSET)

        mb_succ_8 = d.pop("mbSucc_8", UNSET)

        mb_succ_19 = d.pop("mbSucc_19", UNSET)

        mb_activate = d.pop("mbActivate", UNSET)

        mb_succ_9 = d.pop("mbSucc_9", UNSET)

        mb_hist_guid = d.pop("mbHistGuid", UNSET)

        wf_node_history_c = cls(
            ln_user_name=ln_user_name,
            ln_hist_guid=ln_hist_guid,
            mb_terminate=mb_terminate,
            mb_user_name=mb_user_name,
            mb_flow_guid=mb_flow_guid,
            mb_node_id=mb_node_id,
            ln_flow_guid=ln_flow_guid,
            mb_all_members=mb_all_members,
            mb_succ_10=mb_succ_10,
            mb_succ_4=mb_succ_4,
            mb_succ_15=mb_succ_15,
            mb_user_id=mb_user_id,
            mb_succ_5=mb_succ_5,
            mb_succ_16=mb_succ_16,
            mb_succ_6=mb_succ_6,
            mb_succ_17=mb_succ_17,
            mb_succ_7=mb_succ_7,
            mb_succ_18=mb_succ_18,
            mb_succ_0=mb_succ_0,
            mb_succ_11=mb_succ_11,
            mb_succ_1=mb_succ_1,
            mb_succ_12=mb_succ_12,
            mb_succ_2=mb_succ_2,
            mb_succ_13=mb_succ_13,
            mb_succ_3=mb_succ_3,
            mb_succ_14=mb_succ_14,
            mb_succ_8=mb_succ_8,
            mb_succ_19=mb_succ_19,
            mb_activate=mb_activate,
            mb_succ_9=mb_succ_9,
            mb_hist_guid=mb_hist_guid,
        )

        wf_node_history_c.additional_properties = d
        return wf_node_history_c

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
