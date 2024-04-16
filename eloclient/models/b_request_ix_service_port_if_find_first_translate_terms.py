from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_info import ClientInfo
    from ..models.find_translate_term_info import FindTranslateTermInfo


T = TypeVar("T", bound="BRequestIXServicePortIFFindFirstTranslateTerms")


@_attrs_define
class BRequestIXServicePortIFFindFirstTranslateTerms:
    """
    Attributes:
        max_ (Union[Unset, int]):
        ci (Union[Unset, ClientInfo]): Contains the session ticket and the users language and country.
            Each Indexserver interface
             function, except the login, requires a <code>ClientInfo</code> object as parameter with a valid
             session ticket.
             <p>
             Copyright: Copyright (c) 2004
             </p>
             <p>
             Organisation: ELO Digital Office GmbH
             </p>
        find_info (Union[Unset, FindTranslateTermInfo]): This class is used to find translations of terms.
            Localization information is stored in two kinds of storage: in the database and in property files
             in the repository. The former kind use the database table <code>translations</code> which has a
             column for each language. This localization data can be modified or extended via API function
             {@link IXServicePortIF#checkinTranslateTerms(ClientInfo, TranslateTerm[], LockZ)}. The latter
             kind stores localization as property files under /Administration/Localization. This data can only
             be changed via checkin/out and takes effect only after Indexserver re-start.

             Indexserver function
             {@link IXServicePortIF#findFirstTranslateTerms(ClientInfo, FindTranslateTermInfo, int)} searches
             over both localization sources and returns matches from both. The translations found in the
             database are returned first.

             EIX-2912: Since IX version 21.3, a language is specified as IETF language tag (lang). The
             language part is from ISO 639-1. It is optionally followed by a country tag from ISO 3166-1
             alpha-2. The parts are separated by hyphen. Examples: de-DE, de-CH, de-AT. The function tries to
             find the translation for a given lang in the following order:

             <pre>
             1. lang as defined, e.g. de-CH
             2. lang without country, e.g. de
             3. first lang with the same language tag, e.g. de-DE
             4. first system language
             </pre>
    """

    max_: Union[Unset, int] = UNSET
    ci: Union[Unset, "ClientInfo"] = UNSET
    find_info: Union[Unset, "FindTranslateTermInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_ = self.max_

        ci: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ci, Unset):
            ci = self.ci.to_dict()

        find_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_info, Unset):
            find_info = self.find_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if ci is not UNSET:
            field_dict["ci"] = ci
        if find_info is not UNSET:
            field_dict["findInfo"] = find_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.client_info import ClientInfo
        from ..models.find_translate_term_info import FindTranslateTermInfo

        d = src_dict.copy()
        max_ = d.pop("max", UNSET)

        _ci = d.pop("ci", UNSET)
        ci: Union[Unset, ClientInfo]
        if isinstance(_ci, Unset):
            ci = UNSET
        else:
            ci = ClientInfo.from_dict(_ci)

        _find_info = d.pop("findInfo", UNSET)
        find_info: Union[Unset, FindTranslateTermInfo]
        if isinstance(_find_info, Unset):
            find_info = UNSET
        else:
            find_info = FindTranslateTermInfo.from_dict(_find_info)

        b_request_ix_service_port_if_find_first_translate_terms = cls(
            max_=max_,
            ci=ci,
            find_info=find_info,
        )

        b_request_ix_service_port_if_find_first_translate_terms.additional_properties = d
        return b_request_ix_service_port_if_find_first_translate_terms

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
