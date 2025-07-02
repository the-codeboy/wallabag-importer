import requests


def get_token(config):
    config = config["wallabag"]
    url = config["url"]
    client_id = config["client-id"]
    client_secret = config["client-secret"]
    username = config["username"]
    password = config["password"]

    url = url + "oauth/v2/token"
    data = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password,
    }

    response = requests.post(url=url, data=data)

    return response.json()["access_token"]


def add_entry(config, entry, token, tags=None):
    config = config["wallabag"]
    url = config["url"] + "api/entries"

    headers = {"Authorization": "Bearer " + token}
    data = {"url": entry}
    if tags:
        data["tags"] = ",".join(tags)
    response = requests.post(url=url, data=data, headers=headers)
