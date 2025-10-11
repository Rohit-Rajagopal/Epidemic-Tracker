from collections import defaultdict
import json


def sort_entries_by_location():

    with open('../../data/coords2.json', 'r') as file:
        data = json.load(file)

    area_coords = defaultdict(list)
    area_entries = defaultdict(list)
    v = set()

    for entry in data['entries']:
        for country, coords in entry['countries'].items():
            if country not in v:
                v.add(country)
                area_coords[country] = coords
            area_entries[country].append({
                'title': entry['title'],
                'url': entry['url'],
            })
        for area, coords in entry['areas'].items():
            if area not in v:
                v.add(area)
                area_coords[area] = coords
            area_entries[area].append({
                'title': entry['title'],
                'url': entry['url'],
            })

        res = []
        for area, entries in area_entries.items():
            d = {
                'area': area,
                'coordinates': area_coords[area],
                'entries': entries
            }
            res.append(d)

        js = {'areas': res}

        with open('../../data/entries_by_location2.json', 'w') as file:
            json.dump(js, file)


if __name__ == "__main__":
    sort_entries_by_location()