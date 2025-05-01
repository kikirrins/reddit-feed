# Reddit Ticker Mentions Tracker

A Python tool to search for stock ticker mentions on Reddit investment subreddits.

## Overview

This application searches popular investment subreddits (wallstreetbets, stocks, investing) for mentions of specific stock tickers. It retrieves posts containing the ticker symbol, sorts them by score, and displays the top posts along with their comments.

## Features

- Search for ticker symbols across multiple subreddits
- Filter results by time period (hour, day, week, month, year)
- Sort posts by popularity
- View top comments from each post
- Customizable search parameters

## Requirements

- Python 3.6+
- praw (Python Reddit API Wrapper)

## Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install praw
   ```

## Environment Variables

Set up the following environment variables:

- `REDDIT_CLIENT_ID` - Your Reddit API client ID
- `REDDIT_CLIENT_SECRET` - Your Reddit API client secret
- `REDDIT_USER_AGENT` - User agent string for Reddit API

## Usage

```python
# Example: Search for NVDA ticker mentions
python main.py
```

You can modify the search query in `main.py`:
```python
# Search for posts containing ticker
q = 'title:$NVDA'  # Change to your desired ticker
```

## Functions

### `search_ticker_mentions()`
Searches for ticker mentions across specified subreddits.

### `get_post_comments()`
Retrieves comments from a specific Reddit post.

## License

MIT
