# 250829

***

# Django 웹 애플리케이션 개발

## 클라이언트와 서버

- **클라이언트**: 서비스를 요청하는 주체로, 브라우저 또는 앱 등 사용자가 상호작용하는 부분을 의미함.
- **서버**: 클라이언트의 요청에 응답하는 주체로, 데이터 처리 및 동작의 본체 역할을 담당함.

***

## 프론트엔드와 백엔드

- **프론트엔드**: 사용자 인터페이스(UI)와 상호작용 담당. 주요 기술로 HTML, CSS, JavaScript, React, Vue 등 프레임워크가 있음.
- **백엔드**: 서버 측 동작, 데이터 처리, DB와의 상호작용, 보안 및 API 제공 담당. 일반적으로 Python, Java, Node.js 등의 언어와 Django, Spring 등 프레임워크를 사용함.

***

## 웹 프레임워크

- **프레임워크의 역할**: 로그인, 회원 관리, 데이터베이스 연동, 보안 등 반복적인 부분을 효율적으로 지원.
- **장점**: 많은 기능을 직접 개발하지 않아도 되고, 빠른 개발 및 안정성과 유지보수가 향상됨.
- **Django**: Python 기반, 대표적인 웹 프레임워크로 사용이 간편하고 확장성이 높음.

***

## 가상환경 관리

```bash
python -m venv venv                # 가상 환경 생성
source venv/Scripts/activate       # 가상 환경 활성화 (Mac/Linux는 source venv/bin/activate)
pip list                           # 설치된 패키지 목록 확인
deactivate                         # 가상 환경 종료
pip freeze > requirements.txt      # 패키지 명세 파일 생성 및 최신화
pip install -r requirements.txt    # 패키지 명세를 통한 설치
```
- **의존성 관리**: 소프트웨어가 동작하는 데 필요한 라이브러리나 패키지의 목록을 프로젝트별로 관리함.
- **.gitignore 사용**: 대용량 및 민감 정보 파일은 Git 저장소에서 제외하도록 반드시 .gitignore에 등록.
- **팁**: gitignore.io에서 각 환경에 맞는 .gitignore 파일을 손쉽게 생성 가능.

***

## Django 프로젝트 생성과 실행

```bash
pip install django
django-admin startproject firstpjt .       # 프로젝트 생성 (현재 폴더에 설치)
python manage.py runserver 8888            # 서버 실행 (포트 지정 가능)
```
- 프로젝트와 앱은 서로 분리되며, 하나의 프로젝트 내에 여러 개의 앱을 생성 및 등록할 수 있음.

***

## 디자인 패턴: MVC와 MTV

- **MVC(Model-View-Controller)**: 데이터, 사용자 인터페이스, 비즈니스 로직을 분리하여 설계함.
- **MTV(Model-Template-View)**: Django의 구조로, 역할은 MVC와 동일하나 용어가 다름.
- 각각의 책임을 명확히 하여 확장성과 관리가 용이해짐.

***

## 프로젝트와 앱 구조

- **프로젝트(Project)**: 여러 애플리케이션(앱)을 포함하는 전체 구조.
- **앱(Application)**: 독립적인 기능 단위. 예: 회원, 게시글, 댓글 등.
- **앱 생성 및 등록**
  1. `python manage.py startapp articles` (앱 이름은 복수형 권장)
  2. settings.py의 `INSTALLED_APPS`에 앱 등록.

***

## 프로젝트 디렉토리 구조

```text
setting.py       : 프로젝트 설정 관리
urls.py          : URL 요청과 views 연결
__init__.py      : 패키지 인식용
asgi.py          : 비동기 웹 서버 설정
wsgi.py          : 동기 웹 서버 설정
manage.py        : 커맨드라인 관리 유틸리티
admin.py         : 관리자 페이지 설정
models.py        : DB 모델 정의(MTV의 Model)
views.py         : HTTP 요청 처리(MTV의 View)
apps.py          : 앱 정보
tests.py         : 테스트 코드
templates/       : 템플릿 파일 저장소
```
- 각 파일의 역할에 따라 기능이 분리되어 있음.

***

## 요청과 응답 과정

1. 클라이언트가 요청 → urls.py에서 해당 경로 확인 → views.py에서 함수 실행 → models.py와 templates 사용 → 응답 반환.
2. 예시:
   - urls.py
     ```python
     from articles import views
     path('index/', views.index)
     ```
   - views.py
     ```python
     def index(request):
         return render(request, 'articles/index.html')
     ```
   - templates: articles 폴더 내 templates 디렉토리를 생성하고, index.html 파일 작성.

***

## Django 프로젝트 생성 루틴

1. 가상 환경 생성
2. 가상 환경 활성화
3. Django 설치
4. requirements.txt 생성 및 관리
5. .gitignore 파일 생성 및 등록
6. Git 저장소 초기화 (`git init`)
7. Django 프로젝트 및 앱 생성

***

## 실무 참고 사항 및 팁

- **LTS(Long-Term Support)**: 장기간 지원 및 안정성 제공되는 Python/Django 버전 권장.
- **render 함수 사용**: 요청, 템플릿 파일, context 데이터 결합 및 HTTPResponse 반환에 사용.
- **Trailing Comma(후행 쉼표)**: 코드 유지보수 및 확장 시 유용, 꼭 넣을 필요는 없음.
- **Django 규칙**
  - urls.py 경로는 '/'로 끝남
  - views.py 모든 함수는 첫 인자로 요청 객체(request) 필수
  - 템플릿 파일 경로(app/templates/) 반드시 준수.
- **MTV 구조의 핵심**: 명확한 분리, 유지보수와 협업에 유리.

***

# 250901 

