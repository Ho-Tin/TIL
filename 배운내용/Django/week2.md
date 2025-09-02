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
