from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="FindBackgroundThreadOptions")


@_attrs_define
class FindBackgroundThreadOptions:
    """
    Attributes:
        incl_active_jobs (Union[Unset, bool]): Includes running Jobs in the result. Defaults to true.
        incl_finished_jobs (Union[Unset, bool]): Includes finished Jobs in the result. Defaults to false.
        incl_full_info (Union[Unset, bool]): enables extended result information in the ProcessInfo member (if
            available)
        sort_order (Union[Unset, int]): The order in which the results has to be sorted.
        user_info (Union[Unset, List['UserInfo']]):
        guids (Union[Unset, List[str]]):
        date_after (Union[Unset, str]): Filter jobs started after this date.
        date_before (Union[Unset, str]): Filter jobs started before this date.
    """

    incl_active_jobs: Union[Unset, bool] = UNSET
    incl_finished_jobs: Union[Unset, bool] = UNSET
    incl_full_info: Union[Unset, bool] = UNSET
    sort_order: Union[Unset, int] = UNSET
    user_info: Union[Unset, List["UserInfo"]] = UNSET
    guids: Union[Unset, List[str]] = UNSET
    date_after: Union[Unset, str] = UNSET
    date_before: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incl_active_jobs = self.incl_active_jobs
        incl_finished_jobs = self.incl_finished_jobs
        incl_full_info = self.incl_full_info
        sort_order = self.sort_order
        user_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_info, Unset):
            user_info = []
            for user_info_item_data in self.user_info:
                user_info_item = user_info_item_data.to_dict()

                user_info.append(user_info_item)

        guids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.guids, Unset):
            guids = self.guids

        date_after = self.date_after
        date_before = self.date_before

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incl_active_jobs is not UNSET:
            field_dict["inclActiveJobs"] = incl_active_jobs
        if incl_finished_jobs is not UNSET:
            field_dict["inclFinishedJobs"] = incl_finished_jobs
        if incl_full_info is not UNSET:
            field_dict["inclFullInfo"] = incl_full_info
        if sort_order is not UNSET:
            field_dict["sortOrder"] = sort_order
        if user_info is not UNSET:
            field_dict["userInfo"] = user_info
        if guids is not UNSET:
            field_dict["guids"] = guids
        if date_after is not UNSET:
            field_dict["dateAfter"] = date_after
        if date_before is not UNSET:
            field_dict["dateBefore"] = date_before

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_info import UserInfo

        d = src_dict.copy()
        incl_active_jobs = d.pop("inclActiveJobs", UNSET)

        incl_finished_jobs = d.pop("inclFinishedJobs", UNSET)

        incl_full_info = d.pop("inclFullInfo", UNSET)

        sort_order = d.pop("sortOrder", UNSET)

        user_info = []
        _user_info = d.pop("userInfo", UNSET)
        for user_info_item_data in _user_info or []:
            user_info_item = UserInfo.from_dict(user_info_item_data)

            user_info.append(user_info_item)

        guids = cast(List[str], d.pop("guids", UNSET))

        date_after = d.pop("dateAfter", UNSET)

        date_before = d.pop("dateBefore", UNSET)

        find_background_thread_options = cls(
            incl_active_jobs=incl_active_jobs,
            incl_finished_jobs=incl_finished_jobs,
            incl_full_info=incl_full_info,
            sort_order=sort_order,
            user_info=user_info,
            guids=guids,
            date_after=date_after,
            date_before=date_before,
        )

        find_background_thread_options.additional_properties = d
        return find_background_thread_options

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
