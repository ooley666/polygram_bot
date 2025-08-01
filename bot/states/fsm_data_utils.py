from aiogram.fsm.context import FSMContext

from poly_logic.classes.event import Event
from utils.json_operations import read_from_json


async def merge_with_state_data (state: FSMContext, new_items: list[Event] | dict[str, str], storage_key: str):
    data = await state.get_data()
    current_data = data.get(storage_key)
    print(f"existing data: {current_data}")
    print("\n\n\n")
    print(f"new data: {new_items}")
    #if used with list of events
    if isinstance(current_data, list) and  isinstance(new_items, list):
        merged_data = current_data + new_items

    #if used with saved events dict
    elif isinstance(current_data, dict) and isinstance(new_items, dict):
        merged_data = {**current_data, **new_items}

    #if there's no cache of data,
    # initialize from file
    elif current_data is None and isinstance(new_items, dict):
        saved_events_data = read_from_json("../db/saved_events.json")
        merged_data = {**saved_events_data, **new_items}

    #use new_item only
    elif current_data is None and isinstance(new_items, list):
        merged_data = new_items

    else:
        raise TypeError(f"Incompatible types: cannot merge {type(current_data)} with {type(new_items)}")
    return merged_data
