from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from aiogram.types import Message, CallbackQuery

from bot.keyboards import keyboards as kb
from bot.handlers.event_search_handlers import router_search
from bot.handlers.event_tracking_handlers import router_tracking
from bot.handlers.saved_events_handlers import router_saved

from bot.services.event_details import show_event_details



router_main = Router()
router_main.include_router(router_search)
router_main.include_router(router_saved)
router_main.include_router(router_tracking)





@router_main.message(CommandStart())
@router_main.message(F.is_(None))
async def cmd_start(message: Message):
    await message.answer(text = "Hi!\nThis bot can help you navigate through Polymarket.", reply_markup=kb.start_menu_kb)

@router_main.callback_query(F.data.startswith("select_id:"))
async def event_details(callback: CallbackQuery, state: FSMContext):
      await show_event_details(callback=callback, state=state)

@router_main.callback_query(F.data == "back_to_start_menu")
async def back_to_start_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text = "Hi!\nThis bot can help you navigate through Polymarket.", reply_markup=kb.start_menu_kb)
    await callback.answer()