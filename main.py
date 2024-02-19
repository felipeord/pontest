from fastapi import FastAPI, Depends
from sqlalchemy.orm.exc import NoResultFound
from ehandler import Route, handler, MsgSpecResponse, http_client
from app.routes import call_center_sim
from app.config.settings import get_settings, Settings

# create app

app = FastAPI(
    title=get_settings().PROJECT_NAME,
    version=get_settings().PROJECT_VERSION,
    openapi_url="/api/v1/openapi.json",
    default_response_class=MsgSpecResponse,
    lifespan=http_client.lifespan,
)

app.router.route_class = Route
handler.handlers += [(ValueError, 400), (NoResultFound, 404)]

app.include_router(call_center_sim.router)
