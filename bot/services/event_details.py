import json
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.keyboards import keyboards as kb
from poly_logic.classes.event import Event
from utils.datetime_formatting import time_until_date


async def show_event_details(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    displayable_events: list[Event] = data["displayable_events"]
    e_id = callback.data.split(":")[1]
    selected_e = next((e for e in displayable_events if e.id == e_id), None)
    #build description with keyboard markup
    if selected_e:
        await callback.message.answer(text=event_details_str_generator(selected_e),
                                      reply_markup=kb.event_details_kb(selected_e))
        await state.update_data(selected_e=selected_e)
    else:
        await callback.message.answer(text="Event not found.")
    await callback.answer()


def event_details_str_generator(event: Event) -> str:
    id = event.id
    title = event.title
    description = event.description
    outcome_prices: list[str] = json.loads(event.markets[0].outcome_prices)
    yes_token_price = outcome_prices[0]
    no_token_price = outcome_prices[1]
    end_date = time_until_date(event.end_date)
    slug = event.slug
    markets = event.markets

    return (f'{title} \nDescription: {description} \n"Yes" price: {yes_token_price} \n"No" price: {no_token_price} \nEnds in: {end_date}')


