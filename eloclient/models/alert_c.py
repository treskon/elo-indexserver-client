from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertC")


@_attrs_define
class AlertC:
    """
    Attributes:
        postmove (Union[Unset, int]): (to be defined)
        delvert (Union[Unset, int]): (to be defined)
        wvseen (Union[Unset, int]): (to be defined)
        wfarrived (Union[Unset, int]): (to be defined)
        maskwf (Union[Unset, int]): (to be defined)
        wvdeleted (Union[Unset, int]): (to be defined)
        maskvert (Union[Unset, int]): (to be defined)
        newvert (Union[Unset, int]): (to be defined)
        message (Union[Unset, int]): (to be defined)
        maskwv (Union[Unset, int]): (to be defined)
        maskpost (Union[Unset, int]): (to be defined)
        maskwvedmsg (Union[Unset, int]): (to be defined)
        maskwvdelmsg (Union[Unset, int]): (to be defined)
        wvedited (Union[Unset, int]): (to be defined)
        wfstart (Union[Unset, int]): (to be defined)
        maskalarm (Union[Unset, int]): (to be defined)
        masksonst (Union[Unset, int]): (to be defined)
        replerr (Union[Unset, int]): Alert is a message from the replication module
    """

    postmove: Union[Unset, int] = UNSET
    delvert: Union[Unset, int] = UNSET
    wvseen: Union[Unset, int] = UNSET
    wfarrived: Union[Unset, int] = UNSET
    maskwf: Union[Unset, int] = UNSET
    wvdeleted: Union[Unset, int] = UNSET
    maskvert: Union[Unset, int] = UNSET
    newvert: Union[Unset, int] = UNSET
    message: Union[Unset, int] = UNSET
    maskwv: Union[Unset, int] = UNSET
    maskpost: Union[Unset, int] = UNSET
    maskwvedmsg: Union[Unset, int] = UNSET
    maskwvdelmsg: Union[Unset, int] = UNSET
    wvedited: Union[Unset, int] = UNSET
    wfstart: Union[Unset, int] = UNSET
    maskalarm: Union[Unset, int] = UNSET
    masksonst: Union[Unset, int] = UNSET
    replerr: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        postmove = self.postmove

        delvert = self.delvert

        wvseen = self.wvseen

        wfarrived = self.wfarrived

        maskwf = self.maskwf

        wvdeleted = self.wvdeleted

        maskvert = self.maskvert

        newvert = self.newvert

        message = self.message

        maskwv = self.maskwv

        maskpost = self.maskpost

        maskwvedmsg = self.maskwvedmsg

        maskwvdelmsg = self.maskwvdelmsg

        wvedited = self.wvedited

        wfstart = self.wfstart

        maskalarm = self.maskalarm

        masksonst = self.masksonst

        replerr = self.replerr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if postmove is not UNSET:
            field_dict["POSTMOVE"] = postmove
        if delvert is not UNSET:
            field_dict["DELVERT"] = delvert
        if wvseen is not UNSET:
            field_dict["WVSEEN"] = wvseen
        if wfarrived is not UNSET:
            field_dict["WFARRIVED"] = wfarrived
        if maskwf is not UNSET:
            field_dict["MASKWF"] = maskwf
        if wvdeleted is not UNSET:
            field_dict["WVDELETED"] = wvdeleted
        if maskvert is not UNSET:
            field_dict["MASKVERT"] = maskvert
        if newvert is not UNSET:
            field_dict["NEWVERT"] = newvert
        if message is not UNSET:
            field_dict["MESSAGE"] = message
        if maskwv is not UNSET:
            field_dict["MASKWV"] = maskwv
        if maskpost is not UNSET:
            field_dict["MASKPOST"] = maskpost
        if maskwvedmsg is not UNSET:
            field_dict["MASKWVEDMSG"] = maskwvedmsg
        if maskwvdelmsg is not UNSET:
            field_dict["MASKWVDELMSG"] = maskwvdelmsg
        if wvedited is not UNSET:
            field_dict["WVEDITED"] = wvedited
        if wfstart is not UNSET:
            field_dict["WFSTART"] = wfstart
        if maskalarm is not UNSET:
            field_dict["MASKALARM"] = maskalarm
        if masksonst is not UNSET:
            field_dict["MASKSONST"] = masksonst
        if replerr is not UNSET:
            field_dict["REPLERR"] = replerr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        postmove = d.pop("POSTMOVE", UNSET)

        delvert = d.pop("DELVERT", UNSET)

        wvseen = d.pop("WVSEEN", UNSET)

        wfarrived = d.pop("WFARRIVED", UNSET)

        maskwf = d.pop("MASKWF", UNSET)

        wvdeleted = d.pop("WVDELETED", UNSET)

        maskvert = d.pop("MASKVERT", UNSET)

        newvert = d.pop("NEWVERT", UNSET)

        message = d.pop("MESSAGE", UNSET)

        maskwv = d.pop("MASKWV", UNSET)

        maskpost = d.pop("MASKPOST", UNSET)

        maskwvedmsg = d.pop("MASKWVEDMSG", UNSET)

        maskwvdelmsg = d.pop("MASKWVDELMSG", UNSET)

        wvedited = d.pop("WVEDITED", UNSET)

        wfstart = d.pop("WFSTART", UNSET)

        maskalarm = d.pop("MASKALARM", UNSET)

        masksonst = d.pop("MASKSONST", UNSET)

        replerr = d.pop("REPLERR", UNSET)

        alert_c = cls(
            postmove=postmove,
            delvert=delvert,
            wvseen=wvseen,
            wfarrived=wfarrived,
            maskwf=maskwf,
            wvdeleted=wvdeleted,
            maskvert=maskvert,
            newvert=newvert,
            message=message,
            maskwv=maskwv,
            maskpost=maskpost,
            maskwvedmsg=maskwvedmsg,
            maskwvdelmsg=maskwvdelmsg,
            wvedited=wvedited,
            wfstart=wfstart,
            maskalarm=maskalarm,
            masksonst=masksonst,
            replerr=replerr,
        )

        alert_c.additional_properties = d
        return alert_c

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
