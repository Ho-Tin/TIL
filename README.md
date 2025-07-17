#  오늘 배운것
* 250716
```
touch  -- 파일 생성
mkdir -- 폴더 생성
cd  .(현재폴더) / ..(상위폴더)  -- 폴더 이동

git 사용하는방법 
git init (저장소 지정)
git st 
git add 파일이름 or .(현재폴더에 있는 모든 파일 add)
git commit -m "commit(저장)"
git log -- log 이력 확인 / git log --oneline > log 간소화 
TIP : git config --global alias.st status -- git status 치는게 힘드니 단축키? 지정 git st
```

* 250717
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
git reflog - hard로 commit 삭제했을때 log 확인하여 commit ID 확인
```