from fastapi import FastAPI, Request, Response
from app.database import SessionLocal
from app.config import URL_PREFIX

from fastapi.middleware.cors import CORSMiddleware
from app.router import api_router

app = FastAPI(
    title="WebApp",
    description="Web Application RESTful API",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@ app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)

    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(api_router)
