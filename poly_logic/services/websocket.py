import json
import os

import websockets
from aiogram.types import CallbackQuery
from py_clob_client.client import ClobClient

from configs.poly_config import websocket_endpoint, host, chain_id
from poly_logic.services.ws_message_handlers import on_message

key = os.getenv("POLY_CLOB_KEY")

def auth():
    client = ClobClient(host, key=key, chain_id=chain_id)

    api_creds = vars(client.create_or_derive_api_creds())

    client.set_api_creds(client.create_or_derive_api_creds())
    print("AUTHENTICATED SUCCESSFULLY")
    return api_creds




async def init_websocket(asset_token,  callback: CallbackQuery, bot):
    await callback.message.edit_text(text = "Connecting...")
    print("Asset token:", asset_token)

    async with websockets.connect(websocket_endpoint) as websocket:
        await websocket.send(json.dumps({
            "auth": auth(),
            "assets_ids": [asset_token],
            "type": "market"
        }))
        await  callback.message.edit_text("Connected")
        while True:
            data = await websocket.recv()
            print(data)
            on_message(data, bot, callback.message.chat.id)
