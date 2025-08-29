# 250829
## Django
### Web Application 

### 클라이언트와 서버
- Client
  - 서비스를 요청하는 주체
- Server
  - 클라이언트의 요청에 응답하는 주체
  ---
### Frontend & Backend
- 프론트엔드
  - 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
  - HTML, CSS, JavaScript, 프론트엔드 프레임워크 등
- 백에드
  - 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 DB와의 상호작용 등을 담당
  - 서버언어(Python,Jave등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등
  ----
### Framework
- 웹 서비스 개발에 필요한 기술 : 로그인/로그아웃, 회원관리, 데이터베이스, 보안 등
- 모든 기능을 직접 개발하기에는 현실적 어려움 존재
- 현대 웹 개발의 핵심
--- 
- Web Framework
  - 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
- django
  - Python 기반의 대표적인 웹 프레임워크
### 가상환경
```
python -m venv venv   # 가상 환경 생성
ls -l
source venv/Scripts/activate  # 가상 환경 활성화
pip list   # package list 보기
deactivate   # 가상 환경 종료
pip freeze > requirements.txt  # 가상 환경에 설치된 모든 패키지를 버전과 함께 출력, 최신화 필수
pip install -r requirements.txt  # 의존성 리스트를 가져와서 가상환경에 설치
```
- 의존성
  - 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른 소프트웨어나 라이브러리
- 의존성 패키지
  - 프로젝트가 의존하는 '개별 라이브러리들'을 가리키는 말
- 의존성 리스트
  - 내가 쓴 패키지가 무엇인지 확인하여 공유
  - requirements.txt <로 관리하여 다른 팀원들과 공유
- 주의사항
  - .gitignore 파일에 작성하여 원격 저장소에 공유되지않게 하는게 중요(파일용량이 큼)
- .gitignore Tip
  - 구글링하여 gitignore.io에서 작성된 파일 가져오기 꿀팁
```
django-admin startproject firstpjt(이름) .(현재폴더에설치)  # 프로젝트 생성
python manage.py runserver 8888(서버 따로 지정가능, 없어도)   # 서버 실행
```
