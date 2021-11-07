from typing import Optional
from .database import engine
from fastapi import FastAPI
from . import models 
from fastapi.middleware.cors import CORSMiddleware
from .routers import list
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello Worldj"}
app.include_router(list.router)


