import json
from kafka import KafkaProducer
import feedparser
from pathlib import Path
import yaml

# 중복 방지를 위한 저장소
stored_links = set()

# 이전에 저장된 링크 로딩 (옵션)
output_path = Path("output/articles.json")
if output_path.exists():
    with open(output_path, "r", encoding="utf-8") as f:
        try:
            stored_links = {article["link"] for article in json.load(f)}
        except:
            stored_links = set()

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# 피드 목록 로드
def load_feeds():
    with open("fetcher/feeds.yaml", "r") as f:
        feeds_yaml = yaml.safe_load(f)
    return feeds_yaml["feeds"]

# RSS 수집기 실행
def fetch_and_publish():
    new_articles = []
    for feed in load_feeds():
        parsed = feedparser.parse(feed["url"])
        for entry in parsed.entries:
            if entry.link in stored_links:
                continue
            article = {
                "source": feed["name"],
                "title": entry.title,
                "link": entry.link,
                "summary": entry.get("summary", ""),
                "published": entry.get("published", "")
            }
            producer.send("news-articles", article)
            new_articles.append(article)
            stored_links.add(entry.link)

    if new_articles:
        output_path.parent.mkdir(exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(new_articles, f, ensure_ascii=False, indent=2)
        print(f"[✓] {len(new_articles)} new articles sent to Kafka and saved to output/articles.json")
    else:
        print("[!] No new articles found.")

if __name__ == "__main__":
    fetch_and_publish()
