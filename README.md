# 📰 Korean News Insight System (with RSS + FastAPI + Vector DB)

한글 뉴스 데이터를 안정적으로 수집하고 AI 기반 분석을 위한 백엔드 프로젝트입니다. 크롤링 대신 **RSS Feed 기반 수집 방식**으로 전환하여 안정성과 유지보수성을 확보했습니다.

---

## 📌 목표
- 한글 뉴스 데이터를 **RSS Feed**로 주기적으로 수집
- 수집된 기사 내용을 **벡터 DB에 임베딩**하여 검색/추천/분석 가능하도록 처리
- **FastAPI**를 통해 프론트엔드나 외부 서비스에 API 제공
- Docker 기반으로 모든 구성 요소를 컨테이너화하여 배포 및 유지 관리 간편화

---

## 🧱 기술 스택
- **언어**: Python 3.11
- **백엔드**: FastAPI
- **데이터 수집**: `feedparser` (RSS 기반)
- **벡터 저장소**: FAISS or Weaviate (선택 가능)
- **DB (옵션)**: SQLite / PostgreSQL
- **배포**: Docker

---

## 📂 프로젝트 구조

```
📁 project-root/
├── main.py                  # 엔트리포인트
├── feeds.yaml               # 구독할 RSS 목록 정의
├── collector.py             # RSS 수집기
├── vector_store.py          # 임베딩 및 벡터 DB 저장
├── api/
│   └── app.py               # FastAPI 서버
├── output/
│   ├── articles.json        # 수집된 기사 저장 위치
│   └── debug/               # 원본 HTML 등 디버깅 용도
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧪 실행 방법

### 1. RSS 수집기 실행 (로컬)
```bash
python collector.py
```

### 2. Docker로 실행
```bash
docker build -t rss-collector .
docker run --rm -v $(pwd)/output:/app/output rss-collector
```

### 3. FastAPI 실행
```bash
cd api
uvicorn app:app --reload
```


---

## 🔄 자동 수집 구성 (선택 사항)

### ⏰ 방법 1. crontab (Docker 기반)
```cron
0 * * * * docker run --rm -v /your/host/output:/app/output rss-collector
```

### ⚙️ 방법 2. FastAPI 내 BackgroundTask
```python
@app.on_event("startup")
@repeat_every(seconds=3600)
def fetch_rss_periodically():
    fetch_and_store_articles()
```

---

## 📰 수집 대상 (예시)

```yaml
feeds:
  - name: etnews
    url: https://rss.etnews.com/ETnews.xml
  - name: hankyoreh
    url: https://www.hani.co.kr/rss/
  - name: yonhap
    url: http://www.yonhapnewstv.co.kr/browse/rss
  - name: edaily
    url: http://rss.edaily.co.kr/edaily.xml
  - name: seoul
    url: http://www.seoul.co.kr/rss/
  - name: kbs
    url: https://news.kbs.co.kr/rss/rss.xml
```

---

## 📦 향후 계획
- [ ] RSS 수집 시 중복 기사 필터링
- [ ] 기사 요약 및 임베딩 자동화
- [ ] 벡터 DB 연동 및 유사 기사 추천 API
- [ ] 뉴스 관심사 기반 개인화 시스템 추가

---

## 🙋‍♂️ 기여 및 커뮤니케이션
본 프로젝트는 실험적인 사이드 프로젝트입니다. 협업 또는 아이디어 제안은 언제든지 환영합니다!
