from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect_assoc import AspectAssoc
    from ..models.aspect_line import AspectLine
    from ..models.doc_mask_line import DocMaskLine
    from ..models.map_to_string import MapToString
    from ..models.sord import Sord


T = TypeVar("T", bound="KeywordsDynamicInfo")


@_attrs_define
class KeywordsDynamicInfo:
    """This Class contains parameters for the IX call
    {@link IXServicePortIF#checkoutKeywordsDynamic(ClientInfo, KeywordsDynamicInfo)} .
     <p>
     There are two ways to execute the script for dynamic keyword lists. According to the parameter in
     this class, the one way or the other is chosen. The first way is to specify
     {@link KeywordsDynamicInfo#sord} and {@link KeywordsDynamicInfo#maskLineFocus}. Then, the IX
     passes these parameters to the script via the script-function open(ec, sord, fieldName). The
     other parameters will be overwritten by <code>null</code> and completely ignored. The other way
     is to set the fields {@link KeywordsDynamicInfo#mapData},
     {@link KeywordsDynamicInfo#mapLineFocus} and {@link KeywordsDynamicInfo#mapScriptName}. In this
     case, the IX passes these parameters to the scripting function openMap(ec, data, fieldName). To
     achieve this, <code>sord</code> as well as <code>maskLineFocus</code> must be <code>null</code>.
     </p>

        Attributes:
            ordinal_focus (Union[Unset, int]): <p>
                Only for sords with data organization based on aspects. If aspectAssocFocus has a cardinality
                 of {@link #Cardinality.MANDATORY_MANY} or {@link #Cardinality.OPTIONAL_MANY}, this value can
                 optionally be given to set the focus to a particular number within the aspectObjects regarding
                 to the index within the sords aspectObjectArray of the given aspect association.
                 </p>
                 <p>
                 If this value is positive or equals to zero, this value is passed to the script to execute.
                 Ignoring this value in the script is a valid use case. This value defaults to -1 which means
                 "no focus on a particular number".
                 </p>
            mask_line_focus (Union[Unset, DocMaskLine]): This class contains data for a line in the document mask.
            map_data (Union[Unset, MapToString]):
            map_line_focus (Union[Unset, str]): Represents the id of a field in a form.
            map_script_name (Union[Unset, str]): Determines the script to execute.
                <p>
                 This value has only an effect if sord and maskLineFocus are set to null. Setting this value
                 requires to set the values mapLineFocus and mapData also.
                 </p>
            sord (Union[Unset, Sord]): <p>
                Indexing information of an archive entry.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            aspect_assoc_focus (Union[Unset, AspectAssoc]): This class defines an aspect association.
                An AspectAssoc defines a reference to a keywording
                 {@link Aspect} in {@link DocMask#aspectAssocs}.
            aspect_line_focus (Union[Unset, AspectLine]): This class contains data for a line in a document mask, if {@link
                DocMask#dataOrganisation} =
                {@link DocMaskC#DATA_ORGANISATION_ASPECT}. AspectLines are contained in keywording
                 {@link Aspect}s.
    """

    ordinal_focus: Union[Unset, int] = UNSET
    mask_line_focus: Union[Unset, "DocMaskLine"] = UNSET
    map_data: Union[Unset, "MapToString"] = UNSET
    map_line_focus: Union[Unset, str] = UNSET
    map_script_name: Union[Unset, str] = UNSET
    sord: Union[Unset, "Sord"] = UNSET
    aspect_assoc_focus: Union[Unset, "AspectAssoc"] = UNSET
    aspect_line_focus: Union[Unset, "AspectLine"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ordinal_focus = self.ordinal_focus

        mask_line_focus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mask_line_focus, Unset):
            mask_line_focus = self.mask_line_focus.to_dict()

        map_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.map_data, Unset):
            map_data = self.map_data.to_dict()

        map_line_focus = self.map_line_focus

        map_script_name = self.map_script_name

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        aspect_assoc_focus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_assoc_focus, Unset):
            aspect_assoc_focus = self.aspect_assoc_focus.to_dict()

        aspect_line_focus: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_line_focus, Unset):
            aspect_line_focus = self.aspect_line_focus.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordinal_focus is not UNSET:
            field_dict["ordinalFocus"] = ordinal_focus
        if mask_line_focus is not UNSET:
            field_dict["maskLineFocus"] = mask_line_focus
        if map_data is not UNSET:
            field_dict["mapData"] = map_data
        if map_line_focus is not UNSET:
            field_dict["mapLineFocus"] = map_line_focus
        if map_script_name is not UNSET:
            field_dict["mapScriptName"] = map_script_name
        if sord is not UNSET:
            field_dict["sord"] = sord
        if aspect_assoc_focus is not UNSET:
            field_dict["aspectAssocFocus"] = aspect_assoc_focus
        if aspect_line_focus is not UNSET:
            field_dict["aspectLineFocus"] = aspect_line_focus

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect_assoc import AspectAssoc
        from ..models.aspect_line import AspectLine
        from ..models.doc_mask_line import DocMaskLine
        from ..models.map_to_string import MapToString
        from ..models.sord import Sord

        d = src_dict.copy()
        ordinal_focus = d.pop("ordinalFocus", UNSET)

        _mask_line_focus = d.pop("maskLineFocus", UNSET)
        mask_line_focus: Union[Unset, DocMaskLine]
        if isinstance(_mask_line_focus, Unset):
            mask_line_focus = UNSET
        else:
            mask_line_focus = DocMaskLine.from_dict(_mask_line_focus)

        _map_data = d.pop("mapData", UNSET)
        map_data: Union[Unset, MapToString]
        if isinstance(_map_data, Unset):
            map_data = UNSET
        else:
            map_data = MapToString.from_dict(_map_data)

        map_line_focus = d.pop("mapLineFocus", UNSET)

        map_script_name = d.pop("mapScriptName", UNSET)

        _sord = d.pop("sord", UNSET)
        sord: Union[Unset, Sord]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = Sord.from_dict(_sord)

        _aspect_assoc_focus = d.pop("aspectAssocFocus", UNSET)
        aspect_assoc_focus: Union[Unset, AspectAssoc]
        if isinstance(_aspect_assoc_focus, Unset):
            aspect_assoc_focus = UNSET
        else:
            aspect_assoc_focus = AspectAssoc.from_dict(_aspect_assoc_focus)

        _aspect_line_focus = d.pop("aspectLineFocus", UNSET)
        aspect_line_focus: Union[Unset, AspectLine]
        if isinstance(_aspect_line_focus, Unset):
            aspect_line_focus = UNSET
        else:
            aspect_line_focus = AspectLine.from_dict(_aspect_line_focus)

        keywords_dynamic_info = cls(
            ordinal_focus=ordinal_focus,
            mask_line_focus=mask_line_focus,
            map_data=map_data,
            map_line_focus=map_line_focus,
            map_script_name=map_script_name,
            sord=sord,
            aspect_assoc_focus=aspect_assoc_focus,
            aspect_line_focus=aspect_line_focus,
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
