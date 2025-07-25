#  오늘 배운것
## 250716
```
touch  -- 파일 생성'
ls -- 현재 폴더내의 파일들 목록 출력
rm (파일이름.확장자명) -- 파일 삭제 // 폴더 삭제시 rm -r (폴더이름)
pwd -- 현재 폴더의 절대경로
mkdir -- 폴더 생성
cd  .(현재폴더) / ..(상위폴더)  -- 폴더 이동
code .  -- vscode 파일을 현재 폴더기준으로 다시 열기

# git 사용하는방법 
git init (저장소 지정)
git st 
git add 파일이름 or .(현재폴더에 있는 모든 파일 add)
git commit -m "commit(저장)"
git log -- log 이력 확인 / git log --oneline > log 간소화 
git commit --amend  --  commit 수정할떄 사용
TIP : git config --global alias.st status -- git status 치는게 힘드니 단축키? 지정 git st
```
---
## 250717
```
git remote add origin(이름) https://(주소) -- github와 연걸
git push origin(이름) master  -- github에 파일 전송
git pull origin master  -- github에서 파일 가져오기(업데이트만)
git clone https://(주소)  --  githun에서 파일 가져오기(전체파일/다운로드)
.gitignore  (API키 같은 공유해서는 안되는 파일을 숨기기 할때 사용)

git remote -v -- github 저장소 목록 (원격저장소)
git log --oneline   
git revert (commit ID) -- 특정 commit을 삭제 할떄 사용 ex) commit 1, 2, 3이 있을떄 commit 2 삭제하고싶을떄
git reset --soft/mixed/hard``` (commit ID) -- 게임 롤백이랑 비슷 - commit 을 돌리고 싶을떄
git reflog --   hard로 commit 삭제했을때 log 확인하여 commit ID 확인

git restore -- 
```
---
## 250718

- AI 관련 GPT 내용
- Generative / Pre-trained / Transformer
- Attention 매커니즘
- Interface
- **cs 지식 공부(computer science)**
- API 
- open AI API  필수 파라미터 : model , messages
### Open AI API 사용하여 chat bot 만들기
- vscode를 이용한 바이브 코딩
- https://github.com/Ho-Tin/SSAFY-Chat-bot 

## 250721
- AI 캠프 시작
- 우편함 레터링 서비스 
- 스터디 공부 방법
- CS, 알고리즘 
**CS공부의 경우 면접에서 발표할수 있을정도로 공부**
- 백준같은 알고리즘 문제를 풀고 한번에 그치지 않고 반복해서 학습(다른사람의 코딩 보는것도 도움됨)
- CS책 : 혼자 공부하는 시리즈 https://www.yes24.com/product/goods/111378840
- 프로그래머스 사용 추천(코딩시-코딩테스트 준비)
- AI를 이용한 광고 제작
- Chat GPT를 이용한 기획서 작성

## 250722
- 각종 AI를 이용한 광고 영상 제작
## 250723
- AI를 이용한 3D 프린터 사용

## 250725
- AI를 이용한 Art 강의
- AI는 상상을 현실화 or 확장시켜주는 도구이다
- AI는 도구이다- 상상은 인간이 하는 것
## 알고리즘 중요성 및 인공지능 프로그래밍
- 알고리즘의 중요성
- 소프트웨어 스택, 기업 코딩 테스트
- 인공지능 프로그래밍
- - 인공지능,신경망,LLM, 삼성 AI 챌린지, CUDA
### 소프트웨어 스택
- Web,Mobile APP - FE
- server, Databse,API - BE
- FE -> AI로 대체가능 << 바이브코딩
- AI 개발 /
### DS(DATA Scientist)- 데이타 분석가
- 소프트웨어 지식
-  - 프로그래밍, 알고리즘, 자료구조, 운영체제, 인공 지능 등
### 문제 해결 능력(코딩테스트)
-  - 알고리즘/자료구조 설계 및 구현
- 브론즈(Chathgpt 100%해결),실버(ChatGpt 80% 해결),**골드(Chathgpt 10%해결)** , 플다(올림피아드 수준)
- 카카오 7문항(4~5문항 합격점)
- 백준 온라인 저지(백준 1000위 - 목표)
 -- 삼성 기출문제
- 프로그래머스
- -- 카카오,현대 기출문제
- 시간복잡도 <<< 면접떄 필수 어필 / 효율적으로 관리를 하기 위함
- - 컴퓨터의 계산 속도 초당 1억번< 알고리즘은 루트n으로 짜는게 좋다 << (타임아웃 중요)
- 서버가 터졌을떄 대처법
- 1. 코드 다시짜기
- 2. 서버증설 -> scale < 확장성
- 루트 n 구하는 방법 if i * i > x:
- Cot(체인 오브 쏘트)?생각의 사슬
**문제를 풀기전 문제를 이해하고 알고리즘 자료구조를 생각할것**  
















- 
