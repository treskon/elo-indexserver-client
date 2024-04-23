from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportInfoC")


@_attrs_define
class ReportInfoC:
    """Report information.
    <p>
     Indexserver writes the following report entries
     </p>
     <table border="2">
     <tr>
     <td>ReportInfo.action</td>
     <td>ReportInfo.objId</td>
     <td>ReportInfo.extra1</td>
     <td>ReportInfo.extra2</td>
     <td>ReportInfo.comment</td>
     </tr>
     <tr>
     <td>ACT_IX_LOGIN</td>
     <td>0</td>
     <td>SSO User ID</td>
     <td>[EXTRA2_SSO_LOGIN]</td>
     <td>Computer name</td>
     </tr>
     <tr>
     <td>ACT_IX_LOGOUT</td>
     <td>0</td>
     <td>0</td>
     <td>0</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_LOCK_ARCHIVE</td>
     <td>0</td>
     <td>Key ID</td>
     <td>0</td>
     <td>Key name</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_USER</td>
     <td>0</td>
     <td>User ID</td>
     <td>User Flags</td>
     <td>User name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_USER</td>
     <td>0</td>
     <td>User ID</td>
     <td>User Flags</td>
     <td>User name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_USER</td>
     <td>0</td>
     <td>User ID</td>
     <td>User Flags</td>
     <td>User name</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_KEY</td>
     <td>0</td>
     <td>Key ID</td>
     <td>0</td>
     <td>Key name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_KEY</td>
     <td>0</td>
     <td>Key ID</td>
     <td>0</td>
     <td>Key name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_KEY</td>
     <td>0</td>
     <td>Key ID</td>
     <td>0</td>
     <td>Key name</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_SORD</td>
     <td>Object ID</td>
     <td>Object type</td>
     <td>Storage mask ID</td>
     <td>Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKOUT_SORD</td>
     <td>Object ID</td>
     <td>0</td>
     <td>combination of EXTRA2_*</td>
     <td>Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_SORD</td>
     <td>Object ID</td>
     <td>0</td>
     <td>combination of EXTRA2_*</td>
     <td>Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_SORD</td>
     <td>Object ID</td>
     <td>Object type</td>
     <td>combination of EXTRA2_*</td>
     <td>Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_REFERENCE</td>
     <td>Object ID</td>
     <td>Parent ID</td>
     <td>combination of EXTRA2_*</td>
     <td>Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_COPY_SORD</td>
     <td>unsupported</td>
     <td></td>
     <td></td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_REFERENCE_SORD</td>
     <td>Parent ID</td>
     <td>Object ID</td>
     <td></td>
     <td>Parent name, Object name</td>
     </tr>
     <tr>
     <td>ACT_IX_MOVE_SORD</td>
     <td>New parent ID</td>
     <td>Object ID</td>
     <td>Old parent ID</td>
     <td>New parent name, old parent name, Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_LINK_SORD</td>
     <td>From object ID</td>
     <td>To object ID</td>
     <td></td>
     <td>From Sord name, To Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_UNLINK_SORD</td>
     <td>From object ID</td>
     <td>To object ID</td>
     <td></td>
     <td>From Sord name, To Sord name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKOUT_DOCVERSION</td>
     <td>Object ID</td>
     <td>Document version ID</td>
     <td>combination of EXTRA2_*</td>
     <td>Objektname, Versionsnummer</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_DOCVERSION</td>
     <td>Objekt-ID</td>
     <td>Doc-ID</td>
     <td>combination of EXTRA2_*</td>
     <td>Objektname, Versionsnummer</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_DOC_MASK</td>
     <td>0</td>
     <td>Mask-ID</td>
     <td>0</td>
     <td>Maskname</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_DOC_MASK</td>
     <td>0</td>
     <td>Mask-ID</td>
     <td>0</td>
     <td>Maskname</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_DOC_MASK</td>
     <td>0</td>
     <td>Mask-ID</td>
     <td>replace with Mask-ID</td>
     <td>Maskname</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_REPL_NAME</td>
     <td>0</td>
     <td>Repl-ID</td>
     <td>0</td>
     <td>ReplSet-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_REPORT_OPTIONS</td>
     <td>0</td>
     <td>0</td>
     <td>0</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_REPORT</td>
     <td>0</td>
     <td>endDate</td>
     <td>0</td>
     <td>TS-End-Date</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_COLOR</td>
     <td>0</td>
     <td>Color-ID</td>
     <td>rgb</td>
     <td>Color-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_USER_PROFILE</td>
     <td>0</td>
     <td>For User-ID</td>
     <td>0</td>
     <td>User-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_USER_PROFILE</td>
     <td>0</td>
     <td>For User-ID</td>
     <td>0</td>
     <td>User-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_WORKFLOW</td>
     <td>0</td>
     <td>Workflow-ID</td>
     <td>combination of EXTRA2_*</td>
     <td>Workflow-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_WORKFLOW</td>
     <td>0</td>
     <td>Workflow-ID</td>
     <td>combination of EXTRA2_*</td>
     <td>Workflow-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_WORKFLOW</td>
     <td>0</td>
     <td>Workflow-ID</td>
     <td>combination of EXTRA2_*</td>
     <td>Workflow name</td>
     </tr>
     <tr>
     <td>ACT_IX_EDIT_WORKFLOW_NODE</td>
     <td>Object-ID</td>
     <td>Workflow-ID</td>
     <td>Node-ID</td>
     <td>Node name</td>
     </tr>
     <tr>
     <td>ACT_IX_START_WORKFLOW</td>
     <td>Object-ID</td>
     <td>Workflow-ID</td>
     <td>Template-WF-ID</td>
     <td>Workflow name</td>
     </tr>
     <tr>
     <td>ACT_IX_START_ADHOC_WORKFLOW</td>
     <td>Object-ID</td>
     <td>Workflow-ID</td>
     <td>0</td>
     <td>Workflow name</td>
     </tr>
     <tr>
     <td>ACT_IX_TERMINATE_WORKFLOW</td>
     <td>Object-ID</td>
     <td>Workflow-ID</td>
     <td>0</td>
     <td>Workflow-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_CONFIG_FILE</td>
     <td>0</td>
     <td>0</td>
     <td>0</td>
     <td>Config file name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_CONFIG_FILE</td>
     <td>0</td>
     <td>0</td>
     <td>0</td>
     <td>Config file name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_COUNTER</td>
     <td>0</td>
     <td>Value</td>
     <td>0</td>
     <td>Counter-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_COUNTER</td>
     <td>0</td>
     <td>0</td>
     <td>0</td>
     <td>Counter-Name</td>
     </tr>
     <tr>
     <td>ACT_IX_INCREMENT_COUNTER</td>
     <td>0</td>
     <td>Value</td>
     <td>0</td>
     <td>Counter name</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_SORD_TYPE</td>
     <td>0</td>
     <td>ID (Sord.type)</td>
     <td>0</td>
     <td>Type name</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_SORD_TYPE</td>
     <td>0</td>
     <td>ID (Sord.type)</td>
     <td>0</td>
     <td>Type name</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_NOTE</td>
     <td>Objekt-ID</td>
     <td>Note-ID (internal)</td>
     <td>combination of EXTRA2_*</td>
     <td>Note-Guid</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_NOTE</td>
     <td>Objekt-ID</td>
     <td>Note-ID (internal)</td>
     <td>combination of EXTRA2_*</td>
     <td>Note-Guid</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_NOTE</td>
     <td>Objekt-ID</td>
     <td>Note-ID (internal)</td>
     <td>combination of EXTRA2_*</td>
     <td>Note-Guid</td>
     </tr>
     <tr>
     <td>ACT_DM_READDOC</td>
     <td>Objekt-ID</td>
     <td>Doc-ID</td>
     <td>0</td>
     <td>&nbsp;</td>
     </tr>

     <tr>
     <td>ACT_IX_SUBSTITUTION_NEW</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_CHANGE</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_DELETE</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_ACTIVATE</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_DEACTIVATE</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>&nbsp;</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_TRANSFER</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>previous substituteId</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_FORWARD</td>
     <td>0</td>
     <td>{@link Substitution#userId}</td>
     <td>{@link Substitution#substituteId}</td>
     <td>previous substituteId</td>
     </tr>

     </table>

     <p>
     To enable or disable reporting of actions, action codes have to be transformed into ERP codes
     first. One ERP code can subsume serverel action codes. The ERP codes can be used in
     checkinReportOptions to manipulate reporting. Furthermore they can be used in
     findFirstReportInfos, FindReportInfo, to search for reported actions. The following table shows
     how actions codes are mapped to report options.
     </p>

     <table border="2">
     <tr>
     <td>Action code, ReportInfoC</td>
     <td>ERP code, ReportOptionsC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_ELOSTART</td>
     <td>ERP_LOGOPENARC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_ELOEND</td>
     <td>ERP_LOGCLOSEARC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_COMPLAIN</td>
     <td>ERP_LOGCOMPLAIN</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_DELETEDOCS</td>
     <td>ERP_LOGERADOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_KEYCHANGED</td>
     <td>ERP_LOGCHANGEKEY</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_USERCHANGED</td>
     <td>ERP_LOGUSERDATA</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_COLORCHANGED</td>
     <td>ERP_LOGCHANGEKIND</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_PATHCHANGED</td>
     <td>ERP_LOGPATHDATA</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_MASKCHANGED</td>
     <td>ERP_LOGMASKDATA</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_PWDCHANGED</td>
     <td>ERP_LOGCHANGEPWD</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CREATEDOC</td>
     <td>ERP_LOGCREATEDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_EDITDOC</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHANGEDOC</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHANGEATTACH</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_VIEWDOC</td>
     <td>ERP_LOGVIEWDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_ERASEDOC</td>
     <td>ERP_LOGERADOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_MOVEDOC</td>
     <td>ERP_LOGMOVEDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_REFDOC</td>
     <td>ERP_LOGREFDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHANGEKEY</td>
     <td>ERP_LOGCHANGEKEY</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHANGEKIND</td>
     <td>ERP_LOGCHANGEKIND</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CONVERT_FORMAT</td>
     <td>ERP_CONVERT_FORMAT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHECKOUT</td>
     <td>ERP_CHECKOUT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHECKIN</td>
     <td>ERP_CHECKIN</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CREATESOR</td>
     <td>ERP_LOGCREATESOR</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CHANGESOR</td>
     <td>ERP_LOGEDITDATA</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_EDITSOR</td>
     <td>ERP_LOGEDITDATA</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_ERASESOR</td>
     <td>ERP_LOGERASOR</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_MOVESOR</td>
     <td>ERP_LOGMOVESOR</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_REFSOR</td>
     <td>ERP_LOGREFSOR</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_ADDREF</td>
     <td>ERP_LOGREFDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_ERASEREF</td>
     <td>ERP_LOGERAREF</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_MOVEREF</td>
     <td>ERP_LOGMOVEDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVNEW</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVCHANGE</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVDELETE</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVSEND</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVRECEIVE</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVNEWSEND</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_WVCHANGESEND</td>
     <td>ERP_WV</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTFIRST</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTDELETE</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTDOCBUILD</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTEDIT</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTSCHLAGWORT</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTCOPYTO</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTMOVETO</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTMOVE</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTCOLLECT</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTNEWOLE</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTEXPAND</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTIMPORT</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_POSTLAST</td>
     <td>ERP_POSTBOX</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_CREATEFLOWTEMPL</td>
     <td>ERP_CREATEFLOWTEMPL</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_EDITFLOWTEMPL</td>
     <td>ERP_EDITFLOWTEMPL</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_DELFLOWTEMPL</td>
     <td>ERP_DELFLOWTEMPL</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_STARTFLOW</td>
     <td>ERP_STARTFLOW</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_RECEIVEFLOW</td>
     <td>ERP_RECEIVEFLOW</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_FORWARDFLOW</td>
     <td>ERP_FORWARDFLOW</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_EDITFLOWACTIVE</td>
     <td>ERP_EDITFLOWACTIVE</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_DELFLOWACTIVE</td>
     <td>ERP_DELFLOWACTIVE</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_FLOWTIMELIMIT</td>
     <td>ERP_FLOWTIMELIMT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_FLOWERRORYESNO</td>
     <td>ERP_FLOWERRORYESNO</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_REPORTCHANGED</td>
     <td>ERP_VERSCHIEDEN</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_MASKTEXTTOOLONG</td>
     <td>ERP_VERSCHIEDEN</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_NEWVERT</td>
     <td>ERP_NEWVERT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_DELVERT</td>
     <td>ERP_DELVERT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_FREEVERT</td>
     <td>ERP_FREEVERT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_REMOVEVERT</td>
     <td>ERP_REMOVEVERT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_SETVERT</td>
     <td>ERP_SETVERT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_RESETVERT</td>
     <td>ERP_RESETVERT</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_SHOWDOC</td>
     <td>ERP_SHOWDOC</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_SHOWSOR</td>
     <td>ERP_SHOWSOR</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_DELVERSION</td>
     <td>ERP_DELVERSION</td>
     </tr>
     <tr>
     <td>ACT_CLIENT_PICKPOST</td>
     <td>ERP_PICKPOST</td>
     </tr>
     <tr>
     <td>ACT_DM_READDOC</td>
     <td>ERP_LOGVIEWDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_LOGIN</td>
     <td>ERP_LOGOPENARC</td>
     </tr>
     <tr>
     <td>ACT_IX_LOGOUT</td>
     <td>ERP_LOGCLOSEARC</td>
     </tr>
     <tr>
     <td>ACT_IX_LOCK_ARCHIVE</td>
     <td>ERP_LOGCHANGEKEY</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_USER</td>
     <td>ERP_LOGUSERDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_USER</td>
     <td>ERP_LOGUSERDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_USER</td>
     <td>ERP_LOGUSERDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_KEY</td>
     <td>ERP_LOGCHANGEKEY</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_KEY</td>
     <td>ERP_LOGCHANGEKEY</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_KEY</td>
     <td>ERP_LOGCHANGEKEY</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_SORD</td>
     <td>ERP_LOGCREATEDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKOUT_SORD</td>
     <td>ERP_LOGVIEWDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_SORD</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_SORD</td>
     <td>ERP_LOGERADOC</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_REFERENCE</td>
     <td>ERP_LOGERAREF</td>
     </tr>
     <tr>
     <td>ACT_IX_COPY_SORD</td>
     <td>ERP_LOGCREATEDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_REFERENCE_SORD</td>
     <td>ERP_LOGREFDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_MOVE_SORD</td>
     <td>ERP_LOGMOVEDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_LINK_SORD</td>
     <td>ERP_LOGREFDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_UNLINK_SORD</td>
     <td>ERP_LOGREFDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKOUT_DOCVERSION</td>
     <td>ERP_LOGVIEWDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_DOCVERSION</td>
     <td>ERP_CHECKIN</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_DOC_MASK</td>
     <td>ERP_LOGMASKDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_DOC_MASK</td>
     <td>ERP_LOGMASKDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_DOC_MASK</td>
     <td>ERP_LOGMASKDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_REPL_NAME</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_REPORT_OPTIONS</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_REPORT</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_COLOR</td>
     <td>ERP_LOGCOLORDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_USER_PROFILE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_USER_PROFILE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_WORKFLOW</td>
     <td>ERP_CREATEFLOWTEMPL</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_WORKFLOW</td>
     <td>ERP_EDITFLOWTEMPL</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_WORKFLOW</td>
     <td>ERP_DELFLOWTEMPL</td>
     </tr>
     <tr>
     <td>ACT_IX_EDIT_WORKFLOW_NODE</td>
     <td>ERP_FORWARDFLOW</td>
     </tr>
     <tr>
     <td>ACT_IX_START_WORKFLOW</td>
     <td>ERP_STARTFLOW</td>
     </tr>
     <tr>
     <td>ACT_IX_START_ADHOC_WORKFLOW</td>
     <td>ERP_STARTFLOW</td>
     </tr>
     <tr>
     <td>ACT_IX_TERMINATE_WORKFLOW</td>
     <td>ERP_FORWARDFLOW</td>
     </tr>
     <tr>
     <td>ACT_IX_TAKE_WORKFLOW_NODE</td>
     <td>ERP_FORWARDFLOW</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_CONFIG_FILE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_CONFIG_FILE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_COUNTER</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_COUNTER</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_INCREMENT_COUNTER</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_SORD_TYPE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_SORD_TYPE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CREATE_NOTE</td>
     <td>ERP_LOGKEYDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_NOTE</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKOUT_NOTE</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_NOTE</td>
     <td>ERP_LOGEDITDOC</td>
     </tr>
     <tr>
     <td>ACT_IX_NEWVERT</td>
     <td>ERP_NEWVERT</td>
     </tr>
     <tr>
     <td>ACT_IX_DELVERT</td>
     <td>ERP_DELVERT</td>
     </tr>
     <tr>
     <td>ACT_IX_FREEVERT</td>
     <td>ERP_FREEVERT</td>
     </tr>
     <tr>
     <td>ACT_IX_REMOVEVERT</td>
     <td>ERP_REMOVEVERT</td>
     </tr>
     <tr>
     <td>ACT_IX_SETVERT</td>
     <td>ERP_SETVERT</td>
     </tr>
     <tr>
     <td>ACT_IX_RESETVERT</td>
     <td>ERP_RESETVERT</td>
     </tr>
     <tr>
     <td>ACT_DM_READDOC</td>
     <td>ERP_DM_READDOC</td>
     </tr>

     <tr>
     <td>ACT_IX_SUBSTITUTION_NEW</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_CHANGE</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_DELETE</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_ACTIVATE</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_DEACTIVATE</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_TRANSFER</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>
     <tr>
     <td>ACT_IX_SUBSTITUTION_FORWARD</td>
     <td>ERP_SUBSTITUTIONS</td>
     </tr>

     <tr>
     <td>ACT_IX_CREATE_ASPECT</td>
     <td>ERP_LOGASPECTDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_CHECKIN_ASPECT</td>
     <td>ERP_LOGASPECTDATA</td>
     </tr>
     <tr>
     <td>ACT_IX_DELETE_ASPECT</td>
     <td>ERP_LOGASPECTDATA</td>
     </tr>
     *
     </table>

        Attributes:
            act_client_refdoc (Union[Unset, int]): unused
            extra2_note_personal (Union[Unset, int]):
            act_ix_take_workflow_node (Union[Unset, int]):
            act_client_viewdoc (Union[Unset, int]): Read the indexing information of a document.
            act_client_masktexttoolong (Union[Unset, int]): unused
            extra2_wf_finished (Union[Unset, int]):
            act_ix_substitution_activate (Union[Unset, int]): A substitution is activated with {@link
                IXServicePortIF#activateSubstitution(ClientInfo, String, LockZ)}.
                <p>
                 The following values in {@link ReportInfo} are set:<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>

                 <p>
                 Overrides {@link #ACT_IX_SETVERT}
                 </p>
            act_ix_delete_aspect (Union[Unset, int]):
            act_client_deletenote (Union[Unset, int]): Delete note.
            act_ix_delete_user (Union[Unset, int]):
            extra2_sso_login (Union[Unset, int]):
            act_client_editnote (Union[Unset, int]): Overwrite note.
            act_client_convert_format (Union[Unset, int]): unused
            act_client_postfirst (Union[Unset, int]): unused
            act_client_createflowtempl (Union[Unset, int]): unused
            act_ix_create_note (Union[Unset, int]):
            act_ix_checkin_config_file (Union[Unset, int]):
            act_client_createsor (Union[Unset, int]): Create new Sord object
            act_ix_substitution_delete (Union[Unset, int]): A substitution is deleted with
                {@link IXServicePortIF#deleteSubstitutions(ClientInfo, de.elo.ix.client.subs.DeleteSubstitutionsInfo, LockZ)}

                 <p>
                 The following values in {@link ReportInfo} are set:<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>

                 <p>
                 Overrides {@link #ACT_IX_DELVERT}
                 </p>
            act_client_postedit (Union[Unset, int]): unused
            act_ix_delete_counter (Union[Unset, int]):
            act_ix_create_user (Union[Unset, int]):
            extra2_note_stamp (Union[Unset, int]):
            act_client_wvchangesend (Union[Unset, int]): unused
            act_client_colorchanged (Union[Unset, int]): unused
            act_client_checkout (Union[Unset, int]): Get document file for editing.
                This report information is written, if
                 IXServicePortIF.checkoutDoc is called with lock.
            act_ix_substitution_transfer (Union[Unset, int]): A substitution is transfered with
                {@link IXServicePortIF#forwardSubstitution(ClientInfo, de.elo.ix.client.subs.ForwardSubstitutionInfo, LockZ)}.

                 <p>
                 The following values in {@link ReportInfo} are set (of the new Substitution object):<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#text} = former substitute id<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>
            act_client_delversion (Union[Unset, int]):
            act_ix_checkin_workflow (Union[Unset, int]):
            act_ix_mini_app_login (Union[Unset, int]): Reporteintrag für Mini-App-Login.
                RID11587
            act_ix_create_workflow (Union[Unset, int]):
            act_ix_newvert (Union[Unset, int]):
            act_client_wvchange (Union[Unset, int]): unused
            act_client_startflow (Union[Unset, int]): unused
            extra2_wf_active (Union[Unset, int]):
            act_client_resetvert (Union[Unset, int]): unused
            act_client_maskchanged (Union[Unset, int]): unused
            act_client_postreceive (Union[Unset, int]): unused
            act_ix_move_sord (Union[Unset, int]):
            act_ix_checkin_key (Union[Unset, int]):
            act_iswritesession (Union[Unset, int]): Used to report a write access session.
            act_ix_link_sord (Union[Unset, int]):
            act_client_showsor (Union[Unset, int]): unused
            act_client_delvert (Union[Unset, int]): unused
            mb_comment (Union[Unset, str]):
            act_ix_checkin_doc_mask (Union[Unset, int]):
            act_client_editflowtempl (Union[Unset, int]): unused
            extra2_signature (Union[Unset, int]):
            act_client_deletedocs (Union[Unset, int]): unused
            act_client_postschlagwort (Union[Unset, int]): unused
            act_ix_first (Union[Unset, int]): Indexserver specific report codes are higher than ACT_IX_FIRST
            act_ix_create_document (Union[Unset, int]):
            extra2_force (Union[Unset, int]):
            act_ix_copy_sord (Union[Unset, int]):
            act_client_postimport (Union[Unset, int]): unused
            act_client_postmove (Union[Unset, int]): unused
            act_ix_delete_note (Union[Unset, int]):
            act_ix_resetvert (Union[Unset, int]):
            act_client_eraseref (Union[Unset, int]): Delete/undelete document.
                <table border="2">
                 <tr>
                 <td>ReportInfo.extra1</td>
                 <td>parent ID.</td>
                 </tr>
                 <tr>
                 <td>ReportInfo.extra2</td>
                 <td>0 if deleted, 1 if undeleted.</td>
                 </tr>
                 </table>
            act_ix_login (Union[Unset, int]):
            act_ix_checkin_user_profile (Union[Unset, int]):
            act_client_erasesor (Union[Unset, int]): Delete/undelete document.
                <table border="2">
                 <tr>
                 <td>ReportInfo.extra1</td>
                 <td>parent ID.</td>
                 </tr>
                 <tr>
                 <td>ReportInfo.extra2</td>
                 <td>0 if deleted, 1 if undeleted.</td>
                 </tr>
                 <tr>
                 <td>ReportInfo.text</td>
                 <td>sord name.</td>
                 </tr>
                 </table>
            act_ix_checkout_docversion (Union[Unset, int]):
            act_client_postcollect (Union[Unset, int]): unused
            act_ix_checkin_user (Union[Unset, int]):
            act_client_keychanged (Union[Unset, int]): unused
            act_ix_start_workflow (Union[Unset, int]):
            act_ix_reference_sord (Union[Unset, int]):
            extra2_note_normal (Union[Unset, int]):
            act_dm_readdoc (Union[Unset, int]): Read document file from DM.
            extra2_wf_terminate (Union[Unset, int]):
            act_ix_checkin_repl_name (Union[Unset, int]):
            act_client_postexpand (Union[Unset, int]): unused
            act_client_editdoc (Union[Unset, int]): Write the indexing information of a document.
            act_client_postdocbuild (Union[Unset, int]): unused
            act_client_postcopyto (Union[Unset, int]): unused
            act_ix_increment_counter (Union[Unset, int]):
            act_ix_checkin_sord_type (Union[Unset, int]):
            act_client_wvfirst (Union[Unset, int]): unused
            act_ix_create_doc_mask (Union[Unset, int]):
            extra2_preview (Union[Unset, int]):
            act_client_elostart (Union[Unset, int]): Login.
            act_ix_checkin_docversion (Union[Unset, int]):
            act_client_checkin (Union[Unset, int]): Checkin a new document file. ReportInfo.
                extra1 ist set to the new document ID
            act_client_pwdchanged (Union[Unset, int]): unused
            act_ix_delete_user_profile (Union[Unset, int]):
            act_ix_checkin_note (Union[Unset, int]):
            act_ix_delegate_workflow (Union[Unset, int]):
            act_ix_delvert (Union[Unset, int]):
            act_ix_substitution_change (Union[Unset, int]): An existing substitution is changed with
                {@link IXServicePortIF#checkinSubstitutions(ClientInfo, de.elo.ix.client.subs.CheckinSubstitutionsInfo,
                de.elo.ix.client.subs.SubstitutionZ, LockZ)}

                 <p>
                 The following values in {@link ReportInfo} are set:<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>
            act_ix_create_aspect (Union[Unset, int]):
            act_client_editsor (Union[Unset, int]): Edited new Sord object
            extra2_annotation_note (Union[Unset, int]):
            extra2_indexsearch (Union[Unset, int]):
            act_ix_change_acl (Union[Unset, int]):
            act_ix_change_deldate (Union[Unset, int]):
            act_ix_substitution_new (Union[Unset, int]): A new substitution is checked in with
                {@link IXServicePortIF#checkinSubstitutions(ClientInfo, de.elo.ix.client.subs.CheckinSubstitutionsInfo,
                de.elo.ix.client.subs.SubstitutionZ, LockZ)}

                 <p>
                 The following values in {@link ReportInfo} are set:<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>

                 <p>
                 Overrides {@link #ACT_IX_NEWVERT}
                 </p>
            act_custom_first (Union[Unset, int]): Custom client specific report codes are higher than ACT_CUSTOM_FIRST
            act_ix_substitution_forward (Union[Unset, int]): A substitution is forwarded with
                {@link IXServicePortIF#forwardSubstitution(ClientInfo, de.elo.ix.client.subs.ForwardSubstitutionInfo, LockZ)}.

                 <p>
                 The following values in {@link ReportInfo} are set (of the new Substitution object):<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#text} = former substitute id<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>
            act_client_flowtimelimit (Union[Unset, int]): unused
            act_client_postlast (Union[Unset, int]): unused
            act_ix_delete_reference (Union[Unset, int]):
            act_client_delflowtempl (Union[Unset, int]): unused
            act_client_postnewole (Union[Unset, int]): unused
            act_client_delflowactive (Union[Unset, int]): unused
            extra2_lock (Union[Unset, int]):
            act_client_changedoc (Union[Unset, int]): unused
            act_ix_logout (Union[Unset, int]):
            act_client_showdoc (Union[Unset, int]): Get document file to display (not to edit).
                This report information is written, if
                 IXServicePortIF.checkoutDoc is called without lock.
            act_custom_last (Union[Unset, int]): Custom client specific report codes are lower than ACT_CUSTOM_LAST
            extra2_annotation_marker (Union[Unset, int]):
            act_client_wvnewsend (Union[Unset, int]): unused
            act_ix_checkin_sord (Union[Unset, int]):
            act_client_addref (Union[Unset, int]): unused
            act_ix_last (Union[Unset, int]):
            act_client_refsor (Union[Unset, int]): unused
            act_ix_setvert (Union[Unset, int]):
            extra2_docversion (Union[Unset, int]):
            act_client_wvdelete (Union[Unset, int]): unused
            act_client_movesor (Union[Unset, int]): unused
            act_client_wvreceive (Union[Unset, int]): unused
            act_client_createnote (Union[Unset, int]): Create note.
            act_client_pathchanged (Union[Unset, int]): unused
            act_client_userchanged (Union[Unset, int]): unused
            act_client_moveref (Union[Unset, int]): unused
            act_client_wvnew (Union[Unset, int]): unused
            act_ix_terminate_workflow (Union[Unset, int]):
            act_client_reportchanged (Union[Unset, int]): unused
            extra2_wf_template (Union[Unset, int]):
            extra2_all_notes_of_sord (Union[Unset, int]): Extra2 value used when all notes of a Sord are read.
            act_client_postdelete (Union[Unset, int]): unused
            act_ix_delete_doc_mask (Union[Unset, int]):
            extra2_finally (Union[Unset, int]):
            act_client_none (Union[Unset, int]):
            act_ix_delete_key (Union[Unset, int]):
            mb_action (Union[Unset, str]):
            act_ix_checkout_sord (Union[Unset, int]):
            act_ix_unlink_sord (Union[Unset, int]):
            act_client_forwardflow (Union[Unset, int]): unused
            mb_user_name (Union[Unset, str]):
            act_client_changesor (Union[Unset, int]): unused
            act_client_freevert (Union[Unset, int]): unused
            act_ix_lock_archive (Union[Unset, int]):
            mb_act_time_iso (Union[Unset, str]):
            act_client_receiveflow (Union[Unset, int]): unused
            act_ix_delete_sord (Union[Unset, int]):
            act_ix_checkin_counter (Union[Unset, int]):
            act_ix_checkin_color (Union[Unset, int]):
            act_client_search (Union[Unset, int]): Used to report search completed
            act_ix_checkout_note (Union[Unset, int]):
            extra2_report_as_login (Union[Unset, int]):
            act_ix_delete_sord_type (Union[Unset, int]):
            act_ix_delete_report (Union[Unset, int]):
            act_ix_checkin_aspect (Union[Unset, int]):
            act_client_changeattach (Union[Unset, int]): unused
            act_client_viewsor (Union[Unset, int]): Checkout Sord object without lock
            act_client_editflowactive (Union[Unset, int]): unused
            act_ix_checkin_report_options (Union[Unset, int]):
            act_ix_edit_workflow_node (Union[Unset, int]):
            act_client_postmoveto (Union[Unset, int]): unused
            act_ix_start_adhoc_workflow (Union[Unset, int]):
            act_ix_removevert (Union[Unset, int]):
            act_client_wvsend (Union[Unset, int]): unused
            act_client_changekind (Union[Unset, int]): unused
            act_ix_create_sord (Union[Unset, int]):
            act_ix_substitution_deactivate (Union[Unset, int]): A substitution is deactivated with {@link
                IXServicePortIF#deactivateSubstitution(ClientInfo, String, LockZ)}
                <p>
                 The following values in {@link ReportInfo} are set:<br>
                 {@link ReportInfo#extra1} = {@link Substitution#userId}<br>
                 {@link ReportInfo#extra2} = {@link Substitution#substituteId}<br>
                 {@link ReportInfo#extraInfo} = {@link Substitution}
                 </p>

                 <p>
                 Overrides {@link #ACT_IX_REMOVEVERT}
                 </p>
            act_client_newvert (Union[Unset, int]): unused
            act_ix_freevert (Union[Unset, int]):
            act_ix_delete_config_file (Union[Unset, int]):
            extra2_attachment (Union[Unset, int]):
            act_client_changekey (Union[Unset, int]): unused
            act_client_createdoc (Union[Unset, int]): Create a new document entry (for indexing information) in the archive
                database. ReportInfo.
                text
                 contains the document name (short description).
            act_client_flowerroryesno (Union[Unset, int]): unused
            act_ix_delete_workflow (Union[Unset, int]):
            act_client_erasedoc (Union[Unset, int]): Delete/undelete document.
                <table border="2">
                 <tr>
                 <td>ReportInfo.extra1</td>
                 <td>parent ID.</td>
                 </tr>
                 <tr>
                 <td>ReportInfo.extra2</td>
                 <td>0 if deleted, 1 if undeleted.</td>
                 </tr>
                 <tr>
                 <td>ReportInfo.text</td>
                 <td>sord name.</td>
                 </tr>
                 </table>
            act_ix_change_rs (Union[Unset, int]):
            act_client_movedoc (Union[Unset, int]): unused
            act_client_pickpost (Union[Unset, int]): unused
            act_client_complain (Union[Unset, int]): unused
            act_client_wvlast (Union[Unset, int]): unused
            act_client_setvert (Union[Unset, int]): unused
            act_client_removevert (Union[Unset, int]): unused
            act_client_eloend (Union[Unset, int]): Logout.
            act_ix_create_key (Union[Unset, int]):
            extra2_wf_cancel (Union[Unset, int]):
    """

    act_client_refdoc: Union[Unset, int] = UNSET
    extra2_note_personal: Union[Unset, int] = UNSET
    act_ix_take_workflow_node: Union[Unset, int] = UNSET
    act_client_viewdoc: Union[Unset, int] = UNSET
    act_client_masktexttoolong: Union[Unset, int] = UNSET
    extra2_wf_finished: Union[Unset, int] = UNSET
    act_ix_substitution_activate: Union[Unset, int] = UNSET
    act_ix_delete_aspect: Union[Unset, int] = UNSET
    act_client_deletenote: Union[Unset, int] = UNSET
    act_ix_delete_user: Union[Unset, int] = UNSET
    extra2_sso_login: Union[Unset, int] = UNSET
    act_client_editnote: Union[Unset, int] = UNSET
    act_client_convert_format: Union[Unset, int] = UNSET
    act_client_postfirst: Union[Unset, int] = UNSET
    act_client_createflowtempl: Union[Unset, int] = UNSET
    act_ix_create_note: Union[Unset, int] = UNSET
    act_ix_checkin_config_file: Union[Unset, int] = UNSET
    act_client_createsor: Union[Unset, int] = UNSET
    act_ix_substitution_delete: Union[Unset, int] = UNSET
    act_client_postedit: Union[Unset, int] = UNSET
    act_ix_delete_counter: Union[Unset, int] = UNSET
    act_ix_create_user: Union[Unset, int] = UNSET
    extra2_note_stamp: Union[Unset, int] = UNSET
    act_client_wvchangesend: Union[Unset, int] = UNSET
    act_client_colorchanged: Union[Unset, int] = UNSET
    act_client_checkout: Union[Unset, int] = UNSET
    act_ix_substitution_transfer: Union[Unset, int] = UNSET
    act_client_delversion: Union[Unset, int] = UNSET
    act_ix_checkin_workflow: Union[Unset, int] = UNSET
    act_ix_mini_app_login: Union[Unset, int] = UNSET
    act_ix_create_workflow: Union[Unset, int] = UNSET
    act_ix_newvert: Union[Unset, int] = UNSET
    act_client_wvchange: Union[Unset, int] = UNSET
    act_client_startflow: Union[Unset, int] = UNSET
    extra2_wf_active: Union[Unset, int] = UNSET
    act_client_resetvert: Union[Unset, int] = UNSET
    act_client_maskchanged: Union[Unset, int] = UNSET
    act_client_postreceive: Union[Unset, int] = UNSET
    act_ix_move_sord: Union[Unset, int] = UNSET
    act_ix_checkin_key: Union[Unset, int] = UNSET
    act_iswritesession: Union[Unset, int] = UNSET
    act_ix_link_sord: Union[Unset, int] = UNSET
    act_client_showsor: Union[Unset, int] = UNSET
    act_client_delvert: Union[Unset, int] = UNSET
    mb_comment: Union[Unset, str] = UNSET
    act_ix_checkin_doc_mask: Union[Unset, int] = UNSET
    act_client_editflowtempl: Union[Unset, int] = UNSET
    extra2_signature: Union[Unset, int] = UNSET
    act_client_deletedocs: Union[Unset, int] = UNSET
    act_client_postschlagwort: Union[Unset, int] = UNSET
    act_ix_first: Union[Unset, int] = UNSET
    act_ix_create_document: Union[Unset, int] = UNSET
    extra2_force: Union[Unset, int] = UNSET
    act_ix_copy_sord: Union[Unset, int] = UNSET
    act_client_postimport: Union[Unset, int] = UNSET
    act_client_postmove: Union[Unset, int] = UNSET
    act_ix_delete_note: Union[Unset, int] = UNSET
    act_ix_resetvert: Union[Unset, int] = UNSET
    act_client_eraseref: Union[Unset, int] = UNSET
    act_ix_login: Union[Unset, int] = UNSET
    act_ix_checkin_user_profile: Union[Unset, int] = UNSET
    act_client_erasesor: Union[Unset, int] = UNSET
    act_ix_checkout_docversion: Union[Unset, int] = UNSET
    act_client_postcollect: Union[Unset, int] = UNSET
    act_ix_checkin_user: Union[Unset, int] = UNSET
    act_client_keychanged: Union[Unset, int] = UNSET
    act_ix_start_workflow: Union[Unset, int] = UNSET
    act_ix_reference_sord: Union[Unset, int] = UNSET
    extra2_note_normal: Union[Unset, int] = UNSET
    act_dm_readdoc: Union[Unset, int] = UNSET
    extra2_wf_terminate: Union[Unset, int] = UNSET
    act_ix_checkin_repl_name: Union[Unset, int] = UNSET
    act_client_postexpand: Union[Unset, int] = UNSET
    act_client_editdoc: Union[Unset, int] = UNSET
    act_client_postdocbuild: Union[Unset, int] = UNSET
    act_client_postcopyto: Union[Unset, int] = UNSET
    act_ix_increment_counter: Union[Unset, int] = UNSET
    act_ix_checkin_sord_type: Union[Unset, int] = UNSET
    act_client_wvfirst: Union[Unset, int] = UNSET
    act_ix_create_doc_mask: Union[Unset, int] = UNSET
    extra2_preview: Union[Unset, int] = UNSET
    act_client_elostart: Union[Unset, int] = UNSET
    act_ix_checkin_docversion: Union[Unset, int] = UNSET
    act_client_checkin: Union[Unset, int] = UNSET
    act_client_pwdchanged: Union[Unset, int] = UNSET
    act_ix_delete_user_profile: Union[Unset, int] = UNSET
    act_ix_checkin_note: Union[Unset, int] = UNSET
    act_ix_delegate_workflow: Union[Unset, int] = UNSET
    act_ix_delvert: Union[Unset, int] = UNSET
    act_ix_substitution_change: Union[Unset, int] = UNSET
    act_ix_create_aspect: Union[Unset, int] = UNSET
    act_client_editsor: Union[Unset, int] = UNSET
    extra2_annotation_note: Union[Unset, int] = UNSET
    extra2_indexsearch: Union[Unset, int] = UNSET
    act_ix_change_acl: Union[Unset, int] = UNSET
    act_ix_change_deldate: Union[Unset, int] = UNSET
    act_ix_substitution_new: Union[Unset, int] = UNSET
    act_custom_first: Union[Unset, int] = UNSET
    act_ix_substitution_forward: Union[Unset, int] = UNSET
    act_client_flowtimelimit: Union[Unset, int] = UNSET
    act_client_postlast: Union[Unset, int] = UNSET
    act_ix_delete_reference: Union[Unset, int] = UNSET
    act_client_delflowtempl: Union[Unset, int] = UNSET
    act_client_postnewole: Union[Unset, int] = UNSET
    act_client_delflowactive: Union[Unset, int] = UNSET
    extra2_lock: Union[Unset, int] = UNSET
    act_client_changedoc: Union[Unset, int] = UNSET
    act_ix_logout: Union[Unset, int] = UNSET
    act_client_showdoc: Union[Unset, int] = UNSET
    act_custom_last: Union[Unset, int] = UNSET
    extra2_annotation_marker: Union[Unset, int] = UNSET
    act_client_wvnewsend: Union[Unset, int] = UNSET
    act_ix_checkin_sord: Union[Unset, int] = UNSET
    act_client_addref: Union[Unset, int] = UNSET
    act_ix_last: Union[Unset, int] = UNSET
    act_client_refsor: Union[Unset, int] = UNSET
    act_ix_setvert: Union[Unset, int] = UNSET
    extra2_docversion: Union[Unset, int] = UNSET
    act_client_wvdelete: Union[Unset, int] = UNSET
    act_client_movesor: Union[Unset, int] = UNSET
    act_client_wvreceive: Union[Unset, int] = UNSET
    act_client_createnote: Union[Unset, int] = UNSET
    act_client_pathchanged: Union[Unset, int] = UNSET
    act_client_userchanged: Union[Unset, int] = UNSET
    act_client_moveref: Union[Unset, int] = UNSET
    act_client_wvnew: Union[Unset, int] = UNSET
    act_ix_terminate_workflow: Union[Unset, int] = UNSET
    act_client_reportchanged: Union[Unset, int] = UNSET
    extra2_wf_template: Union[Unset, int] = UNSET
    extra2_all_notes_of_sord: Union[Unset, int] = UNSET
    act_client_postdelete: Union[Unset, int] = UNSET
    act_ix_delete_doc_mask: Union[Unset, int] = UNSET
    extra2_finally: Union[Unset, int] = UNSET
    act_client_none: Union[Unset, int] = UNSET
    act_ix_delete_key: Union[Unset, int] = UNSET
    mb_action: Union[Unset, str] = UNSET
    act_ix_checkout_sord: Union[Unset, int] = UNSET
    act_ix_unlink_sord: Union[Unset, int] = UNSET
    act_client_forwardflow: Union[Unset, int] = UNSET
    mb_user_name: Union[Unset, str] = UNSET
    act_client_changesor: Union[Unset, int] = UNSET
    act_client_freevert: Union[Unset, int] = UNSET
    act_ix_lock_archive: Union[Unset, int] = UNSET
    mb_act_time_iso: Union[Unset, str] = UNSET
    act_client_receiveflow: Union[Unset, int] = UNSET
    act_ix_delete_sord: Union[Unset, int] = UNSET
    act_ix_checkin_counter: Union[Unset, int] = UNSET
    act_ix_checkin_color: Union[Unset, int] = UNSET
    act_client_search: Union[Unset, int] = UNSET
    act_ix_checkout_note: Union[Unset, int] = UNSET
    extra2_report_as_login: Union[Unset, int] = UNSET
    act_ix_delete_sord_type: Union[Unset, int] = UNSET
    act_ix_delete_report: Union[Unset, int] = UNSET
    act_ix_checkin_aspect: Union[Unset, int] = UNSET
    act_client_changeattach: Union[Unset, int] = UNSET
    act_client_viewsor: Union[Unset, int] = UNSET
    act_client_editflowactive: Union[Unset, int] = UNSET
    act_ix_checkin_report_options: Union[Unset, int] = UNSET
    act_ix_edit_workflow_node: Union[Unset, int] = UNSET
    act_client_postmoveto: Union[Unset, int] = UNSET
    act_ix_start_adhoc_workflow: Union[Unset, int] = UNSET
    act_ix_removevert: Union[Unset, int] = UNSET
    act_client_wvsend: Union[Unset, int] = UNSET
    act_client_changekind: Union[Unset, int] = UNSET
    act_ix_create_sord: Union[Unset, int] = UNSET
    act_ix_substitution_deactivate: Union[Unset, int] = UNSET
    act_client_newvert: Union[Unset, int] = UNSET
    act_ix_freevert: Union[Unset, int] = UNSET
    act_ix_delete_config_file: Union[Unset, int] = UNSET
    extra2_attachment: Union[Unset, int] = UNSET
    act_client_changekey: Union[Unset, int] = UNSET
    act_client_createdoc: Union[Unset, int] = UNSET
    act_client_flowerroryesno: Union[Unset, int] = UNSET
    act_ix_delete_workflow: Union[Unset, int] = UNSET
    act_client_erasedoc: Union[Unset, int] = UNSET
    act_ix_change_rs: Union[Unset, int] = UNSET
    act_client_movedoc: Union[Unset, int] = UNSET
    act_client_pickpost: Union[Unset, int] = UNSET
    act_client_complain: Union[Unset, int] = UNSET
    act_client_wvlast: Union[Unset, int] = UNSET
    act_client_setvert: Union[Unset, int] = UNSET
    act_client_removevert: Union[Unset, int] = UNSET
    act_client_eloend: Union[Unset, int] = UNSET
    act_ix_create_key: Union[Unset, int] = UNSET
    extra2_wf_cancel: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        act_client_refdoc = self.act_client_refdoc

        extra2_note_personal = self.extra2_note_personal

        act_ix_take_workflow_node = self.act_ix_take_workflow_node

        act_client_viewdoc = self.act_client_viewdoc

        act_client_masktexttoolong = self.act_client_masktexttoolong

        extra2_wf_finished = self.extra2_wf_finished

        act_ix_substitution_activate = self.act_ix_substitution_activate

        act_ix_delete_aspect = self.act_ix_delete_aspect

        act_client_deletenote = self.act_client_deletenote

        act_ix_delete_user = self.act_ix_delete_user

        extra2_sso_login = self.extra2_sso_login

        act_client_editnote = self.act_client_editnote

        act_client_convert_format = self.act_client_convert_format

        act_client_postfirst = self.act_client_postfirst

        act_client_createflowtempl = self.act_client_createflowtempl

        act_ix_create_note = self.act_ix_create_note

        act_ix_checkin_config_file = self.act_ix_checkin_config_file

        act_client_createsor = self.act_client_createsor

        act_ix_substitution_delete = self.act_ix_substitution_delete

        act_client_postedit = self.act_client_postedit

        act_ix_delete_counter = self.act_ix_delete_counter

        act_ix_create_user = self.act_ix_create_user

        extra2_note_stamp = self.extra2_note_stamp

        act_client_wvchangesend = self.act_client_wvchangesend

        act_client_colorchanged = self.act_client_colorchanged

        act_client_checkout = self.act_client_checkout

        act_ix_substitution_transfer = self.act_ix_substitution_transfer

        act_client_delversion = self.act_client_delversion

        act_ix_checkin_workflow = self.act_ix_checkin_workflow

        act_ix_mini_app_login = self.act_ix_mini_app_login

        act_ix_create_workflow = self.act_ix_create_workflow

        act_ix_newvert = self.act_ix_newvert

        act_client_wvchange = self.act_client_wvchange

        act_client_startflow = self.act_client_startflow

        extra2_wf_active = self.extra2_wf_active

        act_client_resetvert = self.act_client_resetvert

        act_client_maskchanged = self.act_client_maskchanged

        act_client_postreceive = self.act_client_postreceive

        act_ix_move_sord = self.act_ix_move_sord

        act_ix_checkin_key = self.act_ix_checkin_key

        act_iswritesession = self.act_iswritesession

        act_ix_link_sord = self.act_ix_link_sord

        act_client_showsor = self.act_client_showsor

        act_client_delvert = self.act_client_delvert

        mb_comment = self.mb_comment

        act_ix_checkin_doc_mask = self.act_ix_checkin_doc_mask

        act_client_editflowtempl = self.act_client_editflowtempl

        extra2_signature = self.extra2_signature

        act_client_deletedocs = self.act_client_deletedocs

        act_client_postschlagwort = self.act_client_postschlagwort

        act_ix_first = self.act_ix_first

        act_ix_create_document = self.act_ix_create_document

        extra2_force = self.extra2_force

        act_ix_copy_sord = self.act_ix_copy_sord

        act_client_postimport = self.act_client_postimport

        act_client_postmove = self.act_client_postmove

        act_ix_delete_note = self.act_ix_delete_note

        act_ix_resetvert = self.act_ix_resetvert

        act_client_eraseref = self.act_client_eraseref

        act_ix_login = self.act_ix_login

        act_ix_checkin_user_profile = self.act_ix_checkin_user_profile

        act_client_erasesor = self.act_client_erasesor

        act_ix_checkout_docversion = self.act_ix_checkout_docversion

        act_client_postcollect = self.act_client_postcollect

        act_ix_checkin_user = self.act_ix_checkin_user

        act_client_keychanged = self.act_client_keychanged

        act_ix_start_workflow = self.act_ix_start_workflow

        act_ix_reference_sord = self.act_ix_reference_sord

        extra2_note_normal = self.extra2_note_normal

        act_dm_readdoc = self.act_dm_readdoc

        extra2_wf_terminate = self.extra2_wf_terminate

        act_ix_checkin_repl_name = self.act_ix_checkin_repl_name

        act_client_postexpand = self.act_client_postexpand

        act_client_editdoc = self.act_client_editdoc

        act_client_postdocbuild = self.act_client_postdocbuild

        act_client_postcopyto = self.act_client_postcopyto

        act_ix_increment_counter = self.act_ix_increment_counter

        act_ix_checkin_sord_type = self.act_ix_checkin_sord_type

        act_client_wvfirst = self.act_client_wvfirst

        act_ix_create_doc_mask = self.act_ix_create_doc_mask

        extra2_preview = self.extra2_preview

        act_client_elostart = self.act_client_elostart

        act_ix_checkin_docversion = self.act_ix_checkin_docversion

        act_client_checkin = self.act_client_checkin

        act_client_pwdchanged = self.act_client_pwdchanged

        act_ix_delete_user_profile = self.act_ix_delete_user_profile

        act_ix_checkin_note = self.act_ix_checkin_note

        act_ix_delegate_workflow = self.act_ix_delegate_workflow

        act_ix_delvert = self.act_ix_delvert

        act_ix_substitution_change = self.act_ix_substitution_change

        act_ix_create_aspect = self.act_ix_create_aspect

        act_client_editsor = self.act_client_editsor

        extra2_annotation_note = self.extra2_annotation_note

        extra2_indexsearch = self.extra2_indexsearch

        act_ix_change_acl = self.act_ix_change_acl

        act_ix_change_deldate = self.act_ix_change_deldate

        act_ix_substitution_new = self.act_ix_substitution_new

        act_custom_first = self.act_custom_first

        act_ix_substitution_forward = self.act_ix_substitution_forward

        act_client_flowtimelimit = self.act_client_flowtimelimit

        act_client_postlast = self.act_client_postlast

        act_ix_delete_reference = self.act_ix_delete_reference

        act_client_delflowtempl = self.act_client_delflowtempl

        act_client_postnewole = self.act_client_postnewole

        act_client_delflowactive = self.act_client_delflowactive

        extra2_lock = self.extra2_lock

        act_client_changedoc = self.act_client_changedoc

        act_ix_logout = self.act_ix_logout

        act_client_showdoc = self.act_client_showdoc

        act_custom_last = self.act_custom_last

        extra2_annotation_marker = self.extra2_annotation_marker

        act_client_wvnewsend = self.act_client_wvnewsend

        act_ix_checkin_sord = self.act_ix_checkin_sord

        act_client_addref = self.act_client_addref

        act_ix_last = self.act_ix_last

        act_client_refsor = self.act_client_refsor

        act_ix_setvert = self.act_ix_setvert

        extra2_docversion = self.extra2_docversion

        act_client_wvdelete = self.act_client_wvdelete

        act_client_movesor = self.act_client_movesor

        act_client_wvreceive = self.act_client_wvreceive

        act_client_createnote = self.act_client_createnote

        act_client_pathchanged = self.act_client_pathchanged

        act_client_userchanged = self.act_client_userchanged

        act_client_moveref = self.act_client_moveref

        act_client_wvnew = self.act_client_wvnew

        act_ix_terminate_workflow = self.act_ix_terminate_workflow

        act_client_reportchanged = self.act_client_reportchanged

        extra2_wf_template = self.extra2_wf_template

        extra2_all_notes_of_sord = self.extra2_all_notes_of_sord

        act_client_postdelete = self.act_client_postdelete

        act_ix_delete_doc_mask = self.act_ix_delete_doc_mask

        extra2_finally = self.extra2_finally

        act_client_none = self.act_client_none

        act_ix_delete_key = self.act_ix_delete_key

        mb_action = self.mb_action

        act_ix_checkout_sord = self.act_ix_checkout_sord

        act_ix_unlink_sord = self.act_ix_unlink_sord

        act_client_forwardflow = self.act_client_forwardflow

        mb_user_name = self.mb_user_name

        act_client_changesor = self.act_client_changesor

        act_client_freevert = self.act_client_freevert

        act_ix_lock_archive = self.act_ix_lock_archive

        mb_act_time_iso = self.mb_act_time_iso

        act_client_receiveflow = self.act_client_receiveflow

        act_ix_delete_sord = self.act_ix_delete_sord

        act_ix_checkin_counter = self.act_ix_checkin_counter

        act_ix_checkin_color = self.act_ix_checkin_color

        act_client_search = self.act_client_search

        act_ix_checkout_note = self.act_ix_checkout_note

        extra2_report_as_login = self.extra2_report_as_login

        act_ix_delete_sord_type = self.act_ix_delete_sord_type

        act_ix_delete_report = self.act_ix_delete_report

        act_ix_checkin_aspect = self.act_ix_checkin_aspect

        act_client_changeattach = self.act_client_changeattach

        act_client_viewsor = self.act_client_viewsor

        act_client_editflowactive = self.act_client_editflowactive

        act_ix_checkin_report_options = self.act_ix_checkin_report_options

        act_ix_edit_workflow_node = self.act_ix_edit_workflow_node

        act_client_postmoveto = self.act_client_postmoveto

        act_ix_start_adhoc_workflow = self.act_ix_start_adhoc_workflow

        act_ix_removevert = self.act_ix_removevert

        act_client_wvsend = self.act_client_wvsend

        act_client_changekind = self.act_client_changekind

        act_ix_create_sord = self.act_ix_create_sord

        act_ix_substitution_deactivate = self.act_ix_substitution_deactivate

        act_client_newvert = self.act_client_newvert

        act_ix_freevert = self.act_ix_freevert

        act_ix_delete_config_file = self.act_ix_delete_config_file

        extra2_attachment = self.extra2_attachment

        act_client_changekey = self.act_client_changekey

        act_client_createdoc = self.act_client_createdoc

        act_client_flowerroryesno = self.act_client_flowerroryesno

        act_ix_delete_workflow = self.act_ix_delete_workflow

        act_client_erasedoc = self.act_client_erasedoc

        act_ix_change_rs = self.act_ix_change_rs

        act_client_movedoc = self.act_client_movedoc

        act_client_pickpost = self.act_client_pickpost

        act_client_complain = self.act_client_complain

        act_client_wvlast = self.act_client_wvlast

        act_client_setvert = self.act_client_setvert

        act_client_removevert = self.act_client_removevert

        act_client_eloend = self.act_client_eloend

        act_ix_create_key = self.act_ix_create_key

        extra2_wf_cancel = self.extra2_wf_cancel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if act_client_refdoc is not UNSET:
            field_dict["ACT_CLIENT_REFDOC"] = act_client_refdoc
        if extra2_note_personal is not UNSET:
            field_dict["EXTRA2_NOTE_PERSONAL"] = extra2_note_personal
        if act_ix_take_workflow_node is not UNSET:
            field_dict["ACT_IX_TAKE_WORKFLOW_NODE"] = act_ix_take_workflow_node
        if act_client_viewdoc is not UNSET:
            field_dict["ACT_CLIENT_VIEWDOC"] = act_client_viewdoc
        if act_client_masktexttoolong is not UNSET:
            field_dict["ACT_CLIENT_MASKTEXTTOOLONG"] = act_client_masktexttoolong
        if extra2_wf_finished is not UNSET:
            field_dict["EXTRA2_WF_FINISHED"] = extra2_wf_finished
        if act_ix_substitution_activate is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_ACTIVATE"] = act_ix_substitution_activate
        if act_ix_delete_aspect is not UNSET:
            field_dict["ACT_IX_DELETE_ASPECT"] = act_ix_delete_aspect
        if act_client_deletenote is not UNSET:
            field_dict["ACT_CLIENT_DELETENOTE"] = act_client_deletenote
        if act_ix_delete_user is not UNSET:
            field_dict["ACT_IX_DELETE_USER"] = act_ix_delete_user
        if extra2_sso_login is not UNSET:
            field_dict["EXTRA2_SSO_LOGIN"] = extra2_sso_login
        if act_client_editnote is not UNSET:
            field_dict["ACT_CLIENT_EDITNOTE"] = act_client_editnote
        if act_client_convert_format is not UNSET:
            field_dict["ACT_CLIENT_CONVERT_FORMAT"] = act_client_convert_format
        if act_client_postfirst is not UNSET:
            field_dict["ACT_CLIENT_POSTFIRST"] = act_client_postfirst
        if act_client_createflowtempl is not UNSET:
            field_dict["ACT_CLIENT_CREATEFLOWTEMPL"] = act_client_createflowtempl
        if act_ix_create_note is not UNSET:
            field_dict["ACT_IX_CREATE_NOTE"] = act_ix_create_note
        if act_ix_checkin_config_file is not UNSET:
            field_dict["ACT_IX_CHECKIN_CONFIG_FILE"] = act_ix_checkin_config_file
        if act_client_createsor is not UNSET:
            field_dict["ACT_CLIENT_CREATESOR"] = act_client_createsor
        if act_ix_substitution_delete is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_DELETE"] = act_ix_substitution_delete
        if act_client_postedit is not UNSET:
            field_dict["ACT_CLIENT_POSTEDIT"] = act_client_postedit
        if act_ix_delete_counter is not UNSET:
            field_dict["ACT_IX_DELETE_COUNTER"] = act_ix_delete_counter
        if act_ix_create_user is not UNSET:
            field_dict["ACT_IX_CREATE_USER"] = act_ix_create_user
        if extra2_note_stamp is not UNSET:
            field_dict["EXTRA2_NOTE_STAMP"] = extra2_note_stamp
        if act_client_wvchangesend is not UNSET:
            field_dict["ACT_CLIENT_WVCHANGESEND"] = act_client_wvchangesend
        if act_client_colorchanged is not UNSET:
            field_dict["ACT_CLIENT_COLORCHANGED"] = act_client_colorchanged
        if act_client_checkout is not UNSET:
            field_dict["ACT_CLIENT_CHECKOUT"] = act_client_checkout
        if act_ix_substitution_transfer is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_TRANSFER"] = act_ix_substitution_transfer
        if act_client_delversion is not UNSET:
            field_dict["ACT_CLIENT_DELVERSION"] = act_client_delversion
        if act_ix_checkin_workflow is not UNSET:
            field_dict["ACT_IX_CHECKIN_WORKFLOW"] = act_ix_checkin_workflow
        if act_ix_mini_app_login is not UNSET:
            field_dict["ACT_IX_MINI_APP_LOGIN"] = act_ix_mini_app_login
        if act_ix_create_workflow is not UNSET:
            field_dict["ACT_IX_CREATE_WORKFLOW"] = act_ix_create_workflow
        if act_ix_newvert is not UNSET:
            field_dict["ACT_IX_NEWVERT"] = act_ix_newvert
        if act_client_wvchange is not UNSET:
            field_dict["ACT_CLIENT_WVCHANGE"] = act_client_wvchange
        if act_client_startflow is not UNSET:
            field_dict["ACT_CLIENT_STARTFLOW"] = act_client_startflow
        if extra2_wf_active is not UNSET:
            field_dict["EXTRA2_WF_ACTIVE"] = extra2_wf_active
        if act_client_resetvert is not UNSET:
            field_dict["ACT_CLIENT_RESETVERT"] = act_client_resetvert
        if act_client_maskchanged is not UNSET:
            field_dict["ACT_CLIENT_MASKCHANGED"] = act_client_maskchanged
        if act_client_postreceive is not UNSET:
            field_dict["ACT_CLIENT_POSTRECEIVE"] = act_client_postreceive
        if act_ix_move_sord is not UNSET:
            field_dict["ACT_IX_MOVE_SORD"] = act_ix_move_sord
        if act_ix_checkin_key is not UNSET:
            field_dict["ACT_IX_CHECKIN_KEY"] = act_ix_checkin_key
        if act_iswritesession is not UNSET:
            field_dict["ACT_ISWRITESESSION"] = act_iswritesession
        if act_ix_link_sord is not UNSET:
            field_dict["ACT_IX_LINK_SORD"] = act_ix_link_sord
        if act_client_showsor is not UNSET:
            field_dict["ACT_CLIENT_SHOWSOR"] = act_client_showsor
        if act_client_delvert is not UNSET:
            field_dict["ACT_CLIENT_DELVERT"] = act_client_delvert
        if mb_comment is not UNSET:
            field_dict["mbComment"] = mb_comment
        if act_ix_checkin_doc_mask is not UNSET:
            field_dict["ACT_IX_CHECKIN_DOC_MASK"] = act_ix_checkin_doc_mask
        if act_client_editflowtempl is not UNSET:
            field_dict["ACT_CLIENT_EDITFLOWTEMPL"] = act_client_editflowtempl
        if extra2_signature is not UNSET:
            field_dict["EXTRA2_SIGNATURE"] = extra2_signature
        if act_client_deletedocs is not UNSET:
            field_dict["ACT_CLIENT_DELETEDOCS"] = act_client_deletedocs
        if act_client_postschlagwort is not UNSET:
            field_dict["ACT_CLIENT_POSTSCHLAGWORT"] = act_client_postschlagwort
        if act_ix_first is not UNSET:
            field_dict["ACT_IX_FIRST"] = act_ix_first
        if act_ix_create_document is not UNSET:
            field_dict["ACT_IX_CREATE_DOCUMENT"] = act_ix_create_document
        if extra2_force is not UNSET:
            field_dict["EXTRA2_FORCE"] = extra2_force
        if act_ix_copy_sord is not UNSET:
            field_dict["ACT_IX_COPY_SORD"] = act_ix_copy_sord
        if act_client_postimport is not UNSET:
            field_dict["ACT_CLIENT_POSTIMPORT"] = act_client_postimport
        if act_client_postmove is not UNSET:
            field_dict["ACT_CLIENT_POSTMOVE"] = act_client_postmove
        if act_ix_delete_note is not UNSET:
            field_dict["ACT_IX_DELETE_NOTE"] = act_ix_delete_note
        if act_ix_resetvert is not UNSET:
            field_dict["ACT_IX_RESETVERT"] = act_ix_resetvert
        if act_client_eraseref is not UNSET:
            field_dict["ACT_CLIENT_ERASEREF"] = act_client_eraseref
        if act_ix_login is not UNSET:
            field_dict["ACT_IX_LOGIN"] = act_ix_login
        if act_ix_checkin_user_profile is not UNSET:
            field_dict["ACT_IX_CHECKIN_USER_PROFILE"] = act_ix_checkin_user_profile
        if act_client_erasesor is not UNSET:
            field_dict["ACT_CLIENT_ERASESOR"] = act_client_erasesor
        if act_ix_checkout_docversion is not UNSET:
            field_dict["ACT_IX_CHECKOUT_DOCVERSION"] = act_ix_checkout_docversion
        if act_client_postcollect is not UNSET:
            field_dict["ACT_CLIENT_POSTCOLLECT"] = act_client_postcollect
        if act_ix_checkin_user is not UNSET:
            field_dict["ACT_IX_CHECKIN_USER"] = act_ix_checkin_user
        if act_client_keychanged is not UNSET:
            field_dict["ACT_CLIENT_KEYCHANGED"] = act_client_keychanged
        if act_ix_start_workflow is not UNSET:
            field_dict["ACT_IX_START_WORKFLOW"] = act_ix_start_workflow
        if act_ix_reference_sord is not UNSET:
            field_dict["ACT_IX_REFERENCE_SORD"] = act_ix_reference_sord
        if extra2_note_normal is not UNSET:
            field_dict["EXTRA2_NOTE_NORMAL"] = extra2_note_normal
        if act_dm_readdoc is not UNSET:
            field_dict["ACT_DM_READDOC"] = act_dm_readdoc
        if extra2_wf_terminate is not UNSET:
            field_dict["EXTRA2_WF_TERMINATE"] = extra2_wf_terminate
        if act_ix_checkin_repl_name is not UNSET:
            field_dict["ACT_IX_CHECKIN_REPL_NAME"] = act_ix_checkin_repl_name
        if act_client_postexpand is not UNSET:
            field_dict["ACT_CLIENT_POSTEXPAND"] = act_client_postexpand
        if act_client_editdoc is not UNSET:
            field_dict["ACT_CLIENT_EDITDOC"] = act_client_editdoc
        if act_client_postdocbuild is not UNSET:
            field_dict["ACT_CLIENT_POSTDOCBUILD"] = act_client_postdocbuild
        if act_client_postcopyto is not UNSET:
            field_dict["ACT_CLIENT_POSTCOPYTO"] = act_client_postcopyto
        if act_ix_increment_counter is not UNSET:
            field_dict["ACT_IX_INCREMENT_COUNTER"] = act_ix_increment_counter
        if act_ix_checkin_sord_type is not UNSET:
            field_dict["ACT_IX_CHECKIN_SORD_TYPE"] = act_ix_checkin_sord_type
        if act_client_wvfirst is not UNSET:
            field_dict["ACT_CLIENT_WVFIRST"] = act_client_wvfirst
        if act_ix_create_doc_mask is not UNSET:
            field_dict["ACT_IX_CREATE_DOC_MASK"] = act_ix_create_doc_mask
        if extra2_preview is not UNSET:
            field_dict["EXTRA2_PREVIEW"] = extra2_preview
        if act_client_elostart is not UNSET:
            field_dict["ACT_CLIENT_ELOSTART"] = act_client_elostart
        if act_ix_checkin_docversion is not UNSET:
            field_dict["ACT_IX_CHECKIN_DOCVERSION"] = act_ix_checkin_docversion
        if act_client_checkin is not UNSET:
            field_dict["ACT_CLIENT_CHECKIN"] = act_client_checkin
        if act_client_pwdchanged is not UNSET:
            field_dict["ACT_CLIENT_PWDCHANGED"] = act_client_pwdchanged
        if act_ix_delete_user_profile is not UNSET:
            field_dict["ACT_IX_DELETE_USER_PROFILE"] = act_ix_delete_user_profile
        if act_ix_checkin_note is not UNSET:
            field_dict["ACT_IX_CHECKIN_NOTE"] = act_ix_checkin_note
        if act_ix_delegate_workflow is not UNSET:
            field_dict["ACT_IX_DELEGATE_WORKFLOW"] = act_ix_delegate_workflow
        if act_ix_delvert is not UNSET:
            field_dict["ACT_IX_DELVERT"] = act_ix_delvert
        if act_ix_substitution_change is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_CHANGE"] = act_ix_substitution_change
        if act_ix_create_aspect is not UNSET:
            field_dict["ACT_IX_CREATE_ASPECT"] = act_ix_create_aspect
        if act_client_editsor is not UNSET:
            field_dict["ACT_CLIENT_EDITSOR"] = act_client_editsor
        if extra2_annotation_note is not UNSET:
            field_dict["EXTRA2_ANNOTATION_NOTE"] = extra2_annotation_note
        if extra2_indexsearch is not UNSET:
            field_dict["EXTRA2_INDEXSEARCH"] = extra2_indexsearch
        if act_ix_change_acl is not UNSET:
            field_dict["ACT_IX_CHANGE_ACL"] = act_ix_change_acl
        if act_ix_change_deldate is not UNSET:
            field_dict["ACT_IX_CHANGE_DELDATE"] = act_ix_change_deldate
        if act_ix_substitution_new is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_NEW"] = act_ix_substitution_new
        if act_custom_first is not UNSET:
            field_dict["ACT_CUSTOM_FIRST"] = act_custom_first
        if act_ix_substitution_forward is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_FORWARD"] = act_ix_substitution_forward
        if act_client_flowtimelimit is not UNSET:
            field_dict["ACT_CLIENT_FLOWTIMELIMIT"] = act_client_flowtimelimit
        if act_client_postlast is not UNSET:
            field_dict["ACT_CLIENT_POSTLAST"] = act_client_postlast
        if act_ix_delete_reference is not UNSET:
            field_dict["ACT_IX_DELETE_REFERENCE"] = act_ix_delete_reference
        if act_client_delflowtempl is not UNSET:
            field_dict["ACT_CLIENT_DELFLOWTEMPL"] = act_client_delflowtempl
        if act_client_postnewole is not UNSET:
            field_dict["ACT_CLIENT_POSTNEWOLE"] = act_client_postnewole
        if act_client_delflowactive is not UNSET:
            field_dict["ACT_CLIENT_DELFLOWACTIVE"] = act_client_delflowactive
        if extra2_lock is not UNSET:
            field_dict["EXTRA2_LOCK"] = extra2_lock
        if act_client_changedoc is not UNSET:
            field_dict["ACT_CLIENT_CHANGEDOC"] = act_client_changedoc
        if act_ix_logout is not UNSET:
            field_dict["ACT_IX_LOGOUT"] = act_ix_logout
        if act_client_showdoc is not UNSET:
            field_dict["ACT_CLIENT_SHOWDOC"] = act_client_showdoc
        if act_custom_last is not UNSET:
            field_dict["ACT_CUSTOM_LAST"] = act_custom_last
        if extra2_annotation_marker is not UNSET:
            field_dict["EXTRA2_ANNOTATION_MARKER"] = extra2_annotation_marker
        if act_client_wvnewsend is not UNSET:
            field_dict["ACT_CLIENT_WVNEWSEND"] = act_client_wvnewsend
        if act_ix_checkin_sord is not UNSET:
            field_dict["ACT_IX_CHECKIN_SORD"] = act_ix_checkin_sord
        if act_client_addref is not UNSET:
            field_dict["ACT_CLIENT_ADDREF"] = act_client_addref
        if act_ix_last is not UNSET:
            field_dict["ACT_IX_LAST"] = act_ix_last
        if act_client_refsor is not UNSET:
            field_dict["ACT_CLIENT_REFSOR"] = act_client_refsor
        if act_ix_setvert is not UNSET:
            field_dict["ACT_IX_SETVERT"] = act_ix_setvert
        if extra2_docversion is not UNSET:
            field_dict["EXTRA2_DOCVERSION"] = extra2_docversion
        if act_client_wvdelete is not UNSET:
            field_dict["ACT_CLIENT_WVDELETE"] = act_client_wvdelete
        if act_client_movesor is not UNSET:
            field_dict["ACT_CLIENT_MOVESOR"] = act_client_movesor
        if act_client_wvreceive is not UNSET:
            field_dict["ACT_CLIENT_WVRECEIVE"] = act_client_wvreceive
        if act_client_createnote is not UNSET:
            field_dict["ACT_CLIENT_CREATENOTE"] = act_client_createnote
        if act_client_pathchanged is not UNSET:
            field_dict["ACT_CLIENT_PATHCHANGED"] = act_client_pathchanged
        if act_client_userchanged is not UNSET:
            field_dict["ACT_CLIENT_USERCHANGED"] = act_client_userchanged
        if act_client_moveref is not UNSET:
            field_dict["ACT_CLIENT_MOVEREF"] = act_client_moveref
        if act_client_wvnew is not UNSET:
            field_dict["ACT_CLIENT_WVNEW"] = act_client_wvnew
        if act_ix_terminate_workflow is not UNSET:
            field_dict["ACT_IX_TERMINATE_WORKFLOW"] = act_ix_terminate_workflow
        if act_client_reportchanged is not UNSET:
            field_dict["ACT_CLIENT_REPORTCHANGED"] = act_client_reportchanged
        if extra2_wf_template is not UNSET:
            field_dict["EXTRA2_WF_TEMPLATE"] = extra2_wf_template
        if extra2_all_notes_of_sord is not UNSET:
            field_dict["EXTRA2_ALL_NOTES_OF_SORD"] = extra2_all_notes_of_sord
        if act_client_postdelete is not UNSET:
            field_dict["ACT_CLIENT_POSTDELETE"] = act_client_postdelete
        if act_ix_delete_doc_mask is not UNSET:
            field_dict["ACT_IX_DELETE_DOC_MASK"] = act_ix_delete_doc_mask
        if extra2_finally is not UNSET:
            field_dict["EXTRA2_FINALLY"] = extra2_finally
        if act_client_none is not UNSET:
            field_dict["ACT_CLIENT_NONE"] = act_client_none
        if act_ix_delete_key is not UNSET:
            field_dict["ACT_IX_DELETE_KEY"] = act_ix_delete_key
        if mb_action is not UNSET:
            field_dict["mbAction"] = mb_action
        if act_ix_checkout_sord is not UNSET:
            field_dict["ACT_IX_CHECKOUT_SORD"] = act_ix_checkout_sord
        if act_ix_unlink_sord is not UNSET:
            field_dict["ACT_IX_UNLINK_SORD"] = act_ix_unlink_sord
        if act_client_forwardflow is not UNSET:
            field_dict["ACT_CLIENT_FORWARDFLOW"] = act_client_forwardflow
        if mb_user_name is not UNSET:
            field_dict["mbUserName"] = mb_user_name
        if act_client_changesor is not UNSET:
            field_dict["ACT_CLIENT_CHANGESOR"] = act_client_changesor
        if act_client_freevert is not UNSET:
            field_dict["ACT_CLIENT_FREEVERT"] = act_client_freevert
        if act_ix_lock_archive is not UNSET:
            field_dict["ACT_IX_LOCK_ARCHIVE"] = act_ix_lock_archive
        if mb_act_time_iso is not UNSET:
            field_dict["mbActTimeISO"] = mb_act_time_iso
        if act_client_receiveflow is not UNSET:
            field_dict["ACT_CLIENT_RECEIVEFLOW"] = act_client_receiveflow
        if act_ix_delete_sord is not UNSET:
            field_dict["ACT_IX_DELETE_SORD"] = act_ix_delete_sord
        if act_ix_checkin_counter is not UNSET:
            field_dict["ACT_IX_CHECKIN_COUNTER"] = act_ix_checkin_counter
        if act_ix_checkin_color is not UNSET:
            field_dict["ACT_IX_CHECKIN_COLOR"] = act_ix_checkin_color
        if act_client_search is not UNSET:
            field_dict["ACT_CLIENT_SEARCH"] = act_client_search
        if act_ix_checkout_note is not UNSET:
            field_dict["ACT_IX_CHECKOUT_NOTE"] = act_ix_checkout_note
        if extra2_report_as_login is not UNSET:
            field_dict["EXTRA2_REPORT_AS_LOGIN"] = extra2_report_as_login
        if act_ix_delete_sord_type is not UNSET:
            field_dict["ACT_IX_DELETE_SORD_TYPE"] = act_ix_delete_sord_type
        if act_ix_delete_report is not UNSET:
            field_dict["ACT_IX_DELETE_REPORT"] = act_ix_delete_report
        if act_ix_checkin_aspect is not UNSET:
            field_dict["ACT_IX_CHECKIN_ASPECT"] = act_ix_checkin_aspect
        if act_client_changeattach is not UNSET:
            field_dict["ACT_CLIENT_CHANGEATTACH"] = act_client_changeattach
        if act_client_viewsor is not UNSET:
            field_dict["ACT_CLIENT_VIEWSOR"] = act_client_viewsor
        if act_client_editflowactive is not UNSET:
            field_dict["ACT_CLIENT_EDITFLOWACTIVE"] = act_client_editflowactive
        if act_ix_checkin_report_options is not UNSET:
            field_dict["ACT_IX_CHECKIN_REPORT_OPTIONS"] = act_ix_checkin_report_options
        if act_ix_edit_workflow_node is not UNSET:
            field_dict["ACT_IX_EDIT_WORKFLOW_NODE"] = act_ix_edit_workflow_node
        if act_client_postmoveto is not UNSET:
            field_dict["ACT_CLIENT_POSTMOVETO"] = act_client_postmoveto
        if act_ix_start_adhoc_workflow is not UNSET:
            field_dict["ACT_IX_START_ADHOC_WORKFLOW"] = act_ix_start_adhoc_workflow
        if act_ix_removevert is not UNSET:
            field_dict["ACT_IX_REMOVEVERT"] = act_ix_removevert
        if act_client_wvsend is not UNSET:
            field_dict["ACT_CLIENT_WVSEND"] = act_client_wvsend
        if act_client_changekind is not UNSET:
            field_dict["ACT_CLIENT_CHANGEKIND"] = act_client_changekind
        if act_ix_create_sord is not UNSET:
            field_dict["ACT_IX_CREATE_SORD"] = act_ix_create_sord
        if act_ix_substitution_deactivate is not UNSET:
            field_dict["ACT_IX_SUBSTITUTION_DEACTIVATE"] = act_ix_substitution_deactivate
        if act_client_newvert is not UNSET:
            field_dict["ACT_CLIENT_NEWVERT"] = act_client_newvert
        if act_ix_freevert is not UNSET:
            field_dict["ACT_IX_FREEVERT"] = act_ix_freevert
        if act_ix_delete_config_file is not UNSET:
            field_dict["ACT_IX_DELETE_CONFIG_FILE"] = act_ix_delete_config_file
        if extra2_attachment is not UNSET:
            field_dict["EXTRA2_ATTACHMENT"] = extra2_attachment
        if act_client_changekey is not UNSET:
            field_dict["ACT_CLIENT_CHANGEKEY"] = act_client_changekey
        if act_client_createdoc is not UNSET:
            field_dict["ACT_CLIENT_CREATEDOC"] = act_client_createdoc
        if act_client_flowerroryesno is not UNSET:
            field_dict["ACT_CLIENT_FLOWERRORYESNO"] = act_client_flowerroryesno
        if act_ix_delete_workflow is not UNSET:
            field_dict["ACT_IX_DELETE_WORKFLOW"] = act_ix_delete_workflow
        if act_client_erasedoc is not UNSET:
            field_dict["ACT_CLIENT_ERASEDOC"] = act_client_erasedoc
        if act_ix_change_rs is not UNSET:
            field_dict["ACT_IX_CHANGE_RS"] = act_ix_change_rs
        if act_client_movedoc is not UNSET:
            field_dict["ACT_CLIENT_MOVEDOC"] = act_client_movedoc
        if act_client_pickpost is not UNSET:
            field_dict["ACT_CLIENT_PICKPOST"] = act_client_pickpost
        if act_client_complain is not UNSET:
            field_dict["ACT_CLIENT_COMPLAIN"] = act_client_complain
        if act_client_wvlast is not UNSET:
            field_dict["ACT_CLIENT_WVLAST"] = act_client_wvlast
        if act_client_setvert is not UNSET:
            field_dict["ACT_CLIENT_SETVERT"] = act_client_setvert
        if act_client_removevert is not UNSET:
            field_dict["ACT_CLIENT_REMOVEVERT"] = act_client_removevert
        if act_client_eloend is not UNSET:
            field_dict["ACT_CLIENT_ELOEND"] = act_client_eloend
        if act_ix_create_key is not UNSET:
            field_dict["ACT_IX_CREATE_KEY"] = act_ix_create_key
        if extra2_wf_cancel is not UNSET:
            field_dict["EXTRA2_WF_CANCEL"] = extra2_wf_cancel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        act_client_refdoc = d.pop("ACT_CLIENT_REFDOC", UNSET)

        extra2_note_personal = d.pop("EXTRA2_NOTE_PERSONAL", UNSET)

        act_ix_take_workflow_node = d.pop("ACT_IX_TAKE_WORKFLOW_NODE", UNSET)

        act_client_viewdoc = d.pop("ACT_CLIENT_VIEWDOC", UNSET)

        act_client_masktexttoolong = d.pop("ACT_CLIENT_MASKTEXTTOOLONG", UNSET)

        extra2_wf_finished = d.pop("EXTRA2_WF_FINISHED", UNSET)

        act_ix_substitution_activate = d.pop("ACT_IX_SUBSTITUTION_ACTIVATE", UNSET)

        act_ix_delete_aspect = d.pop("ACT_IX_DELETE_ASPECT", UNSET)

        act_client_deletenote = d.pop("ACT_CLIENT_DELETENOTE", UNSET)

        act_ix_delete_user = d.pop("ACT_IX_DELETE_USER", UNSET)

        extra2_sso_login = d.pop("EXTRA2_SSO_LOGIN", UNSET)

        act_client_editnote = d.pop("ACT_CLIENT_EDITNOTE", UNSET)

        act_client_convert_format = d.pop("ACT_CLIENT_CONVERT_FORMAT", UNSET)

        act_client_postfirst = d.pop("ACT_CLIENT_POSTFIRST", UNSET)

        act_client_createflowtempl = d.pop("ACT_CLIENT_CREATEFLOWTEMPL", UNSET)

        act_ix_create_note = d.pop("ACT_IX_CREATE_NOTE", UNSET)

        act_ix_checkin_config_file = d.pop("ACT_IX_CHECKIN_CONFIG_FILE", UNSET)

        act_client_createsor = d.pop("ACT_CLIENT_CREATESOR", UNSET)

        act_ix_substitution_delete = d.pop("ACT_IX_SUBSTITUTION_DELETE", UNSET)

        act_client_postedit = d.pop("ACT_CLIENT_POSTEDIT", UNSET)

        act_ix_delete_counter = d.pop("ACT_IX_DELETE_COUNTER", UNSET)

        act_ix_create_user = d.pop("ACT_IX_CREATE_USER", UNSET)

        extra2_note_stamp = d.pop("EXTRA2_NOTE_STAMP", UNSET)

        act_client_wvchangesend = d.pop("ACT_CLIENT_WVCHANGESEND", UNSET)

        act_client_colorchanged = d.pop("ACT_CLIENT_COLORCHANGED", UNSET)

        act_client_checkout = d.pop("ACT_CLIENT_CHECKOUT", UNSET)

        act_ix_substitution_transfer = d.pop("ACT_IX_SUBSTITUTION_TRANSFER", UNSET)

        act_client_delversion = d.pop("ACT_CLIENT_DELVERSION", UNSET)

        act_ix_checkin_workflow = d.pop("ACT_IX_CHECKIN_WORKFLOW", UNSET)

        act_ix_mini_app_login = d.pop("ACT_IX_MINI_APP_LOGIN", UNSET)

        act_ix_create_workflow = d.pop("ACT_IX_CREATE_WORKFLOW", UNSET)

        act_ix_newvert = d.pop("ACT_IX_NEWVERT", UNSET)

        act_client_wvchange = d.pop("ACT_CLIENT_WVCHANGE", UNSET)

        act_client_startflow = d.pop("ACT_CLIENT_STARTFLOW", UNSET)

        extra2_wf_active = d.pop("EXTRA2_WF_ACTIVE", UNSET)

        act_client_resetvert = d.pop("ACT_CLIENT_RESETVERT", UNSET)

        act_client_maskchanged = d.pop("ACT_CLIENT_MASKCHANGED", UNSET)

        act_client_postreceive = d.pop("ACT_CLIENT_POSTRECEIVE", UNSET)

        act_ix_move_sord = d.pop("ACT_IX_MOVE_SORD", UNSET)

        act_ix_checkin_key = d.pop("ACT_IX_CHECKIN_KEY", UNSET)

        act_iswritesession = d.pop("ACT_ISWRITESESSION", UNSET)

        act_ix_link_sord = d.pop("ACT_IX_LINK_SORD", UNSET)

        act_client_showsor = d.pop("ACT_CLIENT_SHOWSOR", UNSET)

        act_client_delvert = d.pop("ACT_CLIENT_DELVERT", UNSET)

        mb_comment = d.pop("mbComment", UNSET)

        act_ix_checkin_doc_mask = d.pop("ACT_IX_CHECKIN_DOC_MASK", UNSET)

        act_client_editflowtempl = d.pop("ACT_CLIENT_EDITFLOWTEMPL", UNSET)

        extra2_signature = d.pop("EXTRA2_SIGNATURE", UNSET)

        act_client_deletedocs = d.pop("ACT_CLIENT_DELETEDOCS", UNSET)

        act_client_postschlagwort = d.pop("ACT_CLIENT_POSTSCHLAGWORT", UNSET)

        act_ix_first = d.pop("ACT_IX_FIRST", UNSET)

        act_ix_create_document = d.pop("ACT_IX_CREATE_DOCUMENT", UNSET)

        extra2_force = d.pop("EXTRA2_FORCE", UNSET)

        act_ix_copy_sord = d.pop("ACT_IX_COPY_SORD", UNSET)

        act_client_postimport = d.pop("ACT_CLIENT_POSTIMPORT", UNSET)

        act_client_postmove = d.pop("ACT_CLIENT_POSTMOVE", UNSET)

        act_ix_delete_note = d.pop("ACT_IX_DELETE_NOTE", UNSET)

        act_ix_resetvert = d.pop("ACT_IX_RESETVERT", UNSET)

        act_client_eraseref = d.pop("ACT_CLIENT_ERASEREF", UNSET)

        act_ix_login = d.pop("ACT_IX_LOGIN", UNSET)

        act_ix_checkin_user_profile = d.pop("ACT_IX_CHECKIN_USER_PROFILE", UNSET)

        act_client_erasesor = d.pop("ACT_CLIENT_ERASESOR", UNSET)

        act_ix_checkout_docversion = d.pop("ACT_IX_CHECKOUT_DOCVERSION", UNSET)

        act_client_postcollect = d.pop("ACT_CLIENT_POSTCOLLECT", UNSET)

        act_ix_checkin_user = d.pop("ACT_IX_CHECKIN_USER", UNSET)

        act_client_keychanged = d.pop("ACT_CLIENT_KEYCHANGED", UNSET)

        act_ix_start_workflow = d.pop("ACT_IX_START_WORKFLOW", UNSET)

        act_ix_reference_sord = d.pop("ACT_IX_REFERENCE_SORD", UNSET)

        extra2_note_normal = d.pop("EXTRA2_NOTE_NORMAL", UNSET)

        act_dm_readdoc = d.pop("ACT_DM_READDOC", UNSET)

        extra2_wf_terminate = d.pop("EXTRA2_WF_TERMINATE", UNSET)

        act_ix_checkin_repl_name = d.pop("ACT_IX_CHECKIN_REPL_NAME", UNSET)

        act_client_postexpand = d.pop("ACT_CLIENT_POSTEXPAND", UNSET)

        act_client_editdoc = d.pop("ACT_CLIENT_EDITDOC", UNSET)

        act_client_postdocbuild = d.pop("ACT_CLIENT_POSTDOCBUILD", UNSET)

        act_client_postcopyto = d.pop("ACT_CLIENT_POSTCOPYTO", UNSET)

        act_ix_increment_counter = d.pop("ACT_IX_INCREMENT_COUNTER", UNSET)

        act_ix_checkin_sord_type = d.pop("ACT_IX_CHECKIN_SORD_TYPE", UNSET)

        act_client_wvfirst = d.pop("ACT_CLIENT_WVFIRST", UNSET)

        act_ix_create_doc_mask = d.pop("ACT_IX_CREATE_DOC_MASK", UNSET)

        extra2_preview = d.pop("EXTRA2_PREVIEW", UNSET)

        act_client_elostart = d.pop("ACT_CLIENT_ELOSTART", UNSET)

        act_ix_checkin_docversion = d.pop("ACT_IX_CHECKIN_DOCVERSION", UNSET)

        act_client_checkin = d.pop("ACT_CLIENT_CHECKIN", UNSET)

        act_client_pwdchanged = d.pop("ACT_CLIENT_PWDCHANGED", UNSET)

        act_ix_delete_user_profile = d.pop("ACT_IX_DELETE_USER_PROFILE", UNSET)

        act_ix_checkin_note = d.pop("ACT_IX_CHECKIN_NOTE", UNSET)

        act_ix_delegate_workflow = d.pop("ACT_IX_DELEGATE_WORKFLOW", UNSET)

        act_ix_delvert = d.pop("ACT_IX_DELVERT", UNSET)

        act_ix_substitution_change = d.pop("ACT_IX_SUBSTITUTION_CHANGE", UNSET)

        act_ix_create_aspect = d.pop("ACT_IX_CREATE_ASPECT", UNSET)

        act_client_editsor = d.pop("ACT_CLIENT_EDITSOR", UNSET)

        extra2_annotation_note = d.pop("EXTRA2_ANNOTATION_NOTE", UNSET)

        extra2_indexsearch = d.pop("EXTRA2_INDEXSEARCH", UNSET)

        act_ix_change_acl = d.pop("ACT_IX_CHANGE_ACL", UNSET)

        act_ix_change_deldate = d.pop("ACT_IX_CHANGE_DELDATE", UNSET)

        act_ix_substitution_new = d.pop("ACT_IX_SUBSTITUTION_NEW", UNSET)

        act_custom_first = d.pop("ACT_CUSTOM_FIRST", UNSET)

        act_ix_substitution_forward = d.pop("ACT_IX_SUBSTITUTION_FORWARD", UNSET)

        act_client_flowtimelimit = d.pop("ACT_CLIENT_FLOWTIMELIMIT", UNSET)

        act_client_postlast = d.pop("ACT_CLIENT_POSTLAST", UNSET)

        act_ix_delete_reference = d.pop("ACT_IX_DELETE_REFERENCE", UNSET)

        act_client_delflowtempl = d.pop("ACT_CLIENT_DELFLOWTEMPL", UNSET)

        act_client_postnewole = d.pop("ACT_CLIENT_POSTNEWOLE", UNSET)

        act_client_delflowactive = d.pop("ACT_CLIENT_DELFLOWACTIVE", UNSET)

        extra2_lock = d.pop("EXTRA2_LOCK", UNSET)

        act_client_changedoc = d.pop("ACT_CLIENT_CHANGEDOC", UNSET)

        act_ix_logout = d.pop("ACT_IX_LOGOUT", UNSET)

        act_client_showdoc = d.pop("ACT_CLIENT_SHOWDOC", UNSET)

        act_custom_last = d.pop("ACT_CUSTOM_LAST", UNSET)

        extra2_annotation_marker = d.pop("EXTRA2_ANNOTATION_MARKER", UNSET)

        act_client_wvnewsend = d.pop("ACT_CLIENT_WVNEWSEND", UNSET)

        act_ix_checkin_sord = d.pop("ACT_IX_CHECKIN_SORD", UNSET)

        act_client_addref = d.pop("ACT_CLIENT_ADDREF", UNSET)

        act_ix_last = d.pop("ACT_IX_LAST", UNSET)

        act_client_refsor = d.pop("ACT_CLIENT_REFSOR", UNSET)

        act_ix_setvert = d.pop("ACT_IX_SETVERT", UNSET)

        extra2_docversion = d.pop("EXTRA2_DOCVERSION", UNSET)

        act_client_wvdelete = d.pop("ACT_CLIENT_WVDELETE", UNSET)

        act_client_movesor = d.pop("ACT_CLIENT_MOVESOR", UNSET)

        act_client_wvreceive = d.pop("ACT_CLIENT_WVRECEIVE", UNSET)

        act_client_createnote = d.pop("ACT_CLIENT_CREATENOTE", UNSET)

        act_client_pathchanged = d.pop("ACT_CLIENT_PATHCHANGED", UNSET)

        act_client_userchanged = d.pop("ACT_CLIENT_USERCHANGED", UNSET)

        act_client_moveref = d.pop("ACT_CLIENT_MOVEREF", UNSET)

        act_client_wvnew = d.pop("ACT_CLIENT_WVNEW", UNSET)

        act_ix_terminate_workflow = d.pop("ACT_IX_TERMINATE_WORKFLOW", UNSET)

        act_client_reportchanged = d.pop("ACT_CLIENT_REPORTCHANGED", UNSET)

        extra2_wf_template = d.pop("EXTRA2_WF_TEMPLATE", UNSET)

        extra2_all_notes_of_sord = d.pop("EXTRA2_ALL_NOTES_OF_SORD", UNSET)

        act_client_postdelete = d.pop("ACT_CLIENT_POSTDELETE", UNSET)

        act_ix_delete_doc_mask = d.pop("ACT_IX_DELETE_DOC_MASK", UNSET)

        extra2_finally = d.pop("EXTRA2_FINALLY", UNSET)

        act_client_none = d.pop("ACT_CLIENT_NONE", UNSET)

        act_ix_delete_key = d.pop("ACT_IX_DELETE_KEY", UNSET)

        mb_action = d.pop("mbAction", UNSET)

        act_ix_checkout_sord = d.pop("ACT_IX_CHECKOUT_SORD", UNSET)

        act_ix_unlink_sord = d.pop("ACT_IX_UNLINK_SORD", UNSET)

        act_client_forwardflow = d.pop("ACT_CLIENT_FORWARDFLOW", UNSET)

        mb_user_name = d.pop("mbUserName", UNSET)

        act_client_changesor = d.pop("ACT_CLIENT_CHANGESOR", UNSET)

        act_client_freevert = d.pop("ACT_CLIENT_FREEVERT", UNSET)

        act_ix_lock_archive = d.pop("ACT_IX_LOCK_ARCHIVE", UNSET)

        mb_act_time_iso = d.pop("mbActTimeISO", UNSET)

        act_client_receiveflow = d.pop("ACT_CLIENT_RECEIVEFLOW", UNSET)

        act_ix_delete_sord = d.pop("ACT_IX_DELETE_SORD", UNSET)

        act_ix_checkin_counter = d.pop("ACT_IX_CHECKIN_COUNTER", UNSET)

        act_ix_checkin_color = d.pop("ACT_IX_CHECKIN_COLOR", UNSET)

        act_client_search = d.pop("ACT_CLIENT_SEARCH", UNSET)

        act_ix_checkout_note = d.pop("ACT_IX_CHECKOUT_NOTE", UNSET)

        extra2_report_as_login = d.pop("EXTRA2_REPORT_AS_LOGIN", UNSET)

        act_ix_delete_sord_type = d.pop("ACT_IX_DELETE_SORD_TYPE", UNSET)

        act_ix_delete_report = d.pop("ACT_IX_DELETE_REPORT", UNSET)

        act_ix_checkin_aspect = d.pop("ACT_IX_CHECKIN_ASPECT", UNSET)

        act_client_changeattach = d.pop("ACT_CLIENT_CHANGEATTACH", UNSET)

        act_client_viewsor = d.pop("ACT_CLIENT_VIEWSOR", UNSET)

        act_client_editflowactive = d.pop("ACT_CLIENT_EDITFLOWACTIVE", UNSET)

        act_ix_checkin_report_options = d.pop("ACT_IX_CHECKIN_REPORT_OPTIONS", UNSET)

        act_ix_edit_workflow_node = d.pop("ACT_IX_EDIT_WORKFLOW_NODE", UNSET)

        act_client_postmoveto = d.pop("ACT_CLIENT_POSTMOVETO", UNSET)

        act_ix_start_adhoc_workflow = d.pop("ACT_IX_START_ADHOC_WORKFLOW", UNSET)

        act_ix_removevert = d.pop("ACT_IX_REMOVEVERT", UNSET)

        act_client_wvsend = d.pop("ACT_CLIENT_WVSEND", UNSET)

        act_client_changekind = d.pop("ACT_CLIENT_CHANGEKIND", UNSET)

        act_ix_create_sord = d.pop("ACT_IX_CREATE_SORD", UNSET)

        act_ix_substitution_deactivate = d.pop("ACT_IX_SUBSTITUTION_DEACTIVATE", UNSET)

        act_client_newvert = d.pop("ACT_CLIENT_NEWVERT", UNSET)

        act_ix_freevert = d.pop("ACT_IX_FREEVERT", UNSET)

        act_ix_delete_config_file = d.pop("ACT_IX_DELETE_CONFIG_FILE", UNSET)

        extra2_attachment = d.pop("EXTRA2_ATTACHMENT", UNSET)

        act_client_changekey = d.pop("ACT_CLIENT_CHANGEKEY", UNSET)

        act_client_createdoc = d.pop("ACT_CLIENT_CREATEDOC", UNSET)

        act_client_flowerroryesno = d.pop("ACT_CLIENT_FLOWERRORYESNO", UNSET)

        act_ix_delete_workflow = d.pop("ACT_IX_DELETE_WORKFLOW", UNSET)

        act_client_erasedoc = d.pop("ACT_CLIENT_ERASEDOC", UNSET)

        act_ix_change_rs = d.pop("ACT_IX_CHANGE_RS", UNSET)

        act_client_movedoc = d.pop("ACT_CLIENT_MOVEDOC", UNSET)

        act_client_pickpost = d.pop("ACT_CLIENT_PICKPOST", UNSET)

        act_client_complain = d.pop("ACT_CLIENT_COMPLAIN", UNSET)

        act_client_wvlast = d.pop("ACT_CLIENT_WVLAST", UNSET)

        act_client_setvert = d.pop("ACT_CLIENT_SETVERT", UNSET)

        act_client_removevert = d.pop("ACT_CLIENT_REMOVEVERT", UNSET)

        act_client_eloend = d.pop("ACT_CLIENT_ELOEND", UNSET)

        act_ix_create_key = d.pop("ACT_IX_CREATE_KEY", UNSET)

        extra2_wf_cancel = d.pop("EXTRA2_WF_CANCEL", UNSET)

        report_info_c = cls(
            act_client_refdoc=act_client_refdoc,
            extra2_note_personal=extra2_note_personal,
            act_ix_take_workflow_node=act_ix_take_workflow_node,
            act_client_viewdoc=act_client_viewdoc,
            act_client_masktexttoolong=act_client_masktexttoolong,
            extra2_wf_finished=extra2_wf_finished,
            act_ix_substitution_activate=act_ix_substitution_activate,
            act_ix_delete_aspect=act_ix_delete_aspect,
            act_client_deletenote=act_client_deletenote,
            act_ix_delete_user=act_ix_delete_user,
            extra2_sso_login=extra2_sso_login,
            act_client_editnote=act_client_editnote,
            act_client_convert_format=act_client_convert_format,
            act_client_postfirst=act_client_postfirst,
            act_client_createflowtempl=act_client_createflowtempl,
            act_ix_create_note=act_ix_create_note,
            act_ix_checkin_config_file=act_ix_checkin_config_file,
            act_client_createsor=act_client_createsor,
            act_ix_substitution_delete=act_ix_substitution_delete,
            act_client_postedit=act_client_postedit,
            act_ix_delete_counter=act_ix_delete_counter,
            act_ix_create_user=act_ix_create_user,
            extra2_note_stamp=extra2_note_stamp,
            act_client_wvchangesend=act_client_wvchangesend,
            act_client_colorchanged=act_client_colorchanged,
            act_client_checkout=act_client_checkout,
            act_ix_substitution_transfer=act_ix_substitution_transfer,
            act_client_delversion=act_client_delversion,
            act_ix_checkin_workflow=act_ix_checkin_workflow,
            act_ix_mini_app_login=act_ix_mini_app_login,
            act_ix_create_workflow=act_ix_create_workflow,
            act_ix_newvert=act_ix_newvert,
            act_client_wvchange=act_client_wvchange,
            act_client_startflow=act_client_startflow,
            extra2_wf_active=extra2_wf_active,
            act_client_resetvert=act_client_resetvert,
            act_client_maskchanged=act_client_maskchanged,
            act_client_postreceive=act_client_postreceive,
            act_ix_move_sord=act_ix_move_sord,
            act_ix_checkin_key=act_ix_checkin_key,
            act_iswritesession=act_iswritesession,
            act_ix_link_sord=act_ix_link_sord,
            act_client_showsor=act_client_showsor,
            act_client_delvert=act_client_delvert,
            mb_comment=mb_comment,
            act_ix_checkin_doc_mask=act_ix_checkin_doc_mask,
            act_client_editflowtempl=act_client_editflowtempl,
            extra2_signature=extra2_signature,
            act_client_deletedocs=act_client_deletedocs,
            act_client_postschlagwort=act_client_postschlagwort,
            act_ix_first=act_ix_first,
            act_ix_create_document=act_ix_create_document,
            extra2_force=extra2_force,
            act_ix_copy_sord=act_ix_copy_sord,
            act_client_postimport=act_client_postimport,
            act_client_postmove=act_client_postmove,
            act_ix_delete_note=act_ix_delete_note,
            act_ix_resetvert=act_ix_resetvert,
            act_client_eraseref=act_client_eraseref,
            act_ix_login=act_ix_login,
            act_ix_checkin_user_profile=act_ix_checkin_user_profile,
            act_client_erasesor=act_client_erasesor,
            act_ix_checkout_docversion=act_ix_checkout_docversion,
            act_client_postcollect=act_client_postcollect,
            act_ix_checkin_user=act_ix_checkin_user,
            act_client_keychanged=act_client_keychanged,
            act_ix_start_workflow=act_ix_start_workflow,
            act_ix_reference_sord=act_ix_reference_sord,
            extra2_note_normal=extra2_note_normal,
            act_dm_readdoc=act_dm_readdoc,
            extra2_wf_terminate=extra2_wf_terminate,
            act_ix_checkin_repl_name=act_ix_checkin_repl_name,
            act_client_postexpand=act_client_postexpand,
            act_client_editdoc=act_client_editdoc,
            act_client_postdocbuild=act_client_postdocbuild,
            act_client_postcopyto=act_client_postcopyto,
            act_ix_increment_counter=act_ix_increment_counter,
            act_ix_checkin_sord_type=act_ix_checkin_sord_type,
            act_client_wvfirst=act_client_wvfirst,
            act_ix_create_doc_mask=act_ix_create_doc_mask,
            extra2_preview=extra2_preview,
            act_client_elostart=act_client_elostart,
            act_ix_checkin_docversion=act_ix_checkin_docversion,
            act_client_checkin=act_client_checkin,
            act_client_pwdchanged=act_client_pwdchanged,
            act_ix_delete_user_profile=act_ix_delete_user_profile,
            act_ix_checkin_note=act_ix_checkin_note,
            act_ix_delegate_workflow=act_ix_delegate_workflow,
            act_ix_delvert=act_ix_delvert,
            act_ix_substitution_change=act_ix_substitution_change,
            act_ix_create_aspect=act_ix_create_aspect,
            act_client_editsor=act_client_editsor,
            extra2_annotation_note=extra2_annotation_note,
            extra2_indexsearch=extra2_indexsearch,
            act_ix_change_acl=act_ix_change_acl,
            act_ix_change_deldate=act_ix_change_deldate,
            act_ix_substitution_new=act_ix_substitution_new,
            act_custom_first=act_custom_first,
            act_ix_substitution_forward=act_ix_substitution_forward,
            act_client_flowtimelimit=act_client_flowtimelimit,
            act_client_postlast=act_client_postlast,
            act_ix_delete_reference=act_ix_delete_reference,
            act_client_delflowtempl=act_client_delflowtempl,
            act_client_postnewole=act_client_postnewole,
            act_client_delflowactive=act_client_delflowactive,
            extra2_lock=extra2_lock,
            act_client_changedoc=act_client_changedoc,
            act_ix_logout=act_ix_logout,
            act_client_showdoc=act_client_showdoc,
            act_custom_last=act_custom_last,
            extra2_annotation_marker=extra2_annotation_marker,
            act_client_wvnewsend=act_client_wvnewsend,
            act_ix_checkin_sord=act_ix_checkin_sord,
            act_client_addref=act_client_addref,
            act_ix_last=act_ix_last,
            act_client_refsor=act_client_refsor,
            act_ix_setvert=act_ix_setvert,
            extra2_docversion=extra2_docversion,
            act_client_wvdelete=act_client_wvdelete,
            act_client_movesor=act_client_movesor,
            act_client_wvreceive=act_client_wvreceive,
            act_client_createnote=act_client_createnote,
            act_client_pathchanged=act_client_pathchanged,
            act_client_userchanged=act_client_userchanged,
            act_client_moveref=act_client_moveref,
            act_client_wvnew=act_client_wvnew,
            act_ix_terminate_workflow=act_ix_terminate_workflow,
            act_client_reportchanged=act_client_reportchanged,
            extra2_wf_template=extra2_wf_template,
            extra2_all_notes_of_sord=extra2_all_notes_of_sord,
            act_client_postdelete=act_client_postdelete,
            act_ix_delete_doc_mask=act_ix_delete_doc_mask,
            extra2_finally=extra2_finally,
            act_client_none=act_client_none,
            act_ix_delete_key=act_ix_delete_key,
            mb_action=mb_action,
            act_ix_checkout_sord=act_ix_checkout_sord,
            act_ix_unlink_sord=act_ix_unlink_sord,
            act_client_forwardflow=act_client_forwardflow,
            mb_user_name=mb_user_name,
            act_client_changesor=act_client_changesor,
            act_client_freevert=act_client_freevert,
            act_ix_lock_archive=act_ix_lock_archive,
            mb_act_time_iso=mb_act_time_iso,
            act_client_receiveflow=act_client_receiveflow,
            act_ix_delete_sord=act_ix_delete_sord,
            act_ix_checkin_counter=act_ix_checkin_counter,
            act_ix_checkin_color=act_ix_checkin_color,
            act_client_search=act_client_search,
            act_ix_checkout_note=act_ix_checkout_note,
            extra2_report_as_login=extra2_report_as_login,
            act_ix_delete_sord_type=act_ix_delete_sord_type,
            act_ix_delete_report=act_ix_delete_report,
            act_ix_checkin_aspect=act_ix_checkin_aspect,
            act_client_changeattach=act_client_changeattach,
            act_client_viewsor=act_client_viewsor,
            act_client_editflowactive=act_client_editflowactive,
            act_ix_checkin_report_options=act_ix_checkin_report_options,
            act_ix_edit_workflow_node=act_ix_edit_workflow_node,
            act_client_postmoveto=act_client_postmoveto,
            act_ix_start_adhoc_workflow=act_ix_start_adhoc_workflow,
            act_ix_removevert=act_ix_removevert,
            act_client_wvsend=act_client_wvsend,
            act_client_changekind=act_client_changekind,
            act_ix_create_sord=act_ix_create_sord,
            act_ix_substitution_deactivate=act_ix_substitution_deactivate,
            act_client_newvert=act_client_newvert,
            act_ix_freevert=act_ix_freevert,
            act_ix_delete_config_file=act_ix_delete_config_file,
            extra2_attachment=extra2_attachment,
            act_client_changekey=act_client_changekey,
            act_client_createdoc=act_client_createdoc,
            act_client_flowerroryesno=act_client_flowerroryesno,
            act_ix_delete_workflow=act_ix_delete_workflow,
            act_client_erasedoc=act_client_erasedoc,
            act_ix_change_rs=act_ix_change_rs,
            act_client_movedoc=act_client_movedoc,
            act_client_pickpost=act_client_pickpost,
            act_client_complain=act_client_complain,
            act_client_wvlast=act_client_wvlast,
            act_client_setvert=act_client_setvert,
            act_client_removevert=act_client_removevert,
            act_client_eloend=act_client_eloend,
            act_ix_create_key=act_ix_create_key,
            extra2_wf_cancel=extra2_wf_cancel,
        )

        report_info_c.additional_properties = d
        return report_info_c

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
