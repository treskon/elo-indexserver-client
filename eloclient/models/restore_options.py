from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestoreOptions")


@_attrs_define
class RestoreOptions:
    """<p>
    This class contains several options for undeleting archive SORDs by <code>restoreSord</code>
     </p>
     <p>
     Copyright: Copyright (c) 2004-2006
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            min_delete_date (Union[Unset, str]): <p>
                Restore only document versions that are deleted after <code>minDeleteDate</code>. Its String
                 representation is the ISO format in the client's time zone.
                 </p>
            single_object (Union[Unset, bool]): <p>
                <code>singleObject=true</code> restricts the operation to the specified object not traversing
                 sub trees.
                 </p>
            min_i_date (Union[Unset, str]): <p>
                <code>minIDate</code> ist the ISO representation of the local date used to mark the lower limit
                 for restoring.
                 </p>
            parent_id (Union[Unset, str]): <p>
                Since references also got a delete date, they can be restored independently from their main
                 reference. To restore a reference selectively, set parentId to the references' parentId.
                 Restoring a reference does not affect the delete status of its main reference.
                 </p>
                 <p>
                 Setting parentId implies singleObject=true.
                 </p>
    """

    min_delete_date: Union[Unset, str] = UNSET
    single_object: Union[Unset, bool] = UNSET
    min_i_date: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        min_delete_date = self.min_delete_date

        single_object = self.single_object

        min_i_date = self.min_i_date

        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_delete_date is not UNSET:
            field_dict["minDeleteDate"] = min_delete_date
        if single_object is not UNSET:
            field_dict["singleObject"] = single_object
        if min_i_date is not UNSET:
            field_dict["minIDate"] = min_i_date
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        min_delete_date = d.pop("minDeleteDate", UNSET)

        single_object = d.pop("singleObject", UNSET)

        min_i_date = d.pop("minIDate", UNSET)

        parent_id = d.pop("parentId", UNSET)

        restore_options = cls(
            min_delete_date=min_delete_date,
            single_object=single_object,
            min_i_date=min_i_date,
            parent_id=parent_id,
        )

        restore_options.additional_properties = d
        return restore_options

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
