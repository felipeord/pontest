from fastapi import APIRouter
from ehandler import Route

router = APIRouter(route_class=Route)


@router.get("/", tags=["Sim"])
async def run_sim():
    """
    Run the call center simulation
    """
    return {"message": "Call center simulation is running"}
