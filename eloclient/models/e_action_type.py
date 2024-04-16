from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EActionType")


@_attrs_define
class EActionType:
    """Types of document feed entries.

    Attributes:
        undefined (Union[Unset, EActionType]): Types of document feed entries.
        survey (Union[Unset, EActionType]): Types of document feed entries.
        released (Union[Unset, EActionType]): Types of document feed entries.
        feed_created (Union[Unset, EActionType]): Types of document feed entries.
        user_comment (Union[Unset, EActionType]): Types of document feed entries.
        auto_comment (Union[Unset, EActionType]): Types of document feed entries.
        work_version_created (Union[Unset, EActionType]): Types of document feed entries.
        work_version_switched (Union[Unset, EActionType]): Types of document feed entries.
        sord_created (Union[Unset, EActionType]): Types of document feed entries.
        version_created (Union[Unset, EActionType]): Types of document feed entries.
    """

    undefined: Union[Unset, "EActionType"] = UNSET
    survey: Union[Unset, "EActionType"] = UNSET
    released: Union[Unset, "EActionType"] = UNSET
    feed_created: Union[Unset, "EActionType"] = UNSET
    user_comment: Union[Unset, "EActionType"] = UNSET
    auto_comment: Union[Unset, "EActionType"] = UNSET
    work_version_created: Union[Unset, "EActionType"] = UNSET
    work_version_switched: Union[Unset, "EActionType"] = UNSET
    sord_created: Union[Unset, "EActionType"] = UNSET
    version_created: Union[Unset, "EActionType"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        undefined: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.undefined, Unset):
            undefined = self.undefined.to_dict()

        survey: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.survey, Unset):
            survey = self.survey.to_dict()

        released: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.released, Unset):
            released = self.released.to_dict()

        feed_created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.feed_created, Unset):
            feed_created = self.feed_created.to_dict()

        user_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_comment, Unset):
            user_comment = self.user_comment.to_dict()

        auto_comment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.auto_comment, Unset):
            auto_comment = self.auto_comment.to_dict()

        work_version_created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_version_created, Unset):
            work_version_created = self.work_version_created.to_dict()

        work_version_switched: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.work_version_switched, Unset):
            work_version_switched = self.work_version_switched.to_dict()

        sord_created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord_created, Unset):
            sord_created = self.sord_created.to_dict()

        version_created: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version_created, Unset):
            version_created = self.version_created.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if undefined is not UNSET:
            field_dict["Undefined"] = undefined
        if survey is not UNSET:
            field_dict["Survey"] = survey
        if released is not UNSET:
            field_dict["Released"] = released
        if feed_created is not UNSET:
            field_dict["FeedCreated"] = feed_created
        if user_comment is not UNSET:
            field_dict["UserComment"] = user_comment
        if auto_comment is not UNSET:
            field_dict["AutoComment"] = auto_comment
        if work_version_created is not UNSET:
            field_dict["WorkVersionCreated"] = work_version_created
        if work_version_switched is not UNSET:
            field_dict["WorkVersionSwitched"] = work_version_switched
        if sord_created is not UNSET:
            field_dict["SordCreated"] = sord_created
        if version_created is not UNSET:
            field_dict["VersionCreated"] = version_created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _undefined = d.pop("Undefined", UNSET)
        undefined: Union[Unset, EActionType]
        if isinstance(_undefined, Unset):
            undefined = UNSET
        else:
            undefined = EActionType.from_dict(_undefined)

        _survey = d.pop("Survey", UNSET)
        survey: Union[Unset, EActionType]
        if isinstance(_survey, Unset):
            survey = UNSET
        else:
            survey = EActionType.from_dict(_survey)

        _released = d.pop("Released", UNSET)
        released: Union[Unset, EActionType]
        if isinstance(_released, Unset):
            released = UNSET
        else:
            released = EActionType.from_dict(_released)

        _feed_created = d.pop("FeedCreated", UNSET)
        feed_created: Union[Unset, EActionType]
        if isinstance(_feed_created, Unset):
            feed_created = UNSET
        else:
            feed_created = EActionType.from_dict(_feed_created)

        _user_comment = d.pop("UserComment", UNSET)
        user_comment: Union[Unset, EActionType]
        if isinstance(_user_comment, Unset):
            user_comment = UNSET
        else:
            user_comment = EActionType.from_dict(_user_comment)

        _auto_comment = d.pop("AutoComment", UNSET)
        auto_comment: Union[Unset, EActionType]
        if isinstance(_auto_comment, Unset):
            auto_comment = UNSET
        else:
            auto_comment = EActionType.from_dict(_auto_comment)

        _work_version_created = d.pop("WorkVersionCreated", UNSET)
        work_version_created: Union[Unset, EActionType]
        if isinstance(_work_version_created, Unset):
            work_version_created = UNSET
        else:
            work_version_created = EActionType.from_dict(_work_version_created)

        _work_version_switched = d.pop("WorkVersionSwitched", UNSET)
        work_version_switched: Union[Unset, EActionType]
        if isinstance(_work_version_switched, Unset):
            work_version_switched = UNSET
        else:
            work_version_switched = EActionType.from_dict(_work_version_switched)

        _sord_created = d.pop("SordCreated", UNSET)
        sord_created: Union[Unset, EActionType]
        if isinstance(_sord_created, Unset):
            sord_created = UNSET
        else:
            sord_created = EActionType.from_dict(_sord_created)

        _version_created = d.pop("VersionCreated", UNSET)
        version_created: Union[Unset, EActionType]
        if isinstance(_version_created, Unset):
            version_created = UNSET
        else:
            version_created = EActionType.from_dict(_version_created)

        e_action_type = cls(
            undefined=undefined,
            survey=survey,
            released=released,
            feed_created=feed_created,
            user_comment=user_comment,
            auto_comment=auto_comment,
            work_version_created=work_version_created,
            work_version_switched=work_version_switched,
            sord_created=sord_created,
            version_created=version_created,
        )

        e_action_type.additional_properties = d
        return e_action_type

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
