from datetime import datetime


async def get_datetime(date: str) -> datetime:
    """Get datetime from string"""
    return datetime.strptime(date, "%Y-%m-%d %H:%M")
