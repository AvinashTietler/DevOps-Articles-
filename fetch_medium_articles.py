import feedparser
from datetime import datetime

FEED_URL = "https://medium.com/feed/@devopsdiariesinfo"
OUTPUT_FILE = "medium-articles.md"

def fetch_and_write_articles():
    try:
        feed = feedparser.parse(FEED_URL)
        if not feed.entries:
            print("No articles found. Check feed URL or network connectivity.")
            return

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("# 📝 My Medium Articles\n\n")
            f.write(f"_Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')}_\n\n")
            for entry in feed.entries:
                f.write(f"- [{entry.title}]({entry.link})\n")

        print(f"Successfully updated {OUTPUT_FILE} with {len(feed.entries)} articles.")

    except Exception as e:
        print(f"Error fetching Medium articles: {e}")

if __name__ == "__main__":
    fetch_and_write_articles()
