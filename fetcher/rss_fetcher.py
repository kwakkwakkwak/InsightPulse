import feedparser
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import time

RSS_FEEDS = [
    "https://www.hani.co.kr/rss/",
    "https://rss.donga.com/rss/news.xml",
    "https://www.chosun.com/arc/outboundfeeds/rss/?outputType=xml",
]

TOPIC_NAME = "rss-topic"

def fetch_rss_articles(limit=5):
    articles = []
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:limit]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")
            })
    return articles


# Kafka 연결 재시도 (최대 10번, 5초 간격)
producer = None
for attempt in range(10):
    try:
        producer = KafkaProducer(
            bootstrap_servers="kafka:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            retries=5,
        )
        print("✅ Kafka 연결 성공")
        break
    except NoBrokersAvailable:
        print(f"❌ Kafka 브로커 연결 실패 (시도 {attempt + 1}/10). 5초 후 재시도...")
        time.sleep(5)

if not producer:
    raise RuntimeError("Kafka 브로커에 연결할 수 없습니다.")


if __name__ == "__main__":
    articles = fetch_rss_articles(limit=5)
    for article in articles:
        producer.send(TOPIC_NAME, article)
        print(f"[✓] Sent article: {article['title']}")
    producer.flush()
    print(f"[✓] {len(articles)}개 기사 전송 완료.")
