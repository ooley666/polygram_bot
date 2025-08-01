from aiogram.client.session import aiohttp

from poly_logic.classes.event import Event
from configs.poly_config import events_endpoint




async def get_events_aiohttp(ids: list[str] | None = None) -> list[Event]:
    params = {"active": "true", "closed": "false", "limit": "1000000"}
    if ids is not None:
        params["id"] = ids
    async with aiohttp.ClientSession() as session:
        async with session.get(
            events_endpoint,
            params=params,
            timeout=10  # optional
        ) as response:
            raw_json = await response.json()
            events = [Event(**e) for e in raw_json]
            return events




