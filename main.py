import feedparser
from config import load_config
from api import get_token, add_entry


def main():
    config = load_config()
    token = get_token(config)
    feeds = config["feeds"]

    add_entry(config, "https://the-codeboy.com", token)

    for feed in feeds:
        f = feedparser.parse(feed["url"])
        for entry in f["entries"]:
            add_entry(
                config, entry["link"], token, feed["tags"] if "tags" in feed else None
            )


if __name__ == "__main__":
    main()
