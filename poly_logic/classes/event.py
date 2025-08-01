from typing import List, Optional, Union

from pydantic import BaseModel, Field


class Tag(BaseModel):
    id: Optional[Union[int, str]] = None
    label: Optional[str] = None
    slug: Optional[str] = None
    force_show: Optional[bool] = Field(None, alias="forceShow")
    published_at: Optional[str] = Field(None, alias="publishedAt")
    updated_by: Optional[int] = Field(None, alias="updatedBy")
    created_at: Optional[str] = Field(None, alias="createdAt")
    updated_at: Optional[str] = Field(None, alias="updatedAt")
    force_hide: Optional[bool] = Field(None, alias="forceHide")


class ClobReward(BaseModel):
    id: Optional[Union[int, str]] = None
    condition_id: Optional[str] = Field(None, alias="conditionId")
    asset_address: Optional[str] = Field(None, alias="assetAddress")
    rewards_amount: Optional[float] = Field(None, alias="rewardsAmount")
    rewards_daily_rate: Optional[float] = Field(None, alias="rewardsDailyRate")
    start_date: Optional[str] = Field(None, alias="startDate")
    end_date: Optional[str] = Field(None, alias="endDate")


class Market(BaseModel):
    id: Optional[Union[int, str]] = None
    question: Optional[str] = None
    condition_id: Optional[str] = Field(None, alias="conditionId")
    slug: Optional[str] = None
    resolution_source: Optional[str] = Field(None, alias="resolutionSource")
    end_date: Optional[str] = Field(None, alias="endDate")
    liquidity: Optional[Union[str, float]] = None
    start_date: Optional[str] = Field(None, alias="startDate")
    image: Optional[str] = None
    icon: Optional[str] = None
    description: Optional[str] = None
    outcomes: Optional[str] = None  # JSON string
    outcome_prices: Optional[str] = Field(None, alias="outcomePrices")  # JSON string
    volume: Optional[Union[str, float]] = None
    active: Optional[bool] = None
    closed: Optional[bool] = None
    market_maker_address: Optional[str] = Field(None, alias="marketMakerAddress")
    created_at: Optional[str] = Field(None, alias="createdAt")
    updated_at: Optional[str] = Field(None, alias="updatedAt")
    new: Optional[bool] = None
    featured: Optional[bool] = None
    submitted_by: Optional[str] = Field(None, alias="submitted_by")
    archived: Optional[bool] = None
    resolved_by: Optional[str] = Field(None, alias="resolvedBy")
    restricted: Optional[bool] = None
    group_item_title: Optional[str] = Field(None, alias="groupItemTitle")
    group_item_threshold: Optional[str] = Field(None, alias="groupItemThreshold")
    question_id: Optional[str] = Field(None, alias="questionID")
    enable_order_book: Optional[bool] = Field(None, alias="enableOrderBook")
    order_price_min_tick_size: Optional[float] = Field(None, alias="orderPriceMinTickSize")
    order_min_size: Optional[float] = Field(None, alias="orderMinSize")
    volume_num: Optional[float] = Field(None, alias="volumeNum")
    liquidity_num: Optional[float] = Field(None, alias="liquidityNum")
    end_date_iso: Optional[str] = Field(None, alias="endDateIso")
    start_date_iso: Optional[str] = Field(None, alias="startDateIso")
    has_reviewed_dates: Optional[bool] = Field(None, alias="hasReviewedDates")
    volume_24hr: Optional[float] = Field(None, alias="volume24hr")
    volume_1wk: Optional[float] = Field(None, alias="volume1wk")
    volume_1mo: Optional[float] = Field(None, alias="volume1mo")
    volume_1yr: Optional[float] = Field(None, alias="volume1yr")
    game_start_time: Optional[str] = Field(None, alias="gameStartTime")
    clob_token_ids: Optional[str] = Field(None, alias="clobTokenIds")  # JSON string
    uma_bond: Optional[str] = Field(None, alias="umaBond")
    uma_reward: Optional[str] = Field(None, alias="umaReward")
    volume_24hr_clob: Optional[float] = Field(None, alias="volume24hrClob")
    volume_1wk_clob: Optional[float] = Field(None, alias="volume1wkClob")
    volume_1mo_clob: Optional[float] = Field(None, alias="volume1moClob")
    volume_1yr_clob: Optional[float] = Field(None, alias="volume1yrClob")
    volume_clob: Optional[float] = Field(None, alias="volumeClob")
    liquidity_clob: Optional[float] = Field(None, alias="liquidityClob")
    accepting_orders: Optional[bool] = Field(None, alias="acceptingOrders")
    neg_risk: Optional[bool] = Field(None, alias="negRisk")
    ready: Optional[bool] = None
    funded: Optional[bool] = None
    accepting_orders_timestamp: Optional[str] = Field(None, alias="acceptingOrdersTimestamp")
    cyom: Optional[bool] = None
    competitive: Optional[float] = None
    pager_duty_notification_enabled: Optional[bool] = Field(None, alias="pagerDutyNotificationEnabled")
    approved: Optional[bool] = None
    clob_rewards: Optional[List[ClobReward]] = Field(None, alias="clobRewards")
    rewards_min_size: Optional[float] = Field(None, alias="rewardsMinSize")
    rewards_max_spread: Optional[float] = Field(None, alias="rewardsMaxSpread")
    spread: Optional[float] = None
    one_day_price_change: Optional[float] = Field(None, alias="oneDayPriceChange")
    one_week_price_change: Optional[float] = Field(None, alias="oneWeekPriceChange")
    one_month_price_change: Optional[float] = Field(None, alias="oneMonthPriceChange")
    last_trade_price: Optional[float] = Field(None, alias="lastTradePrice")
    best_bid: Optional[float] = Field(None, alias="bestBid")
    best_ask: Optional[float] = Field(None, alias="bestAsk")
    automatically_active: Optional[bool] = Field(None, alias="automaticallyActive")
    clear_book_on_start: Optional[bool] = Field(None, alias="clearBookOnStart")
    manual_activation: Optional[bool] = Field(None, alias="manualActivation")
    neg_risk_other: Optional[bool] = Field(None, alias="negRiskOther")
    uma_resolution_statuses: Optional[str] = Field(None, alias="umaResolutionStatuses")  # JSON string
    pending_deployment: Optional[bool] = Field(None, alias="pendingDeployment")
    deploying: Optional[bool] = None
    rfq_enabled: Optional[bool] = Field(None, alias="rfqEnabled")
    holding_rewards_enabled: Optional[bool] = Field(None, alias="holdingRewardsEnabled")


class Event(BaseModel):
    """
    Pydantic model for Polymarket prediction market events.
    All fields are optional to accommodate varying data structures.
    """

    # Basic identification
    id: Optional[Union[int, str]] = None
    ticker: Optional[str] = None
    slug: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    resolution_source: Optional[str] = Field(None, alias="resolutionSource")

    # Dates
    start_date: Optional[str] = Field(None, alias="startDate")
    creation_date: Optional[str] = Field(None, alias="creationDate")
    end_date: Optional[str] = Field(None, alias="endDate")
    created_at: Optional[str] = Field(None, alias="createdAt")
    updated_at: Optional[str] = Field(None, alias="updatedAt")

    # Images
    image: Optional[str] = None
    icon: Optional[str] = None

    # Status flags
    active: Optional[bool] = None
    closed: Optional[bool] = None
    archived: Optional[bool] = None
    new: Optional[bool] = None
    featured: Optional[bool] = None
    restricted: Optional[bool] = None

    # Financial metrics
    liquidity: Optional[Union[str, float]] = None
    volume: Optional[Union[str, float]] = None
    open_interest: Optional[Union[str, float]] = Field(None, alias="openInterest")
    competitive: Optional[float] = None

    # Volume metrics by time period
    volume_24hr: Optional[float] = Field(None, alias="volume24hr")
    volume_1wk: Optional[float] = Field(None, alias="volume1wk")
    volume_1mo: Optional[float] = Field(None, alias="volume1mo")
    volume_1yr: Optional[float] = Field(None, alias="volume1yr")

    # Order book settings
    enable_order_book: Optional[bool] = Field(None, alias="enableOrderBook")
    liquidity_clob: Optional[float] = Field(None, alias="liquidityClob")

    # Engagement
    comment_count: Optional[int] = Field(None, alias="commentCount")

    # Related data
    markets: Optional[List[Market]] = None
    tags: Optional[List[Tag]] = None

    # Configuration flags
    cyom: Optional[bool] = None
    show_all_outcomes: Optional[bool] = Field(None, alias="showAllOutcomes")
    show_market_images: Optional[bool] = Field(None, alias="showMarketImages")
    enable_neg_risk: Optional[bool] = Field(None, alias="enableNegRisk")
    automatically_active: Optional[bool] = Field(None, alias="automaticallyActive")
    neg_risk_augmented: Optional[bool] = Field(None, alias="negRiskAugmented")
    pending_deployment: Optional[bool] = Field(None, alias="pendingDeployment")
    deploying: Optional[bool] = None

    class Config:
        # Allow population by field name or alias
        allow_population_by_field_name = True
        # Handle extra fields gracefully
        extra = "ignore"