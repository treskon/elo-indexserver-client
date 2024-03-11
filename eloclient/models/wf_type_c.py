from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_type_z import WFTypeZ


T = TypeVar("T", bound="WFTypeC")


@_attrs_define
class WFTypeC:
    """Constants class for WFType. This class describes the workflow type/status.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            bset_active (Union[Unset, str]):
            bset_finished (Union[Unset, str]):
            bset_template (Union[Unset, str]):
            active (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            finished (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            template (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    bset_active: Union[Unset, str] = UNSET
    bset_finished: Union[Unset, str] = UNSET
    bset_template: Union[Unset, str] = UNSET
    active: Union[Unset, "WFTypeZ"] = UNSET
    finished: Union[Unset, "WFTypeZ"] = UNSET
    template: Union[Unset, "WFTypeZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_active = self.bset_active
        bset_finished = self.bset_finished
        bset_template = self.bset_template
        active: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        finished: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.to_dict()

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_active is not UNSET:
            field_dict["bsetACTIVE"] = bset_active
        if bset_finished is not UNSET:
            field_dict["bsetFINISHED"] = bset_finished
        if bset_template is not UNSET:
            field_dict["bsetTEMPLATE"] = bset_template
        if active is not UNSET:
            field_dict["ACTIVE"] = active
        if finished is not UNSET:
            field_dict["FINISHED"] = finished
        if template is not UNSET:
            field_dict["TEMPLATE"] = template

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_type_z import WFTypeZ

        d = src_dict.copy()
        bset_active = d.pop("bsetACTIVE", UNSET)

        bset_finished = d.pop("bsetFINISHED", UNSET)

        bset_template = d.pop("bsetTEMPLATE", UNSET)

        _active = d.pop("ACTIVE", UNSET)
        active: Union[Unset, WFTypeZ]
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = WFTypeZ.from_dict(_active)

        _finished = d.pop("FINISHED", UNSET)
        finished: Union[Unset, WFTypeZ]
        if isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = WFTypeZ.from_dict(_finished)

        _template = d.pop("TEMPLATE", UNSET)
        template: Union[Unset, WFTypeZ]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = WFTypeZ.from_dict(_template)

        wf_type_c = cls(
            bset_active=bset_active,
            bset_finished=bset_finished,
            bset_template=bset_template,
            active=active,
            finished=finished,
            template=template,
        )

        wf_type_c.additional_properties = d
        return wf_type_c

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
