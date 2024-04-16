from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.b_request_system_information_count_docs_in_store_path import (
    BRequestSystemInformationCountDocsInStorePath,
)
from ...models.b_result_276702696 import BResult276702696
from ...types import Response


def _get_kwargs(
    *,
    body: BRequestSystemInformationCountDocsInStorePath,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/SystemInformation/countDocsInStorePath",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[BResult276702696]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BResult276702696.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[BResult276702696]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BRequestSystemInformationCountDocsInStorePath,
) -> Response[BResult276702696]:
    """
    Args:
        body (BRequestSystemInformationCountDocsInStorePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BResult276702696]
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
    body: BRequestSystemInformationCountDocsInStorePath,
) -> Optional[BResult276702696]:
    """
    Args:
        body (BRequestSystemInformationCountDocsInStorePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BResult276702696
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BRequestSystemInformationCountDocsInStorePath,
) -> Response[BResult276702696]:
    """
    Args:
        body (BRequestSystemInformationCountDocsInStorePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BResult276702696]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: BRequestSystemInformationCountDocsInStorePath,
) -> Optional[BResult276702696]:
    """
    Args:
        body (BRequestSystemInformationCountDocsInStorePath):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BResult276702696
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
