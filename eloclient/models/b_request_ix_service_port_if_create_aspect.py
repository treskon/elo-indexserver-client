from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aspect_line import AspectLine
    from ..models.client_info import ClientInfo


T = TypeVar("T", bound="BRequestIXServicePortIFCreateAspect")


@_attrs_define
class BRequestIXServicePortIFCreateAspect:
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
        name (Union[Unset, str]):
        lines (Union[Unset, List['AspectLine']]):
    """

    ci: Union[Unset, "ClientInfo"] = UNSET
    name: Union[Unset, str] = UNSET
    lines: Union[Unset, List["AspectLine"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        name = self.name

        lines: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for componentsschemas_list_of_aspect_line_item_data in self.lines:
                componentsschemas_list_of_aspect_line_item = componentsschemas_list_of_aspect_line_item_data.to_dict()
                lines.append(componentsschemas_list_of_aspect_line_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ci is not UNSET:
            field_dict["ci"] = ci
        if name is not UNSET:
            field_dict["name"] = name
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.aspect_line import AspectLine
        from ..models.client_info import ClientInfo

        d = src_dict.copy()
        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        name = d.pop("name", UNSET)

        lines = []
        _lines = d.pop("lines", UNSET)
        for componentsschemas_list_of_aspect_line_item_data in _lines or []:
            componentsschemas_list_of_aspect_line_item = AspectLine.from_dict(
                componentsschemas_list_of_aspect_line_item_data
            )

            lines.append(componentsschemas_list_of_aspect_line_item)

        b_request_ix_service_port_if_create_aspect = cls(
            ci=ci,
            name=name,
            lines=lines,
        )

        b_request_ix_service_port_if_create_aspect.additional_properties = d
        return b_request_ix_service_port_if_create_aspect

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
