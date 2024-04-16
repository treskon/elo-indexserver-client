import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

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
            server_stream_version (Union[Unset, str]): API stream version.
                EIX-2519
            license_ (Union[Unset, License]): <p>
                This class contains license information.
                 </p>
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            index_servers (Union[Unset, List['IndexServerForArchive']]):
            repl_process_on_server_id (Union[Unset, str]): This value defines the server ID which is checked when a workflow
                is forwared.
            instance_name (Union[Unset, str]): Indexserver name. This is the name configured in config.xml or web.xml as
                "ixid".
            server_time (Union[Unset, datetime.datetime]): Server time.
                EIX-2519
            postbox_disabled (Union[Unset, bool]): Serverside inbox is disabled.
                The serverside inbox is disabled in cloud installations.
            version (Union[Unset, str]): The version of the Index Server. Read only.
            database_engine (Union[Unset, str]): Database engine name. E. g.
                MSSQL, ORACLE, DB2 If connected to DB2, the character set UTF-8 is
                 assumed for database columns that store Strings. In this case the length members of the
                 constant classes (e.g. SordC.lnName resp. CONST.SORD.lnName) contain the column widths in bytes
                 rather than characters. Use the IXConnection.truncate function to truncate a String value to
                 fit the corresponding database column.
    """

    server_stream_version: Union[Unset, str] = UNSET
    license_: Union[Unset, "License"] = UNSET
    index_servers: Union[Unset, List["IndexServerForArchive"]] = UNSET
    repl_process_on_server_id: Union[Unset, str] = UNSET
    instance_name: Union[Unset, str] = UNSET
    server_time: Union[Unset, datetime.datetime] = UNSET
    postbox_disabled: Union[Unset, bool] = UNSET
    version: Union[Unset, str] = UNSET
    database_engine: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        server_stream_version = self.server_stream_version

        license_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        index_servers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.index_servers, Unset):
            index_servers = []
            for index_servers_item_data in self.index_servers:
                index_servers_item = index_servers_item_data.to_dict()
                index_servers.append(index_servers_item)

        repl_process_on_server_id = self.repl_process_on_server_id

        instance_name = self.instance_name

        server_time: Union[Unset, str] = UNSET
        if not isinstance(self.server_time, Unset):
            server_time = self.server_time.isoformat()

        postbox_disabled = self.postbox_disabled

        version = self.version

        database_engine = self.database_engine

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_stream_version is not UNSET:
            field_dict["serverStreamVersion"] = server_stream_version
        if license_ is not UNSET:
            field_dict["license"] = license_
        if index_servers is not UNSET:
            field_dict["indexServers"] = index_servers
        if repl_process_on_server_id is not UNSET:
            field_dict["replProcessOnServerId"] = repl_process_on_server_id
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if server_time is not UNSET:
            field_dict["serverTime"] = server_time
        if postbox_disabled is not UNSET:
            field_dict["postboxDisabled"] = postbox_disabled
        if version is not UNSET:
            field_dict["version"] = version
        if database_engine is not UNSET:
            field_dict["databaseEngine"] = database_engine

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.index_server_for_archive import IndexServerForArchive
        from ..models.license_ import License

        d = src_dict.copy()
        server_stream_version = d.pop("serverStreamVersion", UNSET)

        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, License]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = License.from_dict(_license_)

        index_servers = []
        _index_servers = d.pop("indexServers", UNSET)
        for index_servers_item_data in _index_servers or []:
            index_servers_item = IndexServerForArchive.from_dict(index_servers_item_data)

            index_servers.append(index_servers_item)

        repl_process_on_server_id = d.pop("replProcessOnServerId", UNSET)

        instance_name = d.pop("instanceName", UNSET)

        _server_time = d.pop("serverTime", UNSET)
        server_time: Union[Unset, datetime.datetime]
        if isinstance(_server_time, Unset):
            server_time = UNSET
        else:
            server_time = isoparse(_server_time)

        postbox_disabled = d.pop("postboxDisabled", UNSET)

        version = d.pop("version", UNSET)

        database_engine = d.pop("databaseEngine", UNSET)

        server_info = cls(
            server_stream_version=server_stream_version,
            license_=license_,
            index_servers=index_servers,
            repl_process_on_server_id=repl_process_on_server_id,
            instance_name=instance_name,
            server_time=server_time,
            postbox_disabled=postbox_disabled,
            version=version,
            database_engine=database_engine,
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
