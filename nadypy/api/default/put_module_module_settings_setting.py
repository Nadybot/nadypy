from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import Response


def _get_kwargs(
    module: str,
    setting: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[bool, int, str],
) -> Dict[str, Any]:
    url = "{}/module/{module}/settings/{setting}".format(client.base_url, module=module, setting=setting)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    setting: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[bool, int, str],
) -> Response[Any]:
    kwargs = _get_kwargs(
        module=module,
        setting=setting,
        client=client,
        json_body=json_body,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    module: str,
    setting: str,
    *,
    client: AuthenticatedClient,
    json_body: Union[bool, int, str],
) -> Response[Any]:
    kwargs = _get_kwargs(
        module=module,
        setting=setting,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)
