from backend.app.database import Base, engine
from backend.app import models
from fastapi import FastAPI
from backend.app.routers import locations

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Epidemic Mapping System")

app.include_router(locations.router)


@app.get('/')
def home():
    return {'hello': 'world'}