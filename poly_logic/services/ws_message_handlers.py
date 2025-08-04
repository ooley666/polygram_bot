import json
from aiogram import Bot

def on_message(data, bot:Bot, chat_id ):
    print(data)
    msg = json.loads(data)[0]
    event_type = msg.get("event_type")

    if event_type == "book":
        handle_book(msg, bot, chat_id)
    elif event_type == "price_change":
        handle_price_change(msg, bot, chat_id)
    elif event_type == "tick_size_change":
        handle_tick_size_change(msg, bot, chat_id)
    elif event_type == "last_trade_price":
        handle_last_trade_price(msg, bot, chat_id)



def handle_book(msg, bot: Bot, chat_id):
    asset_id = msg["asset_id"]
    bids = msg["bids"]
    asks = msg["asks"]
    spread = float(asks[0]["price"]) - float(bids[0]["price"]) if bids and asks else None
    bot.send_message(chat_id = chat_id,text = f"\n📘 BOOK SNAPSHOT for {asset_id}")
    bot.send_message(chat_id = chat_id,text = f"Top Bid: {bids[0] if bids else 'N/A'}, Top Ask: {asks[0] if asks else 'N/A'}, Spread: {spread}")
    # Suggest action based on spread or depth
    if spread and spread < 0.01:
        bot.send_message(chat_id = chat_id,text = "🔎 Action: Spread tight. Consider placing or adjusting orders.")

def handle_price_change(msg, bot, chat_id):
    bot.send_message(chat_id = chat_id,text = f"\n📈 PRICE CHANGE on {msg['asset_id']}")
    bot.send_message(chat_id = chat_id,text = f"Side: {msg['side']} | Price: {msg['price']} | Size: {msg['size']}")
    # Use logic to detect stacking or large single-side pressure
    if float(msg["size"]) > 1000:
        bot.send_message(chat_id = chat_id,text = "🚨 Action: Large volume at level. Monitor or follow order pressure.")

def handle_tick_size_change(msg, bot, chat_id):
    bot.send_message(chat_id = chat_id,text = f"\n⚙️ TICK SIZE CHANGE on {msg['asset_id']}")
    bot.send_message(chat_id = chat_id,text = f"Old: {msg['old_tick_size']} → New: {msg['new_tick_size']}")
    # Adjust order strategy to match new precision
    bot.send_message(chat_id = chat_id,text = "🧠 Action: Update limit order precision accordingly.")

def handle_last_trade_price(msg, bot, chat_id):
    bot.send_message(chat_id = chat_id,text = f"\n💰 LAST TRADE on {msg['asset_id']}")
    bot.send_message(chat_id = chat_id,text = f"Price: {msg['price']} | Side: {msg['side']} | Size: {msg['size']} | Timestamp: {msg['timestamp']}")
    # Detect buying/selling pressure
    if msg["side"] == "buy":
        bot.send_message(chat_id = chat_id,text = "🚀 Action: Buyer-initiated trade. Momentum building?")
    elif msg["side"] == "sell":
        bot.send_message(chat_id = chat_id,text = "🔻 Action: Seller aggression. Possible reversal?")

# def on_open(ws):
#     print("🌐 WebSocket connection opened")
#     sub_msg = {
#         "type": "market",
#         "assets_ids": ASSET_IDS,
#         "auth": None
#     }
#     ws.send(json.dumps(sub_msg))
#
# def on_error(ws, error):
#     print("⚠️ WebSocket error:", error)
#
# def on_close(ws, close_status_code, close_msg):
#     print("🔌 WebSocket connection closed")




