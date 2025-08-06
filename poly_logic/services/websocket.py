import json
import os

import websockets
from aiogram.types import CallbackQuery
from py_clob_client.client import ClobClient
from websockets import ConnectionClosedOK, ConnectionClosedError

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
    await callback.message.answer(text = "Connecting...")
    await callback.answer()
    while True:
        async with websockets.connect(websocket_endpoint) as websocket:
            print("Websocket connected")
            await websocket.send(json.dumps({
                "auth": auth(),
                "assets_ids": [asset_token],
                "type": "market"
            }))
            await callback.message.answer(text = "Connected")
            while True:
                try:
                    data = await websocket.recv()
                    await  on_message(data, bot, callback.message.chat.id)
                except ConnectionClosedOK:
                    print("WebSocket closed normally. Will reconnect shortly.")
                    break
                except ConnectionClosedError as e:
                        print(f"WebSocket closed with error: {e}. Will reconnect.")
                        break
                except Exception as e:
                    print(f"Unexpected error in receive loop: {e}")
                    break
