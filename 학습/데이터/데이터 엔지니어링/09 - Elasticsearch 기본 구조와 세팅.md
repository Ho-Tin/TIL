
---

# 🔍 Elasticsearch 설치 및 기본 개념 정리

## 1. Elasticsearch 개요

* **정의**: Apache Lucene 기반의 강력한 오픈소스 분산 검색 및 분석 엔진입니다.
* **특징**:
* **분산 구조**: 데이터를 여러 노드에 분산 저장하여 대량의 데이터를 실시간으로 처리합니다.
* **전문 검색(Full-Text Search)**: 단순 일치 검색을 넘어선 복잡한 검색을 지원합니다.
* **확장성**: 수백 대의 서버로 수평적 확장이 가능합니다.
* **유연성**: 스키마리스(Schemaless) 구조로 JSON 형태의 비정형 데이터를 자유롭게 저장합니다.



## 2. 아키텍처 및 분산 처리

* **클러스터(Cluster)**: 하나 이상의 노드 집합으로, 데이터를 공동으로 관리합니다.
* **노드(Node)**: 클러스터의 개별 인스턴스입니다.
* **마스터 노드**: 클러스터 상태 관리 및 노드 추가/제거 담당.
* **데이터 노드**: 실제 데이터 저장 및 CRUD, 검색, 집계 작업 수행.
* **코디네이팅 노드**: 사용자 요청을 라우팅하고 결과를 취합.


* **샤드(Shard) & 레플리카(Replica)**:
* **Shard**: 인덱스를 나눈 단위로 물리적 저장 공간입니다.
* **Replica**: 샤드의 복사본으로, 데이터 안정성과 읽기 성능을 높입니다.



---

## 3. 환경 구성 (Docker Compose)

Elasticsearch를 안정적으로 실행하기 위한 `docker-compose.yml` 설정 예시입니다.

```yaml
version: '2.2'
services:
  es01:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.10.1
    container_name: es01
    environment:
      - node.name=es01
      - cluster.name=elastic-docker-cluster
      - discovery.seed_hosts=es02,es03
      - cluster.initial_master_nodes=es01,es02,es03
      - bootstrap.memory_lock=true
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - data01:/usr/share/elasticsearch/data
    ports:
      - 9200:9200
    networks:
      - elastic

  # (es02, es03 노드 설정도 유사한 방식으로 추가 가능)

networks:
  elastic:
    driver: bridge

volumes:
  data01:
    driver: local

```

---

## 4. REST API 및 Document CRUD

Elasticsearch는 RESTful API를 통해 데이터를 관리합니다.

### 4.1 인덱스 생성 및 도큐먼트 삽입

파이썬 클라이언트를 사용한 예시 코드입니다.

```python
from elasticsearch import Elasticsearch

# 클라이언트 연결
es = Elasticsearch("http://localhost:9200")

# 도큐먼트 데이터 정의
doc = {
    "name": "Samsung Galaxy S24 Ultra",
    "brand": "Samsung",
    "price": 1199.99,
    "category": "smartphone",
    "rating": 4.8
}

# 인덱스 생성 및 데이터 삽입 (ID: 1001)
response = es.index(index="products", id="1001", document=doc)
print(response)

```

### 4.2 도큐먼트 업데이트 (Update)

기존 데이터의 특정 필드만 수정하는 방법입니다.

```python
# 업데이트할 내용
update_body = {
    "doc": {
        "price": 1099
    }
}

# 도큐먼트 업데이트 수행
response = es.update(index="products", id="1001", body=update_body)
print(response)

```

### 4.3 Upsert (Update + Insert)

데이터가 있으면 업데이트하고, 없으면 새로 삽입하는 연산입니다.

```python
# Upsert를 위한 데이터
upsert_body = {
    "doc": {
        "price": 1099,
        "stock": 150
    },
    "doc_as_upsert": True
}

# Upsert 수행
response = es.update(index="products", id="1001", body=upsert_body)
print(response)

```

---

## 💡 구현 시 참고사항

* **Immutability**: Elasticsearch의 세그먼트(Segment)는 한 번 생성되면 수정되지 않습니다. 업데이트 시 내부적으로는 이전 문서를 '삭제됨' 표시하고 새 문서를 생성합니다.
* **Refresh**: 기본적으로 1초마다 Refresh가 발생하여 데이터가 검색 가능해집니다.
* **NRT(Near Real-Time)**: 위와 같은 구조 덕분에 거의 실시간(약 1초 내외)으로 검색 결과를 확인할 수 있습니다.

---
