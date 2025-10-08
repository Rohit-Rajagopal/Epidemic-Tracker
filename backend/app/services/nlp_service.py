import spacy
import json
from backend.app.database import get_db
from backend.app.models import Countries, Locations
from sqlalchemy import select
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
nlp = spacy.load("en_core_web_lg")
db = next(get_db())


def setup():
    logging.info('Setup start')
    logging.info('Extracting location names')
    data = db.execute(select(Locations.name).distinct()).scalars()
    logging.info('Location names extracted')
    name_data = [x.lower() for x in data if x]
    set1 = set(name_data)
    logging.info('Extracting country names')
    data = db.execute(select(Countries.COUNTRY)).scalars()
    logging.info('Country names extracted')
    country_data = [x.lower() for x in data]
    set2 = set(country_data)
    logging.info('Setup end')
    return set1.union(set2), set2


def setup_iso():
    logging.info('Country iso setup start')
    d = {}
    data = db.execute(select(Countries)).scalars()
    for country in data:
        d[country.COUNTRY.lower()] = country.ISO
    logging.info('Country iso setup end')
    return d


name_set, country_set = setup()
country_iso = setup_iso()


def extract_locations(text, origin):
    doc = nlp(text)
    locations = []
    prev = None
    for word in doc:
        if word.ent_type_ == "GPE":
            if prev and prev.ent_type_ == "GPE":
                locations[-1] += ' ' + word.text
            else:
                locations.append(word.text)
        elif word.ent_type_ == "ORG" and word in name_set:
            locations.append(word.text)
        elif word.ent_type_ == "NORP" and word in name_set:
            locations.append(word.text)
        prev = word
    countries = []
    areas = []
    for area in locations:
        if area.lower() in country_set:
            countries.append(country_iso[area.lower()])
        else:
            areas.append(area)
    if not countries and origin != '':
        countries.append(country_iso[origin.lower()])
    return countries, areas


def get_locations():
    logging.info('NLP start')

    with open("../../data/gdelt.json", 'r') as file:
        data = json.load(file)

    res = []
    i = 1
    for entry in data['entries']:
        logging.info(f'Processing entry {i}')
        countries, areas = extract_locations(entry['title'], entry['country'])
        d = {
            'title': entry['title'],
            'url': entry['url'],
            'countries': countries,
            'areas': areas,
        }
        res.append(d)
        i += 1

    js = {'entries': res}

    with open("../../data/nlp.json", 'w', encoding='utf-8') as file:
        json.dump(js, file)

    logging.info('NLP end')


if __name__ == "__main__":
    get_locations()