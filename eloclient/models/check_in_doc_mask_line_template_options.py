from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_mask_line_template_z import DocMaskLineTemplateZ


T = TypeVar("T", bound="CheckInDocMaskLineTemplateOptions")


@_attrs_define
class CheckInDocMaskLineTemplateOptions:
    """Option class for the methode CheckInDocMaskLineTemplate

    Attributes:
        keep_modified_line_members (Union[Unset, bool]): Modified line members in the table masklines are kept.
        dmlt_z (Union[Unset, DocMaskLineTemplateZ]): This class encapsulates the constants of the DocMaskLineTemplateC
            class.
        only_modified_template_members (Union[Unset, bool]): Only change template members are passed to the document
            mask lines, which are using this
            template. This variable is ignored if dmltZ does not equal NULL.
    """

    keep_modified_line_members: Union[Unset, bool] = UNSET
    dmlt_z: Union[Unset, "DocMaskLineTemplateZ"] = UNSET
    only_modified_template_members: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keep_modified_line_members = self.keep_modified_line_members

        dmlt_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dmlt_z, Unset):
            dmlt_z = self.dmlt_z.to_dict()

        only_modified_template_members = self.only_modified_template_members

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keep_modified_line_members is not UNSET:
            field_dict["keepModifiedLineMembers"] = keep_modified_line_members
        if dmlt_z is not UNSET:
            field_dict["dmltZ"] = dmlt_z
        if only_modified_template_members is not UNSET:
            field_dict["onlyModifiedTemplateMembers"] = only_modified_template_members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_mask_line_template_z import DocMaskLineTemplateZ

        d = src_dict.copy()
        keep_modified_line_members = d.pop("keepModifiedLineMembers", UNSET)

        _dmlt_z = d.pop("dmltZ", UNSET)
        dmlt_z: Union[Unset, DocMaskLineTemplateZ]
        if isinstance(_dmlt_z, Unset):
            dmlt_z = UNSET
        else:
            dmlt_z = DocMaskLineTemplateZ.from_dict(_dmlt_z)

        only_modified_template_members = d.pop("onlyModifiedTemplateMembers", UNSET)

        check_in_doc_mask_line_template_options = cls(
            keep_modified_line_members=keep_modified_line_members,
            dmlt_z=dmlt_z,
            only_modified_template_members=only_modified_template_members,
        )

        check_in_doc_mask_line_template_options.additional_properties = d
        return check_in_doc_mask_line_template_options

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
