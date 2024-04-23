from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_mode_z import SearchModeZ


T = TypeVar("T", bound="SearchModeC")


@_attrs_define
class SearchModeC:
    """<p>
    This class defines options used in <code>FindOptions.searchMode</code>.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            bset_and (Union[Unset, str]):
            or_ (Union[Unset, SearchModeZ]): <p>
                This class encapsulates the constants of <code>SearchModeC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            one_term (Union[Unset, SearchModeZ]): <p>
                This class encapsulates the constants of <code>SearchModeC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_expression (Union[Unset, str]):
            and_ (Union[Unset, SearchModeZ]): <p>
                This class encapsulates the constants of <code>SearchModeC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            bset_one_term (Union[Unset, str]):
            bset_or (Union[Unset, str]):
            expression (Union[Unset, SearchModeZ]): <p>
                This class encapsulates the constants of <code>SearchModeC</code>
                 </p>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    bset_and: Union[Unset, str] = UNSET
    or_: Union[Unset, "SearchModeZ"] = UNSET
    one_term: Union[Unset, "SearchModeZ"] = UNSET
    bset_expression: Union[Unset, str] = UNSET
    and_: Union[Unset, "SearchModeZ"] = UNSET
    bset_one_term: Union[Unset, str] = UNSET
    bset_or: Union[Unset, str] = UNSET
    expression: Union[Unset, "SearchModeZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_and = self.bset_and

        or_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.or_, Unset):
            or_ = self.or_.to_dict()

        one_term: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.one_term, Unset):
            one_term = self.one_term.to_dict()

        bset_expression = self.bset_expression

        and_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.and_, Unset):
            and_ = self.and_.to_dict()

        bset_one_term = self.bset_one_term

        bset_or = self.bset_or

        expression: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expression, Unset):
            expression = self.expression.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_and is not UNSET:
            field_dict["bsetAND"] = bset_and
        if or_ is not UNSET:
            field_dict["OR"] = or_
        if one_term is not UNSET:
            field_dict["ONE_TERM"] = one_term
        if bset_expression is not UNSET:
            field_dict["bsetEXPRESSION"] = bset_expression
        if and_ is not UNSET:
            field_dict["AND"] = and_
        if bset_one_term is not UNSET:
            field_dict["bsetONE_TERM"] = bset_one_term
        if bset_or is not UNSET:
            field_dict["bsetOR"] = bset_or
        if expression is not UNSET:
            field_dict["EXPRESSION"] = expression

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_mode_z import SearchModeZ

        d = src_dict.copy()
        bset_and = d.pop("bsetAND", UNSET)

        _or_ = d.pop("OR", UNSET)
        or_: Union[Unset, SearchModeZ]
        if isinstance(_or_, Unset):
            or_ = UNSET
        else:
            or_ = SearchModeZ.from_dict(_or_)

        _one_term = d.pop("ONE_TERM", UNSET)
        one_term: Union[Unset, SearchModeZ]
        if isinstance(_one_term, Unset):
            one_term = UNSET
        else:
            one_term = SearchModeZ.from_dict(_one_term)

        bset_expression = d.pop("bsetEXPRESSION", UNSET)

        _and_ = d.pop("AND", UNSET)
        and_: Union[Unset, SearchModeZ]
        if isinstance(_and_, Unset):
            and_ = UNSET
        else:
            and_ = SearchModeZ.from_dict(_and_)

        bset_one_term = d.pop("bsetONE_TERM", UNSET)

        bset_or = d.pop("bsetOR", UNSET)

        _expression = d.pop("EXPRESSION", UNSET)
        expression: Union[Unset, SearchModeZ]
        if isinstance(_expression, Unset):
            expression = UNSET
        else:
            expression = SearchModeZ.from_dict(_expression)

        search_mode_c = cls(
            bset_and=bset_and,
            or_=or_,
            one_term=one_term,
            bset_expression=bset_expression,
            and_=and_,
            bset_one_term=bset_one_term,
            bset_or=bset_or,
            expression=expression,
        )

        search_mode_c.additional_properties = d
        return search_mode_c

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
