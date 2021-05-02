import asyncio

import pytest


@pytest.fixture(scope="session")
def event_loop():
    """
    Redefine default function scoped event loop
    https://github.com/pytest-dev/pytest-asyncio#pytestmarkasyncio
    """
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
