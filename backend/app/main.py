from backend.app.database import Base, engine
from backend.app import models
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers import locations, clusters

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Epidemic Mapping System")

origins = [
    "http://localhost:3000",        # React dev server
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8080",
    "https://optionally-resolved-cicada.ngrok-free.app",  # replace with your real ngrok URL
    "null"  # if loading frontend directly from file://
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(locations.router)
app.include_router(clusters.router)


@app.get('/')
def home():
    return {'hello': 'world'}