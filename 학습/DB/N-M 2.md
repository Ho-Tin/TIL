
-----

# SSAFY - Database: Many To Many Relationships 02 (Python)

이 자료는 Django의 M:N 관계를 활용한 팔로우 기능 구현, 데이터 관리를 위한 Fixtures, 그리고 성능 최적화를 위한 쿼리 개선 방법을 상세히 다룹니다.

## 🎯 학습 목표

  * 팔로우 기능을 위한 N:M 모델 설계 및 구현
  * **Fixtures** (`dumpdata`, `loaddata`)를 활용한 효율적인 데이터 입출력
  * `annotate`, `select_related`, `prefetch_related`를 사용한 **N+1 문제** 해결
  * `exists` 유틸 메서드를 활용한 성능 개선
  * Django ORM 최적화 전략 적용

-----

## 1\. 팔로우 기능 구현

### \#\#\# 1. 프로필 페이지 (URL 및 템플릿)

팔로우 기능을 구현하기 전에, 사용자의 프로필 페이지를 설정합니다.

  * **URL 설정** (`accounts/urls.py`):

      * 사용자 이름(username)을 URL 파라미터로 받아 해당 유저의 프로필 페이지를 M:N으로 연결합니다.

    <!-- end list -->

    ```python
    # accounts/urls.py
    urlpatterns = [
        ...
        path('profile/<username>/', views.profile, name='profile'),
    ]
    ```

  * **템플릿 링크** (`index.html` 등):

      * **내 프로필**로 이동하는 링크 (`index.html`):
        ```html
        <a href="{% url 'accounts:profile' user.username %}">내 프로필</a>
        ```
      * **다른 유저 프로필**로 이동하는 링크 (`articles/index.html`):
        ```html
        <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user.username }}</a>
        ```
      * views 
        ```python
        # accounts/views.py
        def profile(request, username):
            User = get_user_model()
            person = User.objects.get(username=username)
            context = {
                'person': person,
                
            }
            return render(request, 'accounts/profile.html', context)
        ```

### \#\#\# 2. 모델 관계 설정 (User-User)

User 모델이 자신(User)을 팔로우하는 M:N 관계를 설정합니다.

  * **개념**: User(M) - User(N)
      * 한 명의 유저(A)는 여러 명(N)의 유저를 팔로우할 수 있습니다. (Followings)
      * 한 명의 유저(B)는 여러 명(M)의 유저에게 팔로우될 수 있습니다. (Followers)
  * **구현**:
      * `ManyToManyField`를 `User` 모델에 추가합니다.
      * `'self'` 키워드를 사용하여 자기 자신과의 관계를 정의합니다.
      * `symmetrical=False`로 설정하여 비대칭 관계(A가 B를 팔로우해도 B가 A를 팔로우하는 것은 아님)를 만듭니다.
      * `related_name='followers'`를 설정하여 `user.followers`로 접근할 수 있게 합니다.
      * (참고) `user.followings`는 기본적으로 `User` 모델이 참조하는 필드명이 됩니다.
  * **중간 테이블**: 이 관계를 설정하면 Django는 `accounts_user_followings`와 같은 중간 테이블을 자동으로 생성합니다. (컬럼: `id`, `from_user_id`, `to_user_id`)
  * 
        ```python
        # accounts/models.py
        class User(AbstractUser):
            following = models.ManyToManyField('self', symetrical=False, related_name='followers')
        ```

### \#\#\# 3. 팔로우 기능 View 및 템플릿

  * **View 함수** (`accounts/views.py`):

      * `follow` 함수는 `user_pk`를 받아 해당 유저(`person`)를 찾습니다.
      * `request.user`(로그인 유저)가 `person.followers`에 이미 있는지 확인합니다.
      * **있으면** `remove` (팔로우 취소), **없으면** `add` (팔로우)를 실행합니다.

    <!-- end list -->

    ```python
    # accounts/views.py
    @login_required
    def follow(request, user_pk):
        User = get_user_model()
        you = User.objects.get(pk=user_pk)
        me = request.user
        if you != me:
            if me in you.followers.all():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    ```

  * **템플릿** (`profile.html`):

      * `followings.all|length`와 `followers.all|length`를 사용해 팔로잉/팔로워 수를 표시합니다.

    <!-- end list -->

    ```html
    <h1>{{ person.username }}님의 프로필</h1>
    ...
    <div>
        팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
    </div>
    ```

-----

## 2\. Fixtures (데이터 입출력)

**Fixtures**는 Django 개발 시 데이터베이스의 데이터를 내보내고(dump) 불러와서(load) 초기 데이터 세팅, 테스트, 협업을 용이하게 하는 기능입니다.

### \#\#\# 1. `dumpdata` (데이터 내보내기)

데이터베이스의 현재 데이터를 JSON, XML, YAML 형식의 파일로 추출합니다.

  * **사용 목적**: 데이터 백업, 다른 환경으로 데이터 이전
  * **기본 명령어**:
    ```bash
    $ python manage.py dumpdata [앱이름.모델이름] [옵션] > [출력파일.json]
    ```
  * **옵션**:
      * `--indent 4`: JSON 파일의 가독성을 높이기 위해 들여쓰기를 적용합니다.
  * **예시**:
    ```bash
    # articles 앱의 comment 모델 데이터만 추출
    $ python manage.py dumpdata --indent 4 articles.comment > comments.json

    # accounts 앱의 user 모델 데이터만 추출
    $ python manage.py dumpdata --indent 4 accounts.user > users.json

    # 여러 모델 한꺼번에 추출
    $ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json
    ```

### \#\#\# 2. `loaddata` (데이터 불러오기)

`dumpdata`로 생성한 fixture 파일을 읽어 데이터베이스에 데이터를 반영합니다.

  * **사전 준비 (중요)**:
    1.  데이터를 로드할 **각 앱 폴더** 내에 `fixtures`라는 이름의 폴더를 생성합니다.
    2.  생성한 `fixtures` 폴더 안에 `.json` 파일들을 위치시킵니다.
    3.  (선택) `db.sqlite3` 파일을 삭제하여 데이터베이스를 깨끗한 상태에서 시작할 수 있습니다.
  * **명령어**:
    ```bash
    $ python manage.py loaddata [fixture_파일이름1.json] [fixture_파일이름2.json] ...
    ```
  * **⚠️ 주의: 로드 순서**
      * `loaddata`는 **외래 키(FK) 관계**를 고려해야 합니다.
      * 참조되는 부모 모델(예: `User`, `Article`)이 먼저 로드되어야 합니다.
      * **잘못된 순서 예시**: `Comment` (User와 Article을 참조)를 `User`나 `Article`보다 먼저 로드하면 `IntegrityError` (무결성 오류)가 발생합니다.
      * **올바른 순서 예시**:
        ```bash
        $ python manage.py loaddata users.json articles.json comments.json
        ```

-----

## 3\. 쿼리 개선 (Improve Query)

### \#\#\# 1. N+1 Problem

**N+1 문제**는 1개의 쿼리를 실행한 후, 그 결과(N개)에 대해 연관된 데이터를 가져오기 위해 N개의 추가 쿼리가 발생하는 심각한 성능 저하 문제입니다.

### \#\#\# 2. `annotate()` (집계)

쿼리셋의 각 객체에 대해 `GROUP BY`와 `Count`, `Sum` 같은 집계 함수를 적용하여 **계산된 필드를 추가**합니다.

  * **N+1 상황**: 게시글 목록(N개)을 보면서 각 게시글의 댓글 수(`article.comment_set.count()`)를 표시할 때, N번의 추가 쿼리 발생.
  * **해결**: `annotate`를 사용해 `comment_count`라는 필드를 미리 계산합니다.
    ```python
    # views.py
    from django.db.models import Count

    def index(request):
        articles = Article.objects.annotate(comment_count=Count('comment')).order_by('-pk')
        context = {'articles': articles}
        return render(request, 'articles/index_1.html', context)
    ```
    ```html
    <p>댓글 수 : {{ article.comment_count }}</p>
    ```

### \#\#\# 3. `select_related()` (정참조 N:1)

**정참조 (N:1, 1:1)** 관계 (예: `ForeignKey`)에서 `JOIN`을 사용하여 관련 데이터를 **하나의 쿼리**로 미리 가져옵니다.

  * **N+1 상황**: 게시글 목록(N개)에서 각 게시글의 작성자 이름(`article.user.username`)을 표시할 때, N번의 추가 쿼리 발생.
  * **해결**: `select_related('user')`를 사용하여 게시글을 가져올 때 `user` 데이터도 함께 `JOIN`합니다.
    ```python
    # views.py
    def index(request):
        # N+1 발생 코드
        # articles = Article.objects.order_by('-pk')
        
        # 해결 코드 (1개의 쿼리)
        articles = Article.objects.select_related('user').order_by('-pk')
        context = {'articles': articles}
        return render(request, 'articles/index_2.html', context)
    ```
    ```html
    <p>작성자 : {{ article.user.username }}</p>
    ```

### \#\#\# 4. `prefetch_related()` (역참조 1:N, M:N)

**역참조 (1:N, M:N)** 관계에서 `JOIN`이 아닌 **별도의 쿼리** (총 2개)를 실행한 후, Python이 데이터를 조합하여 성능을 향상시킵니다.

  * **N+1 상황**: 게시글 목록(N개)에서 각 게시글의 댓글 목록(`article.comment_set.all`)을 표시할 때, N번의 추가 쿼리 발생.
  * **해결**: `prefetch_related('comment_set')`를 사용하여 게시글 쿼리(1) + 모든 댓글 쿼리(1) = 총 2개의 쿼리로 해결합니다.
    ```python
    # views.py
    def index(request):
        # N+1 발생 코드
        # articles = Article.objects.order_by('-pk')
        
        # 해결 코드 (2개의 쿼리)
        articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
        context = {'articles': articles}
        return render(request, 'articles/index_3.html', context)
    ```
    ```html
    {% for comment in article.comment_set.all %}
        <p>{{ comment.content }}</p>
    {% endfor %}
    ```

### \#\#\# 5. `select_related` + `prefetch_related` (중첩 최적화)

  * **최악의 N+1 상황**: 게시글 목록(N) -\> 각 게시글의 댓글 목록(M) -\> 각 댓글의 작성자(`comment.user.username`) (N\*M).
  * **해결**: `prefetch_related` 내부에 `Prefetch` 객체를 사용하여 중첩 `select_related`를 적용합니다.
    ```python
    # views.py
    from django.db.models import Prefetch

    def index(request):
        articles = Article.objects.order_by('-pk') \
            .select_related('user') \  # 1. 게시글 작성자 (N:1)
            .prefetch_related(          # 2. 댓글 목록 (1:N)
                Prefetch('comment_set', queryset=Comment.objects.select_related('user')) # 3. 댓글 작성자 (N:1)
            )
        ...
    ```

-----

## 4\. 참고 (Reference)

### \#\#\# 1. `exists()` 메서드

`QuerySet`에 데이터가 \*\*존재하는지 여부(`True`/`False`)\*\*만 빠르고 효율적으로 확인합니다. 데이터를 실제로 가져오지 않기 때문에 `if queryset:` 또는 `len(queryset)`보다 성능이 우수합니다.

  * **기존 `follow` View (비효율적)**:
    ```python
    if request.user in person.followers.all(): # .all()이 모든 데이터를 가져옴
    ```
  * **`exists()` 적용 (효율적)**:
    ```python
    # accounts/views.py (개선)
    def follow(request, user_pk):
        ...
        if person != request.user:
            # .filter()는 쿼리셋만 반환 (DB 접근 X)
            # .exists()가 DB에 존재 여부만 확인 (효율적)
            if person.followers.filter(pk=request.user.pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        ...
    ```

### \#\#\# 2. loaddata 인코딩 문제

  * **문제**: `loaddata` 실행 시 `UnicodeDecodeError: 'utf-8' codec can't decode ...` 발생.
  * **원인**:
    1.  JSON 파일이 `UTF-8`이 아닌 `ASCII` 등으로 저장되었을 때 (주로 Windows).
    2.  Windows(CP949) 환경에서 생성한 파일을 Linux(UTF-8) 환경에서 로드할 때.
  * **해결**: `dumpdata` 시점부터 파일 인코딩이 `UTF-8`로 일관되게 유지되도록 관리해야 합니다.

-----

## 5\. 요약 정리

1.  **팔로우 기능**: `User` 모델에 `ManyToManyField('self', symmetrical=False)`를 사용하여 M:N 관계를 구현합니다.
2.  **Fixtures**: `dumpdata`로 데이터를 추출하고 `loaddata`로 데이터를 로드합니다. (로드 시 FK 순서 주의)
3.  **쿼리 최적화**:
      * `annotate`: 집계 데이터가 필요할 때 사용 (`Count`).
      * `select_related`: N:1 관계 (FK) 최적화 (`JOIN`).
      * `prefetch_related`: 1:N, M:N 관계 최적화 (별도 쿼리).
      * `exists`: 데이터 존재 여부만 효율적으로 확인할 때 사용.
