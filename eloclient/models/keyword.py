from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Keyword")


@_attrs_define
class Keyword:
    """
    Attributes:
        add (Union[Unset, bool]): <p>
            Prefix the text of a child keyword with the text of this keyword. This member is interpreted in
             <code>cookKeywords</code>. The following relationship exists between the members
             <code>enabled, add, raw</code>
             </p>
             <table border="2">
             <tr>
             <td>condition</td>
             <td>conclusion</td>
             </tr>
             <tr>
             <td><code>add=true</code></td>
             <td><code>enabled=false, raw=true</code></td>
             </tr>
             <tr>
             <td><code>enabled=true</code></td>
             <td><code>add=false, raw=any</code></td>
             </tr>
             </table>
        display_value (Union[Unset, str]): Only used in keywords for aspect lines with type = {@link
            AspectLineC#TYPE_STATUS}.
            This field
             contains the translated text of the status value (field {@link text}) into user's language.
        children (Union[Unset, List['Keyword']]):
        text_translation_key (Union[Unset, str]): Translation key for text.
        raw (Union[Unset, bool]): The function <code>cookKeyword()</code> must be called for this keyword in order to
            use it for
            an index property. This is because it contains placeholders that must be substituted or one of
             the parent keywords should be added.
        id (Union[Unset, str]): Keyword ID. Consists of: groupid + orderid, orderid begins with a ".".
        text (Union[Unset, str]): Keyword text. This term is assigned to an index property.
            The member <code>raw</code> should be
             checked before this term is used. This text can be translated into reps. from the users
             language: set <code>SessionOptionsC.TRANSLATE_TERM</code>.
        enabled (Union[Unset, bool]): If true, this keyword can be used as a value for an index property.
            Otherwise its only purpose
             is to structure the keyword hierachy.
    """

    add: Union[Unset, bool] = UNSET
    display_value: Union[Unset, str] = UNSET
    children: Union[Unset, List["Keyword"]] = UNSET
    text_translation_key: Union[Unset, str] = UNSET
    raw: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add = self.add

        display_value = self.display_value

        children: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)

        text_translation_key = self.text_translation_key

        raw = self.raw

        id = self.id

        text = self.text

        enabled = self.enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add is not UNSET:
            field_dict["add"] = add
        if display_value is not UNSET:
            field_dict["displayValue"] = display_value
        if children is not UNSET:
            field_dict["children"] = children
        if text_translation_key is not UNSET:
            field_dict["textTranslationKey"] = text_translation_key
        if raw is not UNSET:
            field_dict["raw"] = raw
        if id is not UNSET:
            field_dict["id"] = id
        if text is not UNSET:
            field_dict["text"] = text
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        add = d.pop("add", UNSET)

        display_value = d.pop("displayValue", UNSET)

        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in _children or []:
            children_item = Keyword.from_dict(children_item_data)

            children.append(children_item)

        text_translation_key = d.pop("textTranslationKey", UNSET)

        raw = d.pop("raw", UNSET)

        id = d.pop("id", UNSET)

        text = d.pop("text", UNSET)

        enabled = d.pop("enabled", UNSET)

        keyword = cls(
            add=add,
            display_value=display_value,
            children=children,
            text_translation_key=text_translation_key,
            raw=raw,
            id=id,
            text=text,
            enabled=enabled,
        )

        keyword.additional_properties = d
        return keyword

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
