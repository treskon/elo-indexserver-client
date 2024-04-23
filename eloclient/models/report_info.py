from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportInfo")


@_attrs_define
class ReportInfo:
    """This class describes a report/protocol entry for an action carried out in the archive.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            extra2 (Union[Unset, int]): Reserved - internal, dependant on actionNo
            act_time (Union[Unset, int]): Reserved - internal function.
            extra3 (Union[Unset, str]): Reserved.
            extra1 (Union[Unset, int]): Reserved - internal, dependant on actionNo.
            user_name (Union[Unset, str]): Name of the user who carried out the action.
            session_no (Union[Unset, int]): Id of the session which carried out the action.
            user_id (Union[Unset, int]): Id of the user who carried out the action.
            obj_id (Union[Unset, int]): Id of the object for which the action is entered in the protocoll.
            action (Union[Unset, str]): ActionNo as name.
            comment (Union[Unset, str]): Descriptive text or details.
            id (Union[Unset, str]): Identifier
            text (Union[Unset, str]): Reserved - internal, dependant on actionNo
            act_time_iso (Union[Unset, str]): Time of the action in ISO format.
            action_no (Union[Unset, int]): Action number in numeric form.
            extra_info (Union[Unset, str]): Extra information.
                This member is always null for report entries written by Windows-Client or
                 by ELOix versions older than 9.00.016. The type of data depends on {@link #actionNo} as shown
                 in the following table:
                 <table>
                 <tr>
                 <td>ReportInfoC.ACT_LOGIN_IX</td>
                 <td>{@link ReportInfoUserProps} object, member userInfo is set to the user logged on.</td>
                 </tr>
                 <tr>
                 <td>ReportInfoC.ACT_IX_CREATE_USER</td>
                 <td>{@link ReportInfoUserModified} object, member newProps is set to the new user.</td>
                 </tr>
                 <tr>
                 <td>ReportInfoC.ACT_IX_DELETE_USER</td>
                 <td>{@link ReportInfoUserModified} object, member newProps is set to deleted user.</td>
                 </tr>
                 <tr>
                 <td>ReportInfoC.ACT_IX_CHECKIN_USER</td>
                 <td>{@link ReportInfoUserModified} object, member newProps is set to the modified values.
                 Member oldProps is set to the values before modification.</td>
                 </tr>
                 </table>
    """

    extra2: Union[Unset, int] = UNSET
    act_time: Union[Unset, int] = UNSET
    extra3: Union[Unset, str] = UNSET
    extra1: Union[Unset, int] = UNSET
    user_name: Union[Unset, str] = UNSET
    session_no: Union[Unset, int] = UNSET
    user_id: Union[Unset, int] = UNSET
    obj_id: Union[Unset, int] = UNSET
    action: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    act_time_iso: Union[Unset, str] = UNSET
    action_no: Union[Unset, int] = UNSET
    extra_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extra2 = self.extra2

        act_time = self.act_time

        extra3 = self.extra3

        extra1 = self.extra1

        user_name = self.user_name

        session_no = self.session_no

        user_id = self.user_id

        obj_id = self.obj_id

        action = self.action

        comment = self.comment

        id = self.id

        text = self.text

        act_time_iso = self.act_time_iso

        action_no = self.action_no

        extra_info = self.extra_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extra2 is not UNSET:
            field_dict["extra2"] = extra2
        if act_time is not UNSET:
            field_dict["actTime"] = act_time
        if extra3 is not UNSET:
            field_dict["extra3"] = extra3
        if extra1 is not UNSET:
            field_dict["extra1"] = extra1
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if session_no is not UNSET:
            field_dict["sessionNo"] = session_no
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if action is not UNSET:
            field_dict["action"] = action
        if comment is not UNSET:
            field_dict["comment"] = comment
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if act_time_iso is not UNSET:
            field_dict["actTimeISO"] = act_time_iso
        if action_no is not UNSET:
            field_dict["actionNo"] = action_no
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extra2 = d.pop("extra2", UNSET)

        act_time = d.pop("actTime", UNSET)

        extra3 = d.pop("extra3", UNSET)

        extra1 = d.pop("extra1", UNSET)

        user_name = d.pop("userName", UNSET)

        session_no = d.pop("sessionNo", UNSET)

        user_id = d.pop("userId", UNSET)

        obj_id = d.pop("objId", UNSET)

        action = d.pop("action", UNSET)

        comment = d.pop("comment", UNSET)

        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        act_time_iso = d.pop("actTimeISO", UNSET)

        action_no = d.pop("actionNo", UNSET)

        extra_info = d.pop("extraInfo", UNSET)

        report_info = cls(
            extra2=extra2,
            act_time=act_time,
            extra3=extra3,
            extra1=extra1,
            user_name=user_name,
            session_no=session_no,
            user_id=user_id,
            obj_id=obj_id,
            action=action,
            comment=comment,
            id=id,
            text=text,
            act_time_iso=act_time_iso,
            action_no=action_no,
            extra_info=extra_info,
        )

        report_info.additional_properties = d
        return report_info

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
