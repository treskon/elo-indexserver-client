from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindConfigFileInfo")


@_attrs_define
class FindConfigFileInfo:
    """This class describes the files to select from a postbox directory or from a configuration
    directory.

        Attributes:
            incl_deputy (Union[Unset, bool]): Find files in the in-tray folder of all deputized users.
                This member is ignored, if
                 <code>names</code> is set.
            names (Union[Unset, List[str]]):
            postbox_user_id (Union[Unset, str]): Find files in the in-tray of the user specified by ID or name.
                This member is ignored, if
                 <code>names</code> is set. If neither <code>names</code> nor <code>postboxUserId</code> is set,
                 the in-tray of the current user is listed.
    """

    incl_deputy: Union[Unset, bool] = UNSET
    names: Union[Unset, List[str]] = UNSET
    postbox_user_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incl_deputy = self.incl_deputy

        names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.names, Unset):
            names = self.names

        postbox_user_id = self.postbox_user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incl_deputy is not UNSET:
            field_dict["inclDeputy"] = incl_deputy
        if names is not UNSET:
            field_dict["names"] = names
        if postbox_user_id is not UNSET:
            field_dict["postboxUserId"] = postbox_user_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incl_deputy = d.pop("inclDeputy", UNSET)

        names = cast(List[str], d.pop("names", UNSET))

        postbox_user_id = d.pop("postboxUserId", UNSET)

        find_config_file_info = cls(
            incl_deputy=incl_deputy,
            names=names,
            postbox_user_id=postbox_user_id,
        )

        find_config_file_info.additional_properties = d
        return find_config_file_info

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
