import pytest

from nadypy.api.default import get_sysinfo
from nadypy.client import BasicAuthClient, SignedAuthClient
from nadypy.models import SystemInformation

basic_auth_client = BasicAuthClient("http://localhost:8080/api", "Sachan", "8dc18f1b35caa9f31db1a48b")
signed_auth_client = SignedAuthClient(
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


@pytest.mark.asyncio
async def test_basic_system_information():
    my_data = await get_sysinfo.asyncio(client=signed_auth_client)

    print(my_data)
