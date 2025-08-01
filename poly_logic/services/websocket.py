import json

import websockets
from aiogram.types import CallbackQuery
from py_clob_client.client import ClobClient

from configs.poly_config import websocket_endpoint, host, key, chain_id


def auth():
    client = ClobClient(host, key=key, chain_id=chain_id)

    api_creds = vars(client.create_or_derive_api_creds())

    client.set_api_creds(client.create_or_derive_api_creds())
    print("AUTHENTICATED SUCCESSFULLY")
    return api_creds




async def init_websocket(asset_token, ws_message_handler, callback: CallbackQuery):
    async with websockets.connect(websocket_endpoint) as websocket:
        await websocket.send(json.dumps({
            "auth": auth(),
            "assets_ids": [asset_token],
            "type": "market"
        }))
    while True:
        response = await websocket.recv()
        message = json.loads(response)
        if message.get('event_type') == 'book':
            await ws_message_handler(message, callback)
