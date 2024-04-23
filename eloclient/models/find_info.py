from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.find_by_acl import FindByAcl
    from ..models.find_by_e_search import FindByESearch
    from ..models.find_by_fulltext import FindByFulltext
    from ..models.find_by_fulltext_ctrl import FindByFulltextCtrl
    from ..models.find_by_index import FindByIndex
    from ..models.find_by_notes import FindByNotes
    from ..models.find_by_preview_ctrl import FindByPreviewCtrl
    from ..models.find_by_registered_function import FindByRegisteredFunction
    from ..models.find_by_sord_hist import FindBySordHist
    from ..models.find_by_type import FindByType
    from ..models.find_by_version import FindByVersion
    from ..models.find_children import FindChildren
    from ..models.find_direct import FindDirect
    from ..models.find_for_keywording_relation import FindForKeywordingRelation
    from ..models.find_links import FindLinks
    from ..models.find_options import FindOptions


T = TypeVar("T", bound="FindInfo")


@_attrs_define
class FindInfo:
    """This class controls the search function findFirstSords.
    <p>
     Copyright: Copyright (c) 2004
     </p>
     <p>
     Organisation: ELO Digital Office GmbH
     </p>

        Attributes:
            find_by_fulltext (Union[Unset, FindByFulltext]): <p>
                Performs a fulltext search.
                 </p>

                 <p>
                 The fulltext search is performed via iSearch. Therefore, use
                 {@link de.elo.ix.client.esearch.FindByESearch} instead. The {@link #term} should be replaces by
                 the actual query term and additional filters (e.g. DocMask) should be submitted by
                 {@link de.elo.ix.client.esearch.ESearchParams#queryOperator}. The areas in which should be search
                 should be set in {@link de.elo.ix.client.esearch.ESearchParams#searchIn}.<br>
                 Searches using this class are still executed but internally mapped to
                 {@link de.elo.ix.client.esearch.FindByESearch} objects and some values might be ignored.
                 </p>
            find_by_notes (Union[Unset, FindByNotes]): Finds an object according to the objects notes (sticky notes)
                content.
            find_by_registered_function (Union[Unset, FindByRegisteredFunction]):
            find_direct (Union[Unset, FindDirect]): <p>
                Search query for locating text in the archive.
                 </p>

                 <p>
                 The fulltext search is performed via iSearch. Therefore, use
                 {@link de.elo.ix.client.esearch.FindByESearch} instead. The {@link #query} should be replaces by
                 the actual query term and additional filters (e.g. DocMask) should be submitted by
                 {@link de.elo.ix.client.esearch.ESearchParams#queryOperator}. The areas in which should be search
                 should be set in {@link de.elo.ix.client.esearch.ESearchParams#searchIn}.<br>
                 Searches using this class are still executed but internally mapped to
                 {@link de.elo.ix.client.esearch.FindByESearch} objects and some values might be ignored.
                 </p>
            find_by_index (Union[Unset, FindByIndex]): Finds an object according to the object's index properties.
                The search terms are concatinated by
                 the operator specified with FindOptions.searchMode. If FindOptionsC.OPERATOR_OR is the specified
                 searchMode the members of this class are concatinated in the search string with the boolean
                 operator "OR". Any other searchMode concatinates with "AND". Exception: userId and maskId are
                 always used as "AND" terms.
                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            find_by_version (Union[Unset, FindByVersion]): This class holds additional information for FindInfo, in order to
                restrict a search using the
                document history (version).

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            find_by_sord_hist (Union[Unset, FindBySordHist]):
            find_by_acl (Union[Unset, FindByAcl]): Find objects by ACL
            find_links (Union[Unset, FindLinks]): Finds the links of an object.
            find_by_fulltext_ctrl (Union[Unset, FindByFulltextCtrl]): This class is used to search for objects that have to
                be indexed by the fulltext database engine.
                <p>
                 The selected objects are ordered by their timestamp. If the search process is interrupted because
                 of a timeout or because the FindOptions.totalCount limit is reached, all the Objects of the lates
                 timestamp second are discarded.
                 </p>
                 <p>
                 If the search process is terminated due to breakTotalCount and the array of results is empty, the
                 search should be repeated with a greater value for totalCount.
                 </p>
                 <p>
                 Access checking is performed as in all other searches.
                 </p>
                 <p>
                 A search of this type can only be combined with FindOptions.totalCount and
                 FindOptions.timeoutSeconds.
                 </p>
                 <p>
                 The results are returned in the member FindInfo.fulltextCtrlResultItems. The Sord objects are
                 available in the member FindInfo.sords too.
                 </p>
            find_by_preview_ctrl (Union[Unset, FindByPreviewCtrl]): This class can be used to find the documents for which
                preview files have to be created.
                The main
                 purpose is to control the automatic preview generation in a server process.
            find_children (Union[Unset, FindChildren]): This class controls the search for child objects of an archive
                entry.
                <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            find_by_e_search (Union[Unset, FindByESearch]): Use this class to search by iSearch with API functionality
                starting with ELO 11.
            find_by_type (Union[Unset, FindByType]): This class holds additional information for FindInfo, in order to
                restrict a search using
                document types. The default resolving sequence is ordered by the grade of restriction: <br>
                 1. typeIDs, typeNames, typeExtensions is the most specialised information, <br>
                 2. typeDocuments containing all document types (IDs, Names, Extensions), <br>
                 3. and typeStructures including all levels of structure elements. <br>
                 4. If none of the parameters above is valid, the complete restriction FindByType is omitted. <br>

                 <p>
                 Copyright: Copyright (c) 2004
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            find_options (Union[Unset, FindOptions]): This class contains several options to control the search process of
                findFirstSords.
            find_for_keywording_relation (Union[Unset, FindForKeywordingRelation]): Criteria for searching sords for
                keywording relation.
    """

    find_by_fulltext: Union[Unset, "FindByFulltext"] = UNSET
    find_by_notes: Union[Unset, "FindByNotes"] = UNSET
    find_by_registered_function: Union[Unset, "FindByRegisteredFunction"] = UNSET
    find_direct: Union[Unset, "FindDirect"] = UNSET
    find_by_index: Union[Unset, "FindByIndex"] = UNSET
    find_by_version: Union[Unset, "FindByVersion"] = UNSET
    find_by_sord_hist: Union[Unset, "FindBySordHist"] = UNSET
    find_by_acl: Union[Unset, "FindByAcl"] = UNSET
    find_links: Union[Unset, "FindLinks"] = UNSET
    find_by_fulltext_ctrl: Union[Unset, "FindByFulltextCtrl"] = UNSET
    find_by_preview_ctrl: Union[Unset, "FindByPreviewCtrl"] = UNSET
    find_children: Union[Unset, "FindChildren"] = UNSET
    find_by_e_search: Union[Unset, "FindByESearch"] = UNSET
    find_by_type: Union[Unset, "FindByType"] = UNSET
    find_options: Union[Unset, "FindOptions"] = UNSET
    find_for_keywording_relation: Union[Unset, "FindForKeywordingRelation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        find_by_fulltext: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_fulltext, Unset):
            find_by_fulltext = self.find_by_fulltext.to_dict()

        find_by_notes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_notes, Unset):
            find_by_notes = self.find_by_notes.to_dict()

        find_by_registered_function: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_registered_function, Unset):
            find_by_registered_function = self.find_by_registered_function.to_dict()

        find_direct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_direct, Unset):
            find_direct = self.find_direct.to_dict()

        find_by_index: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_index, Unset):
            find_by_index = self.find_by_index.to_dict()

        find_by_version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_version, Unset):
            find_by_version = self.find_by_version.to_dict()

        find_by_sord_hist: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_sord_hist, Unset):
            find_by_sord_hist = self.find_by_sord_hist.to_dict()

        find_by_acl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_acl, Unset):
            find_by_acl = self.find_by_acl.to_dict()

        find_links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_links, Unset):
            find_links = self.find_links.to_dict()

        find_by_fulltext_ctrl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_fulltext_ctrl, Unset):
            find_by_fulltext_ctrl = self.find_by_fulltext_ctrl.to_dict()

        find_by_preview_ctrl: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_preview_ctrl, Unset):
            find_by_preview_ctrl = self.find_by_preview_ctrl.to_dict()

        find_children: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_children, Unset):
            find_children = self.find_children.to_dict()

        find_by_e_search: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_e_search, Unset):
            find_by_e_search = self.find_by_e_search.to_dict()

        find_by_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_by_type, Unset):
            find_by_type = self.find_by_type.to_dict()

        find_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_options, Unset):
            find_options = self.find_options.to_dict()

        find_for_keywording_relation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.find_for_keywording_relation, Unset):
            find_for_keywording_relation = self.find_for_keywording_relation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if find_by_fulltext is not UNSET:
            field_dict["findByFulltext"] = find_by_fulltext
        if find_by_notes is not UNSET:
            field_dict["findByNotes"] = find_by_notes
        if find_by_registered_function is not UNSET:
            field_dict["findByRegisteredFunction"] = find_by_registered_function
        if find_direct is not UNSET:
            field_dict["findDirect"] = find_direct
        if find_by_index is not UNSET:
            field_dict["findByIndex"] = find_by_index
        if find_by_version is not UNSET:
            field_dict["findByVersion"] = find_by_version
        if find_by_sord_hist is not UNSET:
            field_dict["findBySordHist"] = find_by_sord_hist
        if find_by_acl is not UNSET:
            field_dict["findByAcl"] = find_by_acl
        if find_links is not UNSET:
            field_dict["findLinks"] = find_links
        if find_by_fulltext_ctrl is not UNSET:
            field_dict["findByFulltextCtrl"] = find_by_fulltext_ctrl
        if find_by_preview_ctrl is not UNSET:
            field_dict["findByPreviewCtrl"] = find_by_preview_ctrl
        if find_children is not UNSET:
            field_dict["findChildren"] = find_children
        if find_by_e_search is not UNSET:
            field_dict["findByESearch"] = find_by_e_search
        if find_by_type is not UNSET:
            field_dict["findByType"] = find_by_type
        if find_options is not UNSET:
            field_dict["findOptions"] = find_options
        if find_for_keywording_relation is not UNSET:
            field_dict["findForKeywordingRelation"] = find_for_keywording_relation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.find_by_acl import FindByAcl
        from ..models.find_by_e_search import FindByESearch
        from ..models.find_by_fulltext import FindByFulltext
        from ..models.find_by_fulltext_ctrl import FindByFulltextCtrl
        from ..models.find_by_index import FindByIndex
        from ..models.find_by_notes import FindByNotes
        from ..models.find_by_preview_ctrl import FindByPreviewCtrl
        from ..models.find_by_registered_function import FindByRegisteredFunction
        from ..models.find_by_sord_hist import FindBySordHist
        from ..models.find_by_type import FindByType
        from ..models.find_by_version import FindByVersion
        from ..models.find_children import FindChildren
        from ..models.find_direct import FindDirect
        from ..models.find_for_keywording_relation import FindForKeywordingRelation
        from ..models.find_links import FindLinks
        from ..models.find_options import FindOptions

        d = src_dict.copy()
        _find_by_fulltext = d.pop("findByFulltext", UNSET)
        find_by_fulltext: Union[Unset, FindByFulltext]
        if isinstance(_find_by_fulltext, Unset):
            find_by_fulltext = UNSET
        else:
            find_by_fulltext = FindByFulltext.from_dict(_find_by_fulltext)

        _find_by_notes = d.pop("findByNotes", UNSET)
        find_by_notes: Union[Unset, FindByNotes]
        if isinstance(_find_by_notes, Unset):
            find_by_notes = UNSET
        else:
            find_by_notes = FindByNotes.from_dict(_find_by_notes)

        _find_by_registered_function = d.pop("findByRegisteredFunction", UNSET)
        find_by_registered_function: Union[Unset, FindByRegisteredFunction]
        if isinstance(_find_by_registered_function, Unset):
            find_by_registered_function = UNSET
        else:
            find_by_registered_function = FindByRegisteredFunction.from_dict(_find_by_registered_function)

        _find_direct = d.pop("findDirect", UNSET)
        find_direct: Union[Unset, FindDirect]
        if isinstance(_find_direct, Unset):
            find_direct = UNSET
        else:
            find_direct = FindDirect.from_dict(_find_direct)

        _find_by_index = d.pop("findByIndex", UNSET)
        find_by_index: Union[Unset, FindByIndex]
        if isinstance(_find_by_index, Unset):
            find_by_index = UNSET
        else:
            find_by_index = FindByIndex.from_dict(_find_by_index)

        _find_by_version = d.pop("findByVersion", UNSET)
        find_by_version: Union[Unset, FindByVersion]
        if isinstance(_find_by_version, Unset):
            find_by_version = UNSET
        else:
            find_by_version = FindByVersion.from_dict(_find_by_version)

        _find_by_sord_hist = d.pop("findBySordHist", UNSET)
        find_by_sord_hist: Union[Unset, FindBySordHist]
        if isinstance(_find_by_sord_hist, Unset):
            find_by_sord_hist = UNSET
        else:
            find_by_sord_hist = FindBySordHist.from_dict(_find_by_sord_hist)

        _find_by_acl = d.pop("findByAcl", UNSET)
        find_by_acl: Union[Unset, FindByAcl]
        if isinstance(_find_by_acl, Unset):
            find_by_acl = UNSET
        else:
            find_by_acl = FindByAcl.from_dict(_find_by_acl)

        _find_links = d.pop("findLinks", UNSET)
        find_links: Union[Unset, FindLinks]
        if isinstance(_find_links, Unset):
            find_links = UNSET
        else:
            find_links = FindLinks.from_dict(_find_links)

        _find_by_fulltext_ctrl = d.pop("findByFulltextCtrl", UNSET)
        find_by_fulltext_ctrl: Union[Unset, FindByFulltextCtrl]
        if isinstance(_find_by_fulltext_ctrl, Unset):
            find_by_fulltext_ctrl = UNSET
        else:
            find_by_fulltext_ctrl = FindByFulltextCtrl.from_dict(_find_by_fulltext_ctrl)

        _find_by_preview_ctrl = d.pop("findByPreviewCtrl", UNSET)
        find_by_preview_ctrl: Union[Unset, FindByPreviewCtrl]
        if isinstance(_find_by_preview_ctrl, Unset):
            find_by_preview_ctrl = UNSET
        else:
            find_by_preview_ctrl = FindByPreviewCtrl.from_dict(_find_by_preview_ctrl)

        _find_children = d.pop("findChildren", UNSET)
        find_children: Union[Unset, FindChildren]
        if isinstance(_find_children, Unset):
            find_children = UNSET
        else:
            find_children = FindChildren.from_dict(_find_children)

        _find_by_e_search = d.pop("findByESearch", UNSET)
        find_by_e_search: Union[Unset, FindByESearch]
        if isinstance(_find_by_e_search, Unset):
            find_by_e_search = UNSET
        else:
            find_by_e_search = FindByESearch.from_dict(_find_by_e_search)

        _find_by_type = d.pop("findByType", UNSET)
        find_by_type: Union[Unset, FindByType]
        if isinstance(_find_by_type, Unset):
            find_by_type = UNSET
        else:
            find_by_type = FindByType.from_dict(_find_by_type)

        _find_options = d.pop("findOptions", UNSET)
        find_options: Union[Unset, FindOptions]
        if isinstance(_find_options, Unset):
            find_options = UNSET
        else:
            find_options = FindOptions.from_dict(_find_options)

        _find_for_keywording_relation = d.pop("findForKeywordingRelation", UNSET)
        find_for_keywording_relation: Union[Unset, FindForKeywordingRelation]
        if isinstance(_find_for_keywording_relation, Unset):
            find_for_keywording_relation = UNSET
        else:
            find_for_keywording_relation = FindForKeywordingRelation.from_dict(_find_for_keywording_relation)

        find_info = cls(
            find_by_fulltext=find_by_fulltext,
            find_by_notes=find_by_notes,
            find_by_registered_function=find_by_registered_function,
            find_direct=find_direct,
            find_by_index=find_by_index,
            find_by_version=find_by_version,
            find_by_sord_hist=find_by_sord_hist,
            find_by_acl=find_by_acl,
            find_links=find_links,
            find_by_fulltext_ctrl=find_by_fulltext_ctrl,
            find_by_preview_ctrl=find_by_preview_ctrl,
            find_children=find_children,
            find_by_e_search=find_by_e_search,
            find_by_type=find_by_type,
            find_options=find_options,
            find_for_keywording_relation=find_for_keywording_relation,
        )

        find_info.additional_properties = d
        return find_info

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
