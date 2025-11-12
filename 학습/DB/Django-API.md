제공된 동영상 강의 내용을 기반으로 마크다운(MD) 파일을 작성했습니다.

-----

# REST API

## 💻 목차

  * REST API
      * API
      * REST API
      * 자원의 식별
      * 자원의 행위
      * 자원의 표현
      * JSON 데이터 응답

-----

## 🚀 학습 시작

오늘의 학습 목표는 다음과 같습니다.

  * 오늘 이렇게 다양한 서비스들이 서로 약속된 방법으로 대화하는 방식, **REST API**를 배워볼 거예요.
  * 복잡한 설명 없이, 주소를 정하고(**GET**), 행동을 선택하고(**POST**, **DELETE**), 결과를 받아보는 경험을 할 수 있어요.
  * 내가 만든 서버가 스마트폰 앱처럼 응답하도록 바꿔보는 실습도 함께 진행해볼 거예요.

### 📝 예시: 배달 앱

1.  배달 앱이 **REST API**를 통해 가게에 주문 정보를 전달하고
2.  가게는 그 정보를 받아서 **JSON** 형식으로 "주문 확인"을 응답합니다.
3.  우리는 어떤 메뉴를 주문했는지 **GET** 요청으로 다시 확인할 수도 있어요.

-----

## 🧐 이론

### API (Application Programming Interface)

  * 소프트웨어와 소프트웨어 간 지정된 형식(형식)으로 소통하는 수단 -\> **API**
  * "이렇게 요청을 보내면, 이렇게 정보를 제공해줄 것이다"라는 **매뉴얼**
  * **예시**: 스마트폰의 날씨 앱은 기상청에서 제공하는 API를 통해 기상청 시스템과 대화하여 매일 최신 날씨 정보를 표시할 수 있습니다.

### Web API

  * 웹 서버 또는 웹 브라우저를 위한 API
  * 현대 웹 개발은 하나부터 열까지 직접 개발하기보다 여러 **Open API**들을 활용합니다.
  * **대표적인 Third Party Open API 서비스 목록**
      * Youtube API
      * Google Map API
      * Naver Papago API
      * Kakao Map API

### REST API 정의

  * **REST (Representational State Transfer)**
  * API Server를 개발하기 위한 일종의 **소프트웨어 설계 방법론**입니다.
  * 엄격한 규칙을 의미하는 것은 아닙니다.
  * API마다 제각각 구조를 정의하고, 누구나 예측 가능한 방식으로 통신할 수 있도록 설계 기준을 제안한 것이 바로 REST입니다.
  * **실제 활용 예시**: Naver Cloud API, Kakao Login API

-----

## 1\. 자원의 식별

### URI (Uniform Resource Identifier: 통합 자원 식별자)

  * 인터넷에서 리소스(자원)를 식별하는 문자열
  * 가장 일반적인 URI는 웹 주소로 알려진 **URL**입니다.

### URL (Uniform Resource Locator: 통합 자원 위치)

  * URL은 다음과 같은 구성 요소를 가집니다.
  * `Scheme://Authority(Domain Name:Port)/Path?Parameters#Anchor`
      * **Domain Name**: 요청 중인 웹 서버를 나타냅니다. (예: `google.com`)
      * **Path**: 웹 서버의 리소스 경로를 나타냅니다. (예: `/articles/create/`)
          * 오늘날은 실제 물리적 위치가 아닌 추상화된 형태의 구조를 표현합니다.
      * **Anchor**: 일종의 "북마크"로, 해당 지점으로 이동합니다. (예: `#quick-install-guide`)
          * Anchor(fragment)는 서버에 전달되지 않습니다.

-----

## 2\. 자원의 행위

### HTTP Request Methods

  * 리소스에 대한 **행위**, 즉 **수행하고자 하는 동작**을 정의합니다.
  * "이 주소로 물건 좀 보내주세요" → **POST** (생성)
  * "방금 보낸 물건 도착했나요?" → **GET** (조회)
  * "그 물건 취소할게요" → **DELETE** (삭제)
  * "받는 사람 전화번호 바뀌었어요" → **PUT** (수정)

### HTTP response status codes

  * 특정 HTTP 요청이 **성공적**으로 완료되었는지 여부를 나타내는 숫자입니다.
  * 클라이언트는 이 코드를 보고 어떤 일이 일어났는지 판단할 수 있습니다.

-----

## 3\. 자원의 표현

  * 그동안 Django는 사용자에게 \*\*page(html)\*\*만 응답하고 있었습니다.
  * 하지만 서버는 페이지뿐만 아니라 **다양한 데이터 타입**을 응답할 수 있습니다.
  * REST API 중에서는 **JSON** 타입으로 응답하는 것을 권장합니다.

### JSON (JavaScript Object Notation)

  * 데이터를 전달하기 위한 **최소한의 형식**입니다.
  * 어떤 클라이언트와도 언어와 플랫폼에 **독립적**으로 통신할 수 있게 해줍니다.
  * 서버는 HTML 페이지를 만들지 않고, **JSON 데이터만 응답**하는 방식으로 동작할 수 있습니다.
  * HTML 대신 JSON만 전달하므로, **응답 용량이 줄고 처리 속도가 빨라집니다.**

### Fixtures (실습 데이터)

  * 초기 데이터를 데이터베이스로 불러오기 위한 JSON 형식의 데이터 파일입니다.
  * 실습용 데이터 입력 명령어:
    ```bash
    $ python manage.py loaddata articles.json
    Installed 20 object(s) from 1 fixture(s)
    ```

-----

## 🚀 Django REST Framework (DRF)

### 프로젝트 준비 (실습)

1.  사전 제공된 `drf` 프로젝트 기반 시작
2.  가상 환경 생성 및 패키지 설치
3.  `migrate` 진행
    ```bash
    $ python manage.py migrate
    ```
4.  `fixtures` 로드하여 실습용 데이터 입력
    ```bash
    $ python manage.py loaddata articles.json
    ```

### Serialization (직렬화)

  * 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태(예: Python 객체)를 **재구성할 수 있는 포맷(예: JSON)으로 변환하는 과정**입니다.
  * 이 변환 과정은 **Serializer Class**가 담당하며, `serializers.py` 파일에 작성합니다.

-----

## 🛠️ CRUD with ModelSerializer

### 1\. GET (조회)

  * **List (전체 조회)**

      * `# articles/views.py`
        ```python
        @api_view(['GET'])
        def article_list(request):
            articles = Article.objects.all()
            serializer = ArticleListSerializer(articles, many=True)
            return Response(serializer.data)
        ```
      * **`many=True`** 옵션: 직렬화 대상이 QuerySet(여러 개)인 경우 사용합니다.

  * **Detail (단일 조회)**

      * `# articles/serializers.py`
        ```python
        class ArticleSerializer(serializers.ModelSerializer):
            class Meta:
                model = Article
                fields = '__all__'
        ```

### 2\. POST (생성)

  * `article_list` 함수에 `POST` 메서드 분기 처리를 추가합니다.
  * `# articles/views.py`
    ```python
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    ```

### 3\. DELETE (삭제)

  * 일반적으로 DELETE 요청은 \*\*`204 No Content`\*\*로 본문(Body) 없이 응답하는 것이 RESTful 한 설계 방식입니다.
  * **TIP**: 만약 삭제된 데이터를 확인하는 등 응답이 필요한 경우, `204` 대신 `200 OK` 코드와 함께 데이터를 반환할 수 있습니다.

### 4\. PUT (수정 - 전체)

  * `PUT`은 리소스의 **전체**를 수정할 때 사용합니다.
  * `# articles/views.py` (article\_detail 함수 내)
    ```python
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # raise_exception=True로 인해 400 응답은 자동 처리됨
    ```
  * `is_valid(raise_exception=True)`: 유효성 검사 실패 시 `ValidationError` 예외를 발생시키고, DRF가 자동으로 `HTTP 400` 응답을 반환합니다.

### 5\. PATCH (수정 - 일부)

  * `PATCH`는 리소스의 **일부만** 수정할 때 사용합니다.
  * Serializer를 생성할 때 **`partial=True`** 속성을 설정합니다.
  * `# articles/views.py` (article\_detail 함수 내)
    ```python
    elif request.method == 'PATCH':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    ```
```python
# 최종코드
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'DELETE', 'PATCH'])
def article_detail(request, article_pk):
    
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET': 
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PATCH':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
-----

## 🏁 요약 정리

  * **API**: 서로 다른 소프트웨어 간 통신을 가능하게 하는 인터페이스.
  * **REST API**: 자원을 **URI**로 식별하고 **HTTP 메서드**로 행위를 정의하며 **JSON** 등으로 자원을 표현하는 설계 방식.
  * **자원의 식별**: URI (예: `/articles/1/`)
  * **자원의 행위**: HTTP Methods (GET, POST, PUT, DELETE, PATCH)
  * **자원의 표현**: JSON
  * **Serialization**: Python 객체(QuerySet 등)를 JSON 등 외부 시스템과 통신 가능한 형태로 변환하는 과정.
  * **Django (DRF)**: DRF를 사용하면 JSON 기반의 RESTful API를 빠르고 쉽게 구축할 수 있습니다.