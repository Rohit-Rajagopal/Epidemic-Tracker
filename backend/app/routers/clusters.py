from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(prefix='/clusters')


@router.get('/')
def get_clusters():
    file_path = Path(__file__).resolve().parents[2] / "data" / "clusters2.json"
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data