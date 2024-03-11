from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.index_server_for_archive import IndexServerForArchive
    from ..models.license_ import License


T = TypeVar("T", bound="ServerInfo")


@_attrs_define
class ServerInfo:
    """<p>
    License key, version and list of other Indexservers
     </p>
     <p>
     Copyright: Copyright (c) 2003
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            index_servers (Union[Unset, List['IndexServerForArchive']]):
            license_ (Union[Unset, License]): <p>
                This class contains license information.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            version (Union[Unset, str]): The version of the Index Server. Read only.
            repl_process_on_server_id (Union[Unset, str]): This value defines the server ID which is checked when a workflow
                is forwared.
            database_engine (Union[Unset, str]): Database engine name. E. g.
                MSSQL, ORACLE, DB2 If connected to DB2, the character set UTF-8 is assumed for database
                 columns that store Strings. In this case the length members of the constant classes (e.g. SordC.lnName resp.
                 CONST.SORD.lnName) contain the column widths in bytes rather than characters. Use the IXConnection.truncate
                 function to truncate a String value to fit the corresponding database column.
            instance_name (Union[Unset, str]): Indexserver name. This is the name configured in config.xml or web.xml as
                "ixid".
    """

    index_servers: Union[Unset, List["IndexServerForArchive"]] = UNSET
    license_: Union[Unset, "License"] = UNSET
    version: Union[Unset, str] = UNSET
    repl_process_on_server_id: Union[Unset, str] = UNSET
    database_engine: Union[Unset, str] = UNSET
    instance_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index_servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.index_servers, Unset):
            index_servers = []
            for index_servers_item_data in self.index_servers:
                index_servers_item = index_servers_item_data.to_dict()

                index_servers.append(index_servers_item)

        license_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        version = self.version
        repl_process_on_server_id = self.repl_process_on_server_id
        database_engine = self.database_engine
        instance_name = self.instance_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index_servers is not UNSET:
            field_dict["indexServers"] = index_servers
        if license_ is not UNSET:
            field_dict["license"] = license_
        if version is not UNSET:
            field_dict["version"] = version
        if repl_process_on_server_id is not UNSET:
            field_dict["replProcessOnServerId"] = repl_process_on_server_id
        if database_engine is not UNSET:
            field_dict["databaseEngine"] = database_engine
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.index_server_for_archive import IndexServerForArchive
        from ..models.license_ import License

        d = src_dict.copy()
        index_servers = []
        _index_servers = d.pop("indexServers", UNSET)
        for index_servers_item_data in _index_servers or []:
            index_servers_item = IndexServerForArchive.from_dict(index_servers_item_data)

            index_servers.append(index_servers_item)

        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, License]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = License.from_dict(_license_)

        version = d.pop("version", UNSET)

        repl_process_on_server_id = d.pop("replProcessOnServerId", UNSET)

        database_engine = d.pop("databaseEngine", UNSET)

        instance_name = d.pop("instanceName", UNSET)

        server_info = cls(
            index_servers=index_servers,
            license_=license_,
            version=version,
            repl_process_on_server_id=repl_process_on_server_id,
            database_engine=database_engine,
            instance_name=instance_name,
        )

        server_info.additional_properties = d
        return server_info

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
