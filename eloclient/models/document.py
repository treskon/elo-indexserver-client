from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_version import DocVersion


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """Document object with identifier and version arrays for the document and attachments.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            docs (Union[Unset, List['DocVersion']]):
            obj_id (Union[Unset, str]): Object ID for the document.
            atts (Union[Unset, List['DocVersion']]):
    """

    docs: Union[Unset, List["DocVersion"]] = UNSET
    obj_id: Union[Unset, str] = UNSET
    atts: Union[Unset, List["DocVersion"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        docs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.docs, Unset):
            docs = []
            for docs_item_data in self.docs:
                docs_item = docs_item_data.to_dict()
                docs.append(docs_item)

        obj_id = self.obj_id

        atts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.atts, Unset):
            atts = []
            for atts_item_data in self.atts:
                atts_item = atts_item_data.to_dict()
                atts.append(atts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if docs is not UNSET:
            field_dict["docs"] = docs
        if obj_id is not UNSET:
            field_dict["objId"] = obj_id
        if atts is not UNSET:
            field_dict["atts"] = atts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_version import DocVersion

        d = src_dict.copy()
        docs = []
        _docs = d.pop("docs", UNSET)
        for docs_item_data in _docs or []:
            docs_item = DocVersion.from_dict(docs_item_data)

            docs.append(docs_item)

        obj_id = d.pop("objId", UNSET)

        atts = []
        _atts = d.pop("atts", UNSET)
        for atts_item_data in _atts or []:
            atts_item = DocVersion.from_dict(atts_item_data)

            atts.append(atts_item)

        document = cls(
            docs=docs,
            obj_id=obj_id,
            atts=atts,
        )

        document.additional_properties = d
        return document

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
