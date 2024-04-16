from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acl_item import AclItem
    from ..models.cardinality import Cardinality


T = TypeVar("T", bound="AspectAssoc")


@_attrs_define
class AspectAssoc:
    """This class defines an aspect association.
    An AspectAssoc defines a reference to a keywording
     {@link Aspect} in {@link DocMask#aspectAssocs}.

        Attributes:
            region_inherit (Union[Unset, bool]): Indicates if the Sord object passes the aspect object to all sub-entries if
                this AspectAssoc
                object is contained in a region mask.
            translation_key (Union[Unset, str]): Translation-keyword for {@link AspectAssoc#displayName}.
                Defines the {@link #displayName} as
                 technical resource ID. If this value is set, translations are only based on content of
                 properties files and not on translation table.
            display_name (Union[Unset, str]): Locale specific name. Readonly. This value is the resolved {@link
                #translationKey}.
            acl_items (Union[Unset, List['AclItem']]):
            name (Union[Unset, str]): Technical aspect association name. This member must start with a character between 'A'
                and 'Z'.
                The following characters must be alpha-numeric including underscore.
            aspect_id (Union[Unset, int]): ID of the referenced aspect.
            acl (Union[Unset, str]): Access control list.
            cardinality (Union[Unset, Cardinality]): Aspect cardinality.
    """

    region_inherit: Union[Unset, bool] = UNSET
    translation_key: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    acl_items: Union[Unset, List["AclItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    aspect_id: Union[Unset, int] = UNSET
    acl: Union[Unset, str] = UNSET
    cardinality: Union[Unset, "Cardinality"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        region_inherit = self.region_inherit

        translation_key = self.translation_key

        display_name = self.display_name

        acl_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.acl_items, Unset):
            acl_items = []
            for acl_items_item_data in self.acl_items:
                acl_items_item = acl_items_item_data.to_dict()
                acl_items.append(acl_items_item)

        name = self.name

        aspect_id = self.aspect_id

        acl = self.acl

        cardinality: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cardinality, Unset):
            cardinality = self.cardinality.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if region_inherit is not UNSET:
            field_dict["regionInherit"] = region_inherit
        if translation_key is not UNSET:
            field_dict["translationKey"] = translation_key
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if acl_items is not UNSET:
            field_dict["aclItems"] = acl_items
        if name is not UNSET:
            field_dict["name"] = name
        if aspect_id is not UNSET:
            field_dict["aspectId"] = aspect_id
        if acl is not UNSET:
            field_dict["acl"] = acl
        if cardinality is not UNSET:
            field_dict["cardinality"] = cardinality

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.acl_item import AclItem
        from ..models.cardinality import Cardinality

        d = src_dict.copy()
        region_inherit = d.pop("regionInherit", UNSET)

        translation_key = d.pop("translationKey", UNSET)

        display_name = d.pop("displayName", UNSET)

        acl_items = []
        _acl_items = d.pop("aclItems", UNSET)
        for acl_items_item_data in _acl_items or []:
            acl_items_item = AclItem.from_dict(acl_items_item_data)

            acl_items.append(acl_items_item)

        name = d.pop("name", UNSET)

        aspect_id = d.pop("aspectId", UNSET)

        acl = d.pop("acl", UNSET)

        _cardinality = d.pop("cardinality", UNSET)
        cardinality: Union[Unset, Cardinality]
        if isinstance(_cardinality, Unset):
            cardinality = UNSET
        else:
            cardinality = Cardinality.from_dict(_cardinality)

        aspect_assoc = cls(
            region_inherit=region_inherit,
            translation_key=translation_key,
            display_name=display_name,
            acl_items=acl_items,
            name=name,
            aspect_id=aspect_id,
            acl=acl,
            cardinality=cardinality,
        )

        aspect_assoc.additional_properties = d
        return aspect_assoc

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
