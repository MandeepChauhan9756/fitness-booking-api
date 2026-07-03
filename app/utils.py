from datetime import datetime
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")


def convert_to_ist(dt: datetime) -> datetime:
    """
    Convert any timezone-aware datetime to IST.
    """
    if dt.tzinfo is None:
        raise ValueError("Datetime must be timezone-aware.")

    return dt.astimezone(IST)


def get_current_ist() -> datetime:
    """
    Return current IST datetime.
    """
    return datetime.now(IST)


def ensure_ist(dt: datetime) -> datetime:
    """
    SQLite returns naive datetime.
    Attach IST if timezone is missing.
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=IST)

    return dt.astimezone(IST)