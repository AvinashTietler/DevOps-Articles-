import feedparser

FEED_URL = "https://medium.com/feed/@devopsdiariesinfo"
OUTPUT_FILE = "medium-articles.md"

feed = feedparser.parse(FEED_URL)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# 📝 My Medium Articles\n\n")
    for entry in feed.entries:
        f.write(f"- [{entry.title}]({entry.link})\n")
