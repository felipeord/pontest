import csv
import queue
from app.models import Ticket
from app.utils.date_util import get_datetime


async def create_ticket(id: int, creation_date: str, priority: int) -> Ticket:
    """Create a ticket"""
    parsed_date = await get_datetime(creation_date)
    return Ticket(id=id, creation_date=parsed_date, priority=priority)


async def load_tickets(file_path: str) -> list[dict]:
    """Load tickets from file"""
    tickets = queue.Queue()
    with open(file_path, newline='') as csvfile:
        ticket_reader = csv.reader(csvfile, delimiter=',')
        next(ticket_reader)  # encabezado
        for row in ticket_reader:
            ticket = await create_ticket(row[0], row[1], row[2])
            tickets.put(ticket)
    return tickets
