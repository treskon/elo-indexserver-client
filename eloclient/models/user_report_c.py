from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_report_z import UserReportZ


T = TypeVar("T", bound="UserReportC")


@_attrs_define
class UserReportC:
    """<p>
    Constants for user report information. Each member of this class with prefix "mb" has a
     corresponding member in class <code>ReportInfo</code>
     </p>

        Attributes:
            count_documents_over_all_repositories (Union[Unset, UserReportZ]): <p>
                This class encapsulates the constants of <code>UserReportC</code>
                 </p>
            mb_include_usernames (Union[Unset, str]): The user names.
            mb_nothing (Union[Unset, str]): nothing
            full_userreport (Union[Unset, UserReportZ]): <p>
                This class encapsulates the constants of <code>UserReportC</code>
                 </p>
            mb_include_counter (Union[Unset, str]): The counter
            none (Union[Unset, UserReportZ]): <p>
                This class encapsulates the constants of <code>UserReportC</code>
                 </p>
            mb_include_rights (Union[Unset, str]): Rights in numerical form
    """

    count_documents_over_all_repositories: Union[Unset, "UserReportZ"] = UNSET
    mb_include_usernames: Union[Unset, str] = UNSET
    mb_nothing: Union[Unset, str] = UNSET
    full_userreport: Union[Unset, "UserReportZ"] = UNSET
    mb_include_counter: Union[Unset, str] = UNSET
    none: Union[Unset, "UserReportZ"] = UNSET
    mb_include_rights: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count_documents_over_all_repositories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.count_documents_over_all_repositories, Unset):
            count_documents_over_all_repositories = self.count_documents_over_all_repositories.to_dict()

        mb_include_usernames = self.mb_include_usernames

        mb_nothing = self.mb_nothing

        full_userreport: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.full_userreport, Unset):
            full_userreport = self.full_userreport.to_dict()

        mb_include_counter = self.mb_include_counter

        none: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.none, Unset):
            none = self.none.to_dict()

        mb_include_rights = self.mb_include_rights

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_documents_over_all_repositories is not UNSET:
            field_dict["COUNT_DOCUMENTS_OVER_ALL_REPOSITORIES"] = count_documents_over_all_repositories
        if mb_include_usernames is not UNSET:
            field_dict["mbINCLUDE_USERNAMES"] = mb_include_usernames
        if mb_nothing is not UNSET:
            field_dict["mbNOTHING"] = mb_nothing
        if full_userreport is not UNSET:
            field_dict["FULL_USERREPORT"] = full_userreport
        if mb_include_counter is not UNSET:
            field_dict["mbINCLUDE_COUNTER"] = mb_include_counter
        if none is not UNSET:
            field_dict["NONE"] = none
        if mb_include_rights is not UNSET:
            field_dict["mbINCLUDE_RIGHTS"] = mb_include_rights

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_report_z import UserReportZ

        d = src_dict.copy()
        _count_documents_over_all_repositories = d.pop("COUNT_DOCUMENTS_OVER_ALL_REPOSITORIES", UNSET)
        count_documents_over_all_repositories: Union[Unset, UserReportZ]
        if isinstance(_count_documents_over_all_repositories, Unset):
            count_documents_over_all_repositories = UNSET
        else:
            count_documents_over_all_repositories = UserReportZ.from_dict(_count_documents_over_all_repositories)

        mb_include_usernames = d.pop("mbINCLUDE_USERNAMES", UNSET)

        mb_nothing = d.pop("mbNOTHING", UNSET)

        _full_userreport = d.pop("FULL_USERREPORT", UNSET)
        full_userreport: Union[Unset, UserReportZ]
        if isinstance(_full_userreport, Unset):
            full_userreport = UNSET
        else:
            full_userreport = UserReportZ.from_dict(_full_userreport)

        mb_include_counter = d.pop("mbINCLUDE_COUNTER", UNSET)

        _none = d.pop("NONE", UNSET)
        none: Union[Unset, UserReportZ]
        if isinstance(_none, Unset):
            none = UNSET
        else:
            none = UserReportZ.from_dict(_none)

        mb_include_rights = d.pop("mbINCLUDE_RIGHTS", UNSET)

        user_report_c = cls(
            count_documents_over_all_repositories=count_documents_over_all_repositories,
            mb_include_usernames=mb_include_usernames,
            mb_nothing=mb_nothing,
            full_userreport=full_userreport,
            mb_include_counter=mb_include_counter,
            none=none,
            mb_include_rights=mb_include_rights,
        )

        user_report_c.additional_properties = d
        return user_report_c

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
