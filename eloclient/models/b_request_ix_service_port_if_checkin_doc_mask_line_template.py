from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_in_doc_mask_line_template_options import CheckInDocMaskLineTemplateOptions
    from ..models.client_info import ClientInfo
    from ..models.doc_mask_line_template import DocMaskLineTemplate
    from ..models.doc_mask_line_template_z import DocMaskLineTemplateZ
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="BRequestIXServicePortIFCheckinDocMaskLineTemplate")


@_attrs_define
class BRequestIXServicePortIFCheckinDocMaskLineTemplate:
    """
    Attributes:
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        options (Union[Unset, CheckInDocMaskLineTemplateOptions]): Option class for the methode
            CheckInDocMaskLineTemplate
        lock_z (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        dmlt_z (Union[Unset, DocMaskLineTemplateZ]): This class encapsulates the constants of the DocMaskLineTemplateC
            class.
        dmlt (Union[Unset, DocMaskLineTemplate]): This class contains data for a document mask line template.
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    options: Union[Unset, "CheckInDocMaskLineTemplateOptions"] = UNSET
    lock_z: Union[Unset, "LockZ"] = UNSET
    dmlt_z: Union[Unset, "DocMaskLineTemplateZ"] = UNSET
    dmlt: Union[Unset, "DocMaskLineTemplate"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        lock_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock_z, Unset):
            lock_z = self.lock_z.to_dict()

        dmlt_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dmlt_z, Unset):
            dmlt_z = self.dmlt_z.to_dict()

        dmlt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dmlt, Unset):
            dmlt = self.dmlt.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if options is not UNSET:
            field_dict["options"] = options
        if lock_z is not UNSET:
            field_dict["lockZ"] = lock_z
        if dmlt_z is not UNSET:
            field_dict["dmltZ"] = dmlt_z
        if dmlt is not UNSET:
            field_dict["dmlt"] = dmlt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_in_doc_mask_line_template_options import CheckInDocMaskLineTemplateOptions
        from ..models.client_info import ClientInfo
        from ..models.doc_mask_line_template import DocMaskLineTemplate
        from ..models.doc_mask_line_template_z import DocMaskLineTemplateZ
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _options = d.pop("options", UNSET)
        options: Union[Unset, CheckInDocMaskLineTemplateOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = CheckInDocMaskLineTemplateOptions.from_dict(_options)

        _lock_z = d.pop("lockZ", UNSET)
        lock_z: Union[Unset, LockZ]
        if isinstance(_lock_z, Unset):
            lock_z = UNSET
        else:
            lock_z = LockZ.from_dict(_lock_z)

        _dmlt_z = d.pop("dmltZ", UNSET)
        dmlt_z: Union[Unset, DocMaskLineTemplateZ]
        if isinstance(_dmlt_z, Unset):
            dmlt_z = UNSET
        else:
            dmlt_z = DocMaskLineTemplateZ.from_dict(_dmlt_z)

        _dmlt = d.pop("dmlt", UNSET)
        dmlt: Union[Unset, DocMaskLineTemplate]
        if isinstance(_dmlt, Unset):
            dmlt = UNSET
        else:
            dmlt = DocMaskLineTemplate.from_dict(_dmlt)

        b_request_ix_service_port_if_checkin_doc_mask_line_template = cls(
            ci=ci,
            options=options,
            lock_z=lock_z,
            dmlt_z=dmlt_z,
            dmlt=dmlt,
        )

        b_request_ix_service_port_if_checkin_doc_mask_line_template.additional_properties = d
        return b_request_ix_service_port_if_checkin_doc_mask_line_template

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
