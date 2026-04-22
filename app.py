from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.database import start_database
from src.routes.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_database()
    print("INICIANDO APLICACION")
    yield
    print("APAGANDO APLICACION")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
