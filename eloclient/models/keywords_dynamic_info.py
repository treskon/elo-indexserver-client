from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask_line import DocMaskLine
    from ..models.map_to_string import MapToString
    from ..models.sord import Sord


T = TypeVar("T", bound="KeywordsDynamicInfo")


@_attrs_define
class KeywordsDynamicInfo:
    """This Class contains parameters for the IX call
    {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)} .
     <p>
     There are two ways to execute the script for dynamic keyword lists. According to the parameter in this class, the
    one
     way or the other is chosen. The first way is to specify {@link KeywordsDynamicInfo#sord} and
     {@link KeywordsDynamicInfo#maskLineFocus}. Then, the IX passes these parameters to the script via the script-
    function
     open(ec, sord, fieldName). The other parameters will be overwritten by <code>null</code> and completely ignored.
    The
     other way is to set the fields {@link KeywordsDynamicInfo#mapData}, {@link KeywordsDynamicInfo#mapLineFocus} and
     {@link KeywordsDynamicInfo#mapScriptName}. In this case, the IX passes these parameters to the scripting function
     openMap(ec, data, fieldName). To achieve this, <code>sord</code> as well as <code>maskLineFocus</code> must be
     <code>null</code>.
     </p>

        Attributes:
            sord (Union[Unset, Sord]): <p>
                Indexing information of an archive entry.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            mask_line_focus (Union[Unset, DocMaskLine]): This class contains data for a line in the document mask.
            map_script_name (Union[Unset, str]): Determines the script to execute.
                <p>
                 This value has only an effect if sord and maskLineFocus are set to null. Setting this value requires to set the
                 values mapLineFocus and mapData also.
                 </p>
            map_line_focus (Union[Unset, str]): Represents the id of a field in a form.
            map_data (Union[Unset, MapToString]):
    """

    sord: Union[Unset, "Sord"] = UNSET
    mask_line_focus: Union[Unset, "DocMaskLine"] = UNSET
    map_script_name: Union[Unset, str] = UNSET
    map_line_focus: Union[Unset, str] = UNSET
    map_data: Union[Unset, "MapToString"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        mask_line_focus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mask_line_focus, Unset):
            mask_line_focus = self.mask_line_focus.to_dict()

        map_script_name = self.map_script_name
        map_line_focus = self.map_line_focus
        map_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_data, Unset):
            map_data = self.map_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sord is not UNSET:
            field_dict["sord"] = sord
        if mask_line_focus is not UNSET:
            field_dict["maskLineFocus"] = mask_line_focus
        if map_script_name is not UNSET:
            field_dict["mapScriptName"] = map_script_name
        if map_line_focus is not UNSET:
            field_dict["mapLineFocus"] = map_line_focus
        if map_data is not UNSET:
            field_dict["mapData"] = map_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask_line import DocMaskLine
        from ..models.map_to_string import MapToString
        from ..models.sord import Sord

        d = src_dict.copy()
        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        _mask_line_focus = d.pop("maskLineFocus", UNSET)
        mask_line_focus: Union[Unset, DocMaskLine]
        if isinstance(_mask_line_focus, Unset):
            mask_line_focus = UNSET
        else:
            mask_line_focus = DocMaskLine.from_dict(_mask_line_focus)

        map_script_name = d.pop("mapScriptName", UNSET)

        map_line_focus = d.pop("mapLineFocus", UNSET)

        _map_data = d.pop("mapData", UNSET)
        map_data: Union[Unset, MapToString]
        if isinstance(_map_data, Unset):
            map_data = UNSET
        else:
            map_data = MapToString.from_dict(_map_data)

        keywords_dynamic_info = cls(
            sord=sord,
            mask_line_focus=mask_line_focus,
            map_script_name=map_script_name,
            map_line_focus=map_line_focus,
            map_data=map_data,
        )

        keywords_dynamic_info.additional_properties = d
        return keywords_dynamic_info

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
