from fastapi import APIRouter
from fastapi.responses import FileResponse
from ehandler import Route
from app.functions import run_sim

router = APIRouter(route_class=Route)


@router.get("/run_sim",  tags=["Sim"])
async def run_simulation(agents: int = 3):
    """
    Run the call center simulation
    """
    report = await run_sim(agents=agents)
    headers = {
        'Content-Disposition': 'attachment; filename=".csv"'
    }
    return FileResponse(path=report, filename=report, media_type='text/csv')
