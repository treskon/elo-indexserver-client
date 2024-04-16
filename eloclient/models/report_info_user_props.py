from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString
    from ..models.subs_info import SubsInfo
    from ..models.substitution import Substitution
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="ReportInfoUserProps")


@_attrs_define
class ReportInfoUserProps:
    """Additional report information for user modifications.

    Attributes:
        user_info (Union[Unset, UserInfo]): <p>
            Data class containing the user information data for the user logged in to the Index server. User
             information includes ID, name, rights, parent, etc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        substitutions (Union[Unset, List['Substitution']]):
        ids_to_names (Union[Unset, MapToString]):
        user_info_eff (Union[Unset, UserInfo]): <p>
            Data class containing the user information data for the user logged in to the Index server. User
             information includes ID, name, rights, parent, etc.
             </p>
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        subs_infos (Union[Unset, List['SubsInfo']]):
    """

    user_info: Union[Unset, "UserInfo"] = UNSET
    substitutions: Union[Unset, List["Substitution"]] = UNSET
    ids_to_names: Union[Unset, "MapToString"] = UNSET
    user_info_eff: Union[Unset, "UserInfo"] = UNSET
    subs_infos: Union[Unset, List["SubsInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = self.user_info.to_dict()

        substitutions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.substitutions, Unset):
            substitutions = []
            for componentsschemas_list_of_substitution_item_data in self.substitutions:
                componentsschemas_list_of_substitution_item = componentsschemas_list_of_substitution_item_data.to_dict()
                substitutions.append(componentsschemas_list_of_substitution_item)

        ids_to_names: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ids_to_names, Unset):
            ids_to_names = self.ids_to_names.to_dict()

        user_info_eff: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_info_eff, Unset):
            user_info_eff = self.user_info_eff.to_dict()

        subs_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.subs_infos, Unset):
            subs_infos = []
            for componentsschemas_list_of_subs_info_item_data in self.subs_infos:
                componentsschemas_list_of_subs_info_item = componentsschemas_list_of_subs_info_item_data.to_dict()
                subs_infos.append(componentsschemas_list_of_subs_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info
        if substitutions is not UNSET:
            field_dict["substitutions"] = substitutions
        if ids_to_names is not UNSET:
            field_dict["idsToNames"] = ids_to_names
        if user_info_eff is not UNSET:
            field_dict["userInfoEff"] = user_info_eff
        if subs_infos is not UNSET:
            field_dict["subsInfos"] = subs_infos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString
        from ..models.subs_info import SubsInfo
        from ..models.substitution import Substitution
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        _user_info = d.pop("userInfo", UNSET)
        user_info: Union[Unset, UserInfo]
        if isinstance(_user_info, Unset):
            user_info = UNSET
        else:
            user_info = UserInfo.from_dict(_user_info)

        substitutions = []
        _substitutions = d.pop("substitutions", UNSET)
        for componentsschemas_list_of_substitution_item_data in _substitutions or []:
            componentsschemas_list_of_substitution_item = Substitution.from_dict(
                componentsschemas_list_of_substitution_item_data
            )

            substitutions.append(componentsschemas_list_of_substitution_item)

        _ids_to_names = d.pop("idsToNames", UNSET)
        ids_to_names: Union[Unset, MapToString]
        if isinstance(_ids_to_names, Unset):
            ids_to_names = UNSET
        else:
            ids_to_names = MapToString.from_dict(_ids_to_names)

        _user_info_eff = d.pop("userInfoEff", UNSET)
        user_info_eff: Union[Unset, UserInfo]
        if isinstance(_user_info_eff, Unset):
            user_info_eff = UNSET
        else:
            user_info_eff = UserInfo.from_dict(_user_info_eff)

        subs_infos = []
        _subs_infos = d.pop("subsInfos", UNSET)
        for componentsschemas_list_of_subs_info_item_data in _subs_infos or []:
            componentsschemas_list_of_subs_info_item = SubsInfo.from_dict(componentsschemas_list_of_subs_info_item_data)

            subs_infos.append(componentsschemas_list_of_subs_info_item)

        report_info_user_props = cls(
            user_info=user_info,
            substitutions=substitutions,
            ids_to_names=ids_to_names,
            user_info_eff=user_info_eff,
            subs_infos=subs_infos,
        )

        report_info_user_props.additional_properties = d
        return report_info_user_props

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
