from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWebDAVPathOptions")


@_attrs_define
class GetWebDAVPathOptions:
    """Parameter class for the function {@link IXServicePortIF#getWebDAVPathFromObjID2}

    Attributes:
        obj_id (Union[Unset, str]): ObjectId or GUID of the sord to get the path.
        tickket_in_path (Union[Unset, bool]): If true, the ticket is inserted in the path.
        use_short_path (Union[Unset, bool]): From now on the option is no longer considered and is implicitly evaluated
            as true.
    """

    obj_id: Union[Unset, str] = UNSET
    tickket_in_path: Union[Unset, bool] = UNSET
    use_short_path: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        obj_id = self.obj_id

        tickket_in_path = self.tickket_in_path

        use_short_path = self.use_short_path

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if tickket_in_path is not UNSET:
            field_dict["tickketInPath"] = tickket_in_path
        if use_short_path is not UNSET:
            field_dict["useShortPath"] = use_short_path

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        obj_id = d.pop("objId", UNSET)

        tickket_in_path = d.pop("tickketInPath", UNSET)

        use_short_path = d.pop("useShortPath", UNSET)

        get_web_dav_path_options = cls(
            obj_id=obj_id,
            tickket_in_path=tickket_in_path,
            use_short_path=use_short_path,
        )

        get_web_dav_path_options.additional_properties = d
        return get_web_dav_path_options

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
