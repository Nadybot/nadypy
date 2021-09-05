from nadypy.models.system_information import SystemInformation
import pytest

from nadypy.api.default import get_sysinfo, post_chat_web
from nadypy.client import BasicAuthClient, SignedAuthClient


@pytest.fixture
async def basic_auth_client():
    client = BasicAuthClient("http://localhost:8080/api", "Sachan", "8dc18f1b35caa9f31db1a48b")

    yield client

    await client.close()


@pytest.fixture
async def signed_auth_client():
    client = SignedAuthClient(
        "http://localhost:8080/api",
        "bd879e20",
        """\
-----BEGIN EC PRIVATE KEY-----
MHcCAQEEINca+XgCZoLXuu6p77cphsIxMiSaG09tBH6SV9AgEH4ioAoGCCqGSM49
AwEHoUQDQgAEPnzqwJq/el8kyNSPmYhQJ0L2qrMFtM3XDbAHrTQlXbFN2G8NmMBp
i52oubVjuTSHol1BQf4Haftbt0oBvHGUIw==
-----END EC PRIVATE KEY-----
""",
    )

    yield client

    await client.close()


@pytest.mark.asyncio
async def test_basic_system_information_async(signed_auth_client):
    my_data = await get_sysinfo.asyncio(client=signed_auth_client)
    assert isinstance(my_data, SystemInformation)


@pytest.mark.asyncio
async def test_chat(signed_auth_client):
    response = await post_chat_web.asyncio_detailed(client=signed_auth_client, json_body="hi it's me")
    assert response.status_code == 204


def test_basic_system_information_sync(signed_auth_client):
    my_data = get_sysinfo.sync(client=signed_auth_client)
    assert isinstance(my_data, SystemInformation)
