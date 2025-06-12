import json

def load_law_mapping(mapping_path="laws/law_mapping.json"):
    try:
        with open(mapping_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("[X] Law mapping file not found.")
        return {}

def map_breaches_to_laws(breach_types, law_data):
    legal_actions = {}

    for breach in breach_types:
        if breach in law_data:
            legal_actions[breach] = law_data[breach]
        else:
            legal_actions[breach] = {"Info": "No specific legal action mapped."}

    return legal_actions

