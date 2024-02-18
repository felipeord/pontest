from fastapi import APIRouter
from ehandler import Route
from app.functions import run_sim

router = APIRouter(route_class=Route)


@router.get("/run_sim", tags=["Sim"])
async def run_simulation():
    """
    Run the call center simulation
    """
    await run_sim(agents=3)
