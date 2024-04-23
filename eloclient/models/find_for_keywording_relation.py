from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect_line import AspectLine
    from ..models.doc_mask_line import DocMaskLine


T = TypeVar("T", bound="FindForKeywordingRelation")


@_attrs_define
class FindForKeywordingRelation:
    """Criteria for searching sords for keywording relation.

    Attributes:
        filter_ (Union[Unset, str]): Filter string applied to short description of Sords.
            This filter has to match {@link Sord#name}
             to append the Sord to the result. The filter can have one wildcard character at the end that
             matches any character, see {@link SessionOptionsC#DB_WILDCARDS}, wildcard for any character
             (asterix by default).
        doc_mask_line (Union[Unset, DocMaskLine]): This class contains data for a line in the document mask.
        aspect_line (Union[Unset, AspectLine]): This class contains data for a line in a document mask, if {@link
            DocMask#dataOrganisation} =
            {@link DocMaskC#DATA_ORGANISATION_ASPECT}. AspectLines are contained in keywording
             {@link Aspect}s.
    """

    filter_: Union[Unset, str] = UNSET
    doc_mask_line: Union[Unset, "DocMaskLine"] = UNSET
    aspect_line: Union[Unset, "AspectLine"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_ = self.filter_

        doc_mask_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc_mask_line, Unset):
            doc_mask_line = self.doc_mask_line.to_dict()

        aspect_line: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aspect_line, Unset):
            aspect_line = self.aspect_line.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if doc_mask_line is not UNSET:
            field_dict["docMaskLine"] = doc_mask_line
        if aspect_line is not UNSET:
            field_dict["aspectLine"] = aspect_line

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect_line import AspectLine
        from ..models.doc_mask_line import DocMaskLine

        d = src_dict.copy()
        filter_ = d.pop("filter", UNSET)

        _doc_mask_line = d.pop("docMaskLine", UNSET)
        doc_mask_line: Union[Unset, DocMaskLine]
        if isinstance(_doc_mask_line, Unset):
            doc_mask_line = UNSET
        else:
            doc_mask_line = DocMaskLine.from_dict(_doc_mask_line)

        _aspect_line = d.pop("aspectLine", UNSET)
        aspect_line: Union[Unset, AspectLine]
        if isinstance(_aspect_line, Unset):
            aspect_line = UNSET
        else:
            aspect_line = AspectLine.from_dict(_aspect_line)

        find_for_keywording_relation = cls(
            filter_=filter_,
            doc_mask_line=doc_mask_line,
            aspect_line=aspect_line,
        )

        find_for_keywording_relation.additional_properties = d
        return find_for_keywording_relation

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
