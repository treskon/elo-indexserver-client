from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldTypeE")


@_attrs_define
class FieldTypeE:
    """<p>
    This enum defines how should be searched for query terms.
     </p>

     <p>
     It can, for example, be used with {@link QueryFilter#fieldType}
     </p>
     <p>
     For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
     therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
     </p>

        Attributes:
            date (Union[Unset, FieldTypeE]): <p>
                This enum defines how should be searched for query terms.
                 </p>

                 <p>
                 It can, for example, be used with {@link QueryFilter#fieldType}
                 </p>
                 <p>
                 For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
                 therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
                 </p>
            tokenized (Union[Unset, FieldTypeE]): <p>
                This enum defines how should be searched for query terms.
                 </p>

                 <p>
                 It can, for example, be used with {@link QueryFilter#fieldType}
                 </p>
                 <p>
                 For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
                 therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
                 </p>
            not_tokenized (Union[Unset, FieldTypeE]): <p>
                This enum defines how should be searched for query terms.
                 </p>

                 <p>
                 It can, for example, be used with {@link QueryFilter#fieldType}
                 </p>
                 <p>
                 For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
                 therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
                 </p>
            numeric (Union[Unset, FieldTypeE]): <p>
                This enum defines how should be searched for query terms.
                 </p>

                 <p>
                 It can, for example, be used with {@link QueryFilter#fieldType}
                 </p>
                 <p>
                 For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
                 therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
                 </p>
            guid (Union[Unset, FieldTypeE]): <p>
                This enum defines how should be searched for query terms.
                 </p>

                 <p>
                 It can, for example, be used with {@link QueryFilter#fieldType}
                 </p>
                 <p>
                 For every {@link SearchFieldE} it is defined, which {@link FieldTypeE} can be used and,
                 therefore, which data classes (e.g. {@link StringSingleValue}) can be used.
                 </p>
    """

    date: Union[Unset, "FieldTypeE"] = UNSET
    tokenized: Union[Unset, "FieldTypeE"] = UNSET
    not_tokenized: Union[Unset, "FieldTypeE"] = UNSET
    numeric: Union[Unset, "FieldTypeE"] = UNSET
    guid: Union[Unset, "FieldTypeE"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.to_dict()

        tokenized: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tokenized, Unset):
            tokenized = self.tokenized.to_dict()

        not_tokenized: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.not_tokenized, Unset):
            not_tokenized = self.not_tokenized.to_dict()

        numeric: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.numeric, Unset):
            numeric = self.numeric.to_dict()

        guid: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.guid, Unset):
            guid = self.guid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if tokenized is not UNSET:
            field_dict["tokenized"] = tokenized
        if not_tokenized is not UNSET:
            field_dict["notTokenized"] = not_tokenized
        if numeric is not UNSET:
            field_dict["numeric"] = numeric
        if guid is not UNSET:
            field_dict["guid"] = guid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date = d.pop("date", UNSET)
        date: Union[Unset, FieldTypeE]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = FieldTypeE.from_dict(_date)

        _tokenized = d.pop("tokenized", UNSET)
        tokenized: Union[Unset, FieldTypeE]
        if isinstance(_tokenized, Unset):
            tokenized = UNSET
        else:
            tokenized = FieldTypeE.from_dict(_tokenized)

        _not_tokenized = d.pop("notTokenized", UNSET)
        not_tokenized: Union[Unset, FieldTypeE]
        if isinstance(_not_tokenized, Unset):
            not_tokenized = UNSET
        else:
            not_tokenized = FieldTypeE.from_dict(_not_tokenized)

        _numeric = d.pop("numeric", UNSET)
        numeric: Union[Unset, FieldTypeE]
        if isinstance(_numeric, Unset):
            numeric = UNSET
        else:
            numeric = FieldTypeE.from_dict(_numeric)

        _guid = d.pop("guid", UNSET)
        guid: Union[Unset, FieldTypeE]
        if isinstance(_guid, Unset):
            guid = UNSET
        else:
            guid = FieldTypeE.from_dict(_guid)

        field_type_e = cls(
            date=date,
            tokenized=tokenized,
            not_tokenized=not_tokenized,
            numeric=numeric,
            guid=guid,
        )

        field_type_e.additional_properties = d
        return field_type_e

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
