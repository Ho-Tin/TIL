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
git status (현재 상태)
git add 파일이름 or .(현재폴더에 있는 모든 파일 add)
git commit -m "commit(저장)"
git log -- log 이력 확인 / git log --oneline > log 간소화 
git commit --amend  --  commit 수정할떄 사용
TIP : git config --global alias.st status -- git status 치는게 힘드니 단축키? 지정 git st
```
---
## 250717

- Remote Repository
    - 원격 저장소
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













- 
