from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from bot.states.state_groups import GlobalStateFlow
from poly_logic.classes.event import Event
from poly_logic.services.websocket import init_websocket
from utils.datetime_formatting import timestamp_to_readable

router_tracking = Router()

@router_tracking.callback_query(F.data.startswith(f'clob_token:'))
async def track_event(callback: CallbackQuery, state: FSMContext):
    tracked_result = callback.data.split(":")[1]
    data = await state.get_data()
    e: Event = data["selected_e"]
    if tracked_result == "yes":
        clob_token = e.market.clob_token_ids[0]
        await state.set_state(GlobalStateFlow.event_tracking)
        await init_websocket(clob_token, ws_message_handler, callback)
    elif tracked_result == "no":
        clob_token = e.market.clob_token_ids[1]
        await state.set_state(GlobalStateFlow.event_tracking)
        await init_websocket(clob_token, ws_message_handler, callback)

async def ws_message_handler(message, callback: CallbackQuery):
    str =  (f"{timestamp_to_readable(message['timestamp'])}" + "\n" +
    f"Latest price is: {(float(message['asks'][-1]['price']) + float(message['bids'][-1]['price'])) / 2}")
    await callback.message.answer(text = str)
