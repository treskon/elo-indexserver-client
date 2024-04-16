from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_data import FileData


T = TypeVar("T", bound="ExecuteScriptParams")


@_attrs_define
class ExecuteScriptParams:
    """This class is used to specify which script has to be executed in function executeScript.
    The
     script has to be an ELO Windows CLIENT OLE-Automation script.

        Attributes:
            function_params (Union[Unset, List[str]]):
            script_code (Union[Unset, FileData]): Class for the data contained in a file.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            function_name (Union[Unset, str]): Call this function in the script code.
                A function defined in script code that was supplied in a
                 previsious call can be invoked too, as long as this object does not specify scriptCode,
                 scriptString or scriptObjId.
            script_string (Union[Unset, str]): This object contains the script code to be executed as a string object.
                The string must either
                 start with "javascript:" or "vbscript:". The maximum scriptString length is 65535 UTF-8
                 characters. If this member is set, the members scriptCode and scriptObjId should be null.
            script_engine (Union[Unset, str]): This value defines the scripting engine to be used to execute the script.
                Currently, this value
                 must be null or empty or "EloixAuto". If the value is null or empty, EloixAuto is used by
                 default.
            script_obj_id (Union[Unset, str]): If the script to be executed is available in the ELO archive, this member can
                specify the
                object ID (or ARCPATH: - see checkoutSord) of the script document. The file is assumed to be
                 encoded in characterset ISO-8859-1, if it does not start with a BOM. If this member is set, the
                 members scriptCode and scriptString should be null.
    """

    function_params: Union[Unset, List[str]] = UNSET
    script_code: Union[Unset, "FileData"] = UNSET
    function_name: Union[Unset, str] = UNSET
    script_string: Union[Unset, str] = UNSET
    script_engine: Union[Unset, str] = UNSET
    script_obj_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.function_params, Unset):
            function_params = self.function_params

        script_code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.script_code, Unset):
            script_code = self.script_code.to_dict()

        function_name = self.function_name

        script_string = self.script_string

        script_engine = self.script_engine

        script_obj_id = self.script_obj_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function_params is not UNSET:
            field_dict["functionParams"] = function_params
        if script_code is not UNSET:
            field_dict["scriptCode"] = script_code
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if script_string is not UNSET:
            field_dict["scriptString"] = script_string
        if script_engine is not UNSET:
            field_dict["scriptEngine"] = script_engine
        if script_obj_id is not UNSET:
            field_dict["scriptObjId"] = script_obj_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_data import FileData

        d = src_dict.copy()
        function_params = cast(List[str], d.pop("functionParams", UNSET))

        _script_code = d.pop("scriptCode", UNSET)
        script_code: Union[Unset, FileData]
        if isinstance(_script_code, Unset):
            script_code = UNSET
        else:
            script_code = FileData.from_dict(_script_code)

        function_name = d.pop("functionName", UNSET)

        script_string = d.pop("scriptString", UNSET)

        script_engine = d.pop("scriptEngine", UNSET)

        script_obj_id = d.pop("scriptObjId", UNSET)

        execute_script_params = cls(
            function_params=function_params,
            script_code=script_code,
            function_name=function_name,
            script_string=script_string,
            script_engine=script_engine,
            script_obj_id=script_obj_id,
        )

        execute_script_params.additional_properties = d
        return execute_script_params

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
