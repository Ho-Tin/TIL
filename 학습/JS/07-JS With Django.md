

-----

# [SSAFY] Javascript - Ajax with Django

## 1\. 학습 목표

  * **Django view**에서 `JsonResponse`를 반환하여 비동기 요청에 응답한다.
  * `data-*` 속성을 사용해 Django 데이터를 JavaScript로 전달한다.
  * **Axios** 요청 시 헤더에 CSRF tokens를 포함하여 전송할 수 있다.
  * **Axios**를 활용해 팔로우/좋아요 기능을 비동기적으로 구현할 수 있다.
  * 서버의 JSON 응답을 받아 DOM을 동적으로 업데이트한다.
  * \*\*버블링(Bubbling)\*\*을 활용해 여러 요소의 이벤트를 효율적으로 관리한다.

-----

## 2\. 이론: Ajax와 서버

### Ajax를 활용한 클라이언트-서버 간 동작

  * **XHR 객체 생성 및 요청** → **응답 데이터 생성** → **JSON 데이터 응답** → **Promise 객체를 활용해 DOM 조작**
  * 웹 페이지의 일부분(데이터)만 다시 로딩하여 사용자 경험 향상.

-----

## 3\. 비동기 팔로우 구현

### 3.1. HTML (accounts/profile.html)

  * 기존 `form` 태그에서 `action`과 `method` 속성을 삭제 (Axios가 대체).
  * JavaScript에서 제어하기 위해 `id` 및 `data-*` 속성 추가.
  * 팔로우 수/팔로잉 수 업데이트를 위해 `span` 태그에 `id` 부여.

<!-- end list -->

```html
<form id="follow-form" data-user-id="{{ person.pk }}">
  {% csrf_token %}
  {% if request.user in person.followers.all %}
    <input type="submit" value="Unfollow">
  {% else %}
    <input type="submit" value="Follow">
  {% endif %}
</form>

<div>
  팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span> /
  팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span>
</div>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

### 3.2. Django View (accounts/views.py)

  * HTML 문서가 아닌 **JSON 데이터**를 응답해야 ``하므로 `JsonResponse` 사용.
  * 팔로우 상태(`is_followed`)와 갱신된 팔로워/팔로잉 수를 `context`에 담아 반환.

<!-- end list -->

```python
from django.http import JsonResponse

@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            is_followed = False
        else:
            person.followers.add(request.user)
            is_followed = True
        
        context = {
            'is_followed': is_followed,
            'followings_count': person.followings.count(),
            'followers_count': person.followers.count(),
        }
        return JsonResponse(context)
    
    return redirect('accounts:profile', person.username)
```

### 3.3. JavaScript (Axios 요청)

  * `dataset.userId`를 통해 HTML의 `data-user-id` 값 접근.
  * `csrfmiddlewaretoken`을 `input` 태그에서 찾아 헤더에 포함.
  * 응답(`response.data`)을 받아 버튼 텍스트와 팔로우 수를 DOM 업데이트.

<!-- end list -->

```javascript
const form = document.querySelector('#follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

form.addEventListener('submit', function (event) {
  event.preventDefault() // 폼 제출 시 새로고침 방지
  
  const userId = event.target.dataset.userId // data-user-id 값 가져오기

  axios({
    method: 'post',
    url: `/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken},
  })
  .then((response) => {
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector('#follow-form > input[type=submit]') // input 태그 선택
    
    // 버튼 상태 토글
    if (isFollowed === true) {
      followBtn.value = 'Unfollow'
    } else {
      followBtn.value = 'Follow'
    }

    // 팔로워/팔로잉 수 업데이트
    const followingsCountTag = document.querySelector('#followings-count')
    const followersCountTag = document.querySelector('#followers-count')
    
    followingsCountTag.innerText = response.data.followings_count
    followersCountTag.innerText = response.data.followers_count
  })
  .catch((error) => {
    console.log(error)
  })
})
```

-----

## 4\. 비동기 좋아요 구현 (버블링 활용)

### 4.1. 버블링(Bubbling) 개념

  * **문제점:** 페이지에 여러 개의 '좋아요' 버튼이 있을 때, 모든 버튼에 개별적으로 이벤트 리스너를 부착하는 것은 비효율적임 (`querySelectorAll` 사용 시).
  * **해결책:** 부모 요소(최상위 요소)에 단 하나의 이벤트 리스너를 부착하여, 하위 요소에서 발생한 이벤트를 처리.
  * **Event Target:**
      * `event.currentTarget`: 핸들러가 연결된 요소 (부모, 'this'와 같음)
      * `event.target`: 실제 이벤트가 발생한 가장 안쪽의 요소 (클릭한 버튼)

### 4.2. HTML (articles/index.html)

  * 전체 게시글을 감싸는 부모 요소(`article-container`) 생성.
  * 각 form에 `data-article-id` 속성 부여.
  * 좋아요 버튼 식별을 위해 `id`에 pk값을 포함하여 유니크하게 설정 (`like-{{ article.pk }}`).

<!-- end list -->

```html
<article class="article-container">
  {% for article in articles %}
    <form class="like-forms" data-article-id="{{ article.pk }}">
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
      {% else %}
        <input type="submit" value="좋아요" id="like-{{ article.pk }}">
      {% endif %}
    </form>
    <hr>
  {% endfor %}
</article>
```

### 4.3. Django View (articles/views.py)

  * 좋아요 여부(`is_liked`)를 JSON으로 응답.

<!-- end list -->

```python
from django.http import JsonResponse

def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
        
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)
```

### 4.4. JavaScript (버블링 적용)

  * `article-container`에 이벤트 리스너 부착.
  * `event.target.dataset.articleId`가 존재하는 경우에만 Ajax 요청 실행.

<!-- end list -->

```javascript
const articleContainer = document.querySelector('.article-container')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()

  const articleId = event.target.dataset.articleId

  // articleId가 존재하는 경우에만 실행 (다른 요소 클릭 방지)
  if (articleId) {
    axios({
      method: 'post',
      url: `/articles/${articleId}/likes/`,
      headers: {'X-CSRFToken': csrftoken},
    })
    .then((response) => {
      const isLiked = response.data.is_liked
      // id를 이용해 특정 게시글의 버튼 선택
      const likeBtn = document.querySelector(`#like-${articleId}`)
      
      if (isLiked === true) {
        likeBtn.value = '좋아요 취소'
      } else {
        likeBtn.value = '좋아요'
      }
    })
    .catch((error) => {
      console.log(error)
    })
  }
})
```

-----

## 5\. 핵심 정리 및 문법

### 5.1. `data-*` 속성

  * 사용자 지정 데이터 속성을 만들어 HTML과 DOM 사이에서 임의의 데이터를 교환하는 방법.
  * **HTML:** `data-user-id="123"` (속성명은 'xml'로 시작 불가, 세미콜론/대문자 포함 불가)
  * **JavaScript:** `element.dataset.userId` (CamelCase로 접근)

### 5.2. JsonResponse

  * Django View 함수에서 HTML 템플릿 대신 JSON 데이터를 응답할 때 사용하는 객체.
  * Ajax 요청에 대한 상태 정보나 데이터를 전달하는 데 사용됨.

### 5.3. 이벤트 처리

  * **`preventDefault()`**: form의 기본 제출 동작(새로고침)을 막음.
  * **`event.target` vs `event.currentTarget`**: 버블링 활용 시 실제 이벤트 발생 요소를 정확히 파악하기 위해 `target` 사용.