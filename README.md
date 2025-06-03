# InsightPulse

**InsightPulse**는 IT 뉴스를 실시간으로 크롤링하고, AI를 통해 요약/키워드 추출을 수행하여 사용자에게 개인화된 뉴스 피드를 제공하는 플랫폼입니다. 모든 백엔드는 **FastAPI** 기반으로 통합되며, Kafka를 통한 비동기 메시징으로 처리됩니다.

---

## 🚀 프로젝트 개요

- 뉴스 크롤링 → Kafka → AI 요약/분석 → MySQL 저장 → FastAPI API → React 프론트
- Kafka 기반 비동기 처리 아키텍처 학습
- KoBART 기반 텍스트 요약 + 키워드 추출 AI 실습
- AWS 배포까지 포함한 실전 프로젝트

---

## 🧱 기술 스택

| 구성 요소 | 기술 |
|-----------|------|
| 백엔드 API | **Python + FastAPI** |
| 크롤러 | Python (`requests`, `BeautifulSoup`) |
| 메시징 | Apache Kafka |
| AI 요약/키워드 | Huggingface Transformers, KeyBERT |
| 데이터베이스 | MySQL |
| 프론트엔드 | React.js |
| 배포 | AWS EC2, RDS, Docker, S3 |

---

## ⚙️ 시스템 구성도

