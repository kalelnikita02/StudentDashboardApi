from fastapi import FastAPI
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from src.Route.allroutes import router as all_routes
# from prometheus_client import start_http_server
# from os import getenv
# from _thread import start_new_thread
# from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Student Data Portal API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(all_routes)


if __name__ == '__main__':
    logger.info("Started main")
    # start_http_server(int(getenv("PROM_METRICS_PORT")))
    run("main:app", host="0.0.0.0", port=8085, reload=True)