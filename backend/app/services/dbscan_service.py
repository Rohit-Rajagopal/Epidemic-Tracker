import json
import numpy as np
from sklearn.cluster import DBSCAN
from collections import defaultdict
from pathlib import Path


def get_file_path_from_data(file_name):
    file_path = Path(__file__).resolve().parents[2] / "data" / file_name
    return file_path


def get_labels(coords):
    coords_rad = np.radians(coords)

    eps_meters = 5000  # 5 km starting point
    earth_radius = 6371000.0
    eps_radians = eps_meters / earth_radius

    min_samples = 15

    db = DBSCAN(eps=eps_radians, min_samples=min_samples, metric='haversine')
    db.fit(coords_rad)
    labels = db.labels_
    return labels


def find_clusters(input_file="coords2.json", output_file="clusters2.json"):
    with open(get_file_path_from_data(input_file), 'r') as file:
        data = json.load(file)

    coords = []
    for entry in data['entries']:
        # for value in entry['countries'].values():
        #     if value[0] == 0 and value[1] == 0:
        #         continue
        #     coords.append(value)
        for value in entry['areas'].values():
            if value[0] == 0 and value[1] == 0:
                continue
            coords.append(value)
    np_coords = np.array(coords)

    labels = get_labels(np_coords)

    d = defaultdict(list)
    for i in range(len(coords)):
        d[int(labels[i])].append(coords[i])

    with open(get_file_path_from_data(output_file), 'w') as file:
        json.dump(d, file)


if __name__ == "__main__":
    find_clusters()