from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysDelC")


@_attrs_define
class PhysDelC:
    """Constants for the PhysDel.type member.

    Attributes:
        relation (Union[Unset, int]): Relation deleted.
        sord (Union[Unset, int]): Folder or document deleted.
        user (Union[Unset, int]): User deleted.
        mask (Union[Unset, int]): Keywording form deleted.
        color (Union[Unset, int]): Color deleted.
        note (Union[Unset, int]): Note or annotation deleted.
        version (Union[Unset, int]): Document version or attachment deleted.
        link (Union[Unset, int]): Link deleted.
        error (Union[Unset, int]): Unknown object type deleted.
        map_ (Union[Unset, int]): Map deleted.
        activity (Union[Unset, int]): Activity deleted.
        workflow (Union[Unset, int]): Workflow deleted.
        keywordlist (Union[Unset, int]): Keyword list deleted.
    """

    relation: Union[Unset, int] = UNSET
    sord: Union[Unset, int] = UNSET
    user: Union[Unset, int] = UNSET
    mask: Union[Unset, int] = UNSET
    color: Union[Unset, int] = UNSET
    note: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    link: Union[Unset, int] = UNSET
    error: Union[Unset, int] = UNSET
    map_: Union[Unset, int] = UNSET
    activity: Union[Unset, int] = UNSET
    workflow: Union[Unset, int] = UNSET
    keywordlist: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relation = self.relation

        sord = self.sord

        user = self.user

        mask = self.mask

        color = self.color

        note = self.note

        version = self.version

        link = self.link

        error = self.error

        map_ = self.map_

        activity = self.activity

        workflow = self.workflow

        keywordlist = self.keywordlist

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relation is not UNSET:
            field_dict["RELATION"] = relation
        if sord is not UNSET:
            field_dict["SORD"] = sord
        if user is not UNSET:
            field_dict["USER"] = user
        if mask is not UNSET:
            field_dict["MASK"] = mask
        if color is not UNSET:
            field_dict["COLOR"] = color
        if note is not UNSET:
            field_dict["NOTE"] = note
        if version is not UNSET:
            field_dict["VERSION"] = version
        if link is not UNSET:
            field_dict["LINK"] = link
        if error is not UNSET:
            field_dict["ERROR"] = error
        if map_ is not UNSET:
            field_dict["MAP"] = map_
        if activity is not UNSET:
            field_dict["ACTIVITY"] = activity
        if workflow is not UNSET:
            field_dict["WORKFLOW"] = workflow
        if keywordlist is not UNSET:
            field_dict["KEYWORDLIST"] = keywordlist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        relation = d.pop("RELATION", UNSET)

        sord = d.pop("SORD", UNSET)

        user = d.pop("USER", UNSET)

        mask = d.pop("MASK", UNSET)

        color = d.pop("COLOR", UNSET)

        note = d.pop("NOTE", UNSET)

        version = d.pop("VERSION", UNSET)

        link = d.pop("LINK", UNSET)

        error = d.pop("ERROR", UNSET)

        map_ = d.pop("MAP", UNSET)

        activity = d.pop("ACTIVITY", UNSET)

        workflow = d.pop("WORKFLOW", UNSET)

        keywordlist = d.pop("KEYWORDLIST", UNSET)

        phys_del_c = cls(
            relation=relation,
            sord=sord,
            user=user,
            mask=mask,
            color=color,
            note=note,
            version=version,
            link=link,
            error=error,
            map_=map_,
            activity=activity,
            workflow=workflow,
            keywordlist=keywordlist,
        )

        phys_del_c.additional_properties = d
        return phys_del_c

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
