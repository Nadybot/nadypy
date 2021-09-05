from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...models.operation import Operation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    module: str,
    *,
    client: AuthenticatedClient,
    json_body: Operation,
    channel: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/module/{module}".format(client.base_url, module=module)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "channel": channel,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    module: str,
    *,
    client: AuthenticatedClient,
    json_body: Operation,
    channel: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        module=module,
        client=client,
        json_body=json_body,
        channel=channel,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    module: str,
    *,
    client: AuthenticatedClient,
    json_body: Operation,
    channel: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        module=module,
        client=client,
        json_body=json_body,
        channel=channel,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)
