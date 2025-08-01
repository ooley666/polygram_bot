from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.keyboards import keyboards as kb
from poly_logic.classes.event import Event


def e_tracking_str_generator(e: Event) -> str:
    return f'Choose which outcome you would like to track for:\n{e.markets[0].question}'


async def init_tracking (callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    e: Event = data["selected_e"]
    await callback.message.answer(text = e_tracking_str_generator(e), reply_markup=kb.track_event_kb(e))
