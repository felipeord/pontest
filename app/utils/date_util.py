from datetime import datetime


async def get_datetime(date: str) -> datetime:
    """Get datetime from string"""
    return datetime.strptime(date, "%Y-%m-%d %H:%M")


def get_today_str() -> str:
    """Get today in string format"""
    return datetime.now().strftime("%y%m%d%H%M%S")


def format_date_log(date: datetime) -> str:
    """Format date"""
    return date.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
