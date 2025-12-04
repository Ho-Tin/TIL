
-----

# Vue Router 학습 정리

## 1\. 개요 및 사전 준비

### Routing이란?

  * **SSR (Server Side Rendering):** 서버가 사용자가 방문한 URL을 기반으로 완성된 HTML을 응답. 링크 클릭 시 페이지 전체를 새로고침.
  * **SPA (Single Page Application):** 페이지 변화 없이(새로고침 없이) URL만 변경되며, 브라우저가 클라이언트 측에서 필요한 컴포넌트만 새로 렌더링.

### Vue Router 설치 및 설정

Vue.js의 공식 라우터 라이브러리입니다.

**프로젝트 생성 및 구조 변화**

```bash
npm create vue@latest
# Vue Router 선택: Yes
```

**파일 구조 변화**

  * `router/index.js`: 라우팅 설정 파일
  * `views/`: 페이지(View) 역할을 하는 컴포넌트 폴더
  * `App.vue`: `RouterLink`와 `RouterView`가 추가됨

-----

## 2\. Basic Routing (기본 라우팅)

페이지 이동을 위한 링크 생성 및 렌더링 위치 지정.

### 핵심 컴포넌트

1.  **RouterLink**: 페이지를 새로고침하지 않고 URL을 변경하는 링크를 생성 (HTML의 `<a>` 태그 역할).
2.  **RouterView**: URL에 해당하는 컴포넌트가 렌더링되는 위치.

### 코드 예시 (App.vue)

```html
<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>
```

### 라우터 설정 (router/index.js)

```javascript
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    }
  ]
})
```

-----

## 3\. Dynamic Route Matching (동적 라우트 매칭)

URL의 일부를 변수로 사용하여 경로를 동적으로 매칭하는 방식.

### 설정 (router/index.js)

```javascript
{
  // :id 부분이 매개변수(params)가 됨
  path: '/user/:id',
  name: 'user',
  component: UserView
}
```

### 컴포넌트에서 파라미터 사용 (UserView.vue)

`useRoute()` 훅을 사용하여 현재 경로의 정보를 가져옴.

```html
<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
// 경로의 params id 값 접근
const userId = ref(route.params.id)
</script>

<template>
  <h1>User ID: {{ userId }}</h1>
  <h2>{{ $route.params.id }}</h2>
</template>
```

-----

## 4\. Nested Routes (중첩된 라우팅)

특정 페이지(부모)의 레이아웃은 유지한 채, 그 안의 일부 영역만 다른 컴포넌트(자식)로 교체하는 방식.

### 구조 설명

  * URL 예시: `/user/:id/profile`, `/user/:id/posts`
  * 부모 컴포넌트(`UserView`) 안에 또 다른 `<RouterView />`가 존재해야 함.

### 설정 (router/index.js)

`children` 옵션을 사용하여 중첩 구조 정의.

```javascript
{
  path: '/user/:id',
  name: 'user',
  component: UserView,
  children: [
    {
      // /user/:id/profile
      path: 'profile',
      name: 'user-profile',
      component: UserProfile
    },
    {
      // /user/:id/posts
      path: 'posts',
      name: 'user-posts',
      component: UserPosts
    }
  ]
}
```

-----

## 5\. Programmatic Navigation (프로그래밍 방식 네비게이션)

`<RouterLink>` 대신 JavaScript 코드를 사용하여 페이지를 이동시키는 방법.

### 메서드

  * `router.push()`: 새 항목을 history 스택에 추가 (뒤로 가기 가능).
  * `router.replace()`: 현재 위치를 바꾸기만 함 (뒤로 가기 불가).

### 코드 예시

```javascript
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = function() {
  // 경로(path)로 이동
  router.push('/home')
  
  // 이름(name)으로 이동 (권장)
  router.push({ name: 'home' })
  
  // 파라미터와 함께 이동
  router.push({ name: 'user', params: { id: '123' } })
  
  // 현재 위치 교체 (history에 남지 않음)
  router.replace({ name: 'home' })
}
```

-----

## 6\. Navigation Guard (네비게이션 가드)

라우트 진입/이동을 취소하거나 리다이렉트하는 등 네비게이션을 보호/제어하는 기능.

### 1\) Global Guard (전역 가드)

애플리케이션 전역에서 동작. `router.beforeEach` 사용.

**router/index.js**

```javascript
router.beforeEach((to, from) => {
  // to: 이동할 대상 라우트 객체
  // from: 현재 떠나려는 라우트 객체
  
  const isAuthenticated = false // 로그인 상태 예시
  
  // 로그인이 필요하지만 되어있지 않고, 이동하려는 곳이 login 페이지가 아니라면
  if (!isAuthenticated && to.name !== 'login') {
    console.log('로그인이 필요합니다.')
    return { name: 'login' } // 로그인 페이지로 리다이렉트
  }
  
  // return false를 하면 이동 취소
})
```

### 2\) Per-route Guard (라우터 가드)

특정 라우트 설정 객체 내에서 정의. `beforeEnter` 사용.

**router/index.js**

```javascript
{
  path: '/user/:id',
  component: UserView,
  beforeEnter: (to, from) => {
    // 특정 로직 수행
    if (to.params.id === 'admin') {
       return false
    }
  }
}
```

### 3\) In-component Guard (컴포넌트 가드)

컴포넌트 내부 `<script setup>` 등에서 정의.

  * `onBeforeRouteLeave`: 현재 라우트를 떠나기 직전 호출.
  * `onBeforeRouteUpdate`: 경로 파라미터만 변경될 때 호출 (컴포넌트 재사용 시).

**UserView.vue**

```javascript
import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('정말 떠나실 건가요? 저장되지 않은 내용은 소실됩니다.')
  // false 반환 시 이동 취소
  if (!answer) return false
})

onBeforeRouteUpdate((to, from) => {
  // URL의 id가 변경되었을 때 데이터 갱신 로직 등
  console.log('User ID updated:', to.params.id)
})
```

-----

## [참고] 강사의 요약 (영상 말미)

>   * **Props & Emit 복습:**
>       * **부모 → 자식:** `Props`를 통해 데이터를 아래로 전달.
>       * **자식 → 부모:** 데이터 변경이 필요할 때 `Emit` 이벤트를 통해 부모에게 알림.
>   * **Routing과의 관계:** 라우팅 또한 컴포넌트 간의 연결이며, 이 기본적인 데이터 흐름(Props/Emit) 원칙 위에서 동작함을 이해하는 것이 중요.