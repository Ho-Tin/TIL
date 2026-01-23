
---

# MLFlow 데이터 실험 환경 구축 및 활용

## 1. 머신러닝 실험 환경의 필요성

### 머신러닝 실험이란?

* 모델의 성능을 개선하거나 다양한 설정을 비교 분석하기 위해 반복적으로 수행하는 **과정 중심의 실험 활동**.
* "어떤 데이터를 썼서", "어떤 알고리즘에", "어떤 하이퍼파라미터를 적용했더니", "어떤 결과가 나왔는지" 체계적으로 비교하는 작업.
* **과정:** Raw 데이터 → 전처리 된 데이터 → 실험설계(알고리즘, 튜닝) → Model 생성 → 결과 비교.

### 반복 실험의 문제점

* **비효율적인 반복 작업:** "똑같은 실험, 이미 했던 상황"이 발생하거나 기억에 의존하게 됨.
* **버전 관리의 문제:**
* "이 모델, 어떤 코드 버전에서 나온 거지?"
* 같은 `train.py` 파일인데 중간에 코드 바뀜.
* 파일명을 복사해서 `train2.py`, `train_final.py` 등으로 관리하여 혼란 발생.
* 데이터셋도 계속 갱신되면 이력이 안 남음.


* **결과 해석의 어려움:** 버그가 있는 코드에서 나온 모델이 어디에 쓰였는지 추적 불가능.

### 실험 추적 및 관리 도구의 필요성

* **필요성:** 반복 실험에서 발생하는 문제를 해결, 실험마다 사용된 코드/데이터/파라미터/지표 자동 기록, 실험 결과 비교 분석 인터페이스 제공.
* **MLflow:** 실험 추적 + 모델 저장 + 서빙까지 지원하는 통합 도구.
* 다양한 프레임워크와 호환성이 좋음.
* 실험 로그 관리뿐 아니라 모델 저장, 등록, 서빙까지 한번에 가능.



---

## 2. MLflow Tracking을 활용한 실험 관리 전략

### 실험 단위 구분 (Experiments vs Runs)

* **실험 그룹 (Experiment):** `baseline_rf_exp1`, `tuned_rf_exp2` 등 큰 틀의 프로젝트나 실험 주제.
* **실험 실행 (Run):** `max_depth=5`, `max_depth=10` 등 구체적인 파라미터나 데이터 조합에 따른 개별 실행.
* **파일명 형식 권장:** `모델명_전처리 방법_데이터셋 버전` 등으로 하면 명확함.

### 실험 태그 및 노트 관리 방법 (Code)

MLFlow는 메타 정보 태그화 및 검색이 가능합니다.

```python
# 태그 기록 예시
mlflow.set_tag("author", "kim")
mlflow.set_tag("description", "XGBoost with SMOTE")
mlflow.set_tag("data_version", "v2.1")

```

* **용도:** 작성자 이름, 실험 목적, 참고 사항, 사용한 데이터 버전 등 기록.

### 아티팩트(Artifact) 저장 방법 (Code)

결과 이미지(그래프 등)나 파일을 저장하여 UI에서 바로 확인 가능.

```python
# 아티팩트 저장 예시
mlflow.log_artifact("confusion_matrix.png")
mlflow.log_artifact("roc_curve.png")

```

### 실험 자동화 흐름 예시 (Code)

모든 실험 조합을 만들기 위해 Python `itertools` 등을 활용.

```python
import itertools
import yaml

# YAML 파일에 정의된 조건 로드
with open('config.yaml') as f:
    config = yaml.safe_load(f)

keys, values = zip(*config.items())
combinations = [dict(zip(keys, v)) for v in itertools.product(*values)]

# 조합 별 실험 실행
for comb in combinations:
    params = comb
    run_experiment(params)

```

* **config.yaml 예시:**
```yaml
learning_rate: [0.01, 0.001]
batch_size: [16, 32]
optimizer: ['adam', 'sgd']

```



### 실험 관리 팁

1. **실험명 관리:** 실험 목적, 날짜 포함.
2. **Jupyter 요약 정리:** `mlflow.search_runs()`로 테이블 생성하여 비교.
3. **중단 대비 로깅:** `try-finally`로 중간 로그 남기기.

---

## 3. MLflow 하이퍼파라미터 튜닝 (Hyperopt)

### Hyperopt란?

* 머신러닝 모델의 하이퍼파라미터 튜닝을 자동으로 수행해주는 라이브러리.
* **특징:**
* **목적 기반 최적화:** 단순 반복이 아닌 성능을 기반으로 검색.
* 이전 결과 학습(Bayesian Optimization 등)을 통해 다음 탐색 위치를 정교하게 조정.
* GridSearch보다 빠르게 수렴 가능.
* 다양한 공간 지원(실수형, 정수형, 조건부 파라미터 등).



---

## 4. MLflow 모델 관리 및 배포

### Model Stages (모델 상태 관리)

MLFlow Model Registry에서 모델의 상태를 변경하며 관리 가능.

* **None:** 초기 등록 상태.
* **Staging:** 성능 검증 후 테스트 환경 배포 단계.
* **Production:** 실제 서비스에 배포된 모델.
* **Archived:** 더 이상 사용하지 않는 예전 버전 모델.

### 모델 저장 위치 설정 (Code)

로컬 디스크 혹은 S3, GCS 같은 원격 저장소 사용 가능.

```bash
# MLflow 서버 실행 명령어 예시
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root s3://my-bucket/mlruns

```

### 모델 배포(Serving) 전략

MLflow 모델을 API로 서빙하여 예측 서비스 제공.

**1. 기본 구성 (RESTful API)**

* `/invocations` 엔드포인트로 JSON 데이터를 POST 요청.

**2. MLflow 모델 서빙 명령어 (Code)**

```bash
# 모델 서빙 실행
mlflow models serve -m runs:/<run_id>/model -p 5000

```

**3. 예측 요청 테스트 (cURL Code)**

```bash
curl -X POST http://localhost:5000/invocations \
    -H "Content-Type: application/json" \
    -d '{"columns":["feat1", "feat2"], "data":[[1, 2]]}'

```

**4. 서빙 엔진 선택**

* **FastAPI (기본):** 로컬 테스트, 일반 서비스용.
* **MLServer (고성능/확장형):** 고성능 대규모 서비스, Kubernetes 배포 시 적합 (Seldon/Kserve 연동).

---

## 5. 실전 구현 코드 (요약 없음)

### 하이퍼파라미터 최적화 및 모델 로깅 저장

`Hyperopt`와 `MLflow`를 연동하여 최적의 파라미터를 찾고, 모델을 저장하는 전체 코드 구조입니다.

```python
import mlflow
import mlflow.sklearn
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
from sklearn.model_selection import train_test_split
# 기타 필요한 라이브러리 import

def objective(params):
    # 하이퍼 파라미터 값 로깅
    with mlflow.start_run():
        mlflow.log_params(params)
        
        # 데이터 분할 및 모델 학습
        train_x, valid_x, train_y, valid_y = train_test_split(data, target, test_size=0.25, random_state=42)
        
        # 모델 생성 및 학습 (예: XGBoost, LightGBM 등)
        model = train_model(params, train_x, train_y, valid_x, valid_y)
        
        # 예측 및 평가
        accuracy = evaluate_model(model, valid_x, valid_y)
        loss = 1 - accuracy
        
        # 평가지표 로깅
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("loss", loss)
        
        # 모델 저장 (Signature 포함 권장)
        signature = infer_signature(train_x, model.predict(train_x))
        mlflow.sklearn.log_model(model, "model", signature=signature)
        
        return {'loss': loss, 'status': STATUS_OK, 'model': model}

# 탐색 공간 정의 (Hyperopt)
space = {
    'lr': hp.loguniform('lr', -5, -1),
    'num_leaves': hp.choice('num_leaves', [16, 32, 64]),
    # ... 추가 파라미터
}

# 최적화 실행
trials = Trials()
best = fmin(fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=10,
            trials=trials)

print("Best Parameters:", best)

```

### REST API 배포 후 요청 (Python Client)

로컬에서 실행 중인 MLflow Model Server (Port 5002)에 예측 요청을 보내는 코드입니다.

```python
import requests
import pandas as pd

# 예측할 데이터 준비
data = pd.DataFrame({
    "fixed acidity": [7.0, 0.27], 
    "volatile acidity": [0.36, 20.7],
    # ... (기타 feature들)
    "density": [0.9978, 1.001],
    "pH": [3.0, 0.45],
    "sulphates": [0.45, 0.88],
    "alcohol": [8.8, 8.8]
})

# MLflow Serving 포맷에 맞게 변환 (dataframe_split or dictionary orientation)
# 예시에서는 data frame orient='records' 또는 'split' 사용 가능. 
# 영상 코드 기준:
body = {
    "dataframe_records": data.to_dict(orient="records")
}

# POST 요청
response = requests.post(
    "http://localhost:5002/invocations",
    headers={"Content-Type": "application/json"},
    json=body
)

print(response.json())

```