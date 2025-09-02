# 250902
## model
### Model을 통한 DB(데이터베이스) 관리
- Django Model
  - DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  - 테이블 구조를 설계하는 청사
- model class
```
class Article(models.Model):
```
  - model은 model에 관련된 모든 코드가 이미 작성 되어있음
  - 테이블 구조를 어떻게 설계할지에 대한 코드만 작성할수 있음
### model field
- 데이터의 유형과 제약 조건을 정의
- DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의
- Field types( 필드 유형)
  - 데이터의 종류 를 정의
- Field options (필드 옵션)
  - 필드의 동작과 제약 조건을 정의
### Field Type
- charField()
  - 제한된 길이의 문자열을 저장
  - 최대 길이를 결정하는 max_length는 필수 옵션
- TextField()
  - 길이 제한이 없는 대용량 텍스트를 저장
  - 무한대는 아님
- 숫자 필드
  - IntegerField, FloatField
- 날짜/시간 필드
  - DateField, TimeField, DateTimeField
- 파일 관련 필드
  - FileField, ImageField
### Field Options
- 특정 규칙을 강제하기위해 규칙이나 제한사항을 거는 것
- null
  - 의도적으로 값을 비우는것
  - DB에 NULL값을 허용할지 여부를 결정(기본값:False)
- blank
  - form에서 빈 값을 허용할지 결정
- default
  - 필드의 기본값을 설정
### Migrations
- model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법
- Migrations 과정
- auto_now
  - 데이터가 저장될 때마다 현재 시간 저장
- auto_now_add
  - 처음 생성될 떄만 현재 시간 저장
- 추가 모델 필드 작성
  - 1번은 현재 대화를 유지하면서 직접 기본 값을 입력 하는 방법
  - 2번은 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
    - 날짜 데이터이기 때문에 직접 입력보다는 Django가 제아하는 기본값 사용 권장(1번)
  - > git commit 과 유사하게 0002 생성되는것 확인
### Admin site
- Automatic admin interface
  - Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
1. admin 계정 생성
- python manage.py creatsuperuser
2. DB에 생성된 admin 계정 확인
3. admin에 모델 클래스 등록
```
from django.contrib import admin
from .models import Article

admin.site.register(Article)
```
### 참고
- 데이터베이스 초기화
  1. migration 파일 삭제
     - commit 이력 만 삭제 ( 폴더의 init 지우지 않도록 주의)
  2. db.sqlite3 vkdlf tkrwp
- python manage.py showmigrations
  - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
  - '[X]' 표시가 있으면 migrate가 완료되었음을 확인
- python manage.py sqlmigrate articles 0001
  - 해당 migrations 파일이 SQL 언어(DB에서 사용하는 언어)로 어떻게 번역 되어 DB에 전달되는지 확인하는 명령어
  
