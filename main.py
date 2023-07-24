import uvicorn
from fastapi import FastAPI
from database import SessionLocal,engine,Base
from models.router import router

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(router,prefix='/user')