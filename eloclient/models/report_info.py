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
            act_time (Union[Unset, int]): Reserved - internal function.
            action_no (Union[Unset, int]): Action number in numeric form.
            extra1 (Union[Unset, int]): Reserved - internal, dependant on actionNo.
            extra2 (Union[Unset, int]): Reserved - internal, dependant on actionNo
            id (Union[Unset, str]): Identifier
            obj_id (Union[Unset, int]): Id of the object for which the action is entered in the protocoll.
            session_no (Union[Unset, int]): Id of the session which carried out the action.
            text (Union[Unset, str]): Reserved - internal, dependant on actionNo
            user_id (Union[Unset, int]): Id of the user who carried out the action.
            act_time_iso (Union[Unset, str]): Time of the action in ISO format.
            action (Union[Unset, str]): ActionNo as name.
            comment (Union[Unset, str]): Descriptive text or details.
            user_name (Union[Unset, str]): Name of the user who carried out the action.
            extra3 (Union[Unset, str]): Reserved.
            extra_info (Union[Unset, str]): Extra information.
                This member is always null for report entries written by Windows-Client or by ELOix versions
                 older than 9.00.016. The type of data depends on {@link #actionNo} as shown in the following table:
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
                 <td>{@link ReportInfoUserModified} object, member newProps is set to the modified values. Member oldProps is
                set to
                 the values before modification.</td>
                 </tr>
                 </table>
    """

    act_time: Union[Unset, int] = UNSET
    action_no: Union[Unset, int] = UNSET
    extra1: Union[Unset, int] = UNSET
    extra2: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    obj_id: Union[Unset, int] = UNSET
    session_no: Union[Unset, int] = UNSET
    text: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    act_time_iso: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    extra3: Union[Unset, str] = UNSET
    extra_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        act_time = self.act_time
        action_no = self.action_no
        extra1 = self.extra1
        extra2 = self.extra2
        id = self.id
        obj_id = self.obj_id
        session_no = self.session_no
        text = self.text
        user_id = self.user_id
        act_time_iso = self.act_time_iso
        action = self.action
        comment = self.comment
        user_name = self.user_name
        extra3 = self.extra3
        extra_info = self.extra_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if act_time is not UNSET:
            field_dict["actTime"] = act_time
        if action_no is not UNSET:
            field_dict["actionNo"] = action_no
        if extra1 is not UNSET:
            field_dict["extra1"] = extra1
        if extra2 is not UNSET:
            field_dict["extra2"] = extra2
        if id is not UNSET:
            field_dict["id"] = id
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if session_no is not UNSET:
            field_dict["sessionNo"] = session_no
        if text is not UNSET:
            field_dict["text"] = text
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if act_time_iso is not UNSET:
            field_dict["actTimeISO"] = act_time_iso
        if action is not UNSET:
            field_dict["action"] = action
        if comment is not UNSET:
            field_dict["comment"] = comment
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if extra3 is not UNSET:
            field_dict["extra3"] = extra3
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        act_time = d.pop("actTime", UNSET)

        action_no = d.pop("actionNo", UNSET)

        extra1 = d.pop("extra1", UNSET)

        extra2 = d.pop("extra2", UNSET)

        id = d.pop("id", UNSET)

        obj_id = d.pop("objId", UNSET)

        session_no = d.pop("sessionNo", UNSET)

        text = d.pop("text", UNSET)

        user_id = d.pop("userId", UNSET)

        act_time_iso = d.pop("actTimeISO", UNSET)

        action = d.pop("action", UNSET)

        comment = d.pop("comment", UNSET)

        user_name = d.pop("userName", UNSET)

        extra3 = d.pop("extra3", UNSET)

        extra_info = d.pop("extraInfo", UNSET)

        report_info = cls(
            act_time=act_time,
            action_no=action_no,
            extra1=extra1,
            extra2=extra2,
            id=id,
            obj_id=obj_id,
            session_no=session_no,
            text=text,
            user_id=user_id,
            act_time_iso=act_time_iso,
            action=action,
            comment=comment,
            user_name=user_name,
            extra3=extra3,
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
