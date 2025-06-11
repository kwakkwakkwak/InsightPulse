from kafka import KafkaConsumer
import json

# Kafka에서 "news-articles" 토픽을 구독
consumer = KafkaConsumer(
    "news-articles",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="news-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("[✓] Kafka Consumer is listening...")

for message in consumer:
    article = message.value
    print("[+] Received article:", article["title"])
