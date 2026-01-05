import os
import json

def load_json(path, default):
    "Load json data from a file"
    "If the file doesn't exist return the default"

    if not os.path.exists(path):
        return default

    with open(path, 'r') as file:
        try:
            file_json_data = json.load(file)
            return file_json_data

        except Exception as e:
            print("Error loading json data:", e)
            return default


def save_json(path, data):
    "Save json data to a file"

    folder_name = os.path.dirname(path)
    os.makedirs(folder_name, exist_ok = True)
    try:
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print("Error Saving the data: ",e)
