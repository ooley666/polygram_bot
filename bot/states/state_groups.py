from aiogram.fsm.state import StatesGroup, State


class GlobalStateFlow(StatesGroup):
    events = State()
    keyword = State()
    events_filtered_by_keyword = State()
    event_choice = State()
    event_tracking = State()


class Saved_e(StatesGroup):
    event_choice = State()
