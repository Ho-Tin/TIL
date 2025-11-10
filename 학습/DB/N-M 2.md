

# SSAFY - Database: Many To Many Relationships 02 (Python)

## 📑 목차

### 1\. 쿼리 개선 (Improve query)

  * 사전 준비
  * `annotate`
  * `select_related`
  * `prefetch_related`
  * `select_related` & `prefetch_related`

### 2\. 참고 (Reference)

  * `exists()` method
  * 한꺼번에 dump 하기
  * loaddata 인코딩 에러

-----

## 🎯 학습 목표

  * 팔로우 기능을 위한 N:M 모델을 설계하고 구현할 수 있다.
  * **Fixtures** (`dumpdata`, `loaddata`)를 활용하여 데이터 입출력을 효율화할 수 있다.
  * **`annotate`**, **`select_related`**, \*\*`prefetch_related`\*\*를 사용해 **N+1 문제**를 해결할 수 있다.
  * `exists` 등의 유틸 메서드를 활용한 성능 개선 방안을 이해한다.
  * 복잡한 쿼리 요구 상황에서 Django ORM 최적화 전략을 적용할 수 있다.

-----

## 1\. 팔로우 기능 구현

### \#\#\# 프로필 페이지

  * **URL 설정** (`accounts/urls.py`):
    ```python
    path('profile/<username>/', views.profile, name='profile'),
    ```
  * **프로필 페이지 링크 추가** (`index.html`):
      * 내 프로필: `<a href="{% url 'accounts:profile' user.username %}">내 프로필</a>`
      * 다른 유저 프로필: `<a href="{% url 'accounts:profile' article.user.username %}">`

### \#\#\# 모델 관계 설정 (User - User)

  * User와 User 간의 **M:N 관계**로 설정합니다.
  * 회원이 여러 명을 팔로우할 수 있고, 여러 명의 팔로워를 가질 수 있습니다.
  * `ManyToManyField`를 사용하며, 중간 테이블(`accounts_user_followings`)이 생성됩니다.

### \#\#\# 기능 구현

  * **View 함수** (`accounts/views.py`):
    ```python
    # accounts/views.py
    @login_required
    def follow(request, user_pk):
        User = get_user_model()
        person = User.objects.get(pk=user_pk)

        if person != request.user:
            if request.user in person.followers.all():
                # 팔로우 취소
                person.followers.remove(request.user)
            else:
                # 팔로우
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    ```
  * **프로필 템플릿** (`profile.html`):
      * 팔로잉/팔로워 수를 표시합니다.
    <!-- end list -->
    ```html
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    ```

-----

## 2\. Fixtures

Django 개발 시 데이터베이스 초기화 및 공유를 위해 사용되는 파일 형식입니다.

### \#\#\# 사용 목적

  * **초기 데이터 세팅**: 서비스 시작 시 필요한 기본 데이터(카테고리 등)를 미리 세팅합니다.
  * **테스트 샘플 데이터**: 테스트 환경에서 동일한 데이터로 반복 테스트가 가능합니다.
  * **협업 시 환경 통일**: 팀원 간 동일한 데이터 환경을 공유하여 테스트 효율을 높입니다.

### \#\#\# `dumpdata`

데이터베이스의 데이터를 내보내는(추출하는) 명령어입니다.

  * **기본 명령어**:
    ```bash
    $ python manage.py dumpdata [앱이름.모델이름] [옵션] > [출력파일.json]
    ```
  * 특정 앱 또는 모델을 지정할 수 있습니다. (미지정 시 프로젝트 전체)
  * `--indent 4` 옵션: JSON 파일의 가독성을 높여줍니다.
  * **예시**:
    ```bash
    # articles 앱의 comment 모델 데이터만 추출
    $ python manage.py dumpdata --indent 4 articles.comment > comments.json

    # accounts 앱의 user 모델 데이터만 추출
    $ python manage.py dumpdata --indent 4 accounts.user > users.json
    ```

### \#\#\# `loaddata`

`dumpdata`로 추출한 데이터 파일을 다시 데이터베이스에 반영(불러오는)하는 명령어입니다.

  * **실행 전 준비**:
    1.  앱 폴더 내에 `fixtures`라는 폴더를 생성합니다.
    2.  해당 폴더에 `dumpdata`로 생성한 `.json` 파일들을 위치시킵니다.
    3.  (필요시) `db.sqlite3` 파일을 삭제하여 데이터베이스를 초기화합니다.
  * **명령어**:
    ```bash
    $ python manage.py loaddata [fixture_파일이름.json]
    ```
  * **주의사항 (데이터 로드 순서)**:
      * 모델 간 **외래 키(FK) 관계**에 따라 로드 순서가 중요합니다.
      * 참조되는 모델(부모)이 먼저 로드되어야 합니다.
      * 예: `Comment` (N) -\> `Article` (1), `User` (1) 관계일 경우
        1.  `users.json`
        2.  `articles.json`
        3.  `comments.json`
      * 순서가 틀릴 경우 `IntegrityError` (무결성 오류)가 발생합니다.

-----

## 3\. 쿼리 개선 (Improve Query)

### \#\#\# N+1 Problem

> 1개의 쿼리를 실행했지만, 연관된 데이터를 추가로 가져오기 위해 **N개의 추가 쿼리가 실행되는 상황**을 의미합니다. 데이터가 많아질수록 DB 부하가 심각해집니다.

### \#\#\# `annotate()`

  * SQL의 `GROUP BY`와 집계 함수(`Count`, `Sum`, `Avg` 등)를 사용하여, 쿼리셋의 각 객체에 **계산된 필드를 추가**합니다.
  * **예시**: 각 게시글의 댓글 수를 한 번의 쿼리로 가져오기
    ```python
    # views.py
    from django.db.models import Count

    articles = Article.objects.annotate(comment_count=Count('comment')).order_by('-pk')
    ```
    ```html
    <p>댓글 수 : {{ article.comment_count }}</p>
    ```

### \#\#\# `select_related()`

  * **정참조 (N:1, 1:1)** 관계에서 사용됩니다. (ForeignKey, OneToOneField)
  * SQL의 \*\*`JOIN`\*\*을 사용하여 관련된 객체의 데이터를 **하나의 쿼리**로 함께 가져옵니다.
  * **N+1 문제 상황**: 게시글 목록에서 각 게시글의 작성자 이름(`article.user.username`)을 표시할 때, 게시글 수(N)만큼 추가 쿼리가 발생합니다.
  * **해결**:
    ```python
    # N+1 발생 코드
    articles = Article.objects.order_by('-pk')

    # select_related 적용 코드 (1번의 쿼리로 해결)
    articles = Article.objects.select_related('user').order_by('-pk')
    ```

### \#\#\# `prefetch_related()`

  * **역참조 (1:N)** 및 **M:N** 관계에서 사용됩니다.
  * `JOIN`을 사용하지 않고, Python 단에서 데이터를 합칩니다.
  * 기본 쿼리(1) + 관련 데이터 쿼리(1) = **총 2개의 쿼리**로 실행됩니다.
  * **N+1 문제 상황**: 게시글 목록에서 각 게시글의 댓글(`article.comment_set.all`)을 모두 표시할 때, 게시글 수(N)만큼 추가 쿼리가 발생합니다.
  * **해결**:
    ```python
    # N+1 발생 코드
    articles = Article.objects.order_by('-pk')

    # prefetch_related 적용 코드 (2번의 쿼리로 해결)
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    ```

### \#\#\# `select_related` & `prefetch_related` 동시 사용

  * 두 문제를 동시에 해결해야 할 때 함께 사용할 수 있습니다.
  * **N+1 문제 상황**: 게시글 목록에서 **작성자 이름**(`article.user.username`)과 **각 댓글의 작성자 이름**(`comment.user.username`)을 모두 표시할 때.
  * **해결**: `select_related`로 게시글의 작성자를, `prefetch_related`로 댓글 목록을 가져오되, 댓글의 작성자까지 `select_related`를 중첩 적용합니다.
    ```python
    # views.py
    from django.db.models import Prefetch

    articles = Article.objects.order_by('-pk') \
        .select_related('user') \
        .prefetch_related(
            Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
        )
    ```

-----

## 4\. 참고 (Reference)

### \#\#\# `exists()`

  * QuerySet에 결과가 **하나 이상 존재하는지 여부**를 확인합니다. (`True` / `False` 반환)
  * `if queryset:` 이나 `len(queryset)` 보다 훨씬 효율적입니다. (데이터를 실제로 가져오지 않고 존재 여부만 확인)
  * **적용 예시** (Follow 기능):
    ```python
    # 비효율적인 방식
    # if request.user in person.followers.all():

    # exists() 적용 방식
    if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
    ```

### \#\#\# 한꺼번에 `dumpdata` 하기

  * 여러 모델 또는 앱 전체를 한 번에 덤프할 수 있습니다.
    ```bash
    # 3개 모델 동시 덤프
    $ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

    # 프로젝트 전체 덤프
    $ python manage.py dumpdata --indent 4 > data.json
    ```

### \#\#\# `loaddata` 인코딩 문제

  * **에러**: `UnicodeDecodeError: 'utf-8' codec can't decode byte ...`
  * **원인**:
    1.  JSON 파일 생성 시 `UTF-8`이 아닌 다른 인코딩(예: `ASCII`)으로 저장되었는데 한글이 포함된 경우.
    2.  Windows(CP949) 환경에서 생성한 파일을 Linux(UTF-8) 환경에서 로드할 때.
  * **해결**: `dumpdata` 시점 또는 파일 저장 시 **인코딩을 `UTF-8`로 통일**해야 합니다.