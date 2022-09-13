import aiohttp
import asyncio
from typing import Any
from infra.http.http_client import HttpClient


class AioHttpAdapter(HttpClient):
    async def get(self, url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()

    async def post(self, url: str, data: Any):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                return await response.json()
