from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
import bot.keyboards.inline_builders
from bot.services.events_search_and_filter import fetch_and_filter_events
from bot.states.state_groups import GlobalStateFlow

router_search = Router()



@router_search.callback_query(F.data == 'browse_events')
async def prompt_keyword(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text="Enter the keyword to search by:")
    await state.set_state(GlobalStateFlow.keyword)


@router_search.message(GlobalStateFlow.keyword)
async def show_filtered_events(message: Message, state: FSMContext):
    await message.answer("Loading results. Please, wait...")

    events_f = await fetch_and_filter_events(message=message, state=state)

    if events_f != []:
        await message.answer(text=f"\nHere's what we found by your keyword ('{message.text}') \nChoose to view details\n",
                             reply_markup=bot.keyboards.inline_builders.events_overview_kb_builder(events_f))
        await state.set_state(GlobalStateFlow.event_choice)
    else:
        await message.answer(text="No events found by your keyword.\n\nTry again")







