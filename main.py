import feedparser
from config import load_config
from api import get_token, add_entry


def main():
    config = load_config()
    token = get_token(config)
    feeds = config["feeds"]

    for feed in feeds:
        try:
            f = feedparser.parse(feed["url"])
            for entry in f["entries"]:
                add_entry(
                    config, entry["link"], token, feed["tags"] if "tags" in feed else None
                )
            print(f"added {len(f['entries'])} articles from feed {feed['url']}")
        except Exception:
            print(f"failed to add entries for feed {feed['url']}")


if __name__ == "__main__":
    main()
