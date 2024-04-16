from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_class import ValueClass


T = TypeVar("T", bound="InvalidateCacheInfoParam")


@_attrs_define
class InvalidateCacheInfoParam:
    """ParamObject for InvalidateCacheInfo.

    Attributes:
        flag (Union[Unset, int]): Parameter, depends on the purpose of this object. Set flag to InvalidateCacheC.
            HASHTAGCOUNT to
             use for HashtagCountCache. In case of InvalidateCacheC.WORKFLOW: WFDiagram.id
        count (Union[Unset, int]): Parameter, depends on the purpose of this object.
            <p>
             In case of InvalidateCacheC.HASHTAGCOUNT:
             <ul>
             <li>Case 1: Increases count of corresponding Hashtag
             <li>Case -1: Decreases count of corresponding Hashtag
             <li>Any other number: Sets count of corresponding Hashtag this number
             </ul>
             </p>
             <p>
             In case of InvalidateCacheC.WORKFLOW: Hash code computed over WFDiagram members.
             </p>
        guid (Union[Unset, str]): Parameter, depends on the purpose of this object.
            <p>
             In case of InvalidateCacheC.HASHTAGCOUNT:
             <ul>
             <li>Related to HashtagGuid which is set according to count.
             <li>If guid is null or empty, the complete HashtagCountCache is rebuild from DB.
             </ul>
             </p>
             <p>
             In case of InvalidateCacheC.WORKFLOW: WFDiagram.tstamp
             </p>
             <p>
             In case of InvalidateCacheC.TRANSLATE_TERM: TranslateTerm.guid
             </p>
        object_value (Union[Unset, ValueClass]):
    """

    flag: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    guid: Union[Unset, str] = UNSET
    object_value: Union[Unset, "ValueClass"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        flag = self.flag

        count = self.count

        guid = self.guid

        object_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.object_value, Unset):
            object_value = self.object_value.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if flag is not UNSET:
            field_dict["flag"] = flag
        if count is not UNSET:
            field_dict["count"] = count
        if guid is not UNSET:
            field_dict["guid"] = guid
        if object_value is not UNSET:
            field_dict["objectValue"] = object_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.value_class import ValueClass

        d = src_dict.copy()
        flag = d.pop("flag", UNSET)

        count = d.pop("count", UNSET)

        guid = d.pop("guid", UNSET)

        _object_value = d.pop("objectValue", UNSET)
        object_value: Union[Unset, ValueClass]
        if isinstance(_object_value, Unset):
            object_value = UNSET
        else:
            object_value = ValueClass.from_dict(_object_value)

        invalidate_cache_info_param = cls(
            flag=flag,
            count=count,
            guid=guid,
            object_value=object_value,
        )

        invalidate_cache_info_param.additional_properties = d
        return invalidate_cache_info_param

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
