
---

# 데이터 파이프라인 이해와 WSL 강의 요약

## 1. 데이터의 시대 (The Era of Data)

### 정보 vs 데이터

* **과거:** 정리되고 유의미하게 도출되는 **'정보(Information)'**가 중요.
* **현재:** 원시 자료인 **'데이터(Data)'** 자체의 중요성이 강조됨.
* **정보:** 1970~2000년대를 대표. 실제 도움이 되는 유의미한 것.
* **데이터:** 2010년대 이후를 대표. 대규모로 수집된 원시 자료. 나중에 의미를 부여함.



### 데이터의 중요성 (Big Data)

* **데이터의 양(Volume), 다양성(Variety), 증가 속도(Velocity)**의 향상.
* **신뢰성(Veracity), 가치(Value)**가 더해짐.
* **핵심:** 데이터의 수집, 가공, 활용할 수 있는 기술의 대두.
* > "데이터는 미래 경쟁력을 좌우하는 21세기의 원유" - 가트너



---

## 2. 데이터 엔지니어링과 파이프라인 (Data Engineering & Pipeline)

### 데이터 엔지니어의 역할

* **주요 역할:** 데이터를 안정적으로 수집하고 가공하여 전달. 분석과 모델링이 가능하도록 데이터 흐름을 자동화.
* **주요 업무:** 다양한 시스템에서 데이터 수집, 정제 및 변환(ETL/ELT 설계).
* > "좋은 모델은 좋은 파이프라인에서 나온다"



### 데이터 처리 시스템 비교 (OLTP vs OLAP)

| 구분 | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
| --- | --- | --- |
| **목적** | 트랜잭션(주문, 결제, 예약 등) 처리 | 데이터 분석, 의사결정 지원, 리포트 생성 |
| **특징** | 단위 저장 구조, 수정/삭제에 최적화 | 대량의 데이터를 기반으로 통계/분석 |
| **구조** | Client Service <-> Server <-> DB | Data Lake/Warehouse -> Analysis/ML |
| **데이터** | 현재 데이터 중심 | 과거 이력(Historical) 데이터 포함 |

### 데이터 파이프라인 기본 개념

#### 1. ETL vs ELT 구조

* **ETL (Extract, Transform, Load):**
* 데이터를 가공한 후 저장하는 전통적인 방식.
* 순서: **추출(Extract) → 가공(Transform) → 저장(Load)**


* **ELT (Extract, Load, Transform):**
* 데이터를 일단 저장한 후 가공하는 방식. 클라우드 시대에 많이 쓰임.
* 순서: **추출(Extract) → 저장(Load) → 가공(Transform)**



#### 2. 데이터 처리 방식: 배치(Batch)와 스트리밍(Streaming)

| 항목 | 배치 처리 (Batch Processing) | 스트리밍 처리 (Streaming Processing) |
| --- | --- | --- |
| **처리 방식** | 일정 주기로 데이터를 모아서 대량 처리 | 실시간으로 들어오는 데이터를 지속 처리 |
| **예시** | 하루 1회 통계 리포트 생성 | 실시간 사용자 클릭 분석, 이상 탐지 |
| **장점** | 안정적, 대규모 처리 적합, 정확성 높음 | 즉시 대응 가능, 실시간 분석 가능 |
| **단점** | 처리 지연 발생 가능 | 복잡한 설계 필요 |
| **핵심** | **정확성과 안정성 중심** | **실시간성과 즉시성 중심** |

#### 3. 데이터 저장소 개요 (Data Lakehouse)

* **데이터 레이크(Data Lake):** 원천 데이터(정형, 비정형)를 그대로 보존. 유연성 높음.
* **데이터 웨어하우스(Data Warehouse, DW):** 정제된 데이터를 스키마에 맞춰 저장. SQL 분석 용이.
* **데이터 레이크하우스(Lakehouse):** 데이터 레이크의 유연성과 DW의 관리 편의성을 결합한 형태.

### 파이프라인 설계 아키텍처

* **람다(Lambda) 아키텍처:** 배치 레이어(Batch)와 스피드 레이어(Speed/Stream)를 모두 운영하여 정확성과 실시간성을 모두 잡는 구조.
* **카파(Kappa) 아키텍처:** 람다의 복잡도를 줄이기 위해 모든 처리를 스트림으로 처리하는 구조. (배치 레이어 제거)

---

## 3. 리눅스(Linux)의 개념

* **유닉스(Unix):** 리눅스 탄생 이전의 OS. 높은 비용, 하드웨어 종속성.
* **리눅스(Linux):**
* **무료 & 오픈소스:** 누구나 자유롭게 사용, 수정, 배포 가능.
* **가볍고 빠른 성능:** 구형 하드웨어에서도 작동 가능, GUI 없이 CLI(Command Line Interface) 중심 운영 가능.
* **높은 점유율:** 전 세계 서버의 70% 이상이 리눅스 기반. (클라우드, 안드로이드 등)
* **개발 친화적:** Git, Docker, Python 등 개발 도구 활용에 최적화.



---

## 4. WSL (Windows Subsystem for Linux)

### WSL이란?

* Windows 환경에서 별도의 가상머신(VM) 없이 리눅스를 실행할 수 있도록 도와주는 도구.
* 윈도우 파일 시스템과 리눅스 도구를 동시에 사용 가능.
* **장점:** 가볍고 빠르며 설치가 간편함(오버헤드 적음).

### WSL 설치 및 설정 명령어 (상세)

아래 명령어들은 **PowerShell(관리자 권한)** 또는 WSL 터미널에서 실행됩니다.

**1. WSL 설치 (기본)**

```powershell
wsl --install
# Windows 10 (빌드 1903 이상) 또는 Windows 11 필요
# 설치 후 재부팅 필요할 수 있음

```

**2. 설치된 WSL 목록 및 버전 확인**

```powershell
wsl --list --verbose
# 또는
wsl -l -v

```

**3. 특정 배포판 종료 및 등록 해제 (초기화 시 유용)**

```powershell
# 실행 중인 Ubuntu-24.04 종료
wsl --terminate Ubuntu-24.04

# 설치된 배포판 삭제 (주의: 데이터 삭제됨)
wsl --unregister Ubuntu-24.04

```

**4. 기본 배포판 설정**

```powershell
# 특정 버전을 기본값으로 설정
wsl --set-default Ubuntu-22.04

```

**5. Ubuntu 계정 설정 (설치 직후)**

* 터미널 창이 열리면 `username`과 `password`를 입력하여 계정 생성.
* 참고: 비밀번호 입력 시 화면에 표시되지 않음.

**6. 패키지 삭제 관련 (문제 발생 시)**

```powershell
Get-AppxPackage *Ubuntu* | Remove-AppxPackage

```

---

## 5. 리눅스 기본 명령어 (Linux Basic Commands)

### 시작과 종료

* `exit`: WSL 터미널 종료.
* `poweroff`, `reboot`, `shutdown`: 리눅스 시스템 전원 관리 명령어이나, **WSL 특성상 자체적 부팅 구조가 아니므로 해당 명령어는 무시되거나 사용 불가**할 수 있음.

### Root 사용자 권한 (Superuser)

* **개념:** 시스템의 모든 권한을 가진 관리자 계정. 실수로 시스템 파일 삭제 시 복구 불가하므로 주의 필요.
* **권한 전환 명령어:**
```bash
# 현재 명령만 관리자 권한으로 실행
sudo [command]

# root 계정으로 로그인 (환경변수 포함)
sudo -i

# 현재 계정에서 비밀번호 변경
passwd

```



### 파일 생성, 편집, 복사, 삭제

| 명령어 | 설명 | 예시 | 비고 |
| --- | --- | --- | --- |
| `touch` | 빈 파일 생성 | `touch test.txt` | 타임스탬프 갱신용으로도 사용 |
| `echo` | 문자열 출력/파일쓰기 | `echo "Hello" >> hi.txt` | `>` (덮어쓰기), `>>` (이어쓰기) |
| `cat` | 파일 내용 출력 | `cat file.txt` |  |
| `head` / `tail` | 파일의 처음/끝 부분 출력 | `head -n 3 file.txt` | 로그 확인에 유용 |
| `cp` | 파일/폴더 복사 | `cp a.txt b.txt` <br>

<br> `cp -r dir1 dir2` | `-r`: 디렉토리 전체 복사 |
| `mv` | 파일 이동 또는 이름 변경 | `mv a.txt new.txt` |  |
| `rm` | 파일 삭제 | `rm test.txt` <br>

<br> `rm -rf [폴더]` | **주의:** `-rf`는 묻지 않고 강제 삭제 |

### 시스템 정보 및 프로세스

| 명령어 | 설명 | 예시 |
| --- | --- | --- |
| `ps` | 프로세스 상태 확인 | `ps aux |
| `kill` | 프로세스 종료 | `kill 1234` (PID 입력) |
| `top` | 실시간 자원(CPU/MEM) 모니터링 | `top` (종료는 q) |
| `uptime` | 시스템 가동 시간 확인 | `uptime` |
| `whoami` | 현재 사용자 확인 | `whoami` |
| `hostname` | 호스트명 확인 | `hostname` |

### 권한 설정 (chmod)

리눅스는 **소유자(User), 그룹(Group), 그 외(Other)**에 대해 **읽기(r), 쓰기(w), 실행(x)** 권한을 각각 부여합니다.

* **권한 점수:**
* **r (Read):** 4
* **w (Write):** 2
* **x (Execute):** 1


* **명령어 구조:** `chmod [User합][Group합][Other합] [파일명]`

**예시 코드:**

```bash
# sample.sh 파일의 권한 확인
ls -l sample.sh
# 결과: -rwxr--r-- (User: rwx, Group: r--, Other: r--)

# 권한 변경 예시 (755 설정)
# User(4+2+1=7), Group(4+0+1=5), Other(4+0+1=5)
chmod 755 sample.sh

```

### CLI 환경 관련

* `clear`: 터미널 화면 청소.
* `man [명령어]`: 명령어 매뉴얼(사용법) 보기 (종료는 `q`).