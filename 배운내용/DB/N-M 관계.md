
-----

````md
# Django: Many-to-Many (M:N) 관계 이해하기

이 문서는 Django 프레임워크에서 다대다(M:N) 관계를 설정하고 활용하는 방법에 대해 요약합니다.

## 1. M:N 관계의 필요성

-   하나의 모델이 다른 모델의 여러 인스턴스와 관계를 맺고, 그 반대도 성립하는 관계입니다.
-   **예시:** 병원 예약 시스템
    -   한 명의 **의사**는 여러 명의 **환자**를 진료할 수 있습니다.
    -   한 명의 **환자**는 여러 명의 **의사**에게 진료받을 수 있습니다.

---

## 2. N:1 관계의 한계

초기에 모델을 `ForeignKey` (N:1)로 설정할 경우 (예: 환자가 의사를 참조) 다음과 같은 한계가 발생합니다.

-   **데이터 무결성:** 환자는 오직 한 명의 의사만 예약할 수 있습니다.
-   **확장성 문제:** 환자가 여러 의사에게 예약하거나, 의사가 여러 환자를 받는 구조를 구현하기 어렵습니다.

---

## 3. 중개 모델 (Intermediate Model)

-   M:N 관계를 해결하기 위해 두 모델을 연결하는 **별도의 중간 모델**을 사용합니다.
-   **예시:** `Doctor` 모델과 `Patient` 모델 사이에 `Reservation` (예약) 모델을 만듭니다.
    -   `Reservation` 모델은 `Doctor`와 `Patient`에 대한 `ForeignKey`를 각각 가집니다.
    -   이를 통해 "어떤 의사가 어떤 환자를 예약했는지"를 기록하며 M:N 관계를 구현합니다.

```python
# 중개 모델을 직접 정의하는 방식
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    # ... 예약 시간, 증상 등 추가 정보 ...
````

-----

## 4\. `ManyToManyField`

Django는 M:N 관계를 더 쉽게 관리할 수 있도록 `ManyToManyField`를 제공합니다.

### 기본 사용

  - 두 모델 중 한쪽에 `ManyToManyField`를 정의하면, Django가 자동으로 **중개 테이블**을 생성하여 관계를 관리합니다.

<!-- end list -->

```python
class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    # doctors 필드 추가
    doctors = models.ManyToManyField(Doctor)
```

### 데이터 조작

  - `.add()`: 관계 추가
  - `.remove()`: 관계 제거
  - `.clear()`: 모든 관계 제거
  - `.all()`: 관련된 객체 쿼리셋 조회

<!-- end list -->

```python
# 환자1에게 의사1, 의사2 배정
patient1.doctors.add(doctor1, doctor2)

# 환자1의 모든 의사 조회
patient1.doctors.all()

# 의사1의 모든 환자 조회 (기본: 모델명_set)
doctor1.patient_set.all()
```

-----

## 5\. `through` 인자를 사용한 사용자 정의 중개 모델

`ManyToManyField`가 자동으로 생성하는 중개 테이블에는 \*\*추가 정보(예: 예약 시간, 증상)\*\*를 저장할 수 없습니다.

  - 이때 `through` 인자를 사용하여 우리가 직접 만든 **중개 모델**(`Reservation`)을 지정할 수 있습니다.

<!-- end list -->

```python
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation') # 'Reservation' 모델을 중개자로 지정

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    # M:N 관계 외의 추가 데이터
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

  - `through` 모델을 사용하면, 관계를 추가할 때 `Reservation` 객체를 직접 생성하거나 `.add()` 대신 `.create()`를 사용해야 합니다.

-----

## 6\. 기타 주요 인자

### `related_name`

  - 역참조 시 사용할 이름을 지정합니다. (기본값: `[모델명소문자]_set`)
  - **예시:** `ManyToManyField(Doctor, related_name='patients')`
      - `doctor1.patient_set.all()` 대신 `doctor1.patients.all()` 사용 가능.
  - **중요:** 하나의 모델이 다른 모델에 `ForeignKey`와 `ManyToManyField`를 동시에 가질 때, 역참조 이름 충돌(`article_set`)이 발생할 수 있으므로 `related_name` 설정이 권장됩니다.

### `symmetrical`

  - `ManyToManyField('self', ...)`처럼 자기 자신을 참조할 때 사용됩니다.
  - `True` (기본값): 대칭 관계 (A가 B를 팔로우하면, B도 A를 팔로우)
  - `False`: 비대칭 관계 (A가 B를 팔로우해도, B가 A를 팔로우하는 것은 아님 - '팔로우' 기능에 적합)

-----

## 7\. '좋아요(Like)' 기능 구현 예시

M:N 관계는 '좋아요' 기능 구현에 핵심적으로 사용됩니다.

  - **모델:** `User` 모델과 `Article` 모델
  - `Article` 모델에 `like_users = models.ManyToManyField(User, related_name='like_articles')` 필드를 추가합니다.
  - **View (로직):**
      - 이미 '좋아요'를 눌렀는지 확인 (`article.like_users.filter(pk=user.pk).exists()`)
      - **좋아요 추가:** `article.like_users.add(request.user)`
      - **좋아요 취소:** `article.like_users.remove(request.user)`

-----

## 8\. 핵심 키워드 요약

  - **M:N 관계:** 다대다 관계
  - **중개 모델 (Intermediate Model):** M:N 관계를 N:1 관계 두 개로 풀어내기 위한 중간 다리 역할의 모델.
  - **`ManyToManyField`:** Django에서 M:N 관계를 자동화하는 필드.
  - **`through`:** `ManyToManyField`에 사용자 정의 중개 모델을 지정하는 인자 (추가 데이터 저장 시 필수).
  - **`related_name`:** 역참조 시 사용할 이름을 지정하여 코드 가독성을 높이고 충돌을 방지함.

<!-- end list -->

```
```