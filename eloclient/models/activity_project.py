from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_option import ActivityOption


T = TypeVar("T", bound="ActivityProject")


@_attrs_define
class ActivityProject:
    """This class represents an activity project. An activity project is a template for an activity.

    Attributes:
        project (Union[Unset, str]): Project name. This can be one of the predefined project names:
            ActivityProjectC.DEFAULT, ActivityProjectC.
            REQUEST,
             ActivityProjectC.NOTIFY. Or an arbitrary name for an application defined use case. The name must be unique
            because
             it is internally used as an ID. It has to start with a letter and must only contain letters, numbers or
             underscores.
        major (Union[Unset, int]): Reserved.
        minor (Union[Unset, int]): Reserved.
        opt_value (Union[Unset, str]): Reserved.
        options (Union[Unset, List['ActivityOption']]):
        protected_project (Union[Unset, bool]): Activity project is protected.
        locked_when_finished (Union[Unset, bool]): Activity project is locked when finished.
    """

    project: Union[Unset, str] = UNSET
    major: Union[Unset, int] = UNSET
    minor: Union[Unset, int] = UNSET
    opt_value: Union[Unset, str] = UNSET
    options: Union[Unset, List["ActivityOption"]] = UNSET
    protected_project: Union[Unset, bool] = UNSET
    locked_when_finished: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project = self.project
        major = self.major
        minor = self.minor
        opt_value = self.opt_value
        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        protected_project = self.protected_project
        locked_when_finished = self.locked_when_finished

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if project is not UNSET:
            field_dict["project"] = project
        if major is not UNSET:
            field_dict["major"] = major
        if minor is not UNSET:
            field_dict["minor"] = minor
        if opt_value is not UNSET:
            field_dict["optValue"] = opt_value
        if options is not UNSET:
            field_dict["options"] = options
        if protected_project is not UNSET:
            field_dict["protectedProject"] = protected_project
        if locked_when_finished is not UNSET:
            field_dict["lockedWhenFinished"] = locked_when_finished

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.activity_option import ActivityOption

        d = src_dict.copy()
        project = d.pop("project", UNSET)

        major = d.pop("major", UNSET)

        minor = d.pop("minor", UNSET)

        opt_value = d.pop("optValue", UNSET)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = ActivityOption.from_dict(options_item_data)

            options.append(options_item)

        protected_project = d.pop("protectedProject", UNSET)

        locked_when_finished = d.pop("lockedWhenFinished", UNSET)

        activity_project = cls(
            project=project,
            major=major,
            minor=minor,
            opt_value=opt_value,
            options=options,
            protected_project=protected_project,
            locked_when_finished=locked_when_finished,
        )

        activity_project.additional_properties = d
        return activity_project

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
