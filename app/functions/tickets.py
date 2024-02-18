import asyncio
import csv

from datetime import datetime
import random

import aiofiles as aiofiles

from app.models import Ticket
from app.utils.date_util import get_datetime


async def create_ticket(id: int, creation_date: datetime, priority: int) -> Ticket:
    """Create a ticket"""
    return Ticket(id=id, creation_date=creation_date, priority=priority)


async def load_tickets(file_path: str) -> list[dict]:
    """Load tickets from file"""
    tickets = []
    with open(file_path, newline='') as csvfile:
        ticket_reader = csv.reader(csvfile, delimiter=',')
        next(ticket_reader)  # encabezado
        for row in ticket_reader:
            # print(row[0], row[1], row[2])
            ticket = await create_ticket(row[0], row[1], row[2])
            tickets.append(ticket)
    return tickets


async def sort_tickets(tickets: list[Ticket]) -> list[Ticket]:
    """Sort tickets by priority"""
    tickets.sort(key=lambda x: (x.creation_date, -x.priority))
    return tickets


async def queue_tickets(tickets: list[Ticket]) -> asyncio.Queue:
    """Queue tickets"""
    q = asyncio.Queue()
    for ticket in tickets:
        await q.put(ticket)
    return q


async def process_ticket(filename, ticket: Ticket, agent_id: int):
    """Process ticket"""
    print(f"Agent: {agent_id} processing ticket {ticket.id}...")
    date_ticket_assigned = datetime.now()
    processing_time = random.uniform(2, 3)
    await asyncio.sleep(processing_time)
    date_ticket_done = datetime.now()
    print(f"Ticket {ticket.id} processed by agent {agent_id}.")
    await write_to_log(filename, agent_id, ticket, date_ticket_assigned, date_ticket_done)


async def write_to_log(filename, agent_id, ticket, date_ticket_assigned, date_ticket_done):
    async with aiofiles.open(filename, 'a') as csvfile:
        await csvfile.write(
            f"{ticket.id},{ticket.creation_date.strftime('%Y-%m-%d %H:%M')},{ticket.priority},{agent_id},{date_ticket_assigned.strftime('%Y-%m-%d %H:%M')},{date_ticket_done.strftime('%Y-%m-%d %H:%M')},{agent_id}\n")
