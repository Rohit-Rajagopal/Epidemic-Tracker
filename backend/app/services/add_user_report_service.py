import json
from pathlib import Path
from backend.app.database import get_db
from backend.app.models import Countries, Locations
from sqlalchemy import select
from backend.app.services.dbscan_service import find_clusters

db = next(get_db())


def get_file_path_from_data(file_name):
    file_path = Path(__file__).resolve().parents[2] / "data" / file_name
    return file_path


def setup_iso():
    d = {}
    data = db.execute(select(Countries)).scalars()
    for country in data:
        d[country.COUNTRY.lower()] = country.ISO
    return d


def add_to_entries_by_location(area, country, news, url, iso):
    with open(get_file_path_from_data("entries_by_location.json"), 'r', encoding="utf-8") as file:
        data = json.load(file)

    c_flag = True
    a_flag = True

    for a in data["areas"]:
        if a["area"].lower() == area.lower():
            a_flag = False
            a["entries"].append({
                "title": news,
                "url": url,
            })
        elif a["area"].lower() == country.lower():
            c_flag = False
            a["entries"].append({
                "title": news,
                "url": url,
            })

    if a_flag:
        query = select(Locations).where(Locations.name.ilike(area)).where(Locations.country_code == iso)
        area_extracted = db.execute(query).scalars().first()
        if not area_extracted:
            return False
        area_coords = [area_extracted.latitude, area_extracted.longitude]

        data["areas"].append({
            "area": area,
            "coordinates": area_coords,
            "entries": [
                {
                    "title": news,
                    "url": url
                }
            ]
        })

    if c_flag:
        country_extracted = db.execute(select(Countries).where(Countries.COUNTRY.ilike(country))).scalars().first()
        country_coords = [country_extracted.latitude, country_extracted.longitude]

        data["areas"].append({
            "area": country,
            "coordinates": country_coords,
            "entries": [
                {
                    "title": news,
                    "url": url
                }
            ]
        })

    with open(get_file_path_from_data("entries_by_location.json"), 'w', encoding="utf-8") as file:
        json.dump(data, file)

    return True


def add_to_coords(area, country, news, url, iso):
    query = select(Locations).where(Locations.name.ilike(area)).where(Locations.country_code == iso)
    area_extracted = db.execute(query).scalars().first()
    if not area_extracted:
        return False
    area_coords = [area_extracted.latitude, area_extracted.longitude]

    country_extracted = db.execute(select(Countries).where(Countries.COUNTRY.ilike(country))).scalars().first()
    country_coords = [country_extracted.latitude, country_extracted.longitude]

    if not country_extracted:
        return False

    with open(get_file_path_from_data("coords.json"), 'r', encoding="utf-8") as file:
        data = json.load(file)

    data["entries"].append({
        "title": news,
        "url": url,
        "countries": {
            country: country_coords
        },
        "areas": {
            area: area_coords
        }
    })

    with open(get_file_path_from_data("coords.json"), 'w', encoding="utf-8") as file:
        json.dump(data, file)

    return True


def add_report(area, country, news, url):
    country_iso = setup_iso()

    if country.lower() in country_iso:
        iso = country_iso[country.lower()]
    else:
        return False

    f1 = add_to_entries_by_location(area, country, news, url, iso)
    f2 = add_to_coords(area, country, news, url, iso)

    find_clusters("coords.json", "clusters.json")

    return f1 and f2