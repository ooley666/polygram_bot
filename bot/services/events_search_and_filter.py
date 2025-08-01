from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.states.fsm_data_utils import merge_with_state_data
from poly_logic.classes.event import Event
from poly_logic.services.gamma_api import get_events_aiohttp


async def fetch_and_filter_events(message: Message, state: FSMContext) -> list[Event]:
    keyword = message.text
    events = await get_events_aiohttp()
    events_f = filter_events_by_keyword(events, keyword)
    await state.update_data(events=events,
                            keyword=keyword,
                            displayable_events = await merge_with_state_data(state = state,
                                                                             new_items= events_f,
                                                                             storage_key="displayable_events"))
    return events_f




def filter_events_by_keyword(events: list[Event], keyword: str) -> list[Event] | list:
    filtered_events = []
    for event in events:
        if keyword.casefold() in event.ticker:
            filtered_events.append(event)
    return filtered_events