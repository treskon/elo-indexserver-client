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
            bset_template (Union[Unset, str]):
            bset_active (Union[Unset, str]):
            active (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_finished (Union[Unset, str]):
            template (Union[Unset, WFTypeZ]): This class encapsulates the constants of the WFTypeC class.
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
    """

    bset_template: Union[Unset, str] = UNSET
    bset_active: Union[Unset, str] = UNSET
    active: Union[Unset, "WFTypeZ"] = UNSET
    bset_finished: Union[Unset, str] = UNSET
    template: Union[Unset, "WFTypeZ"] = UNSET
    finished: Union[Unset, "WFTypeZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_template = self.bset_template

        bset_active = self.bset_active

        active: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.active, Unset):
            active = self.active.to_dict()

        bset_finished = self.bset_finished

        template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        finished: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.finished, Unset):
            finished = self.finished.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_template is not UNSET:
            field_dict["bsetTEMPLATE"] = bset_template
        if bset_active is not UNSET:
            field_dict["bsetACTIVE"] = bset_active
        if active is not UNSET:
            field_dict["ACTIVE"] = active
        if bset_finished is not UNSET:
            field_dict["bsetFINISHED"] = bset_finished
        if template is not UNSET:
            field_dict["TEMPLATE"] = template
        if finished is not UNSET:
            field_dict["FINISHED"] = finished

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_type_z import WFTypeZ

        d = src_dict.copy()
        bset_template = d.pop("bsetTEMPLATE", UNSET)

        bset_active = d.pop("bsetACTIVE", UNSET)

        _active = d.pop("ACTIVE", UNSET)
        active: Union[Unset, WFTypeZ]
        if isinstance(_active, Unset):
            active = UNSET
        else:
            active = WFTypeZ.from_dict(_active)

        bset_finished = d.pop("bsetFINISHED", UNSET)

        _template = d.pop("TEMPLATE", UNSET)
        template: Union[Unset, WFTypeZ]
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = WFTypeZ.from_dict(_template)

        _finished = d.pop("FINISHED", UNSET)
        finished: Union[Unset, WFTypeZ]
        if isinstance(_finished, Unset):
            finished = UNSET
        else:
            finished = WFTypeZ.from_dict(_finished)

        wf_type_c = cls(
            bset_template=bset_template,
            bset_active=bset_active,
            active=active,
            bset_finished=bset_finished,
            template=template,
            finished=finished,
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
