from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.obj_key import ObjKey


T = TypeVar("T", bound="FindByIndex")


@_attrs_define
class FindByIndex:
    """Finds an object according to the object's index properties.
    The search terms are concatinated by the operator
     specified with FindOptions.searchMode. If FindOptionsC.OPERATOR_OR is the specified searchMode the members of this
     class are concatinated in the search string with the boolean operator "OR". Any other searchMode concatinates with
     "AND".

     Exception: userId and maskId are always used as "AND" terms.

     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            del_date_iso (Union[Unset, str]): Find objects with this due date. It is a single date value or a date range in
                ISO format.
            desc (Union[Unset, str]): Find objects with this term included in the description of the object (case
                insensitive).
                This value can be a list
                 of terms separated by blanks. The terms are concatinated with the operator specified by FindOptions.searchMode.
                The
                 wildcard * is allowed, it matches any number of characters. If desc is to be ignored this value must be set to
                 null.
            i_date_iso (Union[Unset, str]): Find objects with this internal date. It is a single date value or a date range
                in ISO format.
            mask_id (Union[Unset, str]): Find objects related to this mask ID or name.
                If the mask relation is to be ignored this value must be set to an
                 empty string or null.
            name (Union[Unset, str]): Find objects with this term(s) included in the name of the object (case insensitive).
                This value can be a list of
                 terms separated with blanks. They are concatinated with the operator specified by FindOptions.searchMode. The
                 wildcard * is allowed, it matches any number of characters. If name is to be ignored this value must be set to
                 null.
            exact_name (Union[Unset, bool]): If this option is false, all objects are found that contain the term specified
                in <code>name</code> anywhere in
                their short description (Sord.name). In other words: a search by <code>*name*</code> is executed. Set this
                option
                 true, if wildcards should not added implicitly to the search term.
            obj_keys (Union[Unset, List['ObjKey']]):
            owner_id (Union[Unset, str]): Find objects owned by the user with this user ID or name.
                If the owner is to be ignored this value must be set to
                 null.
            x_date_iso (Union[Unset, str]): Find objects with this external date. It is a single date value or a date range
                in ISO format.
                <p>
                 IX versions from 9.00.060 support relative date values. Relative date values give an offset to the current date
                and
                 use a format similar to ISO format: "{+|-}YYYY-MM-DD hh:mm:ss", whereby the separator characters can be
                omitted:
                 "{+|-}YYYYMMDDhhmmss". A relative date has to be prefixed by + (date is added) or - (date is subtracted).
                 </p>
                 <p>
                 Examples, assuming the current date is 2016-06-24 16:29:00
                 <table border="2">
                 <tr>
                 <td>Relative date</td>
                 <td>Resulting absolute date</td>
                 <td>Remark</td>
                 </tr>
                 <tr>
                 <td>+0001-00-00 00:00:00</td>
                 <td>2017-06-24 16:29</td>
                 <td>Next year, same month etc.</td>
                 </tr>
                 <tr>
                 <td>-0000-01-00 00:00:00</td>
                 <td>2016-05-24 16:29</td>
                 <td>Previous month, same day etc.</td>
                 </tr>
                 <tr>
                 <td>+0000</td>
                 <td>2016-01-01 00:00...2016-12-31 23:59</td>
                 <td>Search documents of this year. Incomplete relative dates are automatically expanded to a date range.</td>
                 </tr>
                 <tr>
                 <td>+0000-00</td>
                 <td>2016-06-01 00:00...2016-06-30 23:59</td>
                 <td>Search documents of this month.</td>
                 </tr>
                 <tr>
                 <td>-0000-01</td>
                 <td>2016-05-01 00:00...2016-05-31 23:59</td>
                 <td>Search documents of the last month.</td>
                 </tr>
                 <tr>
                 <td>-0000-00-10...+0000-00-00 00:00:00</td>
                 <td>2016-06-14 00:00...2016-06-24 16:29</td>
                 <td>Search documents from the last 10 days.</td>
                 </tr>
                 <tr>
                 <td>-0001...</td>
                 <td>2015-01-01 00:00...</td>
                 <td>Search documents from last year or newer.</td>
                 </tr>
                 </table>
                 </p>
                 <p>
                 <i>Hint: Only relative date values are allowed that could also be an absolute date. E.g. a relative date of 100
                 days or 13 months cannot be specified.</i>
                 </p>
            acl (Union[Unset, str]): Constrain results to objects with this access control list.
            path_id (Union[Unset, str]): Storage path ID or name
            kind (Union[Unset, str]): Colour. If the colour is to be ignored this value must be set to null.
            lock_id (Union[Unset, str]): Set this value to an user's id or name to search for objects currently locked by
                that user.
                To ignore this option,
                 set this value to <code>null</code> (default).
            mask_ids (Union[Unset, List[str]]):
            delete_user (Union[Unset, str]): Find objects deleted by the user with this user ID or name.
                If the deleted user is to be ignored this value must be
                 set to null.
            delete_date_iso (Union[Unset, str]): Find objects with this delete date. It is a single date value or a date
                range in ISO format.
    """

    del_date_iso: Union[Unset, str] = UNSET
    desc: Union[Unset, str] = UNSET
    i_date_iso: Union[Unset, str] = UNSET
    mask_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    exact_name: Union[Unset, bool] = UNSET
    obj_keys: Union[Unset, List["ObjKey"]] = UNSET
    owner_id: Union[Unset, str] = UNSET
    x_date_iso: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    path_id: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    lock_id: Union[Unset, str] = UNSET
    mask_ids: Union[Unset, List[str]] = UNSET
    delete_user: Union[Unset, str] = UNSET
    delete_date_iso: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        del_date_iso = self.del_date_iso
        desc = self.desc
        i_date_iso = self.i_date_iso
        mask_id = self.mask_id
        name = self.name
        exact_name = self.exact_name
        obj_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.obj_keys, Unset):
            obj_keys = []
            for obj_keys_item_data in self.obj_keys:
                obj_keys_item = obj_keys_item_data.to_dict()

                obj_keys.append(obj_keys_item)

        owner_id = self.owner_id
        x_date_iso = self.x_date_iso
        acl = self.acl
        path_id = self.path_id
        kind = self.kind
        lock_id = self.lock_id
        mask_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mask_ids, Unset):
            mask_ids = self.mask_ids

        delete_user = self.delete_user
        delete_date_iso = self.delete_date_iso

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if del_date_iso is not UNSET:
            field_dict["delDateIso"] = del_date_iso
        if desc is not UNSET:
            field_dict["desc"] = desc
        if i_date_iso is not UNSET:
            field_dict["iDateIso"] = i_date_iso
        if mask_id is not UNSET:
            field_dict["maskId"] = mask_id
        if name is not UNSET:
            field_dict["name"] = name
        if exact_name is not UNSET:
            field_dict["exactName"] = exact_name
        if obj_keys is not UNSET:
            field_dict["objKeys"] = obj_keys
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if x_date_iso is not UNSET:
            field_dict["xDateIso"] = x_date_iso
        if acl is not UNSET:
            field_dict["acl"] = acl
        if path_id is not UNSET:
            field_dict["pathId"] = path_id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if lock_id is not UNSET:
            field_dict["lockId"] = lock_id
        if mask_ids is not UNSET:
            field_dict["maskIds"] = mask_ids
        if delete_user is not UNSET:
            field_dict["deleteUser"] = delete_user
        if delete_date_iso is not UNSET:
            field_dict["deleteDateIso"] = delete_date_iso

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.obj_key import ObjKey

        d = src_dict.copy()
        del_date_iso = d.pop("delDateIso", UNSET)

        desc = d.pop("desc", UNSET)

        i_date_iso = d.pop("iDateIso", UNSET)

        mask_id = d.pop("maskId", UNSET)

        name = d.pop("name", UNSET)

        exact_name = d.pop("exactName", UNSET)

        obj_keys = []
        _obj_keys = d.pop("objKeys", UNSET)
        for obj_keys_item_data in _obj_keys or []:
            obj_keys_item = ObjKey.from_dict(obj_keys_item_data)

            obj_keys.append(obj_keys_item)

        owner_id = d.pop("ownerId", UNSET)

        x_date_iso = d.pop("xDateIso", UNSET)

        acl = d.pop("acl", UNSET)

        path_id = d.pop("pathId", UNSET)

        kind = d.pop("kind", UNSET)

        lock_id = d.pop("lockId", UNSET)

        mask_ids = cast(List[str], d.pop("maskIds", UNSET))

        delete_user = d.pop("deleteUser", UNSET)

        delete_date_iso = d.pop("deleteDateIso", UNSET)

        find_by_index = cls(
            del_date_iso=del_date_iso,
            desc=desc,
            i_date_iso=i_date_iso,
            mask_id=mask_id,
            name=name,
            exact_name=exact_name,
            obj_keys=obj_keys,
            owner_id=owner_id,
            x_date_iso=x_date_iso,
            acl=acl,
            path_id=path_id,
            kind=kind,
            lock_id=lock_id,
            mask_ids=mask_ids,
            delete_user=delete_user,
            delete_date_iso=delete_date_iso,
        )

        find_by_index.additional_properties = d
        return find_by_index

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
