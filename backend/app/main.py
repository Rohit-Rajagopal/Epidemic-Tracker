from backend.app.database import Base, engine
from backend.app import models
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI()

