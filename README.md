#  오늘 배운것
* 250716
touch / mkdir / cd / .(현재폴더) / ..(상위폴더) 
git 사용하는방법 


``` 코드 저장법 "``` ```" ```  
* 250717
```
git remote add origin(이름) https://(주소) -- github와 연걸
git push origin(이름) master  -- github에 파일 전송
git pull origin master  -- github에서 파일 가져오기(업데이트만)
git clone https://(주소)  --  githun에서 파일 가져오기(전체파일/다운로드)
.gitignore  (API키 같은 공유해서는 안되는 파일을 숨기기 할때 사용)

git remote -v -- github 저장소 목록 (원격저장소)
git log --oneline   
git revert () -- 특정 commit을 삭제 할떄 사용 ex) commit 1, 2, 3이 있을떄 commit 2 삭제하고싶을떄
git reset --soft/mixed/hard``` -- 게임 롤백이랑 비슷 - commit 을 돌리고 싶을떄
git reflog - hard로 commit 삭제했을때 복구할때 사용

