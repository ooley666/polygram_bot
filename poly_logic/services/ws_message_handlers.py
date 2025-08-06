import json
from aiogram import Bot


from poly_logic.classes.websocket_messages import *


async def on_message(data, bot:Bot, chat_id ):
    print(data)
    raw_msg = json.loads(data)[0]
    msg: Message = message_adapter.validate_python(raw_msg)



    if isinstance(msg, BookEvent):
        await handle_book(msg, bot, chat_id)
    # elif isinstance(msg, PriceChangeEvent):
    #     await handle_price_change(msg, bot, chat_id)
    elif isinstance(msg, TickSizeChangeEvent):
        await handle_tick_size_change(msg, bot, chat_id)
    elif isinstance(msg, LastTradePriceEvent):
        await handle_last_trade_price(msg, bot, chat_id)


async def handle_book(msg: BookEvent, bot: Bot, chat_id):
    asset_id = msg.asset_id
    bids = msg.bids
    asks = msg.asks
    spread = float(asks[-1].price) - float(bids[-1].price) if bids and asks else None

    message = f"""📘 BOOK: {asset_id}x
Bid     | {bids[-1] if bids else 'N/A'}
Ask     | {asks[-1] if asks else 'N/A'}
Spread  | {spread}"""
    await bot.send_message(chat_id=chat_id, text=message)


# async def handle_price_change(msg: PriceChangeEvent, bot, chat_id):
#     side = msg.changes.side
#
#
#     message = f"""📈 PRICE CHANGE: {msg.asset_id}
# Side    | {msg.changes.}
# Price   | {msg.price}
# Size    | {msg.size}"""
#     await bot.send_message(chat_id=chat_id, text=message)


async def handle_tick_size_change(msg: TickSizeChangeEvent, bot, chat_id):
    message = f"""⚙️ TICK SIZE: {msg.asset_id}
Old     | {msg.old_tick_size}
New     | {msg.new_tick_size}"""
    await bot.send_message(chat_id=chat_id, text=message)


async def handle_last_trade_price(msg: LastTradePriceEvent, bot, chat_id):
    message = f"""💰 LAST TRADE: {msg.asset_id}
Price   | {msg.price}
Side    | {msg.side}
Size    | {msg.size}
Time    | {msg.timestamp}"""
    await bot.send_message(chat_id=chat_id, text=message)





