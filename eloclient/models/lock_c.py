from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lock_z import LockZ


T = TypeVar("T", bound="LockC")


@_attrs_define
class LockC:
    """<p>
    Constants to lock data against concurrent modification.
     </p>

        Attributes:
            bset_no (Union[Unset, str]):
            bset_yes (Union[Unset, str]):
            bset_force (Union[Unset, str]):
            bset_if_free (Union[Unset, str]):
            bset_sord (Union[Unset, str]):
            bset_doc (Union[Unset, str]):
            no (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            yes (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            force (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            if_free (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            sord (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            doc (Union[Unset, LockZ]): This class encapsulates the constants of the LockC class.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
    """

    bset_no: Union[Unset, str] = UNSET
    bset_yes: Union[Unset, str] = UNSET
    bset_force: Union[Unset, str] = UNSET
    bset_if_free: Union[Unset, str] = UNSET
    bset_sord: Union[Unset, str] = UNSET
    bset_doc: Union[Unset, str] = UNSET
    no: Union[Unset, "LockZ"] = UNSET
    yes: Union[Unset, "LockZ"] = UNSET
    force: Union[Unset, "LockZ"] = UNSET
    if_free: Union[Unset, "LockZ"] = UNSET
    sord: Union[Unset, "LockZ"] = UNSET
    doc: Union[Unset, "LockZ"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bset_no = self.bset_no
        bset_yes = self.bset_yes
        bset_force = self.bset_force
        bset_if_free = self.bset_if_free
        bset_sord = self.bset_sord
        bset_doc = self.bset_doc
        no: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.no, Unset):
            no = self.no.to_dict()

        yes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.yes, Unset):
            yes = self.yes.to_dict()

        force: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.force, Unset):
            force = self.force.to_dict()

        if_free: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.if_free, Unset):
            if_free = self.if_free.to_dict()

        sord: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sord, Unset):
            sord = self.sord.to_dict()

        doc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.doc, Unset):
            doc = self.doc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bset_no is not UNSET:
            field_dict["bsetNO"] = bset_no
        if bset_yes is not UNSET:
            field_dict["bsetYES"] = bset_yes
        if bset_force is not UNSET:
            field_dict["bsetFORCE"] = bset_force
        if bset_if_free is not UNSET:
            field_dict["bsetIF_FREE"] = bset_if_free
        if bset_sord is not UNSET:
            field_dict["bsetSORD"] = bset_sord
        if bset_doc is not UNSET:
            field_dict["bsetDOC"] = bset_doc
        if no is not UNSET:
            field_dict["NO"] = no
        if yes is not UNSET:
            field_dict["YES"] = yes
        if force is not UNSET:
            field_dict["FORCE"] = force
        if if_free is not UNSET:
            field_dict["IF_FREE"] = if_free
        if sord is not UNSET:
            field_dict["SORD"] = sord
        if doc is not UNSET:
            field_dict["DOC"] = doc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lock_z import LockZ

        d = src_dict.copy()
        bset_no = d.pop("bsetNO", UNSET)

        bset_yes = d.pop("bsetYES", UNSET)

        bset_force = d.pop("bsetFORCE", UNSET)

        bset_if_free = d.pop("bsetIF_FREE", UNSET)

        bset_sord = d.pop("bsetSORD", UNSET)

        bset_doc = d.pop("bsetDOC", UNSET)

        _no = d.pop("NO", UNSET)
        no: Union[Unset, LockZ]
        if isinstance(_no, Unset):
            no = UNSET
        else:
            no = LockZ.from_dict(_no)

        _yes = d.pop("YES", UNSET)
        yes: Union[Unset, LockZ]
        if isinstance(_yes, Unset):
            yes = UNSET
        else:
            yes = LockZ.from_dict(_yes)

        _force = d.pop("FORCE", UNSET)
        force: Union[Unset, LockZ]
        if isinstance(_force, Unset):
            force = UNSET
        else:
            force = LockZ.from_dict(_force)

        _if_free = d.pop("IF_FREE", UNSET)
        if_free: Union[Unset, LockZ]
        if isinstance(_if_free, Unset):
            if_free = UNSET
        else:
            if_free = LockZ.from_dict(_if_free)

        _sord = d.pop("SORD", UNSET)
        sord: Union[Unset, LockZ]
        if isinstance(_sord, Unset):
            sord = UNSET
        else:
            sord = LockZ.from_dict(_sord)

        _doc = d.pop("DOC", UNSET)
        doc: Union[Unset, LockZ]
        if isinstance(_doc, Unset):
            doc = UNSET
        else:
            doc = LockZ.from_dict(_doc)

        lock_c = cls(
            bset_no=bset_no,
            bset_yes=bset_yes,
            bset_force=bset_force,
            bset_if_free=bset_if_free,
            bset_sord=bset_sord,
            bset_doc=bset_doc,
            no=no,
            yes=yes,
            force=force,
            if_free=if_free,
            sord=sord,
            doc=doc,
        )

        lock_c.additional_properties = d
        return lock_c

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
