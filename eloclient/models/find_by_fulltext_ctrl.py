from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FindByFulltextCtrl")


@_attrs_define
class FindByFulltextCtrl:
    """This class is used to search for objects that have to be indexed by the fulltext database engine.
    <p>
     The selected objects are ordered by their timestamp. If the search process is interrupted because
     of a timeout or because the FindOptions.totalCount limit is reached, all the Objects of the lates
     timestamp second are discarded.
     </p>
     <p>
     If the search process is terminated due to breakTotalCount and the array of results is empty, the
     search should be repeated with a greater value for totalCount.
     </p>
     <p>
     Access checking is performed as in all other searches.
     </p>
     <p>
     A search of this type can only be combined with FindOptions.totalCount and
     FindOptions.timeoutSeconds.
     </p>
     <p>
     The results are returned in the member FindInfo.fulltextCtrlResultItems. The Sord objects are
     available in the member FindInfo.sords too.
     </p>

        Attributes:
            only_docs (Union[Unset, bool]): Find next documents for textreader.
            reindex (Union[Unset, bool]): Re-index processing.
                If this member is true, a search returns objects from the largest object
                 ID to 2. If this member is false, a search returns the next objects in a timestamp interval.
            end_t_stamp (Union[Unset, str]): Find objects from this date or older.
                If the value is null or empty, the time range has no
                 upper limit.
            start_t_stamp (Union[Unset, str]): Find objects from this date or newer.
                This value can be null or empty in which case the time
                 range has no lower limit.
            profile_key_prefix (Union[Unset, str]): Key prefix for loop state.
    """

    only_docs: Union[Unset, bool] = UNSET
    reindex: Union[Unset, bool] = UNSET
    end_t_stamp: Union[Unset, str] = UNSET
    start_t_stamp: Union[Unset, str] = UNSET
    profile_key_prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        only_docs = self.only_docs

        reindex = self.reindex

        end_t_stamp = self.end_t_stamp

        start_t_stamp = self.start_t_stamp

        profile_key_prefix = self.profile_key_prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if only_docs is not UNSET:
            field_dict["onlyDocs"] = only_docs
        if reindex is not UNSET:
            field_dict["reindex"] = reindex
        if end_t_stamp is not UNSET:
            field_dict["endTStamp"] = end_t_stamp
        if start_t_stamp is not UNSET:
            field_dict["startTStamp"] = start_t_stamp
        if profile_key_prefix is not UNSET:
            field_dict["profileKeyPrefix"] = profile_key_prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        only_docs = d.pop("onlyDocs", UNSET)

        reindex = d.pop("reindex", UNSET)

        end_t_stamp = d.pop("endTStamp", UNSET)

        start_t_stamp = d.pop("startTStamp", UNSET)

        profile_key_prefix = d.pop("profileKeyPrefix", UNSET)

        find_by_fulltext_ctrl = cls(
            only_docs=only_docs,
            reindex=reindex,
            end_t_stamp=end_t_stamp,
            start_t_stamp=start_t_stamp,
            profile_key_prefix=profile_key_prefix,
        )

        find_by_fulltext_ctrl.additional_properties = d
        return find_by_fulltext_ctrl

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
