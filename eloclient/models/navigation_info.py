from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_info import FindInfo


T = TypeVar("T", bound="NavigationInfo")


@_attrs_define
class NavigationInfo:
    """NavigationInfo is used as traversal information for structured bulk operations restricting
    specific processsing, e.g. pooled jobs, to scalable amounts. It provides parameters controlling
     the traversal.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            max_depth (Union[Unset, int]): The maximum depth of the tree walk. Passing maxDepth &lt; 1 turns off this limit.
            max_siblings (Union[Unset, int]): The maximum number of siblings for one tree level.
                This limit is most useful for ignoring the
                 contents of large folders. Passing maxSiblings &lt; 1 will turn the limit off.
            ignore_documents (Union[Unset, bool]): ignore the navigation of documents
            find_info (Union[Unset, FindInfo]): This class controls the search function findFirstSords.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            start_i_ds (Union[Unset, List[str]]):
            max_count (Union[Unset, int]): maxCount is the overall maximum amount of visited nodes and is independent of
                successful
                processing. maxCount does not depend on successful processing to be incremented, and it can
                 stop the traversal before any of the other limits have been reached. Passing maxCount &lt; 1
                 will turn off this limit.
    """

    max_depth: Union[Unset, int] = UNSET
    max_siblings: Union[Unset, int] = UNSET
    ignore_documents: Union[Unset, bool] = UNSET
    find_info: Union[Unset, "FindInfo"] = UNSET
    start_i_ds: Union[Unset, List[str]] = UNSET
    max_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_depth = self.max_depth

        max_siblings = self.max_siblings

        ignore_documents = self.ignore_documents

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        start_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.start_i_ds, Unset):
            start_i_ds = self.start_i_ds

        max_count = self.max_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_depth is not UNSET:
            field_dict["maxDepth"] = max_depth
        if max_siblings is not UNSET:
            field_dict["maxSiblings"] = max_siblings
        if ignore_documents is not UNSET:
            field_dict["ignoreDocuments"] = ignore_documents
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info
        if start_i_ds is not UNSET:
            field_dict["startIDs"] = start_i_ds
        if max_count is not UNSET:
            field_dict["maxCount"] = max_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_info import FindInfo

        d = src_dict.copy()
        max_depth = d.pop("maxDepth", UNSET)

        max_siblings = d.pop("maxSiblings", UNSET)

        ignore_documents = d.pop("ignoreDocuments", UNSET)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindInfo.from_dict(_find_info)

        start_i_ds = cast(List[str], d.pop("startIDs", UNSET))

        max_count = d.pop("maxCount", UNSET)

        navigation_info = cls(
            max_depth=max_depth,
            max_siblings=max_siblings,
            ignore_documents=ignore_documents,
            find_info=find_info,
            start_i_ds=start_i_ds,
            max_count=max_count,
        )

        navigation_info.additional_properties = d
        return navigation_info

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
