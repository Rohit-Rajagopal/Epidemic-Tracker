from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(prefix='/locations')


@router.get('/')
def get_locations():
    file_path = Path(__file__).resolve().parents[2] / "data" / "coords2.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


@router.get('/entries_by_location')
def get_entries_by_location():
    file_path = Path(__file__).resolve().parents[2] / "data" / "entries_by_location2.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data