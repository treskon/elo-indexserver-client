from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.copy_options import CopyOptions
    from ..models.copy_result import CopyResult


T = TypeVar("T", bound="ProcessCopyElements")


@_attrs_define
class ProcessCopyElements:
    """Copy archive elements in other position in the archive.
    <p>
     Copyright: Copyright (c) 2009
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            create_mapping (Union[Unset, bool]): If createMapping is true, at the copyResult, the maps source-id to copy-id
                will be filled.
                Defaults to false.
            copy_result (Union[Unset, CopyResult]): Results of a {@link ProcessCopyElements}-Operation.
            copy_options (Union[Unset, CopyOptions]): Structure for the options for the copy-process.
                <p>
                 Copyright: Copyright (c) 2009
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    create_mapping: Union[Unset, bool] = UNSET
    copy_result: Union[Unset, "CopyResult"] = UNSET
    copy_options: Union[Unset, "CopyOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        create_mapping = self.create_mapping

        copy_result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_result, Unset):
            copy_result = self.copy_result.to_dict()

        copy_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_options, Unset):
            copy_options = self.copy_options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_mapping is not UNSET:
            field_dict["createMapping"] = create_mapping
        if copy_result is not UNSET:
            field_dict["copyResult"] = copy_result
        if copy_options is not UNSET:
            field_dict["copyOptions"] = copy_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.copy_options import CopyOptions
        from ..models.copy_result import CopyResult

        d = src_dict.copy()
        create_mapping = d.pop("createMapping", UNSET)

        _copy_result = d.pop("copyResult", UNSET)
        copy_result: Union[Unset, CopyResult]
        if isinstance(_copy_result, Unset):
            copy_result = UNSET
        else:
            copy_result = CopyResult.from_dict(_copy_result)

        _copy_options = d.pop("copyOptions", UNSET)
        copy_options: Union[Unset, CopyOptions]
        if isinstance(_copy_options, Unset):
            copy_options = UNSET
        else:
            copy_options = CopyOptions.from_dict(_copy_options)

        process_copy_elements = cls(
            create_mapping=create_mapping,
            copy_result=copy_result,
            copy_options=copy_options,
        )

        process_copy_elements.additional_properties = d
        return process_copy_elements

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
