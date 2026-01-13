import os
import json

from data import Info

# Routine Processes

# File .json Load Process
def load_process(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# File .json Save Process
def save_process(file_path, file_data):
    with open(file_path, "w") as file:
        json.dump(file_data, file, indent=4)


# Databases Folder Initiate
def create_default_database():
    if not os.path.exists(Info.folder_path):
        os.makedirs(Info.folder_path)
        MsgMode = "notice-default-database-created"

# Mode Processes

# Create Default Parameters For .json File
def create_json_parameters(file_path):
    with open(file_path, 'w') as json_file:
            json.dump([], json_file)


# Write/Add Object To .json File
def write_json(push, file_path):
    file_data = load_process(file_path)

    file_data.append(push)

    save_process(file_path, file_data)


# Remove/Delete Object From .json File
def remove_json(file_path, search_value, search_mode):
    exists = validate_name_id_json(file_path, search_value, search_mode)

    if not exists:
        return -1

    # Load file and remove object
    file_data = load_process(file_path)

    updated_data = [
        obj for obj in file_data
        if str(obj.get("obj_id") if search_mode == "id" else obj.get("obj_name")) != str(search_value)
    ]

    save_process(file_path, updated_data)
    return 0  # success



# Fetch data and return it
def view_json(file_path, search_value, search_mode):
    key_map = {
        "id": "obj_id",
        "name": "obj_name"
    }

    json_key = key_map.get(search_mode)
    if not json_key:
        return 0

    file_data = load_process(file_path)

    for obj in file_data:
        if obj.get(json_key) == search_value:
            return obj

    return 0


# Validate Name/ID availability
def validate_name_id_json(file_path, search_value, search_mode):
    key_map = {
        "id": "obj_id",
        "name": "obj_name"
    }

    json_key = key_map[search_mode]  # safe: always correct
    file_data = load_process(file_path)

    search_value = str(search_value).strip()

    return any(
        str(obj.get(json_key)) == search_value
        for obj in file_data
        if isinstance(obj, dict)
    )