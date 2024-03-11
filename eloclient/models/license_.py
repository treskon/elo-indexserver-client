import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_string import MapToString


T = TypeVar("T", bound="License")


@_attrs_define
class License:
    """<p>
    This class contains license information.
     </p>
     <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            backup (Union[Unset, bool]): Backup enabled.
            cold (Union[Unset, bool]): COLD
            demo_version (Union[Unset, bool]): Demo version.
            dispatch_folder (Union[Unset, bool]): Dispatch folder (Versendemappe)
            domea (Union[Unset, bool]): DOMEA
            email_only (Union[Unset, bool]): EMail
            features (Union[Unset, List[int]]):
            fultext (Union[Unset, bool]): Fulltext enabled.
            http_server (Union[Unset, bool]): HTTP DocServer
            index_server (Union[Unset, bool]): Indexserver
            limited_ig (Union[Unset, bool]): Limited Internet Gateway
            limited_version (Union[Unset, bool]): Limited version.
            nb_of_ig_licenses (Union[Unset, int]): Number of ELO Internet Gateway users.
            nb_of_server_licenses (Union[Unset, int]): Number of server licenses.
            professional (Union[Unset, bool]): True for ELOprofessional
            replication (Union[Unset, bool]): Replication enabled.
            sap_a_link (Union[Unset, bool]): SAPALINK interface
            serno (Union[Unset, str]): License key.
            signature (Union[Unset, bool]): SIGNATURE
            stack (Union[Unset, bool]): STACK
            tobid (Union[Unset, bool]): Tobit
            xml_import (Union[Unset, bool]): XML-Import
            nb_of_fulltext_langs (Union[Unset, int]): Number of languages for which linguistic processing can be used during
                fulltext indexing.
            license_options (Union[Unset, MapToString]):
            license_file_content (Union[Unset, str]): License file content.
            license_valid (Union[Unset, bool]): True, if license is valid.
            validity_date (Union[Unset, datetime.datetime]): License is valid until this date. This valid is null if the
                license does not expire.
    """

    backup: Union[Unset, bool] = UNSET
    cold: Union[Unset, bool] = UNSET
    demo_version: Union[Unset, bool] = UNSET
    dispatch_folder: Union[Unset, bool] = UNSET
    domea: Union[Unset, bool] = UNSET
    email_only: Union[Unset, bool] = UNSET
    features: Union[Unset, List[int]] = UNSET
    fultext: Union[Unset, bool] = UNSET
    http_server: Union[Unset, bool] = UNSET
    index_server: Union[Unset, bool] = UNSET
    limited_ig: Union[Unset, bool] = UNSET
    limited_version: Union[Unset, bool] = UNSET
    nb_of_ig_licenses: Union[Unset, int] = UNSET
    nb_of_server_licenses: Union[Unset, int] = UNSET
    professional: Union[Unset, bool] = UNSET
    replication: Union[Unset, bool] = UNSET
    sap_a_link: Union[Unset, bool] = UNSET
    serno: Union[Unset, str] = UNSET
    signature: Union[Unset, bool] = UNSET
    stack: Union[Unset, bool] = UNSET
    tobid: Union[Unset, bool] = UNSET
    xml_import: Union[Unset, bool] = UNSET
    nb_of_fulltext_langs: Union[Unset, int] = UNSET
    license_options: Union[Unset, "MapToString"] = UNSET
    license_file_content: Union[Unset, str] = UNSET
    license_valid: Union[Unset, bool] = UNSET
    validity_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        backup = self.backup
        cold = self.cold
        demo_version = self.demo_version
        dispatch_folder = self.dispatch_folder
        domea = self.domea
        email_only = self.email_only
        features: Union[Unset, List[int]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        fultext = self.fultext
        http_server = self.http_server
        index_server = self.index_server
        limited_ig = self.limited_ig
        limited_version = self.limited_version
        nb_of_ig_licenses = self.nb_of_ig_licenses
        nb_of_server_licenses = self.nb_of_server_licenses
        professional = self.professional
        replication = self.replication
        sap_a_link = self.sap_a_link
        serno = self.serno
        signature = self.signature
        stack = self.stack
        tobid = self.tobid
        xml_import = self.xml_import
        nb_of_fulltext_langs = self.nb_of_fulltext_langs
        license_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_options, Unset):
            license_options = self.license_options.to_dict()

        license_file_content = self.license_file_content
        license_valid = self.license_valid
        validity_date: Union[Unset, str] = UNSET
        if not isinstance(self.validity_date, Unset):
            validity_date = self.validity_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backup is not UNSET:
            field_dict["backup"] = backup
        if cold is not UNSET:
            field_dict["cold"] = cold
        if demo_version is not UNSET:
            field_dict["demoVersion"] = demo_version
        if dispatch_folder is not UNSET:
            field_dict["dispatchFolder"] = dispatch_folder
        if domea is not UNSET:
            field_dict["domea"] = domea
        if email_only is not UNSET:
            field_dict["emailOnly"] = email_only
        if features is not UNSET:
            field_dict["features"] = features
        if fultext is not UNSET:
            field_dict["fultext"] = fultext
        if http_server is not UNSET:
            field_dict["httpServer"] = http_server
        if index_server is not UNSET:
            field_dict["indexServer"] = index_server
        if limited_ig is not UNSET:
            field_dict["limitedIg"] = limited_ig
        if limited_version is not UNSET:
            field_dict["limitedVersion"] = limited_version
        if nb_of_ig_licenses is not UNSET:
            field_dict["nbOfIgLicenses"] = nb_of_ig_licenses
        if nb_of_server_licenses is not UNSET:
            field_dict["nbOfServerLicenses"] = nb_of_server_licenses
        if professional is not UNSET:
            field_dict["professional"] = professional
        if replication is not UNSET:
            field_dict["replication"] = replication
        if sap_a_link is not UNSET:
            field_dict["sapALink"] = sap_a_link
        if serno is not UNSET:
            field_dict["serno"] = serno
        if signature is not UNSET:
            field_dict["signature"] = signature
        if stack is not UNSET:
            field_dict["stack"] = stack
        if tobid is not UNSET:
            field_dict["tobid"] = tobid
        if xml_import is not UNSET:
            field_dict["xmlImport"] = xml_import
        if nb_of_fulltext_langs is not UNSET:
            field_dict["nbOfFulltextLangs"] = nb_of_fulltext_langs
        if license_options is not UNSET:
            field_dict["licenseOptions"] = license_options
        if license_file_content is not UNSET:
            field_dict["licenseFileContent"] = license_file_content
        if license_valid is not UNSET:
            field_dict["licenseValid"] = license_valid
        if validity_date is not UNSET:
            field_dict["validityDate"] = validity_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        backup = d.pop("backup", UNSET)

        cold = d.pop("cold", UNSET)

        demo_version = d.pop("demoVersion", UNSET)

        dispatch_folder = d.pop("dispatchFolder", UNSET)

        domea = d.pop("domea", UNSET)

        email_only = d.pop("emailOnly", UNSET)

        features = cast(List[int], d.pop("features", UNSET))

        fultext = d.pop("fultext", UNSET)

        http_server = d.pop("httpServer", UNSET)

        index_server = d.pop("indexServer", UNSET)

        limited_ig = d.pop("limitedIg", UNSET)

        limited_version = d.pop("limitedVersion", UNSET)

        nb_of_ig_licenses = d.pop("nbOfIgLicenses", UNSET)

        nb_of_server_licenses = d.pop("nbOfServerLicenses", UNSET)

        professional = d.pop("professional", UNSET)

        replication = d.pop("replication", UNSET)

        sap_a_link = d.pop("sapALink", UNSET)

        serno = d.pop("serno", UNSET)

        signature = d.pop("signature", UNSET)

        stack = d.pop("stack", UNSET)

        tobid = d.pop("tobid", UNSET)

        xml_import = d.pop("xmlImport", UNSET)

        nb_of_fulltext_langs = d.pop("nbOfFulltextLangs", UNSET)

        _license_options = d.pop("licenseOptions", UNSET)
        license_options: Union[Unset, MapToString]
        if isinstance(_license_options, Unset):
            license_options = UNSET
        else:
            license_options = MapToString.from_dict(_license_options)

        license_file_content = d.pop("licenseFileContent", UNSET)

        license_valid = d.pop("licenseValid", UNSET)

        _validity_date = d.pop("validityDate", UNSET)
        validity_date: Union[Unset, datetime.datetime]
        if isinstance(_validity_date, Unset):
            validity_date = UNSET
        else:
            validity_date = isoparse(_validity_date)

        license_ = cls(
            backup=backup,
            cold=cold,
            demo_version=demo_version,
            dispatch_folder=dispatch_folder,
            domea=domea,
            email_only=email_only,
            features=features,
            fultext=fultext,
            http_server=http_server,
            index_server=index_server,
            limited_ig=limited_ig,
            limited_version=limited_version,
            nb_of_ig_licenses=nb_of_ig_licenses,
            nb_of_server_licenses=nb_of_server_licenses,
            professional=professional,
            replication=replication,
            sap_a_link=sap_a_link,
            serno=serno,
            signature=signature,
            stack=stack,
            tobid=tobid,
            xml_import=xml_import,
            nb_of_fulltext_langs=nb_of_fulltext_langs,
            license_options=license_options,
            license_file_content=license_file_content,
            license_valid=license_valid,
            validity_date=validity_date,
        )

        license_.additional_properties = d
        return license_

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
