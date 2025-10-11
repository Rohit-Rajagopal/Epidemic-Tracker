import json
from sqlalchemy import select, func
from backend.app.database import get_db
from backend.app.models import Countries, Locations
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
db = next(get_db())


def get_coords(countries, areas):
    logging.info('Fetching country coordinates')
    country_coords = {}
    for country in countries:
        query = select(Countries).where(Countries.ISO == country)
        coords = db.execute(query).scalars().one()
        country_coords[coords.COUNTRY] = (coords.latitude, coords.longitude)
    logging.info('Fetching area coordinates')
    area_coords = {}
    for area in areas:
        query = select(Locations).where(Locations.name.ilike(area))
        coords = db.execute(query).scalars().all()
        lat, lon = 0, 0
        if not coords:
            continue
        elif len(coords) == 1:
            lat = coords[0].latitude
            lon = coords[0].longitude
        else:
            for coord in coords:
                if coord.country_code in countries:
                    lat = coord.latitude
                    lon = coord.longitude
                    break
        area_coords[area] = (lat, lon)
    return country_coords, area_coords


def generate_coords():
    logging.info('Starting coordinates retrieval process')

    with open('../../data/nlp2.json', 'r') as file:
        data = json.load(file)

    res = []
    i = 1

    for entry in data['entries']:
        logging.info(f'Processing entry {i}')
        countries, areas = get_coords(entry['countries'], entry['areas'])

        d = {
            'title': entry['title'],
            'url': entry['url'],
            'countries': countries,
            'areas': areas
        }

        res.append(d)
        i += 1

    js = {'entries': res}

    with open('../../data/coords2.json', 'w', encoding='utf-8') as file:
        json.dump(js, file)

    logging.info('Coordinates retrieval process complete')


if __name__ == "__main__":
    generate_coords()