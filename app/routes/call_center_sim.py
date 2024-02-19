import csv
from io import StringIO

import aiofiles
from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from ehandler import Route
from app.functions import (
    run_sim,
    load_tickets,
    sort_tickets,
    queue_tickets,
    process_ticket,
    write_to_log,
)

router = APIRouter(route_class=Route)


@router.post("/upload_sim_csv/", summary="Cargar dataset", tags=["Upload"])
async def upload_sim_csv(file: UploadFile = File(...)):
    """
    Load the csv file with the tickets
    """
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="File must be a csv")

    file_path = f"uploads/tickets_dataset.csv"
    async with aiofiles.open(file_path, "wb") as out_file:
        content = await file.read()  # Leer el contenido del archivo subido
        await out_file.write(content)

    await file.close()

    return JSONResponse(content={"filename": file_path})


@router.post("/start_fixed_sims/", summary="Correr simulaciones 3,5,10", tags=["Sim"])
async def start_fixed_sims(background_tasks: BackgroundTasks):
    """
    Correr simulaciones con 3, 5 y 10 agentes.
    """
    background_tasks.add_task(run_sim, 3)
    background_tasks.add_task(run_sim, 5)
    background_tasks.add_task(run_sim, 10)
    return "Simulaciones en ejecución.."


@router.get("/run_sim/", summary="Correr una simulación", tags=["Sim"])
async def run_simulation(agents: int = 3):
    """
    Correr una simulación con con el archivo cargado. El número de agentes es un parámetro opcional.
    """
    report = await run_sim(agents=agents)
    headers = {"Content-Disposition": 'attachment; filename=".csv"'}
    return FileResponse(path=report, filename=report, media_type="text/csv")


@router.get("/get_sorted/", summary="Mostrar dataset ordenado", tags=["Test Data"])
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
