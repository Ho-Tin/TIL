영상 내용을 정리한 마크다운(Markdown) 문서입니다. 요청하신 대로 코드 부분은 요약하지 않고 상세히 기술했습니다.

-----

# Frontend Development & Vue.js 입문

## 1\. Frontend Development 개요

### Client-side frameworks의 필요성

  * **웹의 변화:** 단순히 문서를 읽는 곳에서 무언가를 하는 곳(애플리케이션)으로 변화.
  * **Web Applications:** 음악 스트리밍, 영화 감상, 텍스트/영상 채팅 등 데스크탑 애플리케이션 수준의 기능 수행.
  * **동적 상호작용:** 현대의 웹은 정적이지 않고 복잡한 대화형 웹 사이트.
  * **Framework의 역할:** 클라이언트 사이드 프레임워크가 등장하면서 동적인 대화형 애플리케이션을 훨씬 쉽게 개발하고 관리할 수 있게 됨.

### Vanilla JS만으로는 단순하지 않음 (불필요한 코드의 반복)

순수 자바스크립트만으로 구현 시 코드가 길어지고 복잡해짐.

**[Vanilla JS 예시 코드]**

```html
<label for="inputArea">Username:</label>
<input type="text" id="inputArea" name="inputArea">
<hr>

<h1>안녕하세요 <span id="username1"></span>님의 친구 목록</h1>

<div>
  <span id="username2"></span>님의 친구 목록
</div>
<div>
  <span id="username3"></span>님의 알림 목록
</div>
<div>
  <span id="username4"></span>님의 친구 요청 목록
</div>

<script>
  const initialText = "Unknown User"
  const inputArea = document.querySelector('#inputArea')
  const username1 = document.querySelector('#username1')
  const username2 = document.querySelector('#username2')
  const username3 = document.querySelector('#username3')
  const username4 = document.querySelector('#username4')

  username1.textContent = initialText
  username2.textContent = initialText
  username3.textContent = initialText
  username4.textContent = initialText

  inputArea.addEventListener('input', function (e) {
    username1.textContent = e.target.value
    username2.textContent = e.target.value
    username3.textContent = e.target.value
    username4.textContent = e.target.value
  })
</script>
```

-----

## 2\. SPA & CSR

### SPA (Single Page Application)

  * **작동 원리:**
    1.  최초 로드 시, 애플리케이션에 필요한 주요 리소스를 다운로드.
    2.  페이지 갱신에 대해 필요한 데이터만을 비동기적으로 전달받아 화면의 필요한 부분만 동적으로 갱신.
    3.  **AJAX**와 같은 기술을 사용하여 필요한 데이터만 비동기적으로 로드.
    4.  페이지 전체를 다시 로드할 필요 없음.
    5.  JavaScript를 사용하여 클라이언트 측에서 동적으로 콘텐츠를 생성하고 업데이트 (**CSR 방식**).

### CSR (Client Side Rendering)

  * **개념:** 서버는 뼈대만 주고, 브라우저가 직접 페이지를 그리는 방식.
  * **과정:** 일단 빈 집(HTML)에 들어간 뒤, 브라우저는 거의 텅 빈 HTML을 받고 그 후 JavaScript가 실행되어 내용을 채움.
  * **장점:**
      * 화면 전환 시 필요한 데이터만 가져오므로 전체 페이지를 새로 고칠 필요가 없음 (빠른 인터랙션).
      * 서버 부하 방지 (데이터의 양 최소화).
      * 네이티브 앱과 유사한 사용자 경험 제공.
      * **Backend의 명확한 분리:** UI 렌더링/상호작용은 클라이언트가, 데이터/API 제공은 백엔드가 담당.
  * **비교 (SPA vs MPA / CSR vs SSR):**
      * **MPA (Multi Page Application):** 여러 개의 HTML 파일이 서버로부터 각각 로드됨. 페이지 이동 시 항상 새로운 HTML 로드.
      * **SSR (Server-Side Rendering):** 서버에서 화면을 렌더링하는 방식. 모든 데이터가 담긴 HTML을 서버에서 완성 후 클라이언트에게 전달.

-----

## 3\. Vue.js 소개

### Vue란?

  * 사용자 인터페이스(UI)를 구축하기 위한 JavaScript 프레임워크.
  * 웹사이트 UI를 쉽고 빠르게 만들 수 있게 도와줌.
  * \*\*레고 블록(컴포넌트)\*\*처럼 화면을 조립하고, 데이터가 바뀌면 화면도 자동으로 바뀌는 **반응성**이 가장 큰 특징.

### 특징

  * Angular, React에 비해 문법이 간결하고 직관적임 (낮은 진입 장벽).
  * 활발한 커뮤니티, 풍부한 문서 및 리소스.

### 2가지 핵심 기능

1.  **선언적 렌더링 (Declarative Rendering):** 표준 HTML을 확장하는 Vue "템플릿 구문"을 사용하여 JavaScript 상태(데이터)를 기반으로 화면에 출력될 HTML을 선언적으로 작성.
2.  **반응성 (Reactivity):** JavaScript 상태 변경을 추적하고, 변경사항이 발생하면 자동으로 DOM을 업데이트.

### Component (컴포넌트)

  * 웹 서비스는 여러 개의 Component로 이루어져 있음.
  * UI를 독립적이고 재사용 가능한 조각으로 분할하여 개발.

-----

## 4\. Vue Application 생성

### Vue를 사용하는 방법

1.  **CDN 방식:** 스크립트 태그로 로드 (학습용).
2.  **NPM 설치 방식:** 프로젝트 빌드 도구 사용 (실무용).

### Vue Application 생성 단계 (CDN 예시)

**1. Vue 사용을 위한 CDN 작성**

```html
<div id="app"></div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp } = Vue
  
  const app = createApp({
    setup() {}
  })
  
  app.mount('#app')
</script>
```

**2. Application instance 생성**

  * 모든 Vue 애플리케이션은 `createApp` 함수로 새 Application instance를 생성하는 것으로 시작.

<!-- end list -->

```javascript
const { createApp } = Vue

const app = createApp({
  setup() {}
})
```

**3. Mounting the App (앱 연결)**

  * HTML 요소에 Vue Application instance를 탑재(연결).
  * 각 앱 인스턴스에 대해 `mount()`는 한 번만 호출할 수 있음.

<!-- end list -->

```javascript
app.mount('#app')
```

-----

## 5\. 반응형 상태 (Reactivity)

### ref 함수

  * `.value` 속성이 있는 ref 객체로 래핑(wrapping)하여 반환하는 함수.
  * ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트.
  * 인자는 어떠한 타입도 가능.

**[ref 사용 예시 코드]**

```javascript
const { createApp, ref } = Vue

const app = createApp({
  setup() {
    const message = ref('Hello vue!') // ref 객체 생성
    console.log(message) // ref 객체 출력
    console.log(message.value) // Hello vue! 출력
    
    return {
      message
    }
  }
})
```

-----

## 6\. Vue 기본 구조 및 템플릿 렌더링

### 템플릿 렌더링

  * 반환된 객체의 속성은 템플릿에서 사용할 수 있음.
  * \*\*Mustache syntax (콧수염 구문, `{{ }}`)\*\*를 사용하여 메시지 값을 기반으로 동적 텍스트를 렌더링.

**[템플릿 연결 코드]**

```html
<div id="app">
  <h1>{{ message }}</h1>
</div>

<script>
  const app = createApp({
    setup() {
      const message = ref('Hello vue!')
      return {
        message
      }
    }
  })
</script>
```

  * 콘텐츠는 식별자나 경로에만 국한되지 않으며 유효한 JavaScript 표현식을 사용할 수 있음.

<!-- end list -->

```html
<h1>{{ message.split('').reverse().join('') }}</h1>
```

### 변수 vs. 일반 변수 (비교)

값이 바뀌면 화면이 자동으로 업데이트되지만, 일반 변수는 값이 바뀌어도 화면이 갱신되지 않음.

**[반응형 변수 vs 일반 변수 코드]**

```javascript
const app = createApp({
  setup() {
    const reactiveValue = ref(0) // 반응형
    let normalValue = 0          // 비반응형 (화면 갱신 X)

    const updateValues = function () {
      reactiveValue.value++
      normalValue++
    }

    return {
      reactiveValue,
      normalValue,
      updateValues
    }
  }
})
```

```html
<div id="app">
  <p>반응형 변수: {{ reactiveValue }}</p>
  <p>일반 변수: {{ normalValue }}</p>
  <button v-on:click="updateValues">값 업데이트</button>
</div>
```

-----

## 7\. 주의사항 (Ref Unwrap)

### 템플릿에서의 unwrap 시 주의사항

  * 템플릿에서의 unwrap은 ref가 setup에서 반환된 객체의 **최상위 속성**일 경우에만 적용됨.

**[객체 내부의 ref 사용 시 문제점]**

```javascript
const object = { id: ref(0) }
```

```html
{{ object.id + 1 }} 
```

  * **이유:** `object`는 최상위 속성이지만 `object.id`는 그렇지 않음. 표현식을 평가할 때 `object.id`가 unwrap 되지 않고 ref 객체로 남아있기 때문.
  * **해결:** 이를 인지하고 `.value`를 사용하거나 구조 분해 할당 등을 통해 최상위 속성으로 만들어야 함.

-----

## 8\. 요약 및 정리

### 핵심 키워드

  * **Vue:** 사용자 인터페이스를 구축하기 위한 JS 프레임워크.
  * **SPA:** 단일 페이지에서 동작하는 웹 앱.
  * **CSR:** 클라이언트에서 페이지를 렌더링.
  * **선언적 렌더링:** JS 상태 기반으로 HTML을 선언. (`<h1>{{ message }}</h1>`)
  * **반응성:** 데이터 변경 시 DOM 자동 업데이트. (`count.value++`)
  * **컴포넌트:** 재사용 가능한 독립적 UI 조각.

### 오늘 공부한 내용 요약

1.  **Vue 기본 사용법:** `createApp`, `setup`, `mount`.
2.  **템플릿에 데이터 연결:** 콧수염 구문 `{{ }}` 사용.
3.  **반응형 변수:** `ref()` 함수 사용 (템플릿 안에서는 `.value` 없이 사용 가능하나 중첩 객체 주의).
4.  **이벤트 처리:** `v-on` 디렉티브 등 사용.