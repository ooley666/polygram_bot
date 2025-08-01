from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram import F
import bot.keyboards.inline_builders
from bot.states.state_groups import GlobalStateFlow
from bot.services.event_tracking import init_tracking
from bot.services.saved_events import save_event, fetch_saved_events


router_saved = Router()


@router_saved.callback_query(F.data == "display_saved_events")
async def display_saved_events (callback: CallbackQuery, state: FSMContext):
    saved_events_data = await fetch_saved_events(state=state)
    await callback.message.answer(text = "Your saved events. Choose to view details", reply_markup=bot.keyboards.inline_builders.saved_events_kb_builder(saved_events_data))
    await state.set_state(GlobalStateFlow.event_choice)
    await callback.answer()



@router_saved.callback_query(F.data == "add_to_saved_events")
async def add_e_to_saved(callback: CallbackQuery, state: FSMContext):
   await save_event(callback = callback, state = state)

@router_saved.callback_query(F.data == "add_to_saved_and_track")
async def save_and_track(callback: CallbackQuery, state: FSMContext):
    await save_event(callback = callback, state = state)
    await init_tracking(callback = callback, state = state)