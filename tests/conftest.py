import asyncio
from typing import Generator
from fastapi.testclient import TestClient

import pytest

from server import app


@pytest.fixture(scope="session")
def event_loop():
    """
    Redefine default function scoped event loop
    https://github.com/pytest-dev/pytest-asyncio#pytestmarkasyncio
    """
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
