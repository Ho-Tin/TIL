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
- **사용자**가 웹에서 업로드하는 정적 파일(user-uploaded)
### 이미지 업로드
- imageField()
  - 이미지 업로드에 사용하는 모델 필드
  - 이미지 객체가 직접 DB에 저장되는 것이 아닌 **이미지 파일의 경로** 문자열이 저장됨
- MEDIA_ROOT
  - 미디어 파일들이 위치하는 디렉토리의 절대 경로
- MEDIA_URL
  - STATIC_URL과 동일하게 겉으로 보여지는 경로
1. setting.py에 MEDIA_ROOT, MEDIA_URL 설정
```
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'bonobono/'
```
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정
```
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
- 이미지 업로드
1. models.py에 `image = models.ImageField(blank=True)` 작성
2. ImageField 사용하기 위해서는 Pillow 라이브러리가 필요함
  - `pip install pillow`
3. form 요소의 enctype 속성 추가
  - enctype : form 데이터를 서버로 전송할때 인코딩 방식 결정하는것
  - `enctype="multipart/form-data"`
  - `<form action="{% url "articles:create" %}" method="POST" enctype="multipart/form-data">`
4. ModelForm의 2번째 인자로 요청받은 파일 데이터 작성
```
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
```
### 이미지 업로드 제공
- url 속성을 통해 업로드 파일의 경로 값을 얻을 수 있음
- article(인스턴스 변수명).image(modle 컬럼명).url
  - 업로드 파일의 경로
- article.image
  - 업로드 파일의 파일 이미지명
```
{% if article.image %} # 이미지가 있을때만 이미지 변경
<p>이미지 : <img src="{{article.image.url}}" alt="img"></p>
{% endif %}
```
### 참고
- upload_to
  - ImageField()의 upload_to 속성을 사용해 다양한 추가 경로 설정 가능
<img width="797" height="441" alt="image" src="https://github.com/user-attachments/assets/13cd9590-a955-42a2-a619-f28636006f8a" />

