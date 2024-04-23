from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.es_instance_settings import ESInstanceSettings


T = TypeVar("T", bound="ESSettingsObj")


@_attrs_define
class ESSettingsObj:
    """<p>
    <b>checkoutEsSettings</b> returns the current IX instance name, a list of all available IX
     instances as well as one EsInstanceSettings object for every IX instance of the archive and one
     for the setting "_ALL". If there is no entry for a setting in the database, the default value is
     returned as value.
     </p>

     <p>
     <b>checkinEsSettings</b> writes entries for every EsInstanceSettings to the database:
     </p>
     <ul>
     <li>If a EsSettingsProperty member is null, nothing is written or deleted.
     <li>To delete a setting, the EsSettingsProperty member must be set, but its member 'value' must
     be set to 'null'
     </ul>

        Attributes:
            instance_name (Union[Unset, str]): Name of this IX instance
            all_instance_names (Union[Unset, List[str]]):
            instance_settings (Union[Unset, List['ESInstanceSettings']]):
    """

    instance_name: Union[Unset, str] = UNSET
    all_instance_names: Union[Unset, List[str]] = UNSET
    instance_settings: Union[Unset, List["ESInstanceSettings"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instance_name = self.instance_name

        all_instance_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.all_instance_names, Unset):
            all_instance_names = self.all_instance_names

        instance_settings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.instance_settings, Unset):
            instance_settings = []
            for componentsschemas_array_list_of_es_instance_settings_item_data in self.instance_settings:
                componentsschemas_array_list_of_es_instance_settings_item = (
                    componentsschemas_array_list_of_es_instance_settings_item_data.to_dict()
                )
                instance_settings.append(componentsschemas_array_list_of_es_instance_settings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if instance_name is not UNSET:
            field_dict["instanceName"] = instance_name
        if all_instance_names is not UNSET:
            field_dict["allInstanceNames"] = all_instance_names
        if instance_settings is not UNSET:
            field_dict["instanceSettings"] = instance_settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.es_instance_settings import ESInstanceSettings

        d = src_dict.copy()
        instance_name = d.pop("instanceName", UNSET)

        all_instance_names = cast(List[str], d.pop("allInstanceNames", UNSET))

        instance_settings = []
        _instance_settings = d.pop("instanceSettings", UNSET)
        for componentsschemas_array_list_of_es_instance_settings_item_data in _instance_settings or []:
            componentsschemas_array_list_of_es_instance_settings_item = ESInstanceSettings.from_dict(
                componentsschemas_array_list_of_es_instance_settings_item_data
            )

            instance_settings.append(componentsschemas_array_list_of_es_instance_settings_item)

        es_settings_obj = cls(
            instance_name=instance_name,
            all_instance_names=all_instance_names,
            instance_settings=instance_settings,
        )

        es_settings_obj.additional_properties = d
        return es_settings_obj

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
