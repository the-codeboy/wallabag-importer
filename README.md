
# Wallabag RSS Feed Importer

A Python tool that automatically imports RSS/Atom feed entries into your Wallabag instance. This tool fetches articles from configured RSS feeds and adds them to Wallabag with optional tagging support.

## Features

- 📰 Import articles from multiple RSS/Atom feeds
- 🏷️ Automatic tagging of imported articles per feed
- 🔐 OAuth2 authentication with Wallabag
- ⚙️ JSON-based configuration

## Prerequisites

- Python 3.13 or higher
- A Wallabag instance (self-hosted or cloud)
- Wallabag API credentials

## Installation

1. Clone this repository:

```bash
git clone https://github.com/the-codeboy/wallabag-importer
cd wallabag-importer
```

2. Install dependencies using uv (recommended) or pip:

```bash
# Using uv
uv sync

# Or using pip
pip install -r requirements.txt
```

## Configuration

1. Copy the example configuration file:

```bash
cp config.example.json config.json
```

2. Edit `config.json` with your Wallabag instance details and RSS feeds:

```json
{
    "wallabag": {
        "url": "https://your-wallabag-instance.com/",
        "client-id": "your-client-id",
        "client-secret": "your-client-secret",
        "username": "your-username",
        "password": "your-password"
    },
    "feeds": [
        {
            "url": "https://example.com/feed.xml",
            "tags": ["example", "news"]
        }
    ]
}
```

### Getting Wallabag API Credentials

1. Log into your Wallabag instance
2. Go to `Config` → `API clients management`
3. Create a new client to get your `client-id` and `client-secret`
4. Use your regular Wallabag username and password

## Usage

Run the importer:

```bash
python main.py
```

The script will:

1. Authenticate with your Wallabag instance
2. Fetch entries from all configured RSS feeds
3. Add new articles to Wallabag with the specified tags

## Configuration Options

### Wallabag Configuration

- `url`: Your Wallabag instance URL (must end with `/`)
- `client-id`: OAuth client ID from Wallabag
- `client-secret`: OAuth client secret from Wallabag
- `username`: Your Wallabag username
- `password`: Your Wallabag password

### Feed Configuration

Each feed in the `feeds` array can have:

- `url`: RSS/Atom feed URL
- `tags`: Array of tags to apply to articles from this feed (optional)

## License

MIT License

Copyright (c) 2025 the-codeboy

Permission is hereby granted, free of charge, to any person obtaining a copy

of this software and associated documentation files (the "Software"), to deal

in the Software without restriction, including without limitation the rights

to use, copy, modify, merge, publish, distribute, sublicense, and/or sell

copies of the Software, and to permit persons to whom the Software is

furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all

copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,

OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

SOFTWARE.
