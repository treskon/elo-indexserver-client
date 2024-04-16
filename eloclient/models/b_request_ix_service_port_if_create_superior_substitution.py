from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.create_superior_substitution_info import CreateSuperiorSubstitutionInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCreateSuperiorSubstitution")


@_attrs_define
class BRequestIXServicePortIFCreateSuperiorSubstitution:
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
        create_superior_substitution_info (Union[Unset, CreateSuperiorSubstitutionInfo]): Define how a superior
            substitution is created.
            <p>
             A superior has the right to substitute any of its subordinates.
             </p>
             <p>
             A superior substitution has {@link SubstitutionSettings#superiorSubstitution} set to true.
             </p>
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    create_superior_substitution_info: Union[Unset, "CreateSuperiorSubstitutionInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        create_superior_substitution_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.create_superior_substitution_info, Unset):
            create_superior_substitution_info = self.create_superior_substitution_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if create_superior_substitution_info is not UNSET:
            field_dict["createSuperiorSubstitutionInfo"] = create_superior_substitution_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.create_superior_substitution_info import CreateSuperiorSubstitutionInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _create_superior_substitution_info = d.pop("createSuperiorSubstitutionInfo", UNSET)
        create_superior_substitution_info: Union[Unset, CreateSuperiorSubstitutionInfo]
        if isinstance(_create_superior_substitution_info, Unset):
            create_superior_substitution_info = UNSET
        else:
            create_superior_substitution_info = CreateSuperiorSubstitutionInfo.from_dict(
                _create_superior_substitution_info
            )

        b_request_ix_service_port_if_create_superior_substitution = cls(
            ci=ci,
            create_superior_substitution_info=create_superior_substitution_info,
        )

        b_request_ix_service_port_if_create_superior_substitution.additional_properties = d
        return b_request_ix_service_port_if_create_superior_substitution

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
