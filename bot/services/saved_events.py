from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.states.fsm_data_utils import merge_with_state_data
from poly_logic.classes.event import Event
from poly_logic.services.gamma_api import get_events_aiohttp
from utils.json_operations import write_to_json, read_from_json


async def fetch_saved_events (state: FSMContext):
    saved_events_data = read_from_json("db/saved_events.json")
    saved_events_ids = saved_events_data.keys()
    saved_events = await get_events_aiohttp(list(saved_events_ids))
    await state.update_data(saved_events_data=saved_events_data,
                            displayable_events = await merge_with_state_data(state = state,
                                                                             new_items= saved_events,
                                                                             storage_key="displayable_events"))
    return saved_events_data


async def save_event (state: FSMContext, callback: CallbackQuery):
    data = await state.get_data()
    selected_e: Event = data["selected_e"]
    new_saved_events_entry = {selected_e.id: selected_e.title}
    await state.update_data(
        saved_events_data=await merge_with_state_data(state=state, new_items=new_saved_events_entry,
                                                      storage_key="saved_events_data"))
    data_mutated = await state.get_data()
    saved_events_data_mutated = data_mutated["saved_events_data"]
    write_to_json("db/saved_events.json", saved_events_data_mutated)
    await callback.message.answer(text="Event saved successfully")
    await callback.answer()
