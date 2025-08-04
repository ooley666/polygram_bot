from pydantic import BaseModel, Field, TypeAdapter
from typing import Annotated, Union, List, Literal


class Order(BaseModel):
    price: str
    size: str


class BookEvent(BaseModel):
    event_type: Literal["book"]
    asset_id: str
    market: str
    bids: List[Order]
    asks: List[Order]
    timestamp: str
    hash: str


class PriceChange(BaseModel):
    price: str
    side: str
    size: str


class PriceChangeEvent(BaseModel):
    event_type: Literal["price_change"]
    asset_id: str
    changes: List[PriceChange]
    market: str
    timestamp: str
    hash: str


class TickSizeChangeEvent(BaseModel):
    event_type: Literal["tick_size_change"]
    asset_id: str
    market: str
    old_tick_size: str
    new_tick_size: str
    timestamp: str


class LastTradePriceEvent(BaseModel):
    event_type: Literal["last_trade_price"]
    asset_id: str
    fee_rate_bps: str
    market: str
    price: str
    side: str
    size: str
    timestamp: str

Message = Annotated[
    Union[
        BookEvent,
        PriceChangeEvent,
        TickSizeChangeEvent,
        LastTradePriceEvent
    ],
    Field(discriminator='event_type')
]

message_adapter = TypeAdapter(Message)