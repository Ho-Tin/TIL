 ***

# Authentication System

## Cookie & Session

### HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약  
- **비 연결 지향**
  - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음  
- **무상태 (stateless)**
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음  
  - 따라서 로그인 상태를 유지할 수 없음  

### 쿠키
- 서버가 사용자의 웹 브라우저에 전송하는 데이터 조각  
- 서버가 제공하며 클라이언트 측에 저장되는 작은 데이터 파일  

#### 쿠키 저장 방식
- 브라우저는 **KEY-VALUE 형식**으로 쿠키 저장  
- 쿠키에는 이름, 값 외에도 만료시간, 도메인, 경로 등의 추가 속성이 포함됨  

#### 쿠키 전송 과정
1. 서버는 HTTP 응답 헤더의 **Set-Cookie** 필드를 통해 클라이언트로 쿠키 전송  
2. 브라우저는 받은 쿠키를 저장  
3. 동일한 서버에 재요청 시, HTTP 요청 헤더의 **Cookie 필드**에 저장된 쿠키를 함께 전송  

#### 쿠키 주요 용도
- 동일한 브라우저에서 들어온 요청인지 판단  
- 사용자의 로그인 상태 유지  
- 상태가 없는 HTTP 프로토콜에서 상태정보를 기억시켜주는 역할  

#### 쿠키 사용 목적
- **세션 관리**: 로그인, 자동완성, 장바구니 등  
- **개인화**: 사용자 테마, 언어 설정 저장  
- **트래킹**: 사용자 행동 기록 및 분석  

### 세션
- 서버 측에서 생성되어 클라이언트와 서버 간 상태를 유지하는 데이터 저장 방식  
- **쿠키와 세션의 목적**
  - 클라이언트와 서버 간 상태 정보를 유지  
  - 사용자를 식별  

***

## Django Authentication System
- 사용자 인증과 관련된 기능을 모아 놓은 시스템  

### Authentication
- 사용자가 자신이 누구인지 확인하는 과정  

### 사전 준비
1. `accounts` 앱 생성 및 등록  
   - 계정 관련 앱 이름은 **accounts**로 짓는 것이 관례  

### User 모델
- Django 기본 User 모델은 username, password 등 제한된 필드를 제공  
- 추가 사용자 정보가 필요하면 변경이 어려움  

### Custom User Model
1. `AbstractUser` 클래스를 상속받는 커스텀 User 클래스 작성  

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass  # 추후 확장을 위해 pass 사용
```

2. `settings.py`에서 `AUTH_USER_MODEL`을 변경  

```python
# settings.py
AUTH_USER_MODEL = 'accounts.User'
```

3. 관리자(admin) 사이트에 User 모델 등록  

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

- **주의사항**: 프로젝트 중간에는 `AUTH_USER_MODEL`을 변경할 수 없음  
- 새 프로젝트 시작 시, 기본 User 모델이 충분해 보이더라도 커스텀 User 모델을 사용하는 것을 권장  

***

## Login

- 로그인은 **세션을 생성(Create)** 하는 과정  

### AuthenticationForm
- 로그인 인증에 사용할 데이터를 입력받는 **Django built-in form**  

```python
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

### 로그인 유저 정보 출력
- Django에서는 기본적으로 `user` 객체 제공  
- 템플릿에서 로그인한 유저 이름 출력 가능  
- get_user()
  - 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환
```django
{{ user.username }}
```

***
# Django 회원 관리 정리

## 로그아웃
- 로그아웃은 **세션을 삭제하는 과정**이다.
- `logout(request)` 함수 사용 예시:

```python
# accounts/views.py
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

***

## AbstractUser class
- 관리자 권한과 함께 완전한 기능을 가지고 있는 **User 모델을 구현하는 추상 클래스**.
- **Abstract base classes(추상 기본 클래스)**  
  - 여러 다른 모델에 공통 정보를 넣을 때 사용하는 클래스.  
  - 데이터베이스 테이블은 생성되지 않는다.  

***

## 회원가입
- 회원가입은 **세션 생성 과정**이다.
- Django에서 기본 제공하는 `UserCreationForm`을 사용한다.

```python
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

### 커스텀 User 모델 적용
- 기본 `UserCreationForm` 대신 **커스텀 User 모델**을 연결해야 한다.

```python
# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
```

- `get_user_model()`  
  - 현재 프로젝트에서 활성화된 사용자 모델을 반환.
  - Django는 직접 `User` 클래스를 참조하지 않고, `get_user_model()`을 사용할 것을 권장한다.

```python
# accounts/views.py
from .forms import CustomUserCreationForm
from django.shortcuts import redirect, render

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
```

***

## 회원 탈퇴
- 회원탈퇴는 **User 객체 삭제 과정**이다.

```python
def delete(request):
    request.user.delete()
    return redirect("articles:index")
```

- 회원 탈퇴 시 세션 데이터까지 삭제하려면 **탈퇴 후 로그아웃** 순서로 진행한다.  
  (순서를 바꿀 경우 객체 정보가 없어져 오류 발생)

```python
from django.contrib.auth import logout as auth_logout

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect("articles:index")
```

***

## 인증된 사용자 접근 제한

### is_authenticated 속성
- 사용자 로그인 여부를 확인할 수 있는 User 모델의 속성 (`True` 또는 `False`).
- 템플릿에서 `{% if request.user.is_authenticated %}` 사용 가능.
- 이미 로그인된 사용자가 로그인/회원가입 페이지에 접근하지 못하도록 제한한다.

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
```

### login_required 데코레이터
- 인증된 사용자만 특정 view 함수를 실행할 수 있도록 함.
- 예: 인증된 사용자만 게시글 작성 가능하게 하기

```python
# articles/views.py
from django.contrib.auth.decorators import login_required

@login_required
def create(request):
    pass
```

***

## 회원가입 후 자동 로그인
- 회원가입 시 즉시 로그인하려면 `auth_login` 함수 사용.

```python
from django.contrib.auth import login as auth_login

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # 자동 로그인 추가
            return redirect('articles:index')
```

### 회원정보 수정
- User 객체를 Update 하는 과정
- `UserChangeForm()`
  - 회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm
```
# forms.py
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)
```

```
# views.py
def update(request):
    
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form
        }
    return render(request, 'accounts/update.html', context)
```
### 비밀번호 변경
- 암호 변경시 세션 무효화
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게됨으로 로그아웃 ㅇ처리됨
    - `update_session_auth_hash(request, user)`를 사용하여 sessin 자동 갱
    - 
```
# views.py
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash # 세션 유지를 위한 함수

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user) # 세션 유지를 위한 함수
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form':form
        }
    return render(request, 'accounts/change_password.html', context)
```
Here is the organized and expanded Markdown file version of your notes:  

***

# 비밀번호 암호화 정리

## 비밀번호 암호화의 중요성
- 최근 수많은 해킹 사고가 발생하면서 **비밀번호 암호화**는 보안에서 매우 중요한 요소가 됨.  
- 데이터베이스가 유출되더라도 원문의 비밀번호를 알 수 없게 해야 함.  
- 이를 위해 비밀번호를 **복원이 불가능한 고정된 길이의 문자열**로 변환해 저장하는 방식이 사용됨.  

***

## 해시(Hash)
- **해시(Hash)란?**  
  임의의 크기를 가진 데이터를 고정된 크기의 **고유한 값**으로 변환하는 것.

### 해시 함수의 특징
- 입력값이 **얼마나 길든** 항상 **고정된 길이**의 결과물(해시값)이 나옴.
- 원래의 입력값을 알아낼 수 없는 **단방향 함수**.
- 입력값이 1글자만 달라져도 완전히 다른 해시값이 출력됨. (*눈사태 효과*)
- 같은 입력값을 넣으면 언제나 동일한 해시값이 나옴.
- 작은 변화에도 해시값이 크게 달라지므로 **데이터 변조 여부 확인에 활용 가능**.

***

## SHA-256
- SHA(Secure Hash Algorithm) 계열의 한 방식.  
- 어떤 데이터를 입력하더라도 **256비트(64자리 16진수)** 길이의 해시값을 출력.  
- 현재 널리 사용되는 안전한 해시 방식 중 하나.  

예시)  
```
입력: abc
출력: ba7816bf8f01cfea414140... (256비트 고정 길이 값)
```

***

## 공격 기법과 대응

### 1. 레인보우 테이블(Rainbow Table)
- 공격자가 자주 사용되는 비밀번호를 미리 **수백만~수십억 개 해시값**으로 계산해둔 거대한 "정답지".
- 데이터베이스 해시값과 대조하여 빠르게 원문 비밀번호를 유추할 수 있음.

### 2. 솔트(Salt)
- 같은 비밀번호라도 **임의의 문자열(Salt)** 을 붙여 해시 처리.  
- 동일한 비밀번호를 사용하더라도 항상 **다른 해시값**이 생성되도록 보호.  
- 레인보우 테이블 공격을 사실상 무력화시킴.

### 3. 무차별 대입 공격(Brute Force Attack)
- 가능한 모든 비밀번호를 대입해 해시값이 일치하는지 검사하는 방식.
- 비밀번호가 짧거나 단순하면 빠르게 해킹됨.  
- 따라서 **비밀번호 길이와 복잡성**이 중요.

### 4. 키 스트레칭(Key Stretching)
- 해시 함수를 단 한 번이 아니라 **수천~수만 번 반복** 적용.  
- 공격자가 비밀번호를 추측하는 데 필요한 연산량을 기하급수적으로 늘림.  
- 예: PBKDF2, bcrypt, scrypt, Argon2 등이 이를 구현한 알고리즘.

***

## Django의 비밀번호 저장 방식
- Django는 비밀번호를 다음 형식으로 저장함:

```
<algorithm>$<iterations>$<salt>$<hash>
```

- **algorithm** : 어떤 해시 알고리즘을 사용했는지  
- **iterations** : 몇 번 반복해 해싱했는지 (키 스트레칭)  
- **salt** : 랜덤하게 붙인 문자열  
- **hash** : 실제 비밀번호 해시값  

예시)  
```
pbkdf2_sha256$600000$Salt12345$abcdef123456...
```

이 방식 덕분에 Django는 단순 해킹 시도로부터 사용자의 비밀번호를 안전하게 보호할 수 있음.

***

비밀번호 암호화는 단순히 해시 함수를 쓰는 것을 넘어 **솔트 + 키 스트레칭 + 안전한 알고리즘**을 조합해야 강력한 보안성을 갖출 수 있음.

