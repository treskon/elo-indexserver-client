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
            nb_of_ig_licenses (Union[Unset, int]): Number of ELO Internet Gateway users.
            backup (Union[Unset, bool]): Backup enabled.
            stack (Union[Unset, bool]): STACK
            sap_a_link (Union[Unset, bool]): SAPALINK interface
            license_options (Union[Unset, MapToString]):
            signature (Union[Unset, bool]): SIGNATURE
            xml_import (Union[Unset, bool]): XML-Import
            email_only (Union[Unset, bool]): EMail
            nb_of_fulltext_langs (Union[Unset, int]): Number of languages for which linguistic processing can be used during
                fulltext indexing.
            cold (Union[Unset, bool]): COLD
            professional (Union[Unset, bool]): True for ELOprofessional
            features (Union[Unset, List[int]]):
            limited_ig (Union[Unset, bool]): Limited Internet Gateway
            fultext (Union[Unset, bool]): Fulltext enabled.
            replication (Union[Unset, bool]): Replication enabled.
            license_file_content (Union[Unset, str]): License file content.
            serno (Union[Unset, str]): License key.
            http_server (Union[Unset, bool]): HTTP DocServer
            domea (Union[Unset, bool]): DOMEA
            license_valid (Union[Unset, bool]): True, if license is valid.
            public_license_key (Union[Unset, str]): Public part of key pair supplied for license download.
            nb_of_server_licenses (Union[Unset, int]): Number of server licenses.
            tobid (Union[Unset, bool]): Tobit
            index_server (Union[Unset, bool]): Indexserver
            validity_date (Union[Unset, datetime.datetime]): License is valid until this date. This valid is null if the
                license does not expire.
            demo_version (Union[Unset, bool]): Demo version.
            limited_version (Union[Unset, bool]): Limited version.
            dispatch_folder (Union[Unset, bool]): Dispatch folder (Versendemappe)
    """

    nb_of_ig_licenses: Union[Unset, int] = UNSET
    backup: Union[Unset, bool] = UNSET
    stack: Union[Unset, bool] = UNSET
    sap_a_link: Union[Unset, bool] = UNSET
    license_options: Union[Unset, "MapToString"] = UNSET
    signature: Union[Unset, bool] = UNSET
    xml_import: Union[Unset, bool] = UNSET
    email_only: Union[Unset, bool] = UNSET
    nb_of_fulltext_langs: Union[Unset, int] = UNSET
    cold: Union[Unset, bool] = UNSET
    professional: Union[Unset, bool] = UNSET
    features: Union[Unset, List[int]] = UNSET
    limited_ig: Union[Unset, bool] = UNSET
    fultext: Union[Unset, bool] = UNSET
    replication: Union[Unset, bool] = UNSET
    license_file_content: Union[Unset, str] = UNSET
    serno: Union[Unset, str] = UNSET
    http_server: Union[Unset, bool] = UNSET
    domea: Union[Unset, bool] = UNSET
    license_valid: Union[Unset, bool] = UNSET
    public_license_key: Union[Unset, str] = UNSET
    nb_of_server_licenses: Union[Unset, int] = UNSET
    tobid: Union[Unset, bool] = UNSET
    index_server: Union[Unset, bool] = UNSET
    validity_date: Union[Unset, datetime.datetime] = UNSET
    demo_version: Union[Unset, bool] = UNSET
    limited_version: Union[Unset, bool] = UNSET
    dispatch_folder: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nb_of_ig_licenses = self.nb_of_ig_licenses

        backup = self.backup

        stack = self.stack

        sap_a_link = self.sap_a_link

        license_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_options, Unset):
            license_options = self.license_options.to_dict()

        signature = self.signature

        xml_import = self.xml_import

        email_only = self.email_only

        nb_of_fulltext_langs = self.nb_of_fulltext_langs

        cold = self.cold

        professional = self.professional

        features: Union[Unset, List[int]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        limited_ig = self.limited_ig

        fultext = self.fultext

        replication = self.replication

        license_file_content = self.license_file_content

        serno = self.serno

        http_server = self.http_server

        domea = self.domea

        license_valid = self.license_valid

        public_license_key = self.public_license_key

        nb_of_server_licenses = self.nb_of_server_licenses

        tobid = self.tobid

        index_server = self.index_server

        validity_date: Union[Unset, str] = UNSET
        if not isinstance(self.validity_date, Unset):
            validity_date = self.validity_date.isoformat()

        demo_version = self.demo_version

        limited_version = self.limited_version

        dispatch_folder = self.dispatch_folder

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nb_of_ig_licenses is not UNSET:
            field_dict["nbOfIgLicenses"] = nb_of_ig_licenses
        if backup is not UNSET:
            field_dict["backup"] = backup
        if stack is not UNSET:
            field_dict["stack"] = stack
        if sap_a_link is not UNSET:
            field_dict["sapALink"] = sap_a_link
        if license_options is not UNSET:
            field_dict["licenseOptions"] = license_options
        if signature is not UNSET:
            field_dict["signature"] = signature
        if xml_import is not UNSET:
            field_dict["xmlImport"] = xml_import
        if email_only is not UNSET:
            field_dict["emailOnly"] = email_only
        if nb_of_fulltext_langs is not UNSET:
            field_dict["nbOfFulltextLangs"] = nb_of_fulltext_langs
        if cold is not UNSET:
            field_dict["cold"] = cold
        if professional is not UNSET:
            field_dict["professional"] = professional
        if features is not UNSET:
            field_dict["features"] = features
        if limited_ig is not UNSET:
            field_dict["limitedIg"] = limited_ig
        if fultext is not UNSET:
            field_dict["fultext"] = fultext
        if replication is not UNSET:
            field_dict["replication"] = replication
        if license_file_content is not UNSET:
            field_dict["licenseFileContent"] = license_file_content
        if serno is not UNSET:
            field_dict["serno"] = serno
        if http_server is not UNSET:
            field_dict["httpServer"] = http_server
        if domea is not UNSET:
            field_dict["domea"] = domea
        if license_valid is not UNSET:
            field_dict["licenseValid"] = license_valid
        if public_license_key is not UNSET:
            field_dict["publicLicenseKey"] = public_license_key
        if nb_of_server_licenses is not UNSET:
            field_dict["nbOfServerLicenses"] = nb_of_server_licenses
        if tobid is not UNSET:
            field_dict["tobid"] = tobid
        if index_server is not UNSET:
            field_dict["indexServer"] = index_server
        if validity_date is not UNSET:
            field_dict["validityDate"] = validity_date
        if demo_version is not UNSET:
            field_dict["demoVersion"] = demo_version
        if limited_version is not UNSET:
            field_dict["limitedVersion"] = limited_version
        if dispatch_folder is not UNSET:
            field_dict["dispatchFolder"] = dispatch_folder

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_string import MapToString

        d = src_dict.copy()
        nb_of_ig_licenses = d.pop("nbOfIgLicenses", UNSET)

        backup = d.pop("backup", UNSET)

        stack = d.pop("stack", UNSET)

        sap_a_link = d.pop("sapALink", UNSET)

        _license_options = d.pop("licenseOptions", UNSET)
        license_options: Union[Unset, MapToString]
        if isinstance(_license_options, Unset):
            license_options = UNSET
        else:
            license_options = MapToString.from_dict(_license_options)

        signature = d.pop("signature", UNSET)

        xml_import = d.pop("xmlImport", UNSET)

        email_only = d.pop("emailOnly", UNSET)

        nb_of_fulltext_langs = d.pop("nbOfFulltextLangs", UNSET)

        cold = d.pop("cold", UNSET)

        professional = d.pop("professional", UNSET)

        features = cast(List[int], d.pop("features", UNSET))

        limited_ig = d.pop("limitedIg", UNSET)

        fultext = d.pop("fultext", UNSET)

        replication = d.pop("replication", UNSET)

        license_file_content = d.pop("licenseFileContent", UNSET)

        serno = d.pop("serno", UNSET)

        http_server = d.pop("httpServer", UNSET)

        domea = d.pop("domea", UNSET)

        license_valid = d.pop("licenseValid", UNSET)

        public_license_key = d.pop("publicLicenseKey", UNSET)

        nb_of_server_licenses = d.pop("nbOfServerLicenses", UNSET)

        tobid = d.pop("tobid", UNSET)

        index_server = d.pop("indexServer", UNSET)

        _validity_date = d.pop("validityDate", UNSET)
        validity_date: Union[Unset, datetime.datetime]
        if isinstance(_validity_date, Unset):
            validity_date = UNSET
        else:
            validity_date = isoparse(_validity_date)

        demo_version = d.pop("demoVersion", UNSET)

        limited_version = d.pop("limitedVersion", UNSET)

        dispatch_folder = d.pop("dispatchFolder", UNSET)

        license_ = cls(
            nb_of_ig_licenses=nb_of_ig_licenses,
            backup=backup,
            stack=stack,
            sap_a_link=sap_a_link,
            license_options=license_options,
            signature=signature,
            xml_import=xml_import,
            email_only=email_only,
            nb_of_fulltext_langs=nb_of_fulltext_langs,
            cold=cold,
            professional=professional,
            features=features,
            limited_ig=limited_ig,
            fultext=fultext,
            replication=replication,
            license_file_content=license_file_content,
            serno=serno,
            http_server=http_server,
            domea=domea,
            license_valid=license_valid,
            public_license_key=public_license_key,
            nb_of_server_licenses=nb_of_server_licenses,
            tobid=tobid,
            index_server=index_server,
            validity_date=validity_date,
            demo_version=demo_version,
            limited_version=limited_version,
            dispatch_folder=dispatch_folder,
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
