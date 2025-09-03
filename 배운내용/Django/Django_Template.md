# Django Template System 정리

## Django Template Language(DTL)

- **데이터 표현 제어**  
  Django의 템플릿 시스템은 화면에 데이터를 표현하는 역할을 하며, 로직(비즈니스 주체)이 아닌 표현과 관련된 부분을 담당함.

- **컨텍스트 변수**  
  템플릿에서 `{{ 변수 }}` 문법을 이용하여 컨텍스트 데이터(딕셔너리 등)를 표시 가능함.

- **변수 접근**  
  점(`.`) 연산자를 통해 객체의 속성, 딕셔너리 키 등에 접근 가능  
  예: `{{ user.username }}` .

- **Filters**  
  파이프(`|`) 문법으로 변수 값에 변환·처리 함수 적용  
  예: `{{ value|lower }}` (소문자 변환) .

- **Tags**  
  템플릿 상에서 반복(`for`), 조건문(`if`) 등을 제어  
  예: `{% for item in list %} ... {% endfor %}` .

- **Comments**  
  템플릿 내에서 Django 주석 작성 가능  
  문법: `{# 주석 내용 #}` .

## 템플릿 상속 구조

- **Skeleton Template**  
  전체 페이지 공통 요소(헤더, 푸터 등)를 담는 기본 구조를 작성하고 하위 템플릿에서 필요한 영역을 재정의함.

- **상속 방법**  
  `{% extends "base.html" %}`  
  자식 템플릿이 부모 템플릿의 구조를 확장.

- **block 태그**  
  `{% block content %}{% endblock %}`  
  자식 템플릿에서 해당 영역을 필요에 따라 재정의함.

## 요청과 응답: HTML 폼과 Django Request

- **HTML form 요소**  
  유저 데이터를 서버에 전송하는 기본 방법.

    - **action** : 폼 데이터가 전송될 URL 지정. 미지정시 현재 페이지 URL.
    - **method** : 데이터 전송 방식 지정 (GET/POST).
    - **input** : 유저 데이터 입력받는 폼 컴포넌트. `name` 속성 필수.

- **쿼리 스트링 파라미터**  
  GET 방식에서 입력 데이터가 URL 파라미터로 전달됨  
  형식: `key=value&key2=value2` .

- **request 객체**  
  사용자의 모든 요청 정보가 포함된 Django 객체  
  GET 데이터: `request.GET.get("key")`  
  POST 데이터: `request.POST.get("key")` .

## Django URLs와 라우팅

- **URL Dispatcher**  
  URL 패턴과 이를 처리할 view 함수를 매핑하는 시스템.

- **Variable Routing**  
  URL 일부에 변수를 포함해 동적 경로 처리 가능  
  예: `path('articles/<int:num>/', views.index)`.

    - **Path Converters**:  
      - str, int, slug, uuid, path 등 데이터 타입 지정.

- **App URL Mapping**  
  앱별로 `urls.py`에서 URL 패턴을 따로 정의.

- **include() 함수**  
  프로젝트 내부 여러 앱의 URL 패턴을 모아서 import 및 매핑 가능.

- **URL 이름 지정**  
  각 패턴에 고유 이름 부여하여, 템플릿/뷰에서 사용할 수 있음  
  예: `path('home/', views.home, name='home')`.

***

## 추가 참고 예시

```django
# views.py
def my_view(request):
    context = {'msg': 'Hello!'}
    return render(request, 'template.html', context)

# template.html
<h1>{{ msg }}</h1>
```

```django
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hi/<str:name>/', views.hello, name='hello'),
]
```
