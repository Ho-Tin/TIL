# Static files
## Static files
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
### 웹 서버와 정적 파일
- 웹 서버의 기본동작은 **특정 위치(URL)에 있는 자원**을 요청(HTTP request) 받아서 응답(HTTP response)을 처리하고 제공하는 것
- 자원에 접근 가능한 주소가 있다. 라는 의미
- 웹 서버는 URL로 서버에 존재하는 정적 자원을 제공함
- **정적 파일을 제공하기 위한 경로**(URL)가 있어야함
### static files 경로
- 기본 경로
1. `app폴더/static`에 이미지 저장
2. static files 경로는 DTL의 **static tag**를 사용해야함
  - built-in tag가 아니기 때문에 **load tag**를 사용해 import 후 사용 가능
 ```
{% load static %}

<img src="{% static "articles/sample-1.png" %}" alt="imgimg">
 ```
  - STATIC_URL
    - 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
    - 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재
- 추가 경로
- STATICFILES_DIRS
  - 정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
- 최상위 폴더에 static 폴더 생성후 이미지 저장 (아래 코드 참조)
```
STATICFILES_DIRS = [
    BASE_DIR / 'static'
    ]
```
## Media files
