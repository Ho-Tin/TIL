
### 1\. 사전 준비 및 API 구성

먼저 `articles` 앱의 `Article`과 `Comment` 모델에 대한 마이그레이션을 생성합니다.

```bash
$ python manage.py makemigrations articles

Migrations for 'articles':
  articles/migrations/0001_initial.py
    + Create model Article
    + Create model Comment
```

이후 `comments/` (댓글 목록), `comments/1/` (단일 댓글), `rticles/1/comments/` (게시글의 댓글 생성)와 같이 URL 및 HTTP 메서드(GET, POST, PUT, DELETE)를 구성합니다.

### 2\. GET 메서드 (조회)

`ModelSerializer`를 기반으로 `CommentSerializer`를 만들어 댓글 목록 및 단일 댓글을 조회하는 View 함수를 작성합니다.

  * **댓글 목록 (`comment_list`)**

    ```python
    # articles/views.py

    from .models import Article, Comment
    from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

    @api_view(['GET'])
    def comment_list(request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    ```

  * **단일 댓글 (`comment_detail`)**

    ```python
    # articles/urls.py
    urlpatterns = [
        ...,
        path('comments/<int:comment_pk>/', views.comment_detail),
    ]
    ```

    ```python
    # articles/views.py
    @api_view(['GET'])
    def comment_detail(request, comment_pk):
        # 특정 댓글 데이터 조회
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    ```

### 3\. POST 메서드 (생성)

게시글에 속한 댓글을 생성(`POST .../articles/1/comments/`)할 때, 요청 본문(body)이 아닌 URL에서 게시글 ID(`article`)를 받아옵니다.

이때 `CommentSerializer`에서 `article` 필드를 \*\*`read_only_fields`\*\*로 지정하여 유효성 검사에서 제외시킵니다.

```python
# articles/serializers.py

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',) 
```

### 4\. DELETE & PUT 메서드 (삭제 및 수정)

단일 댓글(`.../api/v1/comments/{{comment_pk}}/`)에 대한 삭제 및 수정 요청은 성공 시 `204 No Content` 상태 코드를 응답합니다.

### 5\. 역참조 데이터 구성 (N -\> 1)

댓글을 조회할 때, 댓글이 속한 게시글의 단순 ID가 아닌 **게시글 제목**(`title`)까지 함께 보여주는 방법입니다.

  * 별도의 `ArticleTitleSerializer`를 정의합니다.
    ```python
    # articles/serializers.py

    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    ```
  * `CommentSerializer`에서 `article` 필드를 이 Serializer로 재정의합니다. 이때 `read_only_fields` 메타 옵션 대신 필드에 직접 `read_only=True`를 설정해야 합니다.
    ```python
    # articles/serializers.py

    class CommentSerializer(serializers.ModelSerializer):
        article = ArticleTitleSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = '__all__'
            # read_only_fields = ('article',)  <- 동작하지 않음
    ```

### 6\. 정참조 데이터 구성 (1 -\> N)

단일 게시글을 조회할 때, 해당 게시글에 달린 **댓글의 개수**를 포함시키는 방법입니다.

  * **방법 1: `annotate` (View에서 처리)**
    View에서 `get_object_or_404`로 객체를 조회할 때 `annotate`와 `Count`를 사용하여 댓글 개수를 계산한 `num_of_comments` 필드를 추가합니다.

    ```python
    # articles/views.py

    @api_view(['GET', 'DELETE', 'PUT'])
    def article_detail(request, article_pk):
        article = get_object_or_404(Article.objects.annotate(num_of_comments=Count('comment')), pk=article_pk)
        # ...
    ```

  * **방법 2: `SerializerMethodField` (Serializer에서 처리)**
    `SerializerMethodField`는 `get_<필드명>` 형태의 메서드를 자동으로 호출하여 그 반환값을 필드의 값으로 사용합니다. View에서 `annotate`로 추가한 값을 Serializer에서 받아 처리할 수 있습니다.

    ```python
    # articles/serializers.py

    class ArticleSerializer(serializers.ModelSerializer):
        num_of_comments = serializers.SerializerMethodField()

        class Meta:
            # ...

        def get_num_of_comments(self, obj):
            # obj: 현재 게시글 객체
            # View에서 annotate를 통해 추가된 num_of_comments 속성을 반환
            return obj.num_of_comments
    ```

  * `SerializerMethodField`는 사용자 정의 로직을 추가할 때 유용합니다. 예를 들어 `UserSerializer`에서 `first_name`과 `last_name`을 합쳐 `full_name`을 만들 수 있습니다.

    ```python
    class UserSerializer(serializers.ModelSerializer):
        full_name = serializers.SerializerMethodField()

        class Meta:
            model = User
            fields = ('id', 'username', 'full_name', 'email',)

        def get_full_name(self, obj):
            return f'{obj.first_name} {obj.last_name}'
    ```

### 7\. API 문서화

`drf-spectacular` 라이브러리를 사용하여 **Swagger** 및 **Redoc** 같은 API 문서를 자동으로 생성하는 방법을 소개합니다.

  * `settings.py`에 앱을 등록합니다.
    ```python
    # ...
        'spectacular.openapi.AutoSchema',
    # ...
    ```
  * `urls.py`에 스키마 URL을 설정합니다.
    ```python
    # ...
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns = [
        # ...
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    ```

### 8\. 참고: 올바른 404 응답

객체 조회 시 객체가 없으면 500 에러가 아닌 `404 Not Found`를 반환하도록 `get_object_or_404()` 또는 `get_list_or_404()` 헬퍼 함수를 사용할 것을 권장합니다.