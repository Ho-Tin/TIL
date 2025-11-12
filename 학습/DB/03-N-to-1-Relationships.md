요청하신 SSAFY 'Database: Many To One Relationships' 강의 영상의 주요 내용을 바탕으로 Markdown(.md) 파일을 작성했습니다.

-----

# Django Many-to-One Relationships - ForeignKey와 댓글 CRUD 구현

## 📑 목차 (Table of Contents)

  * **Many to one relationships**
      * 모델 관계 (Model Relationship)
      * 댓글 모델 정의 (Comment Model Definition)
      * 댓글 생성 연습 (Comment Creation Practice)
  * **관계 모델 참조 (Relational Model Reference)**
      * 역참조 (Reverse Reference)
  * **댓글 구현 (Comment Implementation)**
      * 댓글 CREATE
      * 댓글 READ
      * 댓글 DELETE

-----

## 1\. Many to one relationships

### 🔗 모델 관계 (Model Relationship)

  * **모델 관계의 종류**
      * `1:1 (One to One)`
      * **`N:1 (Many to One)`**
      * `N:M (Many to Many)`
  * **`N:1 (Many to One)` 정의**
      * 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계입니다.
  * **N:1 관계 예시**
      * `Comment(N) : Article(1)` (댓글 : 게시글)
      * `Student(N) : SSAFY Track(1)` (학생 : 트랙)
      * `Account(N) : Bank(1)` (계좌 : 은행)

### 💬 댓글과 게시글의 관계 (Comment & Article)

  * **관계 정의**: `Comment(N) : Article(1)`
      * 하나의 게시글(1)에 여러 개의 댓글(N)이 작성될 수 있습니다. (0개 이상)
  * **Foreign Key (외래 키) 위치**
      * 외래 키는 **N쪽 (Comment)** 테이블에 위치해야 합니다.
      * `Comment` 모델에 `article_id` 필드를 생성하여 `Article` 모델을 참조합니다.
      * *이유: 만약 `Article(1)` 쪽에 FK를 두면, 댓글이 생길 때마다 게시글 정보가 중복 저장되어 데이터 낭비가 발생합니다.*

### 📝 댓글 모델 정의 (Comment Model Definition)

  * **`ForeignKey(to, on_delete)`** 필드를 사용하여 N:1 관계를 정의합니다.
  * **`to`**: 참조할 모델 (e.g., `Article`)
  * **`on_delete`**: 참조하는 부모 객체(게시글)가 삭제될 때의 동작을 정의합니다.
      * **`CASCADE`**: 부모 객체(게시글) 삭제 시, 이를 참조하는 객체(댓글)도 함께 삭제됩니다.
      * **`PROTECT`**: 참조하는 객체(댓글)가 존재하면 부모 객체(게시글) 삭제가 금지됩니다. (Error 발생)
      * **`SET_NULL`**: 부모 객체 삭제 시, 참조 필드(e.g., `article_id`)를 `NULL`로 설정합니다. (단, 필드에 `null=True` 옵션이 필요합니다.)
  * **Migration 결과**:
      * `models.py`에 `ForeignKey` 필드를 정의하고 `migrate`하면, 실제 DB 테이블에는 `[필드명]_id` (e.g., `article_id`)라는 이름의 컬럼이 생성됩니다.

### ➕ 댓글 생성 연습 (Comment Creation Practice)

1.  **게시글 정보 없이 저장 시도 (Error 발생)**

      * 게시글(Article) 정보 없이 댓글(Comment) 저장을 시도하면 `article_id`가 `NOT NULL` 제약 조건에 위배되어 `IntegrityError`가 발생합니다.

    <!-- end list -->

    ```python
    comment = Comment(content='first comment')
    comment.save()
    # IntegrityError: NOT NULL constraint failed: articles_comment.article_id
    ```

2.  **게시글 객체를 참조하여 저장 (성공)**

      * 먼저 참조할 `Article` 객체를 조회해야 합니다.
      * `comment` 인스턴스의 `article` 필드에 조회한 `article` 객체를 할당한 후 저장합니다.

    <!-- end list -->

    ```python
    # 1번 게시글 조회
    article = Article.objects.get(pk=1)

    comment = Comment(content='first comment')

    # 방법 1: 객체 자체를 할당
    comment.article = article
    comment.save()

    # (참고) 방법 2: _id 필드에 PK 값을 직접 할당
    # comment.article_id = article.pk 
    # comment.save()
    ```

3.  **참조 객체 접근**

      * 댓글 객체를 통해 게시글 정보에 쉽게 접근할 수 있습니다.
      * `comment.article` \# 참조하는 Article 객체
      * `comment.article.pk` \# 참조하는 게시글의 PK
      * `comment.article.content` \# 참조하는 게시글의 내용

-----

## 2\. 관계 모델 참조 (Relational Model Reference)

### 🔍 특정 게시글의 댓글 조회 (Querying)

  * **잘못된 방법 (Wrong)**:
      * `Comment.objects.all()`: 특정 게시글이 아닌, DB의 **모든** 댓글을 가져옵니다.
  * **올바른 방법 (Correct - `filter` 활용)**:
      * `article = Article.objects.get(pk=1)`
      * `comments = Comment.objects.filter(article=article)`

### 🔄 역참조 (Reverse Reference)

  * **정의**: 1쪽(Article)에서 N쪽(Comment)을 참조(조회)하는 방법입니다.
  * **`related_manager`**:
      * Django는 N:1 관계에서 1쪽이 N쪽을 쉽게 참조할 수 있도록 `[N쪽 모델명]_set` (e.g., `comment_set`)이라는 이름의 `related_manager`를 자동으로 생성합니다.
  * **사용법**: `[1쪽 모델 인스턴스].[N쪽 모델명]_set.QuerySetAPI()`
  * **예시**:
    ```python
    # 1번 게시글 조회
    article = Article.objects.get(pk=1)

    # 1번 게시글에 달린 모든 댓글 조회 (역참조)
    comments = article.comment_set.all()
    ```

-----

## 3\. 댓글 구현 (Comment Implementation)

### ✅ 댓글 CREATE

1.  **`CommentForm` 정의 (`forms.py`)**

      * 사용자에게는 `content` 필드만 입력받도록 `fields`를 설정합니다. (`article` 필드는 view 함수에서 처리)

    <!-- end list -->

    ```python
    # articles/forms.py
    class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('content',) # '__all__'이 아님
    ```

2.  **HTML 템플릿 (`detail.html`)**

      * `CommentForm`을 렌더링하는 `<form>` 태그를 작성합니다.
      * `action` URL에는 댓글을 작성할 게시글의 `pk`(`article.pk`)가 필요합니다.

    <!-- end list -->

    ```html
    <form action="{% url 'articles:comments_create' article.pk %}" method="POST">
      {% csrf_token %}
      {{ comment_form }}
      <input type="submit">
    </form>
    ```

3.  **`comments_create` View 함수 (`views.py`)**

      * **`save(commit=False)`**: DB에 바로 저장하지 않고, 인스턴스만 반환받습니다.
      * 반환받은 `comment` 인스턴스에 `article` 정보를 추가(할당)합니다.
      * 이후 `.save()`를 호출하여 DB에 최종 저장합니다.

    <!-- end list -->

    ```python
    # articles/views.py
    def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # commit=False: DB에 바로 저장하지 않고 인스턴스만 생성
            comment = comment_form.save(commit=False)
            
            # 인스턴스에 게시글 정보(참조) 할당
            comment.article = article
            
            # DB에 저장
            comment.save()
        return redirect('articles:detail', article.pk)
    ```

### 📖 댓글 READ

  * `detail` View 함수에서 해당 게시글의 댓글 목록을 **역참조**로 조회하여 `context`에 추가합니다.
  * **`views.py`**:
    ```python
    # articles/views.py
    def detail(request, pk):
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm()
        
        # 역참조를 통해 댓글 목록 조회
        comments = article.comment_set.all() 
        
        context = {
            'article': article,
            'comment_form': comment_form,
            'comments': comments, # 댓글 목록을 context에 추가
        }
        return render(request, 'articles/detail.html', context)
    ```
  * **`detail.html`**:
      * `{% for %}` 태그로 댓글 목록을 순회합니다.
      * **`{% for empty %}`**: `comments`가 비어있을 경우(댓글이 없는 경우) 표시할 대체 콘텐츠를 지정합니다.
    <!-- end list -->
    ```html
    {% for comment in comments %}
      <p>{{ comment.content }}</p>
      {% empty %}
      <p>아직 댓글이 없습니다. 첫 번째 댓글을 작성해주세요.</p>
    {% endfor %}
    ```

### ❌ 댓글 DELETE

  * `comments_delete` View 함수를 정의합니다.
  * 삭제할 댓글(`comment`)을 `pk`로 조회한 뒤 `.delete()` 메서드를 호출합니다.
  * 삭제 후, 해당 댓글이 있던 게시글(`comment.article.pk`)의 상세 페이지로 `redirect`합니다.
  * **`views.py`**:
    ```python
    # articles/views.py
    # URL에서 article_pk와 comment_pk를 모두 받아야 함
    def comments_delete(request, article_pk, comment_pk):
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    ```

-----

## 4\. 💡 활동 정리 (Summary)

1.  게시글(1)과 댓글(N)은 **N:1** 관계입니다.
2.  N:1 관계를 모델에 정의하기 위해 **`ForeignKey`** 필드를 **N쪽(Comment)** 모델에 정의합니다.
3.  1쪽(Article)에서 N쪽(Comment)을 조회할 때는 \*\*역참조 (`.comment_set.all()`)\*\*를 사용하면 편리합니다.
4.  댓글 생성 시(View) `save(commit=False)`를 활용하여, 인스턴스에 `article` 정보를 추가(참조)한 뒤 DB에 저장합니다.
5.  댓글이 없을 때를 처리하기 위해 DTL(템플릿)의 `{% for empty %}` 태그를 활용할 수 있습니다.