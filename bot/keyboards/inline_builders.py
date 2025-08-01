from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from poly_logic.classes.event import Event


def events_overview_kb_builder (events: list[Event]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for e in events:
        builder.button(text=e.title, callback_data=f"select_id:{e.id}")
    builder.adjust(1)
    return builder.as_markup()


def saved_events_kb_builder (events: dict[str, str]):
    builder = InlineKeyboardBuilder()
    for id, e_title in events.items():
        builder.button(text=e_title, callback_data=f"select_id:{id}")
    builder.adjust(1)
    return builder.as_markup()
