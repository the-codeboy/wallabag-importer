import json


def load_config():
    with open("config.json") as f:
        d = json.load(f)
        return d
