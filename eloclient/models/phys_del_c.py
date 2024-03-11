from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhysDelC")


@_attrs_define
class PhysDelC:
    """Constants for the PhysDel.type member.

    Attributes:
        error (Union[Unset, int]): Unknown object type deleted.
        user (Union[Unset, int]): User deleted.
        mask (Union[Unset, int]): Keywording form deleted.
        color (Union[Unset, int]): Color deleted.
        keywordlist (Union[Unset, int]): Keyword list deleted.
        sord (Union[Unset, int]): Folder or document deleted.
        relation (Union[Unset, int]): Relation deleted.
        version (Union[Unset, int]): Document version or attachment deleted.
        note (Union[Unset, int]): Note or annotation deleted.
        activity (Union[Unset, int]): Activity deleted.
        workflow (Union[Unset, int]): Workflow deleted.
        map_ (Union[Unset, int]): Map deleted.
        link (Union[Unset, int]): Link deleted.
    """

    error: Union[Unset, int] = UNSET
    user: Union[Unset, int] = UNSET
    mask: Union[Unset, int] = UNSET
    color: Union[Unset, int] = UNSET
    keywordlist: Union[Unset, int] = UNSET
    sord: Union[Unset, int] = UNSET
    relation: Union[Unset, int] = UNSET
    version: Union[Unset, int] = UNSET
    note: Union[Unset, int] = UNSET
    activity: Union[Unset, int] = UNSET
    workflow: Union[Unset, int] = UNSET
    map_: Union[Unset, int] = UNSET
    link: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        user = self.user
        mask = self.mask
        color = self.color
        keywordlist = self.keywordlist
        sord = self.sord
        relation = self.relation
        version = self.version
        note = self.note
        activity = self.activity
        workflow = self.workflow
        map_ = self.map_
        link = self.link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["ERROR"] = error
        if user is not UNSET:
            field_dict["USER"] = user
        if mask is not UNSET:
            field_dict["MASK"] = mask
        if color is not UNSET:
            field_dict["COLOR"] = color
        if keywordlist is not UNSET:
            field_dict["KEYWORDLIST"] = keywordlist
        if sord is not UNSET:
            field_dict["SORD"] = sord
        if relation is not UNSET:
            field_dict["RELATION"] = relation
        if version is not UNSET:
            field_dict["VERSION"] = version
        if note is not UNSET:
            field_dict["NOTE"] = note
        if activity is not UNSET:
            field_dict["ACTIVITY"] = activity
        if workflow is not UNSET:
            field_dict["WORKFLOW"] = workflow
        if map_ is not UNSET:
            field_dict["MAP"] = map_
        if link is not UNSET:
            field_dict["LINK"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("ERROR", UNSET)

        user = d.pop("USER", UNSET)

        mask = d.pop("MASK", UNSET)

        color = d.pop("COLOR", UNSET)

        keywordlist = d.pop("KEYWORDLIST", UNSET)

        sord = d.pop("SORD", UNSET)

        relation = d.pop("RELATION", UNSET)

        version = d.pop("VERSION", UNSET)

        note = d.pop("NOTE", UNSET)

        activity = d.pop("ACTIVITY", UNSET)

        workflow = d.pop("WORKFLOW", UNSET)

        map_ = d.pop("MAP", UNSET)

        link = d.pop("LINK", UNSET)

        phys_del_c = cls(
            error=error,
            user=user,
            mask=mask,
            color=color,
            keywordlist=keywordlist,
            sord=sord,
            relation=relation,
            version=version,
            note=note,
            activity=activity,
            workflow=workflow,
            map_=map_,
            link=link,
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
