from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocMaskLineC")


@_attrs_define
class DocMaskLineC:
    """<p>
    Constants for class <code>DocMaskLine</code>
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            name_mainscale (Union[Unset, str]): Internally used by JavaClient.
            mb_version (Union[Unset, str]):
            mb_translate (Union[Unset, str]):
            ln_acl (Union[Unset, int]): ACL length
            mb_important (Union[Unset, str]):
            type_number_f6 (Union[Unset, int]): Index line contains a number value with six digits after the decimal point.
            mb_read_only (Union[Unset, str]):
            id_personaldata_uid (Union[Unset, int]): Index line used to mark a folder or document as personal data record.
            mb_tab_order (Union[Unset, str]):
            id_link (Union[Unset, int]): Index line ID of links. Sord.linksGoOut and Sord.
                linksComeIn provide a more convinient way to
                 access links. Links can be added and removed with the functions linkSords resp. unlinkSords.
            type_dummy (Union[Unset, int]): Index line contains a dummy entry which should not be displayed.
            key_email_entryid (Union[Unset, str]): Index line key for an internal mail ID. Use this constant as value for
                {@link DocMaskLine#key}.
            min_id_hidden_value (Union[Unset, int]):
            mb_postfix_asterix (Union[Unset, str]):
            mb_acl (Union[Unset, str]): Member bit: ACL
            type_float (Union[Unset, int]): Index line contains a floating point number value with 7 significant digits.
                This type can only
                 be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}. To assign a value
                 of this type to {@link ObjKey#data}, the String representation has to conform to the
                 Float.toString() method of Java. Use dot to separate the fraction part and character 'E' to
                 prefix the exponent.
            key_email_cc (Union[Unset, str]): Index line key for mail CC addresses. Use this constant as value for {@link
                DocMaskLine#key}.
            key_email_from (Union[Unset, str]): Index line key for mail sender address. Use this constant as value for
                {@link DocMaskLine#key}.
            type_az (Union[Unset, int]): Index line contains a reference number ("Aktenzeichen").
            type_long (Union[Unset, int]): Index line contains a number value without fraction in the range of (-2^63) to
                (2^63)-1.
                This
                 type can only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}.
            type_number_f1 (Union[Unset, int]): Index line contains a number value with one digit after the decimal point.
            type_number_f2 (Union[Unset, int]): Index line contains a number value with one digit after the decimal point.
            id_mainscale (Union[Unset, int]): Internally used by JavaClient.
            max_id_hidden_value (Union[Unset, int]):
            type_number_f4 (Union[Unset, int]): Index line contains a number value of with four digits after the decimal
                point.
            type_number_f0 (Union[Unset, int]): Index line contains a number value with an arbitrary number of fraction
                digits.
                The value is
                 internally stored with a padding of &amp; (positive numbers) or @ (negative numbers). This
                 gives the possibility to search over an interval of numeric values, e. b. search for "1 ... 12"
                 finds objects with index values 1,2,3,4,...12. The number must be formatted according to the
                 locale information given in the ClientInfo object. With this type, the user is responsible to
                 enter always the same number of fraction digits. Otherwise, a search over a number range will
                 not return the correct results. The meaning of this field was changed in 8.00.032. The meaning
                 before was a field without any fraction digits.
            name_personaldata_deleteat (Union[Unset, str]): Index line used to specify a delete date for personal data.
                The Value has to be in ISO 8601
                 format without separators and time section. Example value 20180223 specifies 23-Feb-2018.
            mb_acl_items (Union[Unset, str]):
            mb_flags (Union[Unset, str]): Member bit: Line flags
            key_email_to (Union[Unset, str]): Index line key for mail receiver addresses.
                Use this constant as value for
                 {@link DocMaskLine#key}.
            type_iso_date (Union[Unset, int]): Index line contains a date in ISO format.
            dockey_vsl (Union[Unset, int]): Index line ID to store informations used by "Versendemappe".
            key_email_conversationid (Union[Unset, str]): Index line key for a mail's internal conversation ID.
                Use this constant as value for
                 {@link DocMaskLine#key}.
            type_thes (Union[Unset, int]): Thesaurus
            min_id_reserved (Union[Unset, int]): Minimum ID for reserved keywording field
            field_type_type_id (Union[Unset, int]): Used to check wether a correct constant is used.
            mb_hidden (Union[Unset, str]):
            key_email_bcc (Union[Unset, str]): Index line key for mail BCC addresses. Use this constant as value for {@link
                DocMaskLine#key}.
            name_link (Union[Unset, str]): Index line name of links.
            mb_allowed_mask_ids_for_keywording_relation (Union[Unset, str]): Member bit: allowedMaskIds
            type_list (Union[Unset, int]): Index line contains a list entry.
            name_personaldata_uid (Union[Unset, str]): Index line used to mark a folder or document as personal data record.
                Values should uniquely
                 identify the person that belongs to the object. This index line can be added to any Sord and is
                 not available in a keywording form (DocMask).
            docname_vsl (Union[Unset, str]): Index line name to store informations used by "Versendemappe".
            id_filename (Union[Unset, int]): Index line ID of original file name
            mb_only_buzzwords (Union[Unset, str]):
            mb_prefix_asterix (Union[Unset, str]):
            type_double (Union[Unset, int]): Index line contains a floating point number value with 15 significant digits.
                This type can
                 only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}. To assign a
                 value of this type to {@link ObjKey#data}, the String representation has to conform to the
                 Double.toString() method of Java. Use dot to separate the fraction part and character 'E' to
                 prefix the exponent.
            type_date (Union[Unset, int]): Index line contains a date.
            type_integer (Union[Unset, int]): Index line contains a number value without fraction in the range of (-2^31) to
                (2^31)-1.
                This
                 type can only be used for keywording forms with {@link DocMaskC#DATA_ORGANISATION_TABLE}.
            id_personaldata_deleteat (Union[Unset, int]): Index line used to specify a delete date for personal data.
            type_text (Union[Unset, int]): Index line contains text information.
            max_id_docmask_line (Union[Unset, int]): This constant defines a limit for ObjKey.id values. The following table
                defines which ObjKey.
                id
                 values are allowed.
                 <p>
                 <table border="2" summary="">
                 <tr>
                 <td>ObjKey.id</td>
                 <td>Comment</td>
                 </tr>
                 <tr>
                 <td>0 ... MAX_ID_DOCMASK_LINE</td>
                 <td>ObjKeys with ObjKey.data.length &gt; 1 allowed.</td>
                 </tr>
                 <tr>
                 <td>MIN_ID_RESERVED ... MAX_ID_RESERVED</td>
                 <td>ObjKeys for Special purposes, e.g. ID_FILE_NAME</td>
                 </tr>
                 </table>
                 </p>
                 <p>
                 <table border="2">
                 <tr>
                 <td>Symbol</td>
                 <td>Value</td>
                 </tr>
                 <tr>
                 <td>MAX_ID_DOCMASK_LINE</td>
                 <td>199</td>
                 </tr>
                 <tr>
                 <td>MAX_ID_VALUE_ARRAY</td>
                 <td>199</td>
                 </tr>
                 <tr>
                 <td>MIN_ID_RESERVED</td>
                 <td>50</td>
                 </tr>
                 <tr>
                 <td>MAX_ID_RESERVED</td>
                 <td>59</td>
                 </tr>
                 </table>
                 </p>
            type_user (Union[Unset, int]): Index line contains a user name.
            name_filename (Union[Unset, str]): Index line name of original file name
            mb_type (Union[Unset, str]): Member bit: The type of the line information.
                This can be one of the
                 <code>DocMaskLineC.LINETYPE_*</code> constants.
            type_relation (Union[Unset, int]): Index line contains a relation.
                A Relation consists of a {@link Sord#guid} which references a
                 {@link Sord}. with a allowed DocMask {@link DocMaskDetails#keywordingRelationAllowed}.
            secondarytypes (Union[Unset, int]): EIX-2820: This constant defines secondary-types for CMIS.
            mb_next_tab (Union[Unset, str]):
            type_number (Union[Unset, int]): Index line contains a number.
                The number is internally stored as a string value without any
                 padding. Thus it is not possible to search over an interval. Use one of the TYPE_NUMBER_F*
                 types to be able to search over intervals. The number must be formatted according to the locale
                 information of the server.
            key_email_postboxpath (Union[Unset, str]): Index line key for mailbox path. Use this constant as value for
                {@link DocMaskLine#key}.
            max_id_reserved (Union[Unset, int]): Maximum ID for reserved keywording field
            max_id_value_array (Union[Unset, int]): This constant defines a limit for ObjKey.id values.
            default (Union[Unset, int]): Default ist text
    """

    name_mainscale: Union[Unset, str] = UNSET
    mb_version: Union[Unset, str] = UNSET
    mb_translate: Union[Unset, str] = UNSET
    ln_acl: Union[Unset, int] = UNSET
    mb_important: Union[Unset, str] = UNSET
    type_number_f6: Union[Unset, int] = UNSET
    mb_read_only: Union[Unset, str] = UNSET
    id_personaldata_uid: Union[Unset, int] = UNSET
    mb_tab_order: Union[Unset, str] = UNSET
    id_link: Union[Unset, int] = UNSET
    type_dummy: Union[Unset, int] = UNSET
    key_email_entryid: Union[Unset, str] = UNSET
    min_id_hidden_value: Union[Unset, int] = UNSET
    mb_postfix_asterix: Union[Unset, str] = UNSET
    mb_acl: Union[Unset, str] = UNSET
    type_float: Union[Unset, int] = UNSET
    key_email_cc: Union[Unset, str] = UNSET
    key_email_from: Union[Unset, str] = UNSET
    type_az: Union[Unset, int] = UNSET
    type_long: Union[Unset, int] = UNSET
    type_number_f1: Union[Unset, int] = UNSET
    type_number_f2: Union[Unset, int] = UNSET
    id_mainscale: Union[Unset, int] = UNSET
    max_id_hidden_value: Union[Unset, int] = UNSET
    type_number_f4: Union[Unset, int] = UNSET
    type_number_f0: Union[Unset, int] = UNSET
    name_personaldata_deleteat: Union[Unset, str] = UNSET
    mb_acl_items: Union[Unset, str] = UNSET
    mb_flags: Union[Unset, str] = UNSET
    key_email_to: Union[Unset, str] = UNSET
    type_iso_date: Union[Unset, int] = UNSET
    dockey_vsl: Union[Unset, int] = UNSET
    key_email_conversationid: Union[Unset, str] = UNSET
    type_thes: Union[Unset, int] = UNSET
    min_id_reserved: Union[Unset, int] = UNSET
    field_type_type_id: Union[Unset, int] = UNSET
    mb_hidden: Union[Unset, str] = UNSET
    key_email_bcc: Union[Unset, str] = UNSET
    name_link: Union[Unset, str] = UNSET
    mb_allowed_mask_ids_for_keywording_relation: Union[Unset, str] = UNSET
    type_list: Union[Unset, int] = UNSET
    name_personaldata_uid: Union[Unset, str] = UNSET
    docname_vsl: Union[Unset, str] = UNSET
    id_filename: Union[Unset, int] = UNSET
    mb_only_buzzwords: Union[Unset, str] = UNSET
    mb_prefix_asterix: Union[Unset, str] = UNSET
    type_double: Union[Unset, int] = UNSET
    type_date: Union[Unset, int] = UNSET
    type_integer: Union[Unset, int] = UNSET
    id_personaldata_deleteat: Union[Unset, int] = UNSET
    type_text: Union[Unset, int] = UNSET
    max_id_docmask_line: Union[Unset, int] = UNSET
    type_user: Union[Unset, int] = UNSET
    name_filename: Union[Unset, str] = UNSET
    mb_type: Union[Unset, str] = UNSET
    type_relation: Union[Unset, int] = UNSET
    secondarytypes: Union[Unset, int] = UNSET
    mb_next_tab: Union[Unset, str] = UNSET
    type_number: Union[Unset, int] = UNSET
    key_email_postboxpath: Union[Unset, str] = UNSET
    max_id_reserved: Union[Unset, int] = UNSET
    max_id_value_array: Union[Unset, int] = UNSET
    default: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name_mainscale = self.name_mainscale

        mb_version = self.mb_version

        mb_translate = self.mb_translate

        ln_acl = self.ln_acl

        mb_important = self.mb_important

        type_number_f6 = self.type_number_f6

        mb_read_only = self.mb_read_only

        id_personaldata_uid = self.id_personaldata_uid

        mb_tab_order = self.mb_tab_order

        id_link = self.id_link

        type_dummy = self.type_dummy

        key_email_entryid = self.key_email_entryid

        min_id_hidden_value = self.min_id_hidden_value

        mb_postfix_asterix = self.mb_postfix_asterix

        mb_acl = self.mb_acl

        type_float = self.type_float

        key_email_cc = self.key_email_cc

        key_email_from = self.key_email_from

        type_az = self.type_az

        type_long = self.type_long

        type_number_f1 = self.type_number_f1

        type_number_f2 = self.type_number_f2

        id_mainscale = self.id_mainscale

        max_id_hidden_value = self.max_id_hidden_value

        type_number_f4 = self.type_number_f4

        type_number_f0 = self.type_number_f0

        name_personaldata_deleteat = self.name_personaldata_deleteat

        mb_acl_items = self.mb_acl_items

        mb_flags = self.mb_flags

        key_email_to = self.key_email_to

        type_iso_date = self.type_iso_date

        dockey_vsl = self.dockey_vsl

        key_email_conversationid = self.key_email_conversationid

        type_thes = self.type_thes

        min_id_reserved = self.min_id_reserved

        field_type_type_id = self.field_type_type_id

        mb_hidden = self.mb_hidden

        key_email_bcc = self.key_email_bcc

        name_link = self.name_link

        mb_allowed_mask_ids_for_keywording_relation = self.mb_allowed_mask_ids_for_keywording_relation

        type_list = self.type_list

        name_personaldata_uid = self.name_personaldata_uid

        docname_vsl = self.docname_vsl

        id_filename = self.id_filename

        mb_only_buzzwords = self.mb_only_buzzwords

        mb_prefix_asterix = self.mb_prefix_asterix

        type_double = self.type_double

        type_date = self.type_date

        type_integer = self.type_integer

        id_personaldata_deleteat = self.id_personaldata_deleteat

        type_text = self.type_text

        max_id_docmask_line = self.max_id_docmask_line

        type_user = self.type_user

        name_filename = self.name_filename

        mb_type = self.mb_type

        type_relation = self.type_relation

        secondarytypes = self.secondarytypes

        mb_next_tab = self.mb_next_tab

        type_number = self.type_number

        key_email_postboxpath = self.key_email_postboxpath

        max_id_reserved = self.max_id_reserved

        max_id_value_array = self.max_id_value_array

        default = self.default

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_mainscale is not UNSET:
            field_dict["NAME_MAINSCALE"] = name_mainscale
        if mb_version is not UNSET:
            field_dict["mbVersion"] = mb_version
        if mb_translate is not UNSET:
            field_dict["mbTranslate"] = mb_translate
        if ln_acl is not UNSET:
            field_dict["lnAcl"] = ln_acl
        if mb_important is not UNSET:
            field_dict["mbImportant"] = mb_important
        if type_number_f6 is not UNSET:
            field_dict["TYPE_NUMBER_F6"] = type_number_f6
        if mb_read_only is not UNSET:
            field_dict["mbReadOnly"] = mb_read_only
        if id_personaldata_uid is not UNSET:
            field_dict["ID_PERSONALDATA_UID"] = id_personaldata_uid
        if mb_tab_order is not UNSET:
            field_dict["mbTabOrder"] = mb_tab_order
        if id_link is not UNSET:
            field_dict["ID_LINK"] = id_link
        if type_dummy is not UNSET:
            field_dict["TYPE_DUMMY"] = type_dummy
        if key_email_entryid is not UNSET:
            field_dict["KEY_EMAIL_ENTRYID"] = key_email_entryid
        if min_id_hidden_value is not UNSET:
            field_dict["MIN_ID_HIDDEN_VALUE"] = min_id_hidden_value
        if mb_postfix_asterix is not UNSET:
            field_dict["mbPostfixAsterix"] = mb_postfix_asterix
        if mb_acl is not UNSET:
            field_dict["mbAcl"] = mb_acl
        if type_float is not UNSET:
            field_dict["TYPE_FLOAT"] = type_float
        if key_email_cc is not UNSET:
            field_dict["KEY_EMAIL_CC"] = key_email_cc
        if key_email_from is not UNSET:
            field_dict["KEY_EMAIL_FROM"] = key_email_from
        if type_az is not UNSET:
            field_dict["TYPE_AZ"] = type_az
        if type_long is not UNSET:
            field_dict["TYPE_LONG"] = type_long
        if type_number_f1 is not UNSET:
            field_dict["TYPE_NUMBER_F1"] = type_number_f1
        if type_number_f2 is not UNSET:
            field_dict["TYPE_NUMBER_F2"] = type_number_f2
        if id_mainscale is not UNSET:
            field_dict["ID_MAINSCALE"] = id_mainscale
        if max_id_hidden_value is not UNSET:
            field_dict["MAX_ID_HIDDEN_VALUE"] = max_id_hidden_value
        if type_number_f4 is not UNSET:
            field_dict["TYPE_NUMBER_F4"] = type_number_f4
        if type_number_f0 is not UNSET:
            field_dict["TYPE_NUMBER_F0"] = type_number_f0
        if name_personaldata_deleteat is not UNSET:
            field_dict["NAME_PERSONALDATA_DELETEAT"] = name_personaldata_deleteat
        if mb_acl_items is not UNSET:
            field_dict["mbAclItems"] = mb_acl_items
        if mb_flags is not UNSET:
            field_dict["mbFlags"] = mb_flags
        if key_email_to is not UNSET:
            field_dict["KEY_EMAIL_TO"] = key_email_to
        if type_iso_date is not UNSET:
            field_dict["TYPE_ISO_DATE"] = type_iso_date
        if dockey_vsl is not UNSET:
            field_dict["DOCKEY_VSL"] = dockey_vsl
        if key_email_conversationid is not UNSET:
            field_dict["KEY_EMAIL_CONVERSATIONID"] = key_email_conversationid
        if type_thes is not UNSET:
            field_dict["TYPE_THES"] = type_thes
        if min_id_reserved is not UNSET:
            field_dict["MIN_ID_RESERVED"] = min_id_reserved
        if field_type_type_id is not UNSET:
            field_dict["_TYPE_TYPE_ID"] = field_type_type_id
        if mb_hidden is not UNSET:
            field_dict["mbHidden"] = mb_hidden
        if key_email_bcc is not UNSET:
            field_dict["KEY_EMAIL_BCC"] = key_email_bcc
        if name_link is not UNSET:
            field_dict["NAME_LINK"] = name_link
        if mb_allowed_mask_ids_for_keywording_relation is not UNSET:
            field_dict["mbAllowedMaskIdsForKeywordingRelation"] = mb_allowed_mask_ids_for_keywording_relation
        if type_list is not UNSET:
            field_dict["TYPE_LIST"] = type_list
        if name_personaldata_uid is not UNSET:
            field_dict["NAME_PERSONALDATA_UID"] = name_personaldata_uid
        if docname_vsl is not UNSET:
            field_dict["DOCNAME_VSL"] = docname_vsl
        if id_filename is not UNSET:
            field_dict["ID_FILENAME"] = id_filename
        if mb_only_buzzwords is not UNSET:
            field_dict["mbOnlyBuzzwords"] = mb_only_buzzwords
        if mb_prefix_asterix is not UNSET:
            field_dict["mbPrefixAsterix"] = mb_prefix_asterix
        if type_double is not UNSET:
            field_dict["TYPE_DOUBLE"] = type_double
        if type_date is not UNSET:
            field_dict["TYPE_DATE"] = type_date
        if type_integer is not UNSET:
            field_dict["TYPE_INTEGER"] = type_integer
        if id_personaldata_deleteat is not UNSET:
            field_dict["ID_PERSONALDATA_DELETEAT"] = id_personaldata_deleteat
        if type_text is not UNSET:
            field_dict["TYPE_TEXT"] = type_text
        if max_id_docmask_line is not UNSET:
            field_dict["MAX_ID_DOCMASK_LINE"] = max_id_docmask_line
        if type_user is not UNSET:
            field_dict["TYPE_USER"] = type_user
        if name_filename is not UNSET:
            field_dict["NAME_FILENAME"] = name_filename
        if mb_type is not UNSET:
            field_dict["mbType"] = mb_type
        if type_relation is not UNSET:
            field_dict["TYPE_RELATION"] = type_relation
        if secondarytypes is not UNSET:
            field_dict["SECONDARYTYPES"] = secondarytypes
        if mb_next_tab is not UNSET:
            field_dict["mbNextTab"] = mb_next_tab
        if type_number is not UNSET:
            field_dict["TYPE_NUMBER"] = type_number
        if key_email_postboxpath is not UNSET:
            field_dict["KEY_EMAIL_POSTBOXPATH"] = key_email_postboxpath
        if max_id_reserved is not UNSET:
            field_dict["MAX_ID_RESERVED"] = max_id_reserved
        if max_id_value_array is not UNSET:
            field_dict["MAX_ID_VALUE_ARRAY"] = max_id_value_array
        if default is not UNSET:
            field_dict["DEFAULT"] = default

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name_mainscale = d.pop("NAME_MAINSCALE", UNSET)

        mb_version = d.pop("mbVersion", UNSET)

        mb_translate = d.pop("mbTranslate", UNSET)

        ln_acl = d.pop("lnAcl", UNSET)

        mb_important = d.pop("mbImportant", UNSET)

        type_number_f6 = d.pop("TYPE_NUMBER_F6", UNSET)

        mb_read_only = d.pop("mbReadOnly", UNSET)

        id_personaldata_uid = d.pop("ID_PERSONALDATA_UID", UNSET)

        mb_tab_order = d.pop("mbTabOrder", UNSET)

        id_link = d.pop("ID_LINK", UNSET)

        type_dummy = d.pop("TYPE_DUMMY", UNSET)

        key_email_entryid = d.pop("KEY_EMAIL_ENTRYID", UNSET)

        min_id_hidden_value = d.pop("MIN_ID_HIDDEN_VALUE", UNSET)

        mb_postfix_asterix = d.pop("mbPostfixAsterix", UNSET)

        mb_acl = d.pop("mbAcl", UNSET)

        type_float = d.pop("TYPE_FLOAT", UNSET)

        key_email_cc = d.pop("KEY_EMAIL_CC", UNSET)

        key_email_from = d.pop("KEY_EMAIL_FROM", UNSET)

        type_az = d.pop("TYPE_AZ", UNSET)

        type_long = d.pop("TYPE_LONG", UNSET)

        type_number_f1 = d.pop("TYPE_NUMBER_F1", UNSET)

        type_number_f2 = d.pop("TYPE_NUMBER_F2", UNSET)

        id_mainscale = d.pop("ID_MAINSCALE", UNSET)

        max_id_hidden_value = d.pop("MAX_ID_HIDDEN_VALUE", UNSET)

        type_number_f4 = d.pop("TYPE_NUMBER_F4", UNSET)

        type_number_f0 = d.pop("TYPE_NUMBER_F0", UNSET)

        name_personaldata_deleteat = d.pop("NAME_PERSONALDATA_DELETEAT", UNSET)

        mb_acl_items = d.pop("mbAclItems", UNSET)

        mb_flags = d.pop("mbFlags", UNSET)

        key_email_to = d.pop("KEY_EMAIL_TO", UNSET)

        type_iso_date = d.pop("TYPE_ISO_DATE", UNSET)

        dockey_vsl = d.pop("DOCKEY_VSL", UNSET)

        key_email_conversationid = d.pop("KEY_EMAIL_CONVERSATIONID", UNSET)

        type_thes = d.pop("TYPE_THES", UNSET)

        min_id_reserved = d.pop("MIN_ID_RESERVED", UNSET)

        field_type_type_id = d.pop("_TYPE_TYPE_ID", UNSET)

        mb_hidden = d.pop("mbHidden", UNSET)

        key_email_bcc = d.pop("KEY_EMAIL_BCC", UNSET)

        name_link = d.pop("NAME_LINK", UNSET)

        mb_allowed_mask_ids_for_keywording_relation = d.pop("mbAllowedMaskIdsForKeywordingRelation", UNSET)

        type_list = d.pop("TYPE_LIST", UNSET)

        name_personaldata_uid = d.pop("NAME_PERSONALDATA_UID", UNSET)

        docname_vsl = d.pop("DOCNAME_VSL", UNSET)

        id_filename = d.pop("ID_FILENAME", UNSET)

        mb_only_buzzwords = d.pop("mbOnlyBuzzwords", UNSET)

        mb_prefix_asterix = d.pop("mbPrefixAsterix", UNSET)

        type_double = d.pop("TYPE_DOUBLE", UNSET)

        type_date = d.pop("TYPE_DATE", UNSET)

        type_integer = d.pop("TYPE_INTEGER", UNSET)

        id_personaldata_deleteat = d.pop("ID_PERSONALDATA_DELETEAT", UNSET)

        type_text = d.pop("TYPE_TEXT", UNSET)

        max_id_docmask_line = d.pop("MAX_ID_DOCMASK_LINE", UNSET)

        type_user = d.pop("TYPE_USER", UNSET)

        name_filename = d.pop("NAME_FILENAME", UNSET)

        mb_type = d.pop("mbType", UNSET)

        type_relation = d.pop("TYPE_RELATION", UNSET)

        secondarytypes = d.pop("SECONDARYTYPES", UNSET)

        mb_next_tab = d.pop("mbNextTab", UNSET)

        type_number = d.pop("TYPE_NUMBER", UNSET)

        key_email_postboxpath = d.pop("KEY_EMAIL_POSTBOXPATH", UNSET)

        max_id_reserved = d.pop("MAX_ID_RESERVED", UNSET)

        max_id_value_array = d.pop("MAX_ID_VALUE_ARRAY", UNSET)

        default = d.pop("DEFAULT", UNSET)

        doc_mask_line_c = cls(
            name_mainscale=name_mainscale,
            mb_version=mb_version,
            mb_translate=mb_translate,
            ln_acl=ln_acl,
            mb_important=mb_important,
            type_number_f6=type_number_f6,
            mb_read_only=mb_read_only,
            id_personaldata_uid=id_personaldata_uid,
            mb_tab_order=mb_tab_order,
            id_link=id_link,
            type_dummy=type_dummy,
            key_email_entryid=key_email_entryid,
            min_id_hidden_value=min_id_hidden_value,
            mb_postfix_asterix=mb_postfix_asterix,
            mb_acl=mb_acl,
            type_float=type_float,
            key_email_cc=key_email_cc,
            key_email_from=key_email_from,
            type_az=type_az,
            type_long=type_long,
            type_number_f1=type_number_f1,
            type_number_f2=type_number_f2,
            id_mainscale=id_mainscale,
            max_id_hidden_value=max_id_hidden_value,
            type_number_f4=type_number_f4,
            type_number_f0=type_number_f0,
            name_personaldata_deleteat=name_personaldata_deleteat,
            mb_acl_items=mb_acl_items,
            mb_flags=mb_flags,
            key_email_to=key_email_to,
            type_iso_date=type_iso_date,
            dockey_vsl=dockey_vsl,
            key_email_conversationid=key_email_conversationid,
            type_thes=type_thes,
            min_id_reserved=min_id_reserved,
            field_type_type_id=field_type_type_id,
            mb_hidden=mb_hidden,
            key_email_bcc=key_email_bcc,
            name_link=name_link,
            mb_allowed_mask_ids_for_keywording_relation=mb_allowed_mask_ids_for_keywording_relation,
            type_list=type_list,
            name_personaldata_uid=name_personaldata_uid,
            docname_vsl=docname_vsl,
            id_filename=id_filename,
            mb_only_buzzwords=mb_only_buzzwords,
            mb_prefix_asterix=mb_prefix_asterix,
            type_double=type_double,
            type_date=type_date,
            type_integer=type_integer,
            id_personaldata_deleteat=id_personaldata_deleteat,
            type_text=type_text,
            max_id_docmask_line=max_id_docmask_line,
            type_user=type_user,
            name_filename=name_filename,
            mb_type=mb_type,
            type_relation=type_relation,
            secondarytypes=secondarytypes,
            mb_next_tab=mb_next_tab,
            type_number=type_number,
            key_email_postboxpath=key_email_postboxpath,
            max_id_reserved=max_id_reserved,
            max_id_value_array=max_id_value_array,
            default=default,
        )

        doc_mask_line_c.additional_properties = d
        return doc_mask_line_c

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
