from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wf_node_z import WFNodeZ


T = TypeVar("T", bound="WFDelegateNodeInfo")


@_attrs_define
class WFDelegateNodeInfo:
    """This class is used as a parameter in the function
    {@link IXServicePortIF#delegateWorkFlowNode(ClientInfo, WFDelegateNodeInfo, LockZ)}.

        Attributes:
            back_node_name (Union[Unset, str]): Name of the back node.
            copy_members_to_delegate_node_z (Union[Unset, WFNodeZ]): This class encapsulates the constants of the WFNodeC
                class.
                <p>
                 Copyright: Copyright (c) 2011
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            delegate_node_comment (Union[Unset, str]): Description of the new node
            delegate_to_user_ids (Union[Unset, List[str]]):
            delegate_node_name (Union[Unset, str]): Name of the new node
            back_node_move_y (Union[Unset, int]): Vertical distance between the active node and the back node. Recommended
                value is 80.
            delegate_parallel (Union[Unset, bool]): Delegate parallel or serial to the list of users.
                if {@link #delegateToUserIds} is not null or
                 empty, this member describes how the nodes created for delegation are connected.
                 <p>
                 Set this member as true, if all delegation nodes should be activated directly. The delegation
                 returns, if at least one of the users forwards her/his node.
                 </p>
                 <p>
                 Set this member as false, if the delegation nodes should be lined up one after another. The
                 delegation returns, if all users have forwarded their nodes.
                 </p>
                 Ignored, if {@link #delegateToUserIds} is null or empty.
            back_node_move_x (Union[Unset, int]): Horizontal distance between the active node and the back node. Recommended
                value is 0.
            copy_members_to_back_node_z (Union[Unset, WFNodeZ]): This class encapsulates the constants of the WFNodeC class.
                <p>
                 Copyright: Copyright (c) 2011
                 </p>
                 <p>
                 Organisation: ELO Digital Office GmbH
                 </p>
            delegate_node_move_x (Union[Unset, int]): Horizontal distance between the active node and the delegation node.
                Recommended value is 240.
            delegate_node_move_y (Union[Unset, int]): Vertical distance between the active node and the delegation node.
                Recommended value is 0.
            delegate_to_user_id (Union[Unset, str]): Name or ID of user or group to whom the workflow is delegated.
            back_node_comment (Union[Unset, str]): Description of the back node.
            flow_id (Union[Unset, str]): Workflow ID, GUID or name
            node_id (Union[Unset, int]): Node ID
    """

    back_node_name: Union[Unset, str] = UNSET
    copy_members_to_delegate_node_z: Union[Unset, "WFNodeZ"] = UNSET
    delegate_node_comment: Union[Unset, str] = UNSET
    delegate_to_user_ids: Union[Unset, List[str]] = UNSET
    delegate_node_name: Union[Unset, str] = UNSET
    back_node_move_y: Union[Unset, int] = UNSET
    delegate_parallel: Union[Unset, bool] = UNSET
    back_node_move_x: Union[Unset, int] = UNSET
    copy_members_to_back_node_z: Union[Unset, "WFNodeZ"] = UNSET
    delegate_node_move_x: Union[Unset, int] = UNSET
    delegate_node_move_y: Union[Unset, int] = UNSET
    delegate_to_user_id: Union[Unset, str] = UNSET
    back_node_comment: Union[Unset, str] = UNSET
    flow_id: Union[Unset, str] = UNSET
    node_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        back_node_name = self.back_node_name

        copy_members_to_delegate_node_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_members_to_delegate_node_z, Unset):
            copy_members_to_delegate_node_z = self.copy_members_to_delegate_node_z.to_dict()

        delegate_node_comment = self.delegate_node_comment

        delegate_to_user_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.delegate_to_user_ids, Unset):
            delegate_to_user_ids = self.delegate_to_user_ids

        delegate_node_name = self.delegate_node_name

        back_node_move_y = self.back_node_move_y

        delegate_parallel = self.delegate_parallel

        back_node_move_x = self.back_node_move_x

        copy_members_to_back_node_z: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.copy_members_to_back_node_z, Unset):
            copy_members_to_back_node_z = self.copy_members_to_back_node_z.to_dict()

        delegate_node_move_x = self.delegate_node_move_x

        delegate_node_move_y = self.delegate_node_move_y

        delegate_to_user_id = self.delegate_to_user_id

        back_node_comment = self.back_node_comment

        flow_id = self.flow_id

        node_id = self.node_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if back_node_name is not UNSET:
            field_dict["backNodeName"] = back_node_name
        if copy_members_to_delegate_node_z is not UNSET:
            field_dict["copyMembersToDelegateNodeZ"] = copy_members_to_delegate_node_z
        if delegate_node_comment is not UNSET:
            field_dict["delegateNodeComment"] = delegate_node_comment
        if delegate_to_user_ids is not UNSET:
            field_dict["delegateToUserIds"] = delegate_to_user_ids
        if delegate_node_name is not UNSET:
            field_dict["delegateNodeName"] = delegate_node_name
        if back_node_move_y is not UNSET:
            field_dict["backNodeMoveY"] = back_node_move_y
        if delegate_parallel is not UNSET:
            field_dict["delegateParallel"] = delegate_parallel
        if back_node_move_x is not UNSET:
            field_dict["backNodeMoveX"] = back_node_move_x
        if copy_members_to_back_node_z is not UNSET:
            field_dict["copyMembersToBackNodeZ"] = copy_members_to_back_node_z
        if delegate_node_move_x is not UNSET:
            field_dict["delegateNodeMoveX"] = delegate_node_move_x
        if delegate_node_move_y is not UNSET:
            field_dict["delegateNodeMoveY"] = delegate_node_move_y
        if delegate_to_user_id is not UNSET:
            field_dict["delegateToUserId"] = delegate_to_user_id
        if back_node_comment is not UNSET:
            field_dict["backNodeComment"] = back_node_comment
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.wf_node_z import WFNodeZ

        d = src_dict.copy()
        back_node_name = d.pop("backNodeName", UNSET)

        _copy_members_to_delegate_node_z = d.pop("copyMembersToDelegateNodeZ", UNSET)
        copy_members_to_delegate_node_z: Union[Unset, WFNodeZ]
        if isinstance(_copy_members_to_delegate_node_z, Unset):
            copy_members_to_delegate_node_z = UNSET
        else:
            copy_members_to_delegate_node_z = WFNodeZ.from_dict(_copy_members_to_delegate_node_z)

        delegate_node_comment = d.pop("delegateNodeComment", UNSET)

        delegate_to_user_ids = cast(List[str], d.pop("delegateToUserIds", UNSET))

        delegate_node_name = d.pop("delegateNodeName", UNSET)

        back_node_move_y = d.pop("backNodeMoveY", UNSET)

        delegate_parallel = d.pop("delegateParallel", UNSET)

        back_node_move_x = d.pop("backNodeMoveX", UNSET)

        _copy_members_to_back_node_z = d.pop("copyMembersToBackNodeZ", UNSET)
        copy_members_to_back_node_z: Union[Unset, WFNodeZ]
        if isinstance(_copy_members_to_back_node_z, Unset):
            copy_members_to_back_node_z = UNSET
        else:
            copy_members_to_back_node_z = WFNodeZ.from_dict(_copy_members_to_back_node_z)

        delegate_node_move_x = d.pop("delegateNodeMoveX", UNSET)

        delegate_node_move_y = d.pop("delegateNodeMoveY", UNSET)

        delegate_to_user_id = d.pop("delegateToUserId", UNSET)

        back_node_comment = d.pop("backNodeComment", UNSET)

        flow_id = d.pop("flowId", UNSET)

        node_id = d.pop("nodeId", UNSET)

        wf_delegate_node_info = cls(
            back_node_name=back_node_name,
            copy_members_to_delegate_node_z=copy_members_to_delegate_node_z,
            delegate_node_comment=delegate_node_comment,
            delegate_to_user_ids=delegate_to_user_ids,
            delegate_node_name=delegate_node_name,
            back_node_move_y=back_node_move_y,
            delegate_parallel=delegate_parallel,
            back_node_move_x=back_node_move_x,
            copy_members_to_back_node_z=copy_members_to_back_node_z,
            delegate_node_move_x=delegate_node_move_x,
            delegate_node_move_y=delegate_node_move_y,
            delegate_to_user_id=delegate_to_user_id,
            back_node_comment=back_node_comment,
            flow_id=flow_id,
            node_id=node_id,
        )

        wf_delegate_node_info.additional_properties = d
        return wf_delegate_node_info

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
