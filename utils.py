import json
import csv

def save_to_json(movies, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(movies, json_file, indent=4)

def save_to_csv(movies, file_name):
    if not movies:
        print("No movies found to save.")
        return

    keys = movies[0].keys()
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, keys)
        writer.writeheader()
        writer.writerows(movies)