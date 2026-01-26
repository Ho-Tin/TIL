
---

# MLFlow 기본 구조와 세팅

## 1. MLOps 개념 및 MLFlow의 역할

### 1.1 머신러닝 프로세스의 한계점

* **데이터 품질과 양에 대한 의존성 문제:** 대부분의 실제 데이터는 노이즈와 불완전한 데이터가 많아 모델 성능 저하의 원인이 됨.
* **특징 추출의 어려움:** 특정 도메인 전문가가 수동으로 특징을 추출해야 하므로 비용과 시간이 많이 소요됨.
* **새로운 상황에 대한 대응 문제:** 학습된 데이터의 범위 내에서만 정확한 예측이 가능함.
* **모델 해석의 어려움:** 복잡한 모델일수록 내부 동작 방식을 이해하기 어려움.
* **데이터 분포 변화에 대한 민감성:** 시간 흐름에 따른 데이터 분포 변화(Drift)에 기존 모델 성능 저하.
> **해결책:** 이러한 한계를 극복하기 위해 **딥러닝**과 **MLOps** 등의 새로운 접근법이 개발됨.



### 1.2 MLOps의 필요성

* **반복 실험의 체계화:** 수많은 하이퍼파라미터 조합 실험, 데이터 전처리 방식 및 피처 선택 변화, 실험 결과 비교를 위한 자동 기록 필요.
* **협업 효율성 향상:** 여러 팀원이 같은 실험을 반복하지 않음, 실험 결과를 다른 사람과 쉽게 공유, 버전 관리로 변경 사항 추적 용이.
* **재현성 확보:** 시간이 지나도 재현 가능한 구조 (동일한 코드 + 데이터 + 환경 -> 동일한 결과).
* **추적성 확보:** 어떤 실험에 어떤 성능이 나왔는지 확인 (실험 조건, 환경, 결과가 모두 기록됨).

### 1.3 자동화 구조로서의 MLOps (CI / CT / CD)

* **CI (Continuous Integration):**
* 코드 변경 시 자동 테스트 -> 코드 품질 보장.
* 코드(모델 스크립트, 파이프라인) 변경 시 자동으로 통합 및 테스트.
* 데이터 전처리 코드, 모델 구조 변경 사항 포함.


* **CT (Continuous Training):**
* 데이터 변화에 따른 재학습 -> 최신 모델 유지.
* 새로운 데이터가 들어오면 모델을 자동으로 재학습.
* 정기적 스케줄 또는 이벤트 기반으로 작동.
* 실험 추적 도구(MLFlow)와 함께 사용 시 강력함.


* **CD (Continuous Delivery):**
* 모델 자동 배포 -> 운영 자동화, 실시간 대응.
* 학습이 완료된 모델을 자동으로 서빙 환경에 배포.
* REST API 형태, 클라우드 환경 등 다양하게 적용 가능.



### 1.4 MLFlow란?

* **비유:** 붕어빵 장사를 한다고 가정.
1. 여러 시범 착오를 겪으며 요리 (반죽 양, 굽는 시간 등 = **하이퍼파라미터**)
2. 가장 맛있는 붕어빵 레시피 발견 (가장 성능 좋은 **모델 선택**)
3. 실험하면서 만들어진 붕어빵 (**Artifact, 이미지, 로그** 등)
4. 각 붕어빵에 대한 정보 (맛, 재료, 칼로리 등 = **메타데이터**)
5. 물, 슈크림, 김치 붕어빵 판매 (**여러 모델 운영**)


* **정의:** 이 모든 과정을 기록하고 관리하는 도구가 **MLFlow**.



---

## 2. MLFlow 주요 구성 요소

MLFlow는 머신러닝 전체 수명 주기를 관리하기 위한 4대 컴포넌트를 제공합니다.

### 2.1 Tracking

* 머신러닝 실험과 실행을 체계적으로 관리하기 위한 API와 UI를 제공.
* 각 실험은 여러 실행(Run)으로 구성되며, 실행 간 비교를 통해 최적의 모델을 선정.
* **주요 기능:**
* **Parameter (파라미터):** 모델 학습에 사용된 입력 데이터들(Key-Value 쌍) 저장 및 추적.
* **Metric (지표):** 모델의 성능 지표 (예: 정확도, 손실 함수 값 등)를 숫자 형태로 저장 및 추적.
* **Artifact (산출물):** 모델 파일, 이미지, 데이터 파일 등 실험 결과로 생성된 모든 형식의 파일을 저장 및 추적.
* **Source (소스코드):** 실행에 사용된 Git 커밋 해시 등을 기록하여 코드 버전을 추적.
* **Tags:** 실험을 설명하는 커스텀 라벨.



### 2.2 Projects

* 머신러닝 코드를 **재사용하고 재현성 있게 패키징**하기 위한 표준 형식을 제공.
* 데이터 과학자들은 일관된 환경에서 코드를 실행하고 공유할 수 있음.
* `conda.yaml` 등을 통해 의존성과 파라미터를 정의.

### 2.3 Models

* 머신러닝 모델을 다양한 환경에서 일관되게 패키징하고 배포하기 위한 표준 형식을 제공.
* **Model Flavor:** 다양한 라이브러리(Scikit-learn, PyTorch 등)와 프레임워크 지원 및 호환성 유지.
* 저장 구조: 각 모델은 디렉터리 형태로 저장되며, `MLmodel` 파일이 위치하여 메타데이터를 포함함.

### 2.4 Model Registry

* 머신러닝 모델의 **전 생애 주기를 체계적으로 관리**하기 위한 중앙 집중화된 저장소.
* **주요 기능:**
* 모델 버전 관리: 각 모델의 버전을 체계적으로 관리.
* 모델 단계(Stage) 관리: `Staging` -> `Production` -> `Archived` 등 배포 단계 관리.
* 모델의 상태를 태그로 추가하거나 설명을 기록 가능.



---

## 3. MLFlow 설치 및 실행

### 3.1 설치 및 버전 확인

```bash
# 터미널 명령어
mlflow --version  # 버전 확인
mlflow ui         # UI 실행

```

* 접속 주소: `http://127.0.0.1:5000`

### 3.2 Tracking Server 실행

```bash
# backend-store-uri: 실험 메타데이터를 저장할 DB 지정 (예: sqlite)
# default-artifact-root: 모델 플롯 등 Artifact를 저장할 기본 경로
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns \
  --host 127.0.0.1 \
  --port 5000

```

* **주의사항:** `0.0.0.0`으로 설정하면 외부에서 서버 접근이 가능하므로 보안에 유의해야 함.

---

## 4. 실습: 간단한 분류 모델 로깅 (Iris 데이터셋)

### 4.1 모델 로깅 실습 코드 (Python)

동영상 내 슬라이드에 포함된 Iris 데이터셋 학습 및 MLFlow 기록 코드입니다.

```python
import mlflow
import mlflow.sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Iris dataset 로드
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Train/Test 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# MLFlow 실험 시작
with mlflow.start_run():
    # 파라미터 설정
    params = {
        "solver": "lbfgs",
        "max_iter": 1000,
        "multi_class": "auto",
        "random_state": 8888
    }

    # 모델 정의 및 학습
    lr = LogisticRegression(**params)
    lr.fit(X_train, y_train)

    # 예측
    predictions = lr.predict(X_test)

    # Metrics 계산
    accuracy = accuracy_score(y_test, predictions)
    # (다른 metric 계산 코드 생략 가능성 있음, 화면상 visible한 부분 위주)

    # MLFlow에 기록 (Logging)
    mlflow.log_params(params)           # 파라미터 기록
    mlflow.log_metric("accuracy", accuracy) # 성능 지표 기록
    mlflow.sklearn.log_model(lr, "model")   # 모델 저장
    
    print(f"Accuracy: {accuracy}")

```

### 4.2 실행 결과 확인

* **UI 결과:** Parameters 탭에서 `solver`, `max_iter` 등이 기록되고, Metrics 탭에서 `accuracy` 등이 기록됨.
* **Artifacts:** `model.pkl` 파일, `MLmodel` 파일, `conda.yaml` 등이 저장됨.
* **예측 수행:** 저장된 모델을 불러와서 새로운 데이터에 대한 예측 수행 가능.

---

## 5. ML 프로젝트 생성 및 실행 실습

### 5.1 프로젝트 구조

실습 디렉토리는 다음과 같은 파일 구조를 가집니다.

* `~/mlflow/`
* `mlruns/` : 실험 기록 저장 디렉토리
* `Iris_train.ipynb` : 기본 노트북 코드
* `MLproject` : 프로젝트 실행 정의 파일
* `conda.yaml` : 실행 환경 정의 (선택)
* `python_train.py` : 실제 실행 코드



### 5.2 MLproject 파일 내용

프로젝트의 진입점(Entry point)과 파라미터, 실행 명령어를 정의합니다.

```yaml
name: IrisProject

conda_env: conda.yaml

entry_points:
  main:
    parameters:
      C: {type: float, default: 1.0}
    command: "python train.py --C {C}"

```

### 5.3 conda.yaml 파일 내용

프로젝트 실행에 필요한 가상환경 및 의존성을 정의합니다.

```yaml
name: iris_env
channels:
  - defaults
dependencies:
  - python=3.10
  - scikit-learn
  - pip
  - pip:
    - mlflow

```

### 5.4 프로젝트 실행 및 비교

CLI를 통해 프로젝트를 실행하고, 파라미터 `C` 값을 변경하여 비교합니다.

* **실행 확인:** `Experiment ID`와 `Run_id`가 일치하는지 확인하여 로컬 파일에 성공적으로 저장되었는지 확인.
* **UI 비교:** MLFlow UI의 'Parallel Coordinates Plot' 등을 통해 다양한 `C` 값(하이퍼파라미터)에 따른 성능 변화를 시각적으로 비교 분석 가능.