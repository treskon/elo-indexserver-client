from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.b_request_ix_service_port_if_get_archive_statistics import BRequestIXServicePortIFGetArchiveStatistics
from ...models.b_result_2056457945 import BResult2056457945
from ...types import Response


def _get_kwargs(
    *,
    json_body: BRequestIXServicePortIFGetArchiveStatistics,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/IXServicePortIF/getArchiveStatistics",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BResult2056457945]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BResult2056457945.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BResult2056457945]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: BRequestIXServicePortIFGetArchiveStatistics,
) -> Response[BResult2056457945]:
    """
    Args:
        json_body (BRequestIXServicePortIFGetArchiveStatistics):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BResult2056457945]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: BRequestIXServicePortIFGetArchiveStatistics,
) -> Optional[BResult2056457945]:
    """
    Args:
        json_body (BRequestIXServicePortIFGetArchiveStatistics):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BResult2056457945
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: BRequestIXServicePortIFGetArchiveStatistics,
) -> Response[BResult2056457945]:
    """
    Args:
        json_body (BRequestIXServicePortIFGetArchiveStatistics):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BResult2056457945]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: BRequestIXServicePortIFGetArchiveStatistics,
) -> Optional[BResult2056457945]:
    """
    Args:
        json_body (BRequestIXServicePortIFGetArchiveStatistics):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BResult2056457945
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
