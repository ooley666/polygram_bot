from datetime import datetime, timezone


def time_until_date(target_date_str):
    """Return detailed time remaining including days, hours, minutes"""
    if target_date_str.endswith("Z"):
        target_date_str = target_date_str[:-1] + "+00:00"

    target_date_utc = datetime.fromisoformat(target_date_str)
    current_date_local = datetime.now().astimezone()

    target_date_local = target_date_utc.astimezone()
    difference = target_date_local - current_date_local

    if difference.total_seconds() < 0:
        return f"Date has passed {abs(difference.days)} days ago"

    days = difference.days
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return f"{days} days, {hours} hours, {minutes} minutes"


def timestamp_to_readable(timestamp_ms: str):
    timestamp_s = int(timestamp_ms)/1000
    dt = datetime.fromtimestamp(timestamp_s, timezone.utc)
    formatted_date = dt.strftime("%d/%m/%Y, %H:%M:%S UTC")
    return formatted_date
