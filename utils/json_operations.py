import json


def read_from_json(file, default = {}):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File not found")
        return default
    except json.JSONDecodeError:
        print("Empty or invalid JSON file")
        return default


def write_to_json(file, data, mode="w"):
    with open(file, mode, encoding="utf-8") as f:
        f.write("\n")
        json.dump(data, f, ensure_ascii=False, indent=2)
