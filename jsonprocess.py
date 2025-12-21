import json

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


# Mode Processes

# Write/Add Object To .json File
def write_json(push, file_path):
    file_data = load_process(file_path)

    file_data.append(push)

    save_process(file_path, file_data)


# Remode/Delete Object From .json File
def remove_json(file_path, search_value, search_mode):
    key_map = {
        "id": "obj_id",
        "name": "obj_name"
    }

    json_key = key_map.get(search_mode)
    if not json_key:
        return -1  # invalid Search Term

    file_data = load_process(file_path)

    updated_data = [
        obj for obj in file_data
        if obj.get(json_key) != search_value
    ]

    save_process(file_path, updated_data)
    
    return 0  # Successful Deletion