from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessRegion")


@_attrs_define
class ProcessRegion:
    """This class specifies the options for setting a sord's {@link Sord#regionId} (i.e.
    ID of the
     region it belongs to) for sub-trees of sords. It is used as member in {@link ProcessInfo} and
     defines a respective operation.

     <p>
     Copyright: Copyright (c) 2022
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            is_new_region (Union[Unset, bool]): Determines if the root sord has changed from "is no region" to "is region".
                This can only
                 happen during checkin of a sord (flag {@link SordDetails#isRegion()} and never when a sord is
                 moved.
            region_id (Union[Unset, int]): The resulting regionId of the root sord which has to be passed to its sub-tree.
            root_obj_id (Union[Unset, int]): The id of the root sord for which its sub-tree has to be adapted according to
                its region.
    """

    is_new_region: Union[Unset, bool] = UNSET
    region_id: Union[Unset, int] = UNSET
    root_obj_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_new_region = self.is_new_region

        region_id = self.region_id

        root_obj_id = self.root_obj_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_new_region is not UNSET:
            field_dict["isNewRegion"] = is_new_region
        if region_id is not UNSET:
            field_dict["regionId"] = region_id
        if root_obj_id is not UNSET:
            field_dict["rootObjId"] = root_obj_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_new_region = d.pop("isNewRegion", UNSET)

        region_id = d.pop("regionId", UNSET)

        root_obj_id = d.pop("rootObjId", UNSET)

        process_region = cls(
            is_new_region=is_new_region,
            region_id=region_id,
            root_obj_id=root_obj_id,
        )

        process_region.additional_properties = d
        return process_region

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
