from datetime import datetime

from pydantic import BaseModel, Field


class Ticket(BaseModel):  # type: ignore
    """
    Ticket model.
    """

    id: int
    creation_date: datetime
    priority: int

