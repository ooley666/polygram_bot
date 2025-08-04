import json
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from poly_logic.classes.event import Event

start_menu_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Browse events by keyword", callback_data="browse_events")],
                                                      [InlineKeyboardButton(text="Open saved events", callback_data="display_saved_events")]])


def event_details_kb(e: Event):
   return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Open event page in browser", url=f"https://polymarket.com/event/{e.slug}")],
                                          [InlineKeyboardButton(text = "Add the event to your saved events", callback_data="add_to_saved_events")],
                                          [InlineKeyboardButton(text = "Save event and start tracking", callback_data="add_to_saved_and_track")],
                                            [InlineKeyboardButton(text = "Go back to main menu", callback_data="back_to_start_menu")]])


def track_event_kb(e: Event):
    current_outcome_prices = json.loads(e.markets[0].outcome_prices)
    current_yes_price = current_outcome_prices[0]
    current_no_price = current_outcome_prices[1]
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f'Track "Yes" price (current price is {current_yes_price}', callback_data=f'clob_token:yes')],
                                                 [InlineKeyboardButton(text=f'Track "No" price (current price is {current_no_price})', callback_data=f'clob_token:no')]])
