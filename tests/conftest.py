from __future__ import annotations

import contextlib
from typing import AsyncIterator, Iterator

import pytest
import pytest_asyncio
from nats.aio.client import Client as NATS

from nats_contrib.test_server import NATSD


@pytest_asyncio.fixture
async def nats_client() -> AsyncIterator[NATS]:
    client = NATS()
    try:
        yield client
    finally:
        await client.close()


@pytest.fixture
def natsd() -> NATSD:
    return NATSD(
        port=4222,
        address="localhost",
        client_advertise="localhost:4222",
        server_name="test-server-01",
        server_tags={"region": "test01"},
        with_jetstream=True,
        debug=True,
        trace=True,
        trace_verbose=False,
        http_port=8222,
        websocket_listen_address="localhost",
        websocket_listen_port=10080,
        leafnodes_listen_port=7422,
    )


@pytest.fixture
def nats_server(natsd: NATSD) -> Iterator[NATSD]:
    with contextlib.ExitStack() as stack:
        server = stack.enter_context(natsd)
        yield server
