import json
import numpy as np
from sklearn.cluster import DBSCAN
from collections import defaultdict


def get_labels(coords):
    coords_rad = np.radians(coords)

    eps_meters = 5000  # 5 km starting point
    earth_radius = 6371000.0
    eps_radians = eps_meters / earth_radius

    min_samples = 5

    db = DBSCAN(eps=eps_radians, min_samples=min_samples, metric='haversine')
    db.fit(coords_rad)
    labels = db.labels_
    return labels


def find_clusters():
    with open('../../data/coords.json', 'r') as file:
        data = json.load(file)

    coords = []
    for entry in data['entries']:
        for value in entry['countries'].values():
            if value[0] == 0 and value[1] == 0:
                continue
            coords.append(value)
        for value in entry['areas'].values():
            if value[0] == 0 and value[1] == 0:
                continue
            coords.append(value)
    np_coords = np.array(coords)

    labels = get_labels(np_coords)

    d = defaultdict(list)
    for i in range(len(coords)):
        d[int(labels[i])].append(coords[i])

    with open('../../data/clusters.json', 'w') as file:
        json.dump(d, file)


if __name__ == "__main__":
    find_clusters()