from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_task_sort_order_z import UserTaskSortOrderZ


T = TypeVar("T", bound="UserTaskSortOrderC")


@_attrs_define
class UserTaskSortOrderC:
    """
    Attributes:
        priority_date_name_inv (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the
            UserTaskSortOrderC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        date_priority_name (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the
            UserTaskSortOrderC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        priority_date_name (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the
            UserTaskSortOrderC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        name_priority_date_inv (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the
            UserTaskSortOrderC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        bset_name_priority_date_inv (Union[Unset, str]):
        bset_name_priority_date (Union[Unset, str]):
        name_priority_date (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the
            UserTaskSortOrderC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        bset_flag_sort_order_inv (Union[Unset, str]):
        bset_priority_date_name (Union[Unset, str]):
        date_priority_name_inv (Union[Unset, UserTaskSortOrderZ]): This class encapsulates the constants of the
            UserTaskSortOrderC class.
            <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        bset_priority_date_name_inv (Union[Unset, str]):
        bset_date_priority_name (Union[Unset, str]):
        bset_date_priority_name_inv (Union[Unset, str]):
    """

    priority_date_name_inv: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    date_priority_name: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    priority_date_name: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    name_priority_date_inv: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    bset_name_priority_date_inv: Union[Unset, str] = UNSET
    bset_name_priority_date: Union[Unset, str] = UNSET
    name_priority_date: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    bset_flag_sort_order_inv: Union[Unset, str] = UNSET
    bset_priority_date_name: Union[Unset, str] = UNSET
    date_priority_name_inv: Union[Unset, "UserTaskSortOrderZ"] = UNSET
    bset_priority_date_name_inv: Union[Unset, str] = UNSET
    bset_date_priority_name: Union[Unset, str] = UNSET
    bset_date_priority_name_inv: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        priority_date_name_inv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority_date_name_inv, Unset):
            priority_date_name_inv = self.priority_date_name_inv.to_dict()

        date_priority_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_priority_name, Unset):
            date_priority_name = self.date_priority_name.to_dict()

        priority_date_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.priority_date_name, Unset):
            priority_date_name = self.priority_date_name.to_dict()

        name_priority_date_inv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name_priority_date_inv, Unset):
            name_priority_date_inv = self.name_priority_date_inv.to_dict()

        bset_name_priority_date_inv = self.bset_name_priority_date_inv

        bset_name_priority_date = self.bset_name_priority_date

        name_priority_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name_priority_date, Unset):
            name_priority_date = self.name_priority_date.to_dict()

        bset_flag_sort_order_inv = self.bset_flag_sort_order_inv

        bset_priority_date_name = self.bset_priority_date_name

        date_priority_name_inv: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date_priority_name_inv, Unset):
            date_priority_name_inv = self.date_priority_name_inv.to_dict()

        bset_priority_date_name_inv = self.bset_priority_date_name_inv

        bset_date_priority_name = self.bset_date_priority_name

        bset_date_priority_name_inv = self.bset_date_priority_name_inv

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority_date_name_inv is not UNSET:
            field_dict["PRIORITY_DATE_NAME_INV"] = priority_date_name_inv
        if date_priority_name is not UNSET:
            field_dict["DATE_PRIORITY_NAME"] = date_priority_name
        if priority_date_name is not UNSET:
            field_dict["PRIORITY_DATE_NAME"] = priority_date_name
        if name_priority_date_inv is not UNSET:
            field_dict["NAME_PRIORITY_DATE_INV"] = name_priority_date_inv
        if bset_name_priority_date_inv is not UNSET:
            field_dict["bsetNAME_PRIORITY_DATE_INV"] = bset_name_priority_date_inv
        if bset_name_priority_date is not UNSET:
            field_dict["bsetNAME_PRIORITY_DATE"] = bset_name_priority_date
        if name_priority_date is not UNSET:
            field_dict["NAME_PRIORITY_DATE"] = name_priority_date
        if bset_flag_sort_order_inv is not UNSET:
            field_dict["bsetFLAG_SORT_ORDER_INV"] = bset_flag_sort_order_inv
        if bset_priority_date_name is not UNSET:
            field_dict["bsetPRIORITY_DATE_NAME"] = bset_priority_date_name
        if date_priority_name_inv is not UNSET:
            field_dict["DATE_PRIORITY_NAME_INV"] = date_priority_name_inv
        if bset_priority_date_name_inv is not UNSET:
            field_dict["bsetPRIORITY_DATE_NAME_INV"] = bset_priority_date_name_inv
        if bset_date_priority_name is not UNSET:
            field_dict["bsetDATE_PRIORITY_NAME"] = bset_date_priority_name
        if bset_date_priority_name_inv is not UNSET:
            field_dict["bsetDATE_PRIORITY_NAME_INV"] = bset_date_priority_name_inv

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_task_sort_order_z import UserTaskSortOrderZ

        d = src_dict.copy()
        _priority_date_name_inv = d.pop("PRIORITY_DATE_NAME_INV", UNSET)
        priority_date_name_inv: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_priority_date_name_inv, Unset):
            priority_date_name_inv = UNSET
        else:
            priority_date_name_inv = UserTaskSortOrderZ.from_dict(_priority_date_name_inv)

        _date_priority_name = d.pop("DATE_PRIORITY_NAME", UNSET)
        date_priority_name: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_date_priority_name, Unset):
            date_priority_name = UNSET
        else:
            date_priority_name = UserTaskSortOrderZ.from_dict(_date_priority_name)

        _priority_date_name = d.pop("PRIORITY_DATE_NAME", UNSET)
        priority_date_name: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_priority_date_name, Unset):
            priority_date_name = UNSET
        else:
            priority_date_name = UserTaskSortOrderZ.from_dict(_priority_date_name)

        _name_priority_date_inv = d.pop("NAME_PRIORITY_DATE_INV", UNSET)
        name_priority_date_inv: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_name_priority_date_inv, Unset):
            name_priority_date_inv = UNSET
        else:
            name_priority_date_inv = UserTaskSortOrderZ.from_dict(_name_priority_date_inv)

        bset_name_priority_date_inv = d.pop("bsetNAME_PRIORITY_DATE_INV", UNSET)

        bset_name_priority_date = d.pop("bsetNAME_PRIORITY_DATE", UNSET)

        _name_priority_date = d.pop("NAME_PRIORITY_DATE", UNSET)
        name_priority_date: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_name_priority_date, Unset):
            name_priority_date = UNSET
        else:
            name_priority_date = UserTaskSortOrderZ.from_dict(_name_priority_date)

        bset_flag_sort_order_inv = d.pop("bsetFLAG_SORT_ORDER_INV", UNSET)

        bset_priority_date_name = d.pop("bsetPRIORITY_DATE_NAME", UNSET)

        _date_priority_name_inv = d.pop("DATE_PRIORITY_NAME_INV", UNSET)
        date_priority_name_inv: Union[Unset, UserTaskSortOrderZ]
        if isinstance(_date_priority_name_inv, Unset):
            date_priority_name_inv = UNSET
        else:
            date_priority_name_inv = UserTaskSortOrderZ.from_dict(_date_priority_name_inv)

        bset_priority_date_name_inv = d.pop("bsetPRIORITY_DATE_NAME_INV", UNSET)

        bset_date_priority_name = d.pop("bsetDATE_PRIORITY_NAME", UNSET)

        bset_date_priority_name_inv = d.pop("bsetDATE_PRIORITY_NAME_INV", UNSET)

        user_task_sort_order_c = cls(
            priority_date_name_inv=priority_date_name_inv,
            date_priority_name=date_priority_name,
            priority_date_name=priority_date_name,
            name_priority_date_inv=name_priority_date_inv,
            bset_name_priority_date_inv=bset_name_priority_date_inv,
            bset_name_priority_date=bset_name_priority_date,
            name_priority_date=name_priority_date,
            bset_flag_sort_order_inv=bset_flag_sort_order_inv,
            bset_priority_date_name=bset_priority_date_name,
            date_priority_name_inv=date_priority_name_inv,
            bset_priority_date_name_inv=bset_priority_date_name_inv,
            bset_date_priority_name=bset_date_priority_name,
            bset_date_priority_name_inv=bset_date_priority_name_inv,
        )

        user_task_sort_order_c.additional_properties = d
        return user_task_sort_order_c

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
