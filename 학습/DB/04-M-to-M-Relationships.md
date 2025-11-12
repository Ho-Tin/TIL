
-----

`Django_M2M_Summary.md`

````md
# Django Many-to-Many Relationships - 중개 모델과 좋아요 기능

이 문서는 Django(장고)의 Many-to-Many(M:N) 관계 설정, 중개 모델, `ManyToManyField` 사용법 및 '좋아요' 기능 구현 예제를 요약합니다. (SSAFY 10기 강의 자료 기반)

## 1. M:N 관계의 필요성 및 N:1의 한계

M:N(다대다) 관계는 하나의 레코드가 다른 테이블의 여러 레코드와 연결되고, 그 반대도 마찬가지인 관계를 의미합니다.

* **예시**: '병원 예약 시스템'에서 **환자(Patient)** 1명은 여러 **의사(Doctor)**에게 예약할 수 있고, **의사** 1명도 여러 **환자**를 받을 수 있습니다.
* **N:1의 한계**: `ForeignKey` (N:1)를 사용하면, 환자 모델이 단 하나의 의사 외래 키만 가질 수 있습니다.
    * `patient.doctor = doctor1`
* **문제점**:
    1.  환자가 다른 의사에게 예약하려면, 별개의 환자 데이터(새로운 레코드)를 만들어야 하므로 **데이터 중복**이 발생합니다.
    2.  하나의 필드에 여러 ID를 (`'1, 2'`) 저장하는 것은 데이터베이스의 **제1정규형(1NF)**을 위배하며 불가능합니다.
    3.  이러한 한계를 해결하기 위해 별도의 연결 테이블, 즉 **중개 모델**이 필요합니다.

---

## 2. 중개 모델 (Intermediate Model)

M:N 관계는 두 모델을 직접 연결하는 것이 아니라, 두 모델의 ID를 `ForeignKey`로 갖는 **중개 테이블(Intermediate Table)**을 통해 구현됩니다.

### 1) 수동 중개 모델 (N:1 + N:1)

`ManyToManyField`를 사용하지 않고 직접 중개 모델을 정의할 수 있습니다. 예를 들어 `Reservation` (예약) 모델을 만듭니다.

```python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()

# Doctor와 Patient 사이의 중개 모델
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
````

  * `Reservation` 모델은 `doctor_id`와 `patient_id`를 외래 키로 가집니다.
  * 데이터베이스에는 `hospitals_reservation` 테이블이 생성됩니다.

### 2\) Django `ManyToManyField`

Django는 이 중개 테이블 생성을 자동화하는 `ManyToManyField`를 제공합니다.

```python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    # M:N 관계 설정
    doctors = models.ManyToManyField(Doctor)
```

  * `Patient` 모델에 `ManyToManyField`를 정의하면, Django가 자동으로 `hospitals_patient_doctors`라는 중개 테이블을 생성합니다. (규칙: `[앱이름]_[모델이름]_[필드이름]`)
  * 이 자동 생성된 테이블에는 `id`, `patient_id`, `doctor_id` 컬럼만 존재합니다.

-----

## 3\. `ManyToManyField` 사용법

`ManyToManyField`는 관계를 관리하기 위한 특별한 메서드(Manager)를 제공합니다.

  * **.add()**: 관계에 데이터 추가
    ```python
    patient1.doctors.add(doctor1)
    patient1.doctors.add(doctor2, doctor3) # 여러 개 동시 추가 가능
    ```
  * **.remove()**: 관계에서 데이터 제거 (객체 자체가 삭제되지는 않음)
    ```python
    patient1.doctors.remove(doctor1)
    ```
  * **.clear()**: 모든 관계 제거
    ```python
    patient1.doctors.clear()
    ```
  * **.all()**: 관계된 모든 객체 조회 (역참조 포함)
    ```python
    # 환자1이 예약한 모든 의사 조회
    patient1.doctors.all()
    # <QuerySet [<Doctor: 1번 의사 allie>]>

    # (역참조) 의사1에게 예약한 모든 환자 조회
    # 기본 역참조 이름은 '모델명_set'
    doctor1.patient_set.all()
    # <QuerySet [<Patient: 1번 환자 carol>]>
    ```

-----

## 4\. 'through' 옵션: 중개 모델 사용자 정의

기본 `ManyToManyField`가 자동 생성하는 중개 테이블에는 `id`와 두 모델의 `id` 외에 **추가 데이터를 저장할 수 없습니다.**

  * **문제**: 예약 `증상(symptom)`, `예약 시간(reserved_at)` 등 관계 자체에 대한 추가 정보 저장이 불가능합니다.
  * **해결**: `through` 옵션을 사용하여 Django에게 **사용자 정의 중개 모델**을 사용하도록 명시합니다.

<!-- end list -->

```python
# hospitals/models.py

class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    # 'Reservation' 모델을 중개 모델로 사용함을 명시
    doctors = models.ManyToManyField(Doctor, through='Reservation')

# 사용자 정의 중개 모델
class Reservation(models.Model):
    # M:N 관계로 묶일 두 모델을 ForeignKey로 정의
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # 관계에 대한 추가 데이터
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)
```

  * **주의**: `through`를 사용하면 `.add()`, `.clear()` 등을 사용할 수 없습니다. 대신, **중개 모델(`Reservation`)의 인스턴스를 직접 생성/삭제**해야 합니다.
    ```python
    # 데이터 생성
    reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom='headache')
    reservation1.save()

    # 데이터 삭제
    reservation1.delete()
    # 또는 M:N 매니저의 .remove() 사용 가능 (중개 모델 인스턴스가 삭제됨)
    doctor1.patient_set.remove(patient1)
    ```

-----

## 5\. 기타 주요 속성

### 1\) `related_name` (역참조 이름)

  * `doctor.patient_set.all()`처럼, 역참조 시 기본 이름은 `[모델명_소문자]_set` 입니다.
  * 이 이름을 명확하게 변경하거나, **역참조 충돌**을 피하기 위해 `related_name`을 사용합니다.

<!-- end list -->

```python
class Article(models.Model):
    # 작성자 (N:1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 좋아요 누른 사람 (M:N)
    # related_name을 지정하지 않으면 user.article_set이 중복되어 충돌
    like_users = models.ManyToManyField(User, related_name='like_articles')
```

  * `user.article_set.all()`: 유저가 **작성한** 모든 글 (N:1 역참조)
  * `user.like_articles.all()`: 유저가 **좋아요 누른** 모든 글 (M:N 역참조, `related_name` 사용)

### 2\) `symmetrical` (대칭 관계)

  * M:N 관계가 \*\*자기 자신(`self`)\*\*을 참조할 때 사용됩니다. (예: User 모델의 '친구' 관계)
  * `symmetrical=True` (기본값): 대칭 관계. A가 B의 친구이면, B도 A의 친구입니다.
  * `symmetrical=False`: 비대칭 관계. (예: 트위터 팔로우. A가 B를 팔로우해도, B가 A를 팔로우하는 것은 아님). Django는 이 경우 역참조 관계를 만들지 않습니다.

-----

## 6\. 실습: '좋아요' 기능 구현

`User`와 `Article` 간의 M:N 관계를 이용해 '좋아요' 기능을 구현합니다.

### 1\) 모델 (`models.py`)

`Article` 모델에 `User`와의 M:N 관계(`like_users`)를 추가합니다. `related_name`을 설정하여 작성자(`user`)와의 관계와 충돌을 피합니다.

```python
# articles/models.py
from django.conf import settings

class Article(models.Model):
    # 작성자 (N:1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    # 좋아요 (M:N)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                          related_name='like_articles')
```

### 2\) 뷰 (`views.py`)

좋아요 버튼을 눌렀을 때, 이미 좋아요를 누른 상태면 취소(remove)하고, 아니면 추가(add)합니다.

```python
# articles/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    # 현재 유저가 이 글의 like_users 목록에 있는지 확인
    if request.user in article.like_users.all():
        # 있다면, 좋아요 취소 (M:N 관계 제거)
        article.like_users.remove(request.user)
    else:
        # 없다면, 좋아요 (M:N 관계 추가)
        article.like_users.add(request.user)
        
    return redirect('articles:index')
```

### 3\) URL (`urls.py`)

```python
# articles/urls.py
urlpatterns = [
    ...
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

## 7\. 핵심 키워드 요약

  * **N:M 관계**: 다대다 관계
  * **중개 모델**: M:N 관계를 구현하기 위한 중간 테이블 (N:1 + N:1)
  * **ManyToManyField**: Django에서 중개 테이블을 자동으로 관리해주는 필드
  * **through**: 자동 생성되는 중개 테이블 대신, 사용자 정의 중개 모델을 사용하도록 지정하는 옵션 (추가 데이터 저장 시)
  * **related\_name**: 역참조 시 사용할 이름을 지정 (역참조 충돌 방지)
  * **symmetrical**: `self` 참조 시 대칭 여부 설정 (기본값 True)
  * **역참조 충돌**: 하나의 모델이 다른 모델을 N:1, M:N 등 여러 관계로 참조할 때 `_set` 이름이 겹치는 문제.

<!-- end list -->

```
```