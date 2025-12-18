

-----

# Vue with DRF: 게시판 서비스 구현 심화 가이드

이 문서는 Vue.js(Frontend)와 Django REST Framework(Backend)를 연동하여 완전한 게시판 서비스를 구현하는 과정을 상세히 기술합니다. 특히 두 프레임워크 간의 통신 과정, CORS 이슈 해결, 그리고 상태 관리(Pinia)에 중점을 둡니다.

## 1\. 프로젝트 아키텍처 및 데이터 흐름

프론트엔드와 백엔드가 분리된 환경에서의 데이터 처리 과정은 다음과 같습니다.

1.  **Client (Vue)**: 사용자가 웹 페이지에서 이벤트를 발생시킴 (예: "게시글 조회" 버튼 클릭).
2.  **Request (Axios)**: Vue 내부의 `Axios` 라이브러리가 비동기적으로 Django 서버에 HTTP 요청을 보냄.
3.  **Middleware (Django)**: 요청이 도달하면 보안 미들웨어(CORS 등)가 검증을 수행.
4.  **View & Serializer (DRF)**:
      * View는 요청을 처리하고 DB에서 데이터를 조회.
      * Serializer는 Python 객체(Model)를 JSON 데이터로 변환.
5.  **Response**: JSON 데이터를 클라이언트로 응답.
6.  **Store (Pinia)**: Vue는 응답받은 데이터를 중앙 저장소(Store)에 업데이트.
7.  **Render**: Store의 데이터 변경을 감지하여 컴포넌트(DOM)가 자동으로 다시 렌더링됨.

-----

## 2\. Backend 설정 (Django REST Framework)

### 2.1 모델(Model) 구성

게시글 데이터를 저장하기 위한 기본 구조입니다.

```python
# articles/models.py
class Article(models.Model):
    # user = models.ForeignKey(...) # 추후 유저 기능 연동 시 사용
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 2.2 API 명세 및 URL 설정

RESTful한 설계를 위해 다음과 같이 경로를 지정합니다.

```python
# my_api/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/articles/', include('articles.urls')),
]

# articles/urls.py
urlpatterns = [
    path('', views.article_list),          # 전체 조회 및 생성
    path('<int:article_pk>/', views.article_detail), # 상세 조회, 수정, 삭제
]
```

### 2.3 View 함수 (데이터 처리)

DRF의 `@api_view` 데코레이터를 사용하여 HTTP Method(GET, POST)에 따라 분기 처리합니다.

```python
# articles/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleListSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # POST 처리 로직 생략...
```

-----

## 3\. Frontend 설정 (Vue 3 + Pinia)

### 3.1 프로젝트 구조

  * `App.vue`: 최상위 컴포넌트 (`RouterView` 포함).
  * `router/index.js`: URL 경로와 컴포넌트를 매핑.
  * `stores/articles.js`: 게시글 데이터를 중앙 관리하는 Pinia Store.
  * `views/`: 페이지 단위 컴포넌트 (`ArticleView`, `DetailView`, `CreateView`).

### 3.2 Pinia Store 정의 (`stores/articles.js`)

API 요청 로직을 컴포넌트가 아닌 Store의 `actions`에 배치하여 비즈니스 로직을 분리합니다.

```javascript
import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
    const articles = ref([]) // State: 게시글 목록
    const API_URL = 'http://127.0.0.1:8000'

    // Action: 게시글 목록 가져오기
    const getArticles = function () {
        axios({
            method: 'get',
            url: `${API_URL}/api/v1/articles/`
        })
        .then((res) => {
            articles.value = res.data // 응답 데이터를 State에 저장
        })
        .catch((err) => console.log(err))
    }

    return { articles, API_URL, getArticles }
}, { persist: true }) // 새로고침 시 데이터 유지 플러그인 사용
```

-----

## 4\. CORS Policy 이슈 및 해결

### 4.1 문제 상황 (CORS Error)

Vue(`localhost:5173`)에서 Django(`localhost:8000`)로 요청을 보내면 브라우저 콘솔에 에러가 발생합니다.

> **원인:** **SOP (Same-Origin Policy)** 정책 위반.
> 두 주소의 **Port(포트)** 가 다르므로 브라우저는 이를 다른 출처(Origin)로 인식하여 차단합니다.

### 4.2 CORS (Cross-Origin Resource Sharing) 란?

서버가 특정 출처(Origin)에 대해 리소스 접근을 허용하도록 브라우저에게 알려주는 메커니즘입니다. 서버는 응답 헤더에 `Access-Control-Allow-Origin` 정보를 포함해야 합니다.

### 4.3 해결 방법: `django-cors-headers` 라이브러리 활용

Django 서버 측에서 설정을 변경하여 Vue의 요청을 허용해야 합니다.

1.  **설치**:

    ```bash
    $ pip install django-cors-headers
    ```

2.  **`settings.py` 설정**:

    ```python
    # 1. 앱 등록
    INSTALLED_APPS = [
        ...,
        'corsheaders',
        ...,
    ]

    # 2. 미들웨어 추가 (순서 중요: CommonMiddleware 보다 위에 위치해야 함)
    MIDDLEWARE = [
        ...,
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...,
    ]

    # 3. 허용할 출처 등록
    CORS_ALLOWED_ORIGINS = [
        'http://127.0.0.1:5173',
        'http://localhost:5173',
    ]
    ```

-----

## 5\. 기능별 상세 구현

### 5.1 전체 게시글 조회 (Read - List)

  * **컴포넌트**: `views/ArticleView.vue`
  * **로직**:
    1.  `import { useArticleStore } from '@/stores/articles'`
    2.  `onMounted` 훅을 사용하여 페이지 로드 시 `store.getArticles()` 자동 실행.
    3.  Template에서 `v-for`를 사용해 `store.articles` 배열을 순회하며 렌더링.

### 5.2 단일 게시글 상세 조회 (Read - Detail)

  * **라우팅 설정**: 동적 라우팅(`:id`) 사용.
    ```javascript
    // router/index.js
    {
        path: '/articles/:id',
        name: 'DetailView',
        component: DetailView
    }
    ```
  * **컴포넌트**: `views/DetailView.vue`
  * **핵심 코드**:
    ```javascript
    import { useRoute } from 'vue-router'
    const route = useRoute()
    const articleId = route.params.id // URL의 id값 추출

    // Axios 요청 시 id 활용
    axios.get(`${store.API_URL}/api/v1/articles/${articleId}/`)
    ```

### 5.3 게시글 생성 (Create)

  * **컴포넌트**: `views/CreateView.vue`
  * **데이터 바인딩**: `v-model.trim`을 사용하여 사용자 입력값을 반응형 변수에 실시간 저장.
  * **전송 및 이동**:
    ```javascript
    import { useRouter } from 'vue-router'
    const router = useRouter()

    const createArticle = function () {
        axios({
            method: 'post',
            url: `${store.API_URL}/api/v1/articles/`,
            data: {
                title: title.value,
                content: content.value
            }
        })
        .then(() => {
            // 성공 시 목록 페이지로 이동
            router.push({ name: 'ArticleView' })
        })
        .catch((err) => console.log(err))
    }
    ```

-----   

## 6\. 핵심 개념 정리 및 Quiz

### 요약

  * **DRF**: 데이터를 JSON 형태로 응답하는 API 서버 역할.
  * **Vue**: 데이터를 받아 화면을 구성하고 사용자 인터랙션을 담당하는 클라이언트 역할.
  * **Axios**: 비동기 HTTP 통신 라이브러리.
  * **Pinia**: 데이터(상태)를 전역에서 관리하여 컴포넌트 간 데이터 공유를 쉽게 함.
  * **CORS**: 서로 다른 출처 간 리소스 공유를 위한 보안 정책 및 설정.

### 확인 문제 (Review)

1.  **CORS 관련**: SOP 제한을 완화하여 다른 출처의 리소스 공유를 허용하는 정책은?
      * 답: **CORS** (Cross-Origin Resource Sharing)
2.  **Vue Router**: 페이지 이동 없이 URL을 변경하고 컴포넌트를 전환하는 데 사용되는 `<template>` 태그 내의 컴포넌트는?
      * 답: **RouterLink** (이동 링크 생성), **RouterView** (컴포넌트 출력 위치)
3.  **라우팅 정보**: 현재 페이지의 URL 파라미터(id 등) 정보를 조회할 때 사용하는 훅(Hook)은?
      * 답: **useRoute()** (반면, 페이지를 이동시키는 객체는 `useRouter()`)
