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
