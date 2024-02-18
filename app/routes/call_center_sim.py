import csv
from io import StringIO

from fastapi import APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from ehandler import Route
from app.functions import run_sim, load_tickets, sort_tickets, queue_tickets, process_ticket, write_to_log


router = APIRouter(route_class=Route)


@router.get("/run_sim/", tags=["Sim"])
async def run_simulation(agents: int = 3):
    """
    Run the call center simulation
    """
    report = await run_sim(agents=agents)
    headers = {
        'Content-Disposition': 'attachment; filename=".csv"'
    }
    return FileResponse(path=report, filename=report, media_type='text/csv')


@router.get("/get_sorted/", tags=["Sim"])
async def get_sorted():
    """
    Get the sorted tickets
    """
    tickets = await load_tickets("tickets_dataset.csv")
    sorted_tickets = await sort_tickets(tickets)

    output = StringIO()
    writer = csv.writer(output)

    for ticket in sorted_tickets:
        writer.writerow([ticket.id, ticket.creation_date, ticket.priority])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv")

