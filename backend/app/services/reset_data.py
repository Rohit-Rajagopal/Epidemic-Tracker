import json
from pathlib import Path


def get_file_path_from_data(file_name):
    file_path = Path(__file__).resolve().parents[2] / "data" / file_name
    return file_path


def reset_data():
    # nlp.json
    with open(get_file_path_from_data("nlp2.json"), 'r') as file:
        data = json.load(file)

    with open(get_file_path_from_data("nlp.json"), 'w') as file:
        json.dump(data, file)

    # coords.json
    with open(get_file_path_from_data("coords2.json"), 'r') as file:
        data = json.load(file)

    with open(get_file_path_from_data("coords.json"), 'w') as file:
        json.dump(data, file)

    # clusters.json
    with open(get_file_path_from_data("clusters2.json"), 'r') as file:
        data = json.load(file)

    with open(get_file_path_from_data("clusters.json"), 'w') as file:
        json.dump(data, file)

    # entries_by_location.json
    with open(get_file_path_from_data("entries_by_location2.json"), 'r') as file:
        data = json.load(file)

    with open(get_file_path_from_data("entries_by_location.json"), 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    reset_data()