# Django ORM & QuerySet API 정리

## 1. ORM(Object Relational Mapping)

- **정의**  
  ORM은 **객체 지향 프로그래밍 언어**를 이용해 **데이터베이스의 데이터를 객체 형태로 다룰 수 있도록 해주는 기술**이다.  
  즉, 프로그래머는 SQL을 직접 작성하지 않고, 클래스와 객체를 이용해 데이터베이스 조작이 가능하다.

- **특징**
  - 데이터베이스 **테이블 ↔ 클래스**, **행(Row) ↔ 인스턴스 객체**, **열(Column) ↔ 속성(Attribute)** 으로 매핑된다.
  - 사용 언어와 데이터베이스 간의 호환 문제를 줄여준다.
  - 장점: 코드의 재사용성 증가, 유지보수 용이, 안전성(ORM이 SQL 인젝션 방지).
  - 단점: 복잡한 쿼리 작성 시 퍼포먼스 저하 가능 → 직접 SQL 문을 작성해야 하는 경우도 있음.

- **언어별 ORM 예시**  
  - Python : Django ORM, SQLAlchemy  
  - Java : Hibernate  
  - Ruby : ActiveRecord  

***

## 2. Django QuerySet API

- **정의**  
  Django ORM에서 데이터베이스의 객체들을 **검색, 필터링, 정렬 및 그룹화** 하기 위해 제공되는 API.  
  ORM을 통해 데이터베이스와 소통할 때 핵심적으로 사용한다.

- **동작 방식**
  1. 개발자가 ORM 코드 작성 (예: `Article.objects.all()`)
  2. ORM이 SQL 쿼리로 변환 후 DB에 전달
  3. DB가 결과 반환
  4. ORM이 `QuerySet` 객체 형태로 변환하여 반환

***

## 3. QuerySet & Query

- **Query**
  - 데이터베이스에 특정 데이터를 요청하는 것.
  - SQL 대신 Python 문법으로 작성 가능 → 내부적으로 SQL 변환 후 실행.

- **QuerySet**
  - 데이터베이스로부터 전달받은 객체 모음(리스트처럼 동작).
  - 체이닝 기법 사용 가능 (`.filter()`, `.order_by()` 등 연속 호출).

***

## 4. CRUD(생성, 조회, 수정, 삭제)

### 4.1 Create (생성)
```python
# 방법 1 (인스턴스 생성 후 저장)
article = Article()
article.title = 'first'
article.save()

# 방법 2 (편의 메서드 사용)
Article.objects.create(title="123")
```

***

### 4.2 Read (조회)
```python
# 전체 조회 (QuerySet 반환)
Article.objects.all()

# 조건부 조회 (QuerySet 반환)
Article.objects.filter(title="first")

# 단일 객체 조회 (인스턴스 반환, 없거나 여러 개면 오류 발생)
Article.objects.get(id=1)
```

👉 `all()`, `filter()`는 QuerySet 반환 → 후속 작업 가능  
👉 `get()`은 인스턴스 반환 → 후속 체이닝 불가

***

### 4.3 Update (수정)
```python
# 인스턴스를 가져와서 수정 후 save()
article = Article.objects.get(id=1)
article.title = "byebye"
article.save()

# filter() + update() 활용
Article.objects.filter(title="first").update(title="byebye")
```

> ⚠️ `update()`는 QuerySet에 대해서만 가능.  
> `get()`은 인스턴스 반환이므로 `.update()` 사용 불가.

***

### 4.4 Delete (삭제)
```python
# 방법 1: 인스턴스 삭제
article = Article.objects.get(id=1)
article.delete()

# 방법 2: QuerySet 삭제
Article.objects.filter(title="byebye").delete()
```

***

## 5. Field Lookups

Django ORM에서 제공하는 조건문 문법.  
SQL의 `WHERE` 절에 해당.  

예시:
```python
# 특정 값과 일치하는 경우
Article.objects.filter(title__exact="first")

# 대소문자 구분 없는 비교
Article.objects.filter(title__iexact="First")

# 부분 문자열 검색 (LIKE)
Article.objects.filter(title__contains="fir")

# 시작 문자
Article.objects.filter(title__startswith="fi")

# 끝 문자
Article.objects.filter(title__endswith="st")

# 크기 비교
Article.objects.filter(id__gte=10)   # 10 이상
Article.objects.filter(id__lt=5)     # 5 미만
```

👉 [공식 문서 참고](https://docs.djangoproject.com/en/5.2/ref/models/querysets/)

***

## 6. Shell Plus 실습 환경 설정

```bash
pip install ipython
pip install django-extensions
```

- `settings.py`의 `INSTALLED_APPS`에 `'django_extensions'` 추가
- 실행:
```bash
python manage.py shell_plus
```

***

## 7. 정리

- ORM은 SQL을 직접 작성하지 않고 객체지향적으로 데이터베이스를 다루는 기술.  
- Django ORM은 `QuerySet API`를 이용해 CRUD를 수행한다.  
- `all()`, `filter()`는 QuerySet 반환 (체인 가능), `get()`은 단일 인스턴스 반환.  
- `Field lookups`을 활용하면 SQL의 WHERE 조건을 Pythonic하게 표현 가능.

***

📌 **추가 학습**
- QuerySet은 지연 평가(Lazy Evaluation) 방식 사용  
  → 실제 DB 조회는 데이터가 필요할 때 발생(`list()`, `for` loop 등).  
- 이를 활용해 성능 최적화 가능 (`select_related`, `prefetch_related` 등).  

***
