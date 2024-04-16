from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_to_array_ofbyte import MapToArrayOfbyte
    from ..models.map_to_b_stream_reference import MapToBStreamReference
    from ..models.map_to_b_value_class import MapToBValueClass
    from ..models.map_to_string import MapToString
    from ..models.plugin_message_source import PluginMessageSource


T = TypeVar("T", bound="PluginMessage")


@_attrs_define
class PluginMessage:
    """A message that can be sent to or received from a plugin.

    Attributes:
        bytes_ (Union[Unset, MapToArrayOfbyte]):
        objects (Union[Unset, MapToBValueClass]):
        streams (Union[Unset, MapToBStreamReference]):
        source (Union[Unset, PluginMessageSource]): Source of plugin message.
        id (Union[Unset, str]): Message ID.
        uri (Union[Unset, str]): Message URI.
        parameters (Union[Unset, MapToString]):
        status (Union[Unset, int]): Message response status code.
            In case of a HTTP request, this element specifies the response
             status code. A value of 0 is implicitly mapped to 200.
    """

    bytes_: Union[Unset, "MapToArrayOfbyte"] = UNSET
    objects: Union[Unset, "MapToBValueClass"] = UNSET
    streams: Union[Unset, "MapToBStreamReference"] = UNSET
    source: Union[Unset, "PluginMessageSource"] = UNSET
    id: Union[Unset, str] = UNSET
    uri: Union[Unset, str] = UNSET
    parameters: Union[Unset, "MapToString"] = UNSET
    status: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bytes_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bytes_, Unset):
            bytes_ = self.bytes_.to_dict()

        objects: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.objects, Unset):
            objects = self.objects.to_dict()

        streams: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.streams, Unset):
            streams = self.streams.to_dict()

        source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        id = self.id

        uri = self.uri

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_
        if objects is not UNSET:
            field_dict["objects"] = objects
        if streams is not UNSET:
            field_dict["streams"] = streams
        if source is not UNSET:
            field_dict["source"] = source
        if id is not UNSET:
            field_dict["id"] = id
        if uri is not UNSET:
            field_dict["uri"] = uri
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.map_to_array_ofbyte import MapToArrayOfbyte
        from ..models.map_to_b_stream_reference import MapToBStreamReference
        from ..models.map_to_b_value_class import MapToBValueClass
        from ..models.map_to_string import MapToString
        from ..models.plugin_message_source import PluginMessageSource

        d = src_dict.copy()
        _bytes_ = d.pop("bytes", UNSET)
        bytes_: Union[Unset, MapToArrayOfbyte]
        if isinstance(_bytes_, Unset):
            bytes_ = UNSET
        else:
            bytes_ = MapToArrayOfbyte.from_dict(_bytes_)

        _objects = d.pop("objects", UNSET)
        objects: Union[Unset, MapToBValueClass]
        if isinstance(_objects, Unset):
            objects = UNSET
        else:
            objects = MapToBValueClass.from_dict(_objects)

        _streams = d.pop("streams", UNSET)
        streams: Union[Unset, MapToBStreamReference]
        if isinstance(_streams, Unset):
            streams = UNSET
        else:
            streams = MapToBStreamReference.from_dict(_streams)

        _source = d.pop("source", UNSET)
        source: Union[Unset, PluginMessageSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = PluginMessageSource.from_dict(_source)

        id = d.pop("id", UNSET)

        uri = d.pop("uri", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, MapToString]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = MapToString.from_dict(_parameters)

        status = d.pop("status", UNSET)

        plugin_message = cls(
            bytes_=bytes_,
            objects=objects,
            streams=streams,
            source=source,
            id=id,
            uri=uri,
            parameters=parameters,
            status=status,
        )

        plugin_message.additional_properties = d
        return plugin_message

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
