from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientInfo")


@_attrs_define
class ClientInfo:
    """Contains the session ticket and the users language and country.
    Each Indexserver interface function, except the
     login, requires a <code>ClientInfo</code> object as parameter with a valid session ticket.
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            call_id (Union[Unset, str]): This string is used for debugging purposes only. It is displayed in error messages
                and reports.
            country (Union[Unset, str]): Country in ISO 3166 format - this is the country for the ELO Client.
                <table border="2" summary="">
                 <tr>
                 </tr>
                 <tr>
                 <td>CZ</td>
                 <td>Czeach Republic</td>
                 </tr>
                 <tr>
                 <td>FR</td>
                 <td>France</td>
                 </tr>
                 <tr>
                 <td>DE</td>
                 <td>Germany</td>
                 </tr>
                 <tr>
                 <td>GR</td>
                 <td>Greece</td>
                 </tr>
                 <tr>
                 <td>ES</td>
                 <td>Spain</td>
                 </tr>
                 <tr>
                 <td>PL</td>
                 <td>Poland</td>
                 </tr>
                 <tr>
                 <td>GB</td>
                 <td>United Kingdom</td>
                 </tr>
                 <tr>
                 <td>US</td>
                 <td>United States</td>
                 </tr>
                 </table>
            language (Union[Unset, str]): The users language in ISO 639 format. Exception messages will be supplied in this
                language.
                <table border="2" summary="">
                 <tr>
                 </tr>
                 <tr>
                 <td>cs</td>
                 <td>Czech</td>
                 </tr>
                 <tr>
                 <td>de</td>
                 <td>German</td>
                 </tr>
                 <tr>
                 <td>el</td>
                 <td>Greek</td>
                 </tr>
                 <tr>
                 <td>en</td>
                 <td>English</td>
                 </tr>
                 <tr>
                 <td>es</td>
                 <td>Spanish</td>
                 </tr>
                 <tr>
                 <td>fr</td>
                 <td>French</td>
                 </tr>
                 <tr>
                 <td>pl</td>
                 <td>Polish</td>
                 </tr>
                 </table>
                 Only languages for which the localisations of the Indexserver resources exist can be selected, otherwise the
                 messages are displayed in the default language.
            ticket (Union[Unset, str]): <p>
                This is the session ID in the communication between the client and the Indexserver. It has a limited lifetime.
                The
                 lifetime can be configured at the ELOAM (access manager server). The Indexserver returns a valid ticket if the
                 IXServicePortIF.login call succeeds. The lifetime of the ticket can be extended by calling
                IXServicePortIF.alive.
                 </p>
            time_zone (Union[Unset, str]): The time zone for the ELO client.
                Can be one of the predefined time zone IDs in the Java platform or a string of
                 format "GMT" + sign + hh + ":" + mm.
            options (Union[Unset, int]): Internal use only.
                Bit 0 of this member is set for requests that are send from one Indexserver instance to another
                 instance in load balancing scenarios.
    """

    call_id: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    ticket: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    options: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        call_id = self.call_id
        country = self.country
        language = self.language
        ticket = self.ticket
        time_zone = self.time_zone
        options = self.options

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_id is not UNSET:
            field_dict["callId"] = call_id
        if country is not UNSET:
            field_dict["country"] = country
        if language is not UNSET:
            field_dict["language"] = language
        if ticket is not UNSET:
            field_dict["ticket"] = ticket
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        call_id = d.pop("callId", UNSET)

        country = d.pop("country", UNSET)

        language = d.pop("language", UNSET)

        ticket = d.pop("ticket", UNSET)

        time_zone = d.pop("timeZone", UNSET)

        options = d.pop("options", UNSET)

        client_info = cls(
            call_id=call_id,
            country=country,
            language=language,
            ticket=ticket,
            time_zone=time_zone,
            options=options,
        )

        client_info.additional_properties = d
        return client_info

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
