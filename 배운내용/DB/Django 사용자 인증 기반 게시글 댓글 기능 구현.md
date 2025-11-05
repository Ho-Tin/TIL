

````md
# Django: 사용자 인증 기반 게시글/댓글 기능 구현

이 문서는 Django 프로젝트에서 사용자 모델(User model)과 게시글(Article), 댓글(Comment) 모델을 연동하여 인증 기반의 CRUD 기능을 구현하는 방법을 요약합니다.

---

## 1. Article & User 연동

### 1-1. 모델 관계 설정 (N:1)

`Article` 모델이 `User` 모델을 참조하도록 N:1 관계(외래 키)를 설정합니다.

* `articles/models.py`
    * `User` 모델은 직접 참조하지 않고 `settings.AUTH_USER_MODEL`을 사용하는 것을 권장합니다.
    * `on_delete=models.CASCADE`: 사용자가 삭제되면 해당 사용자가 작성한 모든 게시글도 함께 삭제됩니다.

```python
# articles/models.py
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
````

### 1-2. Migration

기존 테이블에 `user`라는 `NOT NULL` 필드를 추가하면, `makemigrations` 실행 시 기본값을 설정하라는 메시지가 나타납니다.

1.  `python manage.py makemigrations`
2.  `1) Provide a one-off default now` 선택
3.  기본값으로 사용할 user\_id (보통 '1') 입력
4.  `python manage.py migrate` 실행
5.  결과: `articles_article` 테이블에 `user_id` 컬럼이 생성됩니다.

### 1-3. 게시글 CREATE (생성)

**문제점**: `ModelForm`을 그냥 사용하면, 게시글 작성 시 글쓴이를 선택하는 드롭다운이 노출됩니다. 이는 보안상/기능상 올바르지 않습니다.

**해결책**:

1.  **Form 변경**: `forms.py`의 `ArticleForm`에서 `fields` 리스트에 `user`를 제외합니다.

    ```python
    # articles/forms.py
    class ArticleForm(forms.ModelForm):
        class Meta:
            model = Article
            fields = ('title', 'content',) # 'user' 필드 제거
    ```

2.  **View 변경**: `views.py`의 `create` 함수에서 `request.user` (현재 로그인한 사용자) 정보를 받아와 `article` 객체에 저장합니다.

      * `form.save(commit=False)`: DB에 바로 저장하지 않고, 인스턴스만 생성합니다.
      * `article.user = request.user`: 인스턴스의 `user` 필드에 현재 로그인한 사용자를 할당합니다.
      * `article.save()`: 변경 사항을 DB에 저장합니다.

    <!-- end list -->

    ```python
    # articles/views.py
    from django.contrib.auth.decorators import login_required

    @login_required
    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False) # 임시 저장
                article.user = request.user       # 작성자 정보 할당
                article.save()                    # DB에 저장
                return redirect('articles:detail', article.pk)
        # ... (GET 요청 처리)
    ```

### 1-4. 게시글 READ (조회)

템플릿에서 `article.user` (또는 `article.user.username`)를 통해 작성자 정보를 출력할 수 있습니다.

```html
<p>작성자 : {{ article.user }}</p>
<p>글 번호 : {{ article.pk }}</p>
<p>글 제목 : {{ article.title }}</p>
<p>글 내용 : {{ article.content }}</p>
```

### 1-5. 게시글 UPDATE & DELETE (수정/삭제)

게시글 수정/삭제 기능은 **글 작성자 본인**에게만 노출되어야 합니다.

1.  **템플릿 (Template)**: `if` 태그를 사용하여 현재 로그인한 사용자(`request.user`)와 게시글 작성자(`article.user`)가 동일한지 확인합니다.

    ```html
    {% if request.user == article.user %}
      <a href="{% url 'articles:update' article.pk %}">UPDATE</a>
      <form action="{% url 'articles:delete' article.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
    {% endif %}
    ```

2.  **뷰 (View)**: `update` 및 `delete` 함수 내부에서도 `request.user == article.user`인지 다시 한번 확인하여 권한이 없는 접근을 서버단에서 차단합니다.

-----

## 2\. Comment & User 연동

`Comment` 모델은 `Article` (어느 게시글의 댓글인지)과 `User` (누가 작성한 댓글인지) 모두와 N:1 관계를 가집니다.

### 2-1. 모델 관계 설정

```python
# articles/models.py
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    # ...
```

### 2-2. 댓글 CREATE (생성)

게시글 생성 로직과 유사하게 `commit=False`를 사용합니다.

```python
# articles/views.py
@require_POST
def comments_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 임시 저장
        comment.article = article                 # 게시글 정보 할당
        comment.user = request.user               # 작성자 정보 할당
        comment.save()
    return redirect('articles:detail', article.pk)
```

### 2-3. 댓글 DELETE (삭제)

게시글 삭제 로직과 동일하게, 템플릿과 뷰 양쪽에서 작성자 본인인지 확인합니다.

1.  **템플릿 (Template)**:
    ```html
    {% for comment in comments %}
      <li>
        {{ comment.user }} - {{ comment.content }}
        {% if request.user == comment.user %}
          <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="DELETE">
          </form>
        {% endif %}
      </li>
    {% endfor %}
    ```
2.  **뷰 (View)**:
    ```python
    # articles/views.py
    @require_POST
    def comments_delete(request, article_pk, comment_pk):
        if not request.user.is_authenticated:
            return redirect('accounts:login')
        
        comment = Comment.objects.get(pk=comment_pk)
        if request.user == comment.user: # 본인 확인
            comment.delete()
        return redirect('articles:detail', article_pk)
    ```

-----

## 3\. View Decorators

View 함수의 수정을 가하거나 추가 기능을 제공하는 Python 데코레이터입니다.

  * `@login_required`: 사용자가 로그인되어 있는지 확인합니다.
  * `@require_http_methods([...])`: 허용된 HTTP 요청 방식(GET, POST 등)을 제한합니다.
      * `@require_POST()`: POST 요청만 허용합니다.
      * `@require_http_methods(['GET', 'POST'])`: GET과 POST 요청만 허용합니다.
      * 허용되지 않은 메서드로 요청 시 405 (Method Not Allowed) 에러를 반환합니다.

-----

## 4\. ERD (Entity Relationship Diagram)

데이터베이스의 구조를 시각적으로 표현하는 다이어그램입니다.

### 4-1. ERD 구성 요소

  * **Entity (엔티티)**: 저장되는 데이터의 단위 (ex: '회원', '게시글'). DB의 **테이블**에 해당합니다.
  * **Attribute (속성)**: 엔티티가 가지는 고유한 항목 (ex: '이름', '내용'). DB의 **컬럼**에 해당합니다.
  * **Relationship (관계)**: 엔티티 간의 관계 (ex: '회원'이 '게시글'을 작성한다). 외래 키(FK) 등으로 표현됩니다.

### 4-2. Cardinality (관계 표현)

관계의 수를 나타내며, **"Crow's foot (까마귀발)"** 표기법이 많이 사용됩니다.

  * `|` : One
  * `O` : Zero
  * `<` (까마귀발) : Many

> 예: `User` (1) --- `Article` (N)
> 한 명의 유저는 여러 개의 게시글을 작성할 수 있습니다. (1:N)

### 4-3. 무료 ERD 제작 사이트

  * **Draw.io (diagrams.net)**
  * **ERDCloud (www.erdcloud.com)**

<!-- end list -->

```
```