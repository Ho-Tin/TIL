# 250902
***

# Django 모델을 통한 DB 관리

## Model 개요
Django의 **Model**은 데이터베이스의 테이블 구조를 정의하고 데이터를 조작하는 기능을 제공합니다. 모델 클래스는 DB 테이블 설계에만 집중할 수 있게 해주며, 관련 기능은 이미 Django가 제공합니다.

```python
from django.db import models

class Article(models.Model):
    # 필드 정의
```
- 모든 모델 코드가 이미 작성되어 있으므로 **테이블 구조 설계**에 관한 코드만 작성하면 됩니다.

## 모델 필드(Fields)

### Field Type(필드 유형)
각 필드는 데이터의 종류와 저장 방식, 제약 조건을 명확하게 정의합니다.

- **CharField**: 제한된 길이의 문자열 저장(필수 옵션: `max_length`)
    ```python
    title = models.CharField(max_length=100)
    ```
- **TextField**: 길이 제한 없는 텍스트 저장(실제로 DB 엔진마다 제한 존재)
    ```python
    content = models.TextField()
    ```
- **숫자 필드**: `IntegerField`, `FloatField` 등
- **날짜/시간 필드**: `DateField`, `TimeField`, `DateTimeField`
- **파일 관련 필드**: `FileField`, `ImageField`

### Field Options(필드 옵션)
필드의 동작과 제약조건을 설정하여 데이터 규칙을 강제할 수 있습니다.

- **null**: DB에 `NULL` 값 허용 여부(기본값: False)
- **blank**: 폼에서 빈 값 허용 여부
- **default**: 기본값 설정
- **choices**: 선택 가능한 값 목록 정의
- **unique**: 값의 중복 허용 여부

예제:
```python
title = models.CharField(max_length=100, blank=True, default="제목 없음")
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

## Migrations(마이그레이션)
모델 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 반영하는 과정입니다.

- **makemigrations**: 모델 변경사항을 감지하여 migration 파일 생성
- **migrate**: DB에 실제로 변경사항 반영

### 자동 날짜/시간 필드 옵션
- **auto_now_add**: 객체 생성 시 현재 시간 자동 저장
- **auto_now**: 객체 저장(수정) 시마다 현재 시간 자동 갱신

권장: 날짜 필드에는 직접 입력보다 Django의 기본값(auto_now, auto_now_add) 옵션 사용

## 관리자(Admin site)
Django는 설치 및 설정만으로 강력한 관리자 인터페이스를 제공합니다.

1. **admin 계정 생성**  
    ```
    python manage.py createsuperuser
    ```
2. **DB에 생성된 admin 계정 확인**
3. **모델 등록 (관리자에서 데이터 관리 가능)**  
    ```python
    from django.contrib import admin
    from .models import Article

    admin.site.register(Article)
    ```

## 기타 명령어 및 참고 사항
- **데이터베이스 초기화**
    1. migration 파일 삭제 시, __init__.py 파일은 삭제하지 않도록 주의
    2. db.sqlite3 파일 삭제로 DB 초기화
- **마이그레이션 상태 확인**
    ```
    python manage.py showmigrations
    ```
    - [X] 마크가 있으면 migrate 완료

- **SQL 코드 확인**
    ```
    python manage.py sqlmigrate articles 0001
    ```
    - migrations가 SQL로 어떻게 변환되는지 확인 가능

***

## 보충 설명
- Django 모델 클래스의 필드는 데이터타입과 옵션, 그리고 데이터의 유효성 조건을 정의하며, 실질적인 DB 테이블 구조의 설계도 역할을 합니다.
- 마이그레이션 과정에서 `makemigrations`로 변경 내역 기록, `migrate`로 실제 DB에 반영하는 것이 일반적 입니다.
- 관리자 사이트는 빠르고 쉽게 데이터 관리가 가능해 실무에서 많이 활용됩니다.

***

복사 후 바로 .md 파일로 활용할 수 있도록 구성했습니다.

***

**참고문헌**
- Django 공식문서 (모델/필드/마이그레이션)
- 실전 Django/ORM 프로그래밍 자료

***
# 250903 
좋습니다! 주신 내용을 기반으로 Django ORM과 QuerySet API에 대한 내용을 정리하고 추가 설명을 포함해서 학습용 **Markdown 문서(`orm_queryset.md`)** 형식으로 작성해드릴게요.  

***

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
