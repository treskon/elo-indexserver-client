from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.b_request_ix_service_port_if_get_edit_info_from_esw import BRequestIXServicePortIFGetEditInfoFromESW
from ...models.b_result_785380175 import BResult785380175
from ...types import Response


def _get_kwargs(
    *,
    body: BRequestIXServicePortIFGetEditInfoFromESW,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/IXServicePortIF/getEditInfoFromESW",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BResult785380175]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BResult785380175.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BResult785380175]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BRequestIXServicePortIFGetEditInfoFromESW,
) -> Response[BResult785380175]:
    """
    Args:
        body (BRequestIXServicePortIFGetEditInfoFromESW):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BResult785380175]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: BRequestIXServicePortIFGetEditInfoFromESW,
) -> Optional[BResult785380175]:
    """
    Args:
        body (BRequestIXServicePortIFGetEditInfoFromESW):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BResult785380175
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BRequestIXServicePortIFGetEditInfoFromESW,
) -> Response[BResult785380175]:
    """
    Args:
        body (BRequestIXServicePortIFGetEditInfoFromESW):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BResult785380175]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BRequestIXServicePortIFGetEditInfoFromESW,
) -> Optional[BResult785380175]:
    """
    Args:
        body (BRequestIXServicePortIFGetEditInfoFromESW):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BResult785380175
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
