from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportOptionsC")


@_attrs_define
class ReportOptionsC:
    """Constants for report mode
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>
     An ERP code is assigned to one or more action codes.

        Attributes:
            erp_logopenarc (Union[Unset, int]):
            erp_delflowtempl (Union[Unset, int]):
            erp_norepdata (Union[Unset, int]):
            erp_logchangekind (Union[Unset, int]):
            erp_writesession (Union[Unset, int]):
            erp_logcreatedoc (Union[Unset, int]):
            erp_logcomplain (Union[Unset, int]):
            erp_flowtimelimt (Union[Unset, int]):
            erp_logerasor (Union[Unset, int]):
            erp_logmovedoc (Union[Unset, int]):
            erp_logmaskdata (Union[Unset, int]):
            erp_postbox (Union[Unset, int]):
            erp_logeditdata (Union[Unset, int]):
            erp_logfirstmessage (Union[Unset, int]):
            erp_logrefdoc (Union[Unset, int]):
            erp_logeraref (Union[Unset, int]):
            erp_logpathdata (Union[Unset, int]):
            erp_flowerroryesno (Union[Unset, int]):
            erp_logcolordata (Union[Unset, int]):
            erp_removevert (Union[Unset, int]):
            erp_forwardflow (Union[Unset, int]):
            erp_pickpost (Union[Unset, int]):
            erp_logcreatesor (Union[Unset, int]):
            erp_logattachment (Union[Unset, int]):
            erp_logmovesor (Union[Unset, int]):
            erp_checkin (Union[Unset, int]):
            erp_search (Union[Unset, int]):
            erp_convert_format (Union[Unset, int]):
            erp_logrefsor (Union[Unset, int]):
            erp_delflowactive (Union[Unset, int]):
            erp_wv (Union[Unset, int]):
            erp_verschieden (Union[Unset, int]):
            erp_setvert (Union[Unset, int]):
            erp_custom (Union[Unset, int]):
            erp_newvert (Union[Unset, int]):
            erp_delversion (Union[Unset, int]):
            erp_editflowtempl (Union[Unset, int]):
            erp_logdeldocs (Union[Unset, int]):
            erp_logchangepwd (Union[Unset, int]):
            erp_startflow (Union[Unset, int]):
            erp_editflowactive (Union[Unset, int]):
            erp_substitutions (Union[Unset, int]): All substitution actions are combined into this code:
                <ul>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_NEW}</li>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_CHANGE}</li>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_ACTIVATE}</li>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_DEACTIVATE}</li>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_FORWARD}</li>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_TRANSFER}</li>
                 <li>{@link ReportInfoC#ACT_IX_SUBSTITUTION_DELETE}</li>
                 </ul>
            erp_resetvert (Union[Unset, int]):
            erp_logclosearc (Union[Unset, int]):
            erp_showdoc (Union[Unset, int]):
            erp_logeditdoc (Union[Unset, int]):
            erp_freevert (Union[Unset, int]):
            erp_logchangekey (Union[Unset, int]):
            erp_postbarcode (Union[Unset, int]):
            erp_dm_readdoc (Union[Unset, int]):
            erp_logviewdoc (Union[Unset, int]):
            erp_logeradoc (Union[Unset, int]):
            erp_loglastmessage (Union[Unset, int]):
            erp_logaspectdata (Union[Unset, int]):
            erp_error (Union[Unset, int]):
            erp_logkeydata (Union[Unset, int]):
            erp_createflowtempl (Union[Unset, int]):
            erp_delvert (Union[Unset, int]):
            erp_loguserdata (Union[Unset, int]):
            erp_receiveflow (Union[Unset, int]):
            erp_showsor (Union[Unset, int]):
            erp_checkout (Union[Unset, int]):
    """

    erp_logopenarc: Union[Unset, int] = UNSET
    erp_delflowtempl: Union[Unset, int] = UNSET
    erp_norepdata: Union[Unset, int] = UNSET
    erp_logchangekind: Union[Unset, int] = UNSET
    erp_writesession: Union[Unset, int] = UNSET
    erp_logcreatedoc: Union[Unset, int] = UNSET
    erp_logcomplain: Union[Unset, int] = UNSET
    erp_flowtimelimt: Union[Unset, int] = UNSET
    erp_logerasor: Union[Unset, int] = UNSET
    erp_logmovedoc: Union[Unset, int] = UNSET
    erp_logmaskdata: Union[Unset, int] = UNSET
    erp_postbox: Union[Unset, int] = UNSET
    erp_logeditdata: Union[Unset, int] = UNSET
    erp_logfirstmessage: Union[Unset, int] = UNSET
    erp_logrefdoc: Union[Unset, int] = UNSET
    erp_logeraref: Union[Unset, int] = UNSET
    erp_logpathdata: Union[Unset, int] = UNSET
    erp_flowerroryesno: Union[Unset, int] = UNSET
    erp_logcolordata: Union[Unset, int] = UNSET
    erp_removevert: Union[Unset, int] = UNSET
    erp_forwardflow: Union[Unset, int] = UNSET
    erp_pickpost: Union[Unset, int] = UNSET
    erp_logcreatesor: Union[Unset, int] = UNSET
    erp_logattachment: Union[Unset, int] = UNSET
    erp_logmovesor: Union[Unset, int] = UNSET
    erp_checkin: Union[Unset, int] = UNSET
    erp_search: Union[Unset, int] = UNSET
    erp_convert_format: Union[Unset, int] = UNSET
    erp_logrefsor: Union[Unset, int] = UNSET
    erp_delflowactive: Union[Unset, int] = UNSET
    erp_wv: Union[Unset, int] = UNSET
    erp_verschieden: Union[Unset, int] = UNSET
    erp_setvert: Union[Unset, int] = UNSET
    erp_custom: Union[Unset, int] = UNSET
    erp_newvert: Union[Unset, int] = UNSET
    erp_delversion: Union[Unset, int] = UNSET
    erp_editflowtempl: Union[Unset, int] = UNSET
    erp_logdeldocs: Union[Unset, int] = UNSET
    erp_logchangepwd: Union[Unset, int] = UNSET
    erp_startflow: Union[Unset, int] = UNSET
    erp_editflowactive: Union[Unset, int] = UNSET
    erp_substitutions: Union[Unset, int] = UNSET
    erp_resetvert: Union[Unset, int] = UNSET
    erp_logclosearc: Union[Unset, int] = UNSET
    erp_showdoc: Union[Unset, int] = UNSET
    erp_logeditdoc: Union[Unset, int] = UNSET
    erp_freevert: Union[Unset, int] = UNSET
    erp_logchangekey: Union[Unset, int] = UNSET
    erp_postbarcode: Union[Unset, int] = UNSET
    erp_dm_readdoc: Union[Unset, int] = UNSET
    erp_logviewdoc: Union[Unset, int] = UNSET
    erp_logeradoc: Union[Unset, int] = UNSET
    erp_loglastmessage: Union[Unset, int] = UNSET
    erp_logaspectdata: Union[Unset, int] = UNSET
    erp_error: Union[Unset, int] = UNSET
    erp_logkeydata: Union[Unset, int] = UNSET
    erp_createflowtempl: Union[Unset, int] = UNSET
    erp_delvert: Union[Unset, int] = UNSET
    erp_loguserdata: Union[Unset, int] = UNSET
    erp_receiveflow: Union[Unset, int] = UNSET
    erp_showsor: Union[Unset, int] = UNSET
    erp_checkout: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        erp_logopenarc = self.erp_logopenarc

        erp_delflowtempl = self.erp_delflowtempl

        erp_norepdata = self.erp_norepdata

        erp_logchangekind = self.erp_logchangekind

        erp_writesession = self.erp_writesession

        erp_logcreatedoc = self.erp_logcreatedoc

        erp_logcomplain = self.erp_logcomplain

        erp_flowtimelimt = self.erp_flowtimelimt

        erp_logerasor = self.erp_logerasor

        erp_logmovedoc = self.erp_logmovedoc

        erp_logmaskdata = self.erp_logmaskdata

        erp_postbox = self.erp_postbox

        erp_logeditdata = self.erp_logeditdata

        erp_logfirstmessage = self.erp_logfirstmessage

        erp_logrefdoc = self.erp_logrefdoc

        erp_logeraref = self.erp_logeraref

        erp_logpathdata = self.erp_logpathdata

        erp_flowerroryesno = self.erp_flowerroryesno

        erp_logcolordata = self.erp_logcolordata

        erp_removevert = self.erp_removevert

        erp_forwardflow = self.erp_forwardflow

        erp_pickpost = self.erp_pickpost

        erp_logcreatesor = self.erp_logcreatesor

        erp_logattachment = self.erp_logattachment

        erp_logmovesor = self.erp_logmovesor

        erp_checkin = self.erp_checkin

        erp_search = self.erp_search

        erp_convert_format = self.erp_convert_format

        erp_logrefsor = self.erp_logrefsor

        erp_delflowactive = self.erp_delflowactive

        erp_wv = self.erp_wv

        erp_verschieden = self.erp_verschieden

        erp_setvert = self.erp_setvert

        erp_custom = self.erp_custom

        erp_newvert = self.erp_newvert

        erp_delversion = self.erp_delversion

        erp_editflowtempl = self.erp_editflowtempl

        erp_logdeldocs = self.erp_logdeldocs

        erp_logchangepwd = self.erp_logchangepwd

        erp_startflow = self.erp_startflow

        erp_editflowactive = self.erp_editflowactive

        erp_substitutions = self.erp_substitutions

        erp_resetvert = self.erp_resetvert

        erp_logclosearc = self.erp_logclosearc

        erp_showdoc = self.erp_showdoc

        erp_logeditdoc = self.erp_logeditdoc

        erp_freevert = self.erp_freevert

        erp_logchangekey = self.erp_logchangekey

        erp_postbarcode = self.erp_postbarcode

        erp_dm_readdoc = self.erp_dm_readdoc

        erp_logviewdoc = self.erp_logviewdoc

        erp_logeradoc = self.erp_logeradoc

        erp_loglastmessage = self.erp_loglastmessage

        erp_logaspectdata = self.erp_logaspectdata

        erp_error = self.erp_error

        erp_logkeydata = self.erp_logkeydata

        erp_createflowtempl = self.erp_createflowtempl

        erp_delvert = self.erp_delvert

        erp_loguserdata = self.erp_loguserdata

        erp_receiveflow = self.erp_receiveflow

        erp_showsor = self.erp_showsor

        erp_checkout = self.erp_checkout

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if erp_logopenarc is not UNSET:
            field_dict["ERP_LOGOPENARC"] = erp_logopenarc
        if erp_delflowtempl is not UNSET:
            field_dict["ERP_DELFLOWTEMPL"] = erp_delflowtempl
        if erp_norepdata is not UNSET:
            field_dict["ERP_NOREPDATA"] = erp_norepdata
        if erp_logchangekind is not UNSET:
            field_dict["ERP_LOGCHANGEKIND"] = erp_logchangekind
        if erp_writesession is not UNSET:
            field_dict["ERP_WRITESESSION"] = erp_writesession
        if erp_logcreatedoc is not UNSET:
            field_dict["ERP_LOGCREATEDOC"] = erp_logcreatedoc
        if erp_logcomplain is not UNSET:
            field_dict["ERP_LOGCOMPLAIN"] = erp_logcomplain
        if erp_flowtimelimt is not UNSET:
            field_dict["ERP_FLOWTIMELIMT"] = erp_flowtimelimt
        if erp_logerasor is not UNSET:
            field_dict["ERP_LOGERASOR"] = erp_logerasor
        if erp_logmovedoc is not UNSET:
            field_dict["ERP_LOGMOVEDOC"] = erp_logmovedoc
        if erp_logmaskdata is not UNSET:
            field_dict["ERP_LOGMASKDATA"] = erp_logmaskdata
        if erp_postbox is not UNSET:
            field_dict["ERP_POSTBOX"] = erp_postbox
        if erp_logeditdata is not UNSET:
            field_dict["ERP_LOGEDITDATA"] = erp_logeditdata
        if erp_logfirstmessage is not UNSET:
            field_dict["ERP_LOGFIRSTMESSAGE"] = erp_logfirstmessage
        if erp_logrefdoc is not UNSET:
            field_dict["ERP_LOGREFDOC"] = erp_logrefdoc
        if erp_logeraref is not UNSET:
            field_dict["ERP_LOGERAREF"] = erp_logeraref
        if erp_logpathdata is not UNSET:
            field_dict["ERP_LOGPATHDATA"] = erp_logpathdata
        if erp_flowerroryesno is not UNSET:
            field_dict["ERP_FLOWERRORYESNO"] = erp_flowerroryesno
        if erp_logcolordata is not UNSET:
            field_dict["ERP_LOGCOLORDATA"] = erp_logcolordata
        if erp_removevert is not UNSET:
            field_dict["ERP_REMOVEVERT"] = erp_removevert
        if erp_forwardflow is not UNSET:
            field_dict["ERP_FORWARDFLOW"] = erp_forwardflow
        if erp_pickpost is not UNSET:
            field_dict["ERP_PICKPOST"] = erp_pickpost
        if erp_logcreatesor is not UNSET:
            field_dict["ERP_LOGCREATESOR"] = erp_logcreatesor
        if erp_logattachment is not UNSET:
            field_dict["ERP_LOGATTACHMENT"] = erp_logattachment
        if erp_logmovesor is not UNSET:
            field_dict["ERP_LOGMOVESOR"] = erp_logmovesor
        if erp_checkin is not UNSET:
            field_dict["ERP_CHECKIN"] = erp_checkin
        if erp_search is not UNSET:
            field_dict["ERP_SEARCH"] = erp_search
        if erp_convert_format is not UNSET:
            field_dict["ERP_CONVERT_FORMAT"] = erp_convert_format
        if erp_logrefsor is not UNSET:
            field_dict["ERP_LOGREFSOR"] = erp_logrefsor
        if erp_delflowactive is not UNSET:
            field_dict["ERP_DELFLOWACTIVE"] = erp_delflowactive
        if erp_wv is not UNSET:
            field_dict["ERP_WV"] = erp_wv
        if erp_verschieden is not UNSET:
            field_dict["ERP_VERSCHIEDEN"] = erp_verschieden
        if erp_setvert is not UNSET:
            field_dict["ERP_SETVERT"] = erp_setvert
        if erp_custom is not UNSET:
            field_dict["ERP_CUSTOM"] = erp_custom
        if erp_newvert is not UNSET:
            field_dict["ERP_NEWVERT"] = erp_newvert
        if erp_delversion is not UNSET:
            field_dict["ERP_DELVERSION"] = erp_delversion
        if erp_editflowtempl is not UNSET:
            field_dict["ERP_EDITFLOWTEMPL"] = erp_editflowtempl
        if erp_logdeldocs is not UNSET:
            field_dict["ERP_LOGDELDOCS"] = erp_logdeldocs
        if erp_logchangepwd is not UNSET:
            field_dict["ERP_LOGCHANGEPWD"] = erp_logchangepwd
        if erp_startflow is not UNSET:
            field_dict["ERP_STARTFLOW"] = erp_startflow
        if erp_editflowactive is not UNSET:
            field_dict["ERP_EDITFLOWACTIVE"] = erp_editflowactive
        if erp_substitutions is not UNSET:
            field_dict["ERP_SUBSTITUTIONS"] = erp_substitutions
        if erp_resetvert is not UNSET:
            field_dict["ERP_RESETVERT"] = erp_resetvert
        if erp_logclosearc is not UNSET:
            field_dict["ERP_LOGCLOSEARC"] = erp_logclosearc
        if erp_showdoc is not UNSET:
            field_dict["ERP_SHOWDOC"] = erp_showdoc
        if erp_logeditdoc is not UNSET:
            field_dict["ERP_LOGEDITDOC"] = erp_logeditdoc
        if erp_freevert is not UNSET:
            field_dict["ERP_FREEVERT"] = erp_freevert
        if erp_logchangekey is not UNSET:
            field_dict["ERP_LOGCHANGEKEY"] = erp_logchangekey
        if erp_postbarcode is not UNSET:
            field_dict["ERP_POSTBARCODE"] = erp_postbarcode
        if erp_dm_readdoc is not UNSET:
            field_dict["ERP_DM_READDOC"] = erp_dm_readdoc
        if erp_logviewdoc is not UNSET:
            field_dict["ERP_LOGVIEWDOC"] = erp_logviewdoc
        if erp_logeradoc is not UNSET:
            field_dict["ERP_LOGERADOC"] = erp_logeradoc
        if erp_loglastmessage is not UNSET:
            field_dict["ERP_LOGLASTMESSAGE"] = erp_loglastmessage
        if erp_logaspectdata is not UNSET:
            field_dict["ERP_LOGASPECTDATA"] = erp_logaspectdata
        if erp_error is not UNSET:
            field_dict["ERP_ERROR"] = erp_error
        if erp_logkeydata is not UNSET:
            field_dict["ERP_LOGKEYDATA"] = erp_logkeydata
        if erp_createflowtempl is not UNSET:
            field_dict["ERP_CREATEFLOWTEMPL"] = erp_createflowtempl
        if erp_delvert is not UNSET:
            field_dict["ERP_DELVERT"] = erp_delvert
        if erp_loguserdata is not UNSET:
            field_dict["ERP_LOGUSERDATA"] = erp_loguserdata
        if erp_receiveflow is not UNSET:
            field_dict["ERP_RECEIVEFLOW"] = erp_receiveflow
        if erp_showsor is not UNSET:
            field_dict["ERP_SHOWSOR"] = erp_showsor
        if erp_checkout is not UNSET:
            field_dict["ERP_CHECKOUT"] = erp_checkout

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        erp_logopenarc = d.pop("ERP_LOGOPENARC", UNSET)

        erp_delflowtempl = d.pop("ERP_DELFLOWTEMPL", UNSET)

        erp_norepdata = d.pop("ERP_NOREPDATA", UNSET)

        erp_logchangekind = d.pop("ERP_LOGCHANGEKIND", UNSET)

        erp_writesession = d.pop("ERP_WRITESESSION", UNSET)

        erp_logcreatedoc = d.pop("ERP_LOGCREATEDOC", UNSET)

        erp_logcomplain = d.pop("ERP_LOGCOMPLAIN", UNSET)

        erp_flowtimelimt = d.pop("ERP_FLOWTIMELIMT", UNSET)

        erp_logerasor = d.pop("ERP_LOGERASOR", UNSET)

        erp_logmovedoc = d.pop("ERP_LOGMOVEDOC", UNSET)

        erp_logmaskdata = d.pop("ERP_LOGMASKDATA", UNSET)

        erp_postbox = d.pop("ERP_POSTBOX", UNSET)

        erp_logeditdata = d.pop("ERP_LOGEDITDATA", UNSET)

        erp_logfirstmessage = d.pop("ERP_LOGFIRSTMESSAGE", UNSET)

        erp_logrefdoc = d.pop("ERP_LOGREFDOC", UNSET)

        erp_logeraref = d.pop("ERP_LOGERAREF", UNSET)

        erp_logpathdata = d.pop("ERP_LOGPATHDATA", UNSET)

        erp_flowerroryesno = d.pop("ERP_FLOWERRORYESNO", UNSET)

        erp_logcolordata = d.pop("ERP_LOGCOLORDATA", UNSET)

        erp_removevert = d.pop("ERP_REMOVEVERT", UNSET)

        erp_forwardflow = d.pop("ERP_FORWARDFLOW", UNSET)

        erp_pickpost = d.pop("ERP_PICKPOST", UNSET)

        erp_logcreatesor = d.pop("ERP_LOGCREATESOR", UNSET)

        erp_logattachment = d.pop("ERP_LOGATTACHMENT", UNSET)

        erp_logmovesor = d.pop("ERP_LOGMOVESOR", UNSET)

        erp_checkin = d.pop("ERP_CHECKIN", UNSET)

        erp_search = d.pop("ERP_SEARCH", UNSET)

        erp_convert_format = d.pop("ERP_CONVERT_FORMAT", UNSET)

        erp_logrefsor = d.pop("ERP_LOGREFSOR", UNSET)

        erp_delflowactive = d.pop("ERP_DELFLOWACTIVE", UNSET)

        erp_wv = d.pop("ERP_WV", UNSET)

        erp_verschieden = d.pop("ERP_VERSCHIEDEN", UNSET)

        erp_setvert = d.pop("ERP_SETVERT", UNSET)

        erp_custom = d.pop("ERP_CUSTOM", UNSET)

        erp_newvert = d.pop("ERP_NEWVERT", UNSET)

        erp_delversion = d.pop("ERP_DELVERSION", UNSET)

        erp_editflowtempl = d.pop("ERP_EDITFLOWTEMPL", UNSET)

        erp_logdeldocs = d.pop("ERP_LOGDELDOCS", UNSET)

        erp_logchangepwd = d.pop("ERP_LOGCHANGEPWD", UNSET)

        erp_startflow = d.pop("ERP_STARTFLOW", UNSET)

        erp_editflowactive = d.pop("ERP_EDITFLOWACTIVE", UNSET)

        erp_substitutions = d.pop("ERP_SUBSTITUTIONS", UNSET)

        erp_resetvert = d.pop("ERP_RESETVERT", UNSET)

        erp_logclosearc = d.pop("ERP_LOGCLOSEARC", UNSET)

        erp_showdoc = d.pop("ERP_SHOWDOC", UNSET)

        erp_logeditdoc = d.pop("ERP_LOGEDITDOC", UNSET)

        erp_freevert = d.pop("ERP_FREEVERT", UNSET)

        erp_logchangekey = d.pop("ERP_LOGCHANGEKEY", UNSET)

        erp_postbarcode = d.pop("ERP_POSTBARCODE", UNSET)

        erp_dm_readdoc = d.pop("ERP_DM_READDOC", UNSET)

        erp_logviewdoc = d.pop("ERP_LOGVIEWDOC", UNSET)

        erp_logeradoc = d.pop("ERP_LOGERADOC", UNSET)

        erp_loglastmessage = d.pop("ERP_LOGLASTMESSAGE", UNSET)

        erp_logaspectdata = d.pop("ERP_LOGASPECTDATA", UNSET)

        erp_error = d.pop("ERP_ERROR", UNSET)

        erp_logkeydata = d.pop("ERP_LOGKEYDATA", UNSET)

        erp_createflowtempl = d.pop("ERP_CREATEFLOWTEMPL", UNSET)

        erp_delvert = d.pop("ERP_DELVERT", UNSET)

        erp_loguserdata = d.pop("ERP_LOGUSERDATA", UNSET)

        erp_receiveflow = d.pop("ERP_RECEIVEFLOW", UNSET)

        erp_showsor = d.pop("ERP_SHOWSOR", UNSET)

        erp_checkout = d.pop("ERP_CHECKOUT", UNSET)

        report_options_c = cls(
            erp_logopenarc=erp_logopenarc,
            erp_delflowtempl=erp_delflowtempl,
            erp_norepdata=erp_norepdata,
            erp_logchangekind=erp_logchangekind,
            erp_writesession=erp_writesession,
            erp_logcreatedoc=erp_logcreatedoc,
            erp_logcomplain=erp_logcomplain,
            erp_flowtimelimt=erp_flowtimelimt,
            erp_logerasor=erp_logerasor,
            erp_logmovedoc=erp_logmovedoc,
            erp_logmaskdata=erp_logmaskdata,
            erp_postbox=erp_postbox,
            erp_logeditdata=erp_logeditdata,
            erp_logfirstmessage=erp_logfirstmessage,
            erp_logrefdoc=erp_logrefdoc,
            erp_logeraref=erp_logeraref,
            erp_logpathdata=erp_logpathdata,
            erp_flowerroryesno=erp_flowerroryesno,
            erp_logcolordata=erp_logcolordata,
            erp_removevert=erp_removevert,
            erp_forwardflow=erp_forwardflow,
            erp_pickpost=erp_pickpost,
            erp_logcreatesor=erp_logcreatesor,
            erp_logattachment=erp_logattachment,
            erp_logmovesor=erp_logmovesor,
            erp_checkin=erp_checkin,
            erp_search=erp_search,
            erp_convert_format=erp_convert_format,
            erp_logrefsor=erp_logrefsor,
            erp_delflowactive=erp_delflowactive,
            erp_wv=erp_wv,
            erp_verschieden=erp_verschieden,
            erp_setvert=erp_setvert,
            erp_custom=erp_custom,
            erp_newvert=erp_newvert,
            erp_delversion=erp_delversion,
            erp_editflowtempl=erp_editflowtempl,
            erp_logdeldocs=erp_logdeldocs,
            erp_logchangepwd=erp_logchangepwd,
            erp_startflow=erp_startflow,
            erp_editflowactive=erp_editflowactive,
            erp_substitutions=erp_substitutions,
            erp_resetvert=erp_resetvert,
            erp_logclosearc=erp_logclosearc,
            erp_showdoc=erp_showdoc,
            erp_logeditdoc=erp_logeditdoc,
            erp_freevert=erp_freevert,
            erp_logchangekey=erp_logchangekey,
            erp_postbarcode=erp_postbarcode,
            erp_dm_readdoc=erp_dm_readdoc,
            erp_logviewdoc=erp_logviewdoc,
            erp_logeradoc=erp_logeradoc,
            erp_loglastmessage=erp_loglastmessage,
            erp_logaspectdata=erp_logaspectdata,
            erp_error=erp_error,
            erp_logkeydata=erp_logkeydata,
            erp_createflowtempl=erp_createflowtempl,
            erp_delvert=erp_delvert,
            erp_loguserdata=erp_loguserdata,
            erp_receiveflow=erp_receiveflow,
            erp_showsor=erp_showsor,
            erp_checkout=erp_checkout,
        )

        report_options_c.additional_properties = d
        return report_options_c

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
