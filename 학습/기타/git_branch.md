
---

## INDEX (목차)

* **Branch**
    * Branch Command (브랜치 명령어)
* **Branch Scenario**
    * Branch 생성 및 조회
    * Branch 이동
    * Branch에서 commit 생성
* **Git Merge**
    * Fast-Forward Merge
    * 3-Way Merge
    * Merge Conflict (병합 충돌)
* **(Collaboration Workflows)**
    * Feature Branch Workflow
    * Git Flow
    * Forking Workflow

---

## 1. Branch

### 🌳 Git Branch란?


* 나뭇가지처럼 여러 갈래로 작업 공간을 나누어 **독립적으로 작업**할 수 있도록 도와주는 Git의 도구입니다.

### 🤔 Branch를 사용해야 하는 이유

1.  상용 중인 서비스(원본)에 영향을 주지 않고 새로운 기능을 개발할 수 있습니다.
2.  브랜치를 통해 별도의 작업 공간에서 기능 개발 및 테스트가 가능합니다.
3.  브랜치는 완전하게 독립되어 있어, 다른 브랜치의 작업에 영향을 끼치지 못합니다.
4.  에러가 발생하더라도, 해결된 브랜치만 원본에 병합(Merge)하여 안정성을 유지할 수 있습니다.

### ⌨️ Branch Command (주요 명령어)

| 명령어 | 기능 |
| :--- | :--- |
| `branch` | 브랜치 목록 확인 |
| `branch -r` | 원격 저장소의 브랜치 목록 확인 |
| `branch <이름>` | 새로운 브랜치 생성 |
| `branch -d <이름>` | 브랜치 삭제 (병합이 완료된 브랜치만 삭제 가능) |
| `branch -D <이름>` | 브랜치 삭제 (강제 삭제) |

### 📍 HEAD란?

* 현재 브랜치나 commit을 가리키는 **포인터**입니다.
* 즉, "현재 내가 바라보는 위치"를 의미합니다.

### ⚠️ git switch 주의사항

* 특정 브랜치(예: feature)에서 파일을 생성하고 `git add`를 하지 않은 상태(untracked file)로 `git switch`를 사용해 다른 브랜치(예: master)로 이동하면, 해당 파일이 그대로 따라오는 현상이 발생할 수 있습니다. (Git 버전에 따라 동작이 다를 수 있음)

---

## 2. Branch Scenario (시나리오)

### 📋 사전 준비

1.  `article.txt` 파일을 생성합니다.
2.  "master-1", "master-2", "master-3" 내용을 순서대로 입력하며 3개의 commit을 작성합니다.

### 🌿 Branch 생성 및 조회

* **`git branch login`**: 현재 위치(master의 최신 commit)를 기준으로 `login` 브랜치를 생성합니다.
* **`git branch`**: 브랜치 목록을 확인합니다.
    * `* master`
    * `  login`
    * (`*` 표시는 현재 HEAD가 가리키는 브랜치를 의미합니다.)
* 이후 master 브랜치에서 "master-4" commit을 추가하면, `master`는 `master-4`를, `login`은 `master-3`를 가리키게 됩니다.

### ➡️ Branch 이동

* **`git switch login`**: `login` 브랜치로 HEAD를 이동합니다.
* 이동 후 `article.txt` 파일을 확인하면, `login` 브랜치가 가리키는 `master-3` 시점의 내용만 보이게 됩니다. ("master-4" 내용은 사라짐)
* **`git log --oneline --all`**: 모든 브랜치의 commit 내역을 함께 볼 수 있습니다.

### ✍️ Branch에서 commit 생성

* `login` 브랜치에서 "login-1" commit을 추가로 생성합니다.
* **`git log --oneline --graph --all`**: 그래프 옵션으로 로그를 확인하면, `master` 브랜치와 `login` 브랜치가 `master-3` 이후로 갈라진(diverged) 것을 시각적으로 확인할 수 있습니다.

### 📝 git branch 정리

1.  **브랜치 이동 (`switch`)**은 **HEAD가 특정 브랜치를 가리키도록** 변경하는 것입니다.
2.  브랜치는 **가장 최신 commit**을 가리킵니다.
3.  따라서 HEAD가 가리키는 브랜치가 바뀌면, **Working Directory의 내용도 해당 브랜치의 최신 commit 상태로** 변화합니다.

---

## 3. Git Merge (병합)

### 🔗 Git Merge란?

* 두 브랜치를 하나로 병합(결합)하는 작업입니다.


### ⚠️ 병합 전 확인 및 주의사항

1.  **수신 브랜치 확인**:
    * 병합을 *받는* 브랜치(예: `master`)로 `switch` (checkout)해야 합니다.
    * `git branch` 명령어로 현재 위치(HEAD)가 수신 브랜치인지 반드시 확인합니다.
2.  **최신 commit 상태 확인**:
    * 수신 브랜치와 병합할 브랜치 모두 최신 상태(pull 완료)인지 확인합니다.

---

### 🚀 Fast-Forward Merge

* **조건**: 수신 브랜치(`master`)가 병합할 브랜치(`hotfix`)의 **공통 조상**인 경우 (즉, `master`에서 추가 commit이 없었을 때) 발생합니다.
* **동작**: "실제로" 병합 commit을 만들지 않고, `master` 브랜치의 포인터가 `hotfix` 브랜치의 최신 commit 위치로 **빨리 감기(Fast-Forward)**처럼 이동합니다.
* **예시**:
    1.  `master` (c2)에서 `git branch hotfix` 생성
    2.  `git switch hotfix` 이동 후 `hotfix`에서 c3, c4 commit 생성
    3.  `git switch master` (c2 상태)
    4.  `git merge hotfix` 실행
    5.  `master`의 포인터가 c4로 이동하며 병합 완료.

### 🤝 3-Way Merge

* **조건**: 수신 브랜치(`master`)와 병합할 브랜치(`hotfix`)가 **서로 다른 commit**을 가지며 갈라진(diverged) 경우 발생합니다.
* **동작**:
    1.  두 브랜치의 **공통 조상**(base)을 찾습니다.
    2.  `master`의 최신 commit과 `hotfix`의 최신 commit, 그리고 **공통 조상**을 비교합니다. (3-Way)
    3.  변경 사항을 모두 합친 **새로운 병합 commit (Merge commit)**을 `master` 브랜치에 생성합니다. (이 commit은 부모가 2개입니다.)
* **예시**:
    1.  `master` (c2)에서 `hotfix` 분기
    2.  `master`에서 c3 commit 생성
    3.  `hotfix`에서 c4, c5 commit 생성
    4.  `git switch master` (c3 상태)
    5.  `git merge hotfix` 실행
    6.  c3과 c5의 내용을 합친 **새로운 commit `c6`**가 `master`에 생성됩니다.

---

### 💥 Merge Conflict (병합 충돌)

* **정의**: 병합하려는 두 브랜치가 **"동일한 파일의 동일한 부분"**을 수정한 경우, Git이 자동으로 합치지 못하고 충돌이 발생하는 것입니다.
* **발생**: 3-Way Merge 시에만 발생할 수 있습니다.

#### 🛠️ Git 충돌 해결 과정

1.  `git merge` 시 충돌이 발생하면, VSCode 등에서 `<<<<<<< HEAD`, `=======`, `>>>>>>> hotfix`와 같은 충돌 표시자를 확인합니다.
2.  **충돌이 발생한 파일**을 열어, 원하는 내용만 남기고 **충돌 표시자를 모두 직접 수정**합니다.
3.  수정이 완료된 파일을 **`git add .`** 명령어로 Staging Area에 추가합니다. (이것이 "충돌을 해결했다"고 Git에 알리는 행위입니다.)
4.  **`git commit`**을 실행하여 **merge commit을 생성**합니다. (이때 vim 에디터가 열리며 기본 commit 메시지가 작성되어 있습니다. `:wq`로 저장 및 종료)
5.  (선택) 병합이 완료된 `hotfix` 브랜치는 **`git branch -d hotfix`**로 삭제합니다.

---

## 4. 협업 워크플로우

### 📁 Feature Branch Workflow (Shared Repository Model)

* **개념**: 모든 팀원이 하나의 공유 원격 저장소(Shared Repository)에 대한 소유권(쓰기 권한)을 가집니다.
* **작업 순서**:
    1.  기능 개발을 위해 `master`에서 `feature/login` 같은 **기능 브랜치(Feature branch)**를 생성합니다.
    2.  해당 브랜치에서 작업 후, 원격 저장소에 `push` 합니다.
    3.  **풀 리퀘스트 (Pull Request, PR)**를 생성하여 `master` 브랜치로 병합을 요청합니다.
* **풀 리퀘스트 (PR)**:
    * 내가 작업한 내용을 `master` 같은 대표 브랜치에 합병해 달라고 공식적으로 요청하는 기능입니다.
    * 단순 코드 합치기 요청을 넘어, **코드 리뷰** 등 협업을 위한 **핵심 소통 도구**로 사용됩니다.

### 🌊 Git Flow

* 더 구조화된 브랜치 전략입니다.
* **`master` (main)**: **실제 배포용** 브랜치. 이 브랜치에 직접 commit하지 않습니다. (v1.0, v1.1 태그 관리)
* **`dev`**: 개발용 메인 브랜치.
* **`feature`**: **`dev` 브랜치에서 분기**하여 기능을 개발합니다. 개발 완료 시 다시 `dev`로 병합합니다. (충돌 주의)
* (그 외 `release`, `hotfix` 브랜치 등이 존재)


### 🍴 Forking Workflow

* **개념**: **오픈 소스 프로젝트**에서 주로 사용하며, 원본 저장소(Upstream)에 대한 쓰기 권한이 없는 외부 기여자가 협업하는 방식입니다.
* **작업 순서**:
    1.  **Fork**: 외부 기여자가 원본 저장소(Upstream)를 **내 개인 계정으로 그대로 복제(Fork)**하여, 독립된 원격 저장소(Origin)를 만듭니다.
    2.  **Clone**: 내 개인 저장소(Origin)를 로컬로 `clone` 합니다.
    3.  **Branch & Commit**: 내 로컬 저장소와 개인 원격 저장소(Origin)에서 자유롭게 작업합니다.
    4.  **Pull Request (PR)**: 작업 완료 후, **내 저장소(Origin)에서 원본 저장소(Upstream)로** "제가 수정한 내용을 반영해 주세요"라고 **PR**을 보냅니다.
    5.  **Review & Merge**: 원본 저장소의 관리자(Maintainer)가 코드를 검토하고 승인하면, 원본 `master`에 병합됩니다.
* **목적**: 원본 프로젝트의 코드 품질과 안정성을 유지하며 외부 기여자의 코드를 안전하게 검토하기 위함입니다.