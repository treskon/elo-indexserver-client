from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IXExceptionC")


@_attrs_define
class IXExceptionC:
    """This class contains constant definitions for Indexserver error numbers used in Indexserver exceptions.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            server_error (Union[Unset, int]): Problem in the server configuration.
            unsupported_protocol_version (Union[Unset, int]): Unsupported protocol version. This error is thrown, if the
                protocol version cannot be negotiated.
                A reason for this
                 can be different major release versions of client and server.
            invalid_license (Union[Unset, int]): License key is invalid.
            invalid_param (Union[Unset, int]): Invalid parameter was given.
            invalid_session (Union[Unset, int]): Session is not (or no longer) valid.
            temp_problem_old (Union[Unset, int]): Temporarily problem, a later try should succeed. The value of TEMP_PROBLEM
                must be changed in IX 8.00.
                054, because
                 the current client libraries recognize it as an exception where relogin is required. This could lead to the
                effect
                 described in TTS001661.
            temp_problem (Union[Unset, int]): Temporarily problem, a later try should succeed.
            invalid_crypt_key (Union[Unset, int]): Encryption key must be set before documents can be encrypted.
            syntax_error (Union[Unset, int]): Syntax error e.g. in search request.
            password_denied (Union[Unset, int]): The given password violates the password rules.
                The passord rules are stored in the user profile value
                 {@link UserProfileC#KEY_PASSWORD_RULES}.
            already_exists (Union[Unset, int]): Specified object to be created already exists.
            locked (Union[Unset, int]): Specified data is locked.
            not_found (Union[Unset, int]): Specified data could not be found.
            access_denied (Union[Unset, int]): Access to the specified object was denied, there are rights missing.
            not_empty (Union[Unset, int]): Specified data could not be found.
            script_error (Union[Unset, int]): An error thrown in a script file is passed to the client application with this
                error code. E.g.
                [ELOIX:6000]
                 "Message text thrown in script".
            not_ix (Union[Unset, int]): Not a ELO IX Exception
            internal (Union[Unset, int]): Internal error.
            unsupported_function (Union[Unset, int]): Function is not currently supported.
            prohibited_operation (Union[Unset, int]): The called function cannot be executed on this object
    """

    server_error: Union[Unset, int] = UNSET
    unsupported_protocol_version: Union[Unset, int] = UNSET
    invalid_license: Union[Unset, int] = UNSET
    invalid_param: Union[Unset, int] = UNSET
    invalid_session: Union[Unset, int] = UNSET
    temp_problem_old: Union[Unset, int] = UNSET
    temp_problem: Union[Unset, int] = UNSET
    invalid_crypt_key: Union[Unset, int] = UNSET
    syntax_error: Union[Unset, int] = UNSET
    password_denied: Union[Unset, int] = UNSET
    already_exists: Union[Unset, int] = UNSET
    locked: Union[Unset, int] = UNSET
    not_found: Union[Unset, int] = UNSET
    access_denied: Union[Unset, int] = UNSET
    not_empty: Union[Unset, int] = UNSET
    script_error: Union[Unset, int] = UNSET
    not_ix: Union[Unset, int] = UNSET
    internal: Union[Unset, int] = UNSET
    unsupported_function: Union[Unset, int] = UNSET
    prohibited_operation: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_error = self.server_error
        unsupported_protocol_version = self.unsupported_protocol_version
        invalid_license = self.invalid_license
        invalid_param = self.invalid_param
        invalid_session = self.invalid_session
        temp_problem_old = self.temp_problem_old
        temp_problem = self.temp_problem
        invalid_crypt_key = self.invalid_crypt_key
        syntax_error = self.syntax_error
        password_denied = self.password_denied
        already_exists = self.already_exists
        locked = self.locked
        not_found = self.not_found
        access_denied = self.access_denied
        not_empty = self.not_empty
        script_error = self.script_error
        not_ix = self.not_ix
        internal = self.internal
        unsupported_function = self.unsupported_function
        prohibited_operation = self.prohibited_operation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_error is not UNSET:
            field_dict["SERVER_ERROR"] = server_error
        if unsupported_protocol_version is not UNSET:
            field_dict["UNSUPPORTED_PROTOCOL_VERSION"] = unsupported_protocol_version
        if invalid_license is not UNSET:
            field_dict["INVALID_LICENSE"] = invalid_license
        if invalid_param is not UNSET:
            field_dict["INVALID_PARAM"] = invalid_param
        if invalid_session is not UNSET:
            field_dict["INVALID_SESSION"] = invalid_session
        if temp_problem_old is not UNSET:
            field_dict["TEMP_PROBLEM_OLD"] = temp_problem_old
        if temp_problem is not UNSET:
            field_dict["TEMP_PROBLEM"] = temp_problem
        if invalid_crypt_key is not UNSET:
            field_dict["INVALID_CRYPT_KEY"] = invalid_crypt_key
        if syntax_error is not UNSET:
            field_dict["SYNTAX_ERROR"] = syntax_error
        if password_denied is not UNSET:
            field_dict["PASSWORD_DENIED"] = password_denied
        if already_exists is not UNSET:
            field_dict["ALREADY_EXISTS"] = already_exists
        if locked is not UNSET:
            field_dict["LOCKED"] = locked
        if not_found is not UNSET:
            field_dict["NOT_FOUND"] = not_found
        if access_denied is not UNSET:
            field_dict["ACCESS_DENIED"] = access_denied
        if not_empty is not UNSET:
            field_dict["NOT_EMPTY"] = not_empty
        if script_error is not UNSET:
            field_dict["SCRIPT_ERROR"] = script_error
        if not_ix is not UNSET:
            field_dict["NOT_IX"] = not_ix
        if internal is not UNSET:
            field_dict["INTERNAL"] = internal
        if unsupported_function is not UNSET:
            field_dict["UNSUPPORTED_FUNCTION"] = unsupported_function
        if prohibited_operation is not UNSET:
            field_dict["PROHIBITED_OPERATION"] = prohibited_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        server_error = d.pop("SERVER_ERROR", UNSET)

        unsupported_protocol_version = d.pop("UNSUPPORTED_PROTOCOL_VERSION", UNSET)

        invalid_license = d.pop("INVALID_LICENSE", UNSET)

        invalid_param = d.pop("INVALID_PARAM", UNSET)

        invalid_session = d.pop("INVALID_SESSION", UNSET)

        temp_problem_old = d.pop("TEMP_PROBLEM_OLD", UNSET)

        temp_problem = d.pop("TEMP_PROBLEM", UNSET)

        invalid_crypt_key = d.pop("INVALID_CRYPT_KEY", UNSET)

        syntax_error = d.pop("SYNTAX_ERROR", UNSET)

        password_denied = d.pop("PASSWORD_DENIED", UNSET)

        already_exists = d.pop("ALREADY_EXISTS", UNSET)

        locked = d.pop("LOCKED", UNSET)

        not_found = d.pop("NOT_FOUND", UNSET)

        access_denied = d.pop("ACCESS_DENIED", UNSET)

        not_empty = d.pop("NOT_EMPTY", UNSET)

        script_error = d.pop("SCRIPT_ERROR", UNSET)

        not_ix = d.pop("NOT_IX", UNSET)

        internal = d.pop("INTERNAL", UNSET)

        unsupported_function = d.pop("UNSUPPORTED_FUNCTION", UNSET)

        prohibited_operation = d.pop("PROHIBITED_OPERATION", UNSET)

        ix_exception_c = cls(
            server_error=server_error,
            unsupported_protocol_version=unsupported_protocol_version,
            invalid_license=invalid_license,
            invalid_param=invalid_param,
            invalid_session=invalid_session,
            temp_problem_old=temp_problem_old,
            temp_problem=temp_problem,
            invalid_crypt_key=invalid_crypt_key,
            syntax_error=syntax_error,
            password_denied=password_denied,
            already_exists=already_exists,
            locked=locked,
            not_found=not_found,
            access_denied=access_denied,
            not_empty=not_empty,
            script_error=script_error,
            not_ix=not_ix,
            internal=internal,
            unsupported_function=unsupported_function,
            prohibited_operation=prohibited_operation,
        )

        ix_exception_c.additional_properties = d
        return ix_exception_c

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
