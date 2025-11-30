제공해주신 동영상을 바탕으로 **Vue Basic Syntax** 강의 내용을 정리한 Markdown 파일입니다. 코드 예제는 요약 없이 슬라이드 내용을 그대로 옮겨 작성했습니다.

-----

# Vue Basic Syntax 학습 정리

## 1\. Computed Property

### **Computed**

  * 반응형 데이터를 포함하는 복잡한 로직의 경우 `computed`를 활용하여 미리 값을 계산하여 계산된 값을 사용
  * 여러 곳에서 사용해야 한다면, `computed`로 정의된 `restOfTodos`를 필요한 곳마다 재사용하면 됨

**Code Example:**

```javascript
const { createApp, ref, computed } = Vue

const restOfTodos = computed(() => {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
})
```

```html
<h2>남은 할 일</h2>
<p>{{ restOfTodos }}</p>
```

### **Computed vs. Methods**

  * **Computed:** 의존된 데이터가 변경되면 자동으로 업데이트 (캐싱 기능 O)
  * **Method:** 호출해야만 실행됨 (렌더링 시마다 매번 재계산)

**Code Example:**

```javascript
// Computed 예시
const restOfTodos = computed(() => {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
})

// Method 예시
const getRestOfTodos = function () {
  return todos.value.length > 0 ? '아직 남았다' : '퇴근!'
}
```

### **캐시 (Cache)**

  * 데이터나 결과를 일시적으로 저장해두는 임시 저장소
  * 웹 페이지의 캐시 데이터: 과거 방문한 적이 있는 페이지에 다시 접속할 때 데이터를 다시 다운로드하지 않고 저장된 데이터를 사용하여 빠르게 렌더링
  * **Computed의 장점:** 의존하는 데이터가 변경되지 않는 한, 이전에 계산된 결과를 즉시 반환 (불필요한 계산 방지)

-----

## 2\. Conditional Rendering

### **v-if**

  * 표현식 값의 true/false를 기반으로 요소를 조건부 렌더링
  * 조건이 거짓(false)이면, 해당 요소는 DOM에서 완전히 제거됨 (문서 구조에서 사라짐)

**Code Example:**

```javascript
const isSeen = ref(true)
```

```html
<p v-if="isSeen">true일때 보여요</p>
<p v-else>false일때 보여요</p>
<button @click="isSeen = !isSeen">토글</button>
```

### **template 태그와 v-if**

  * 여러 요소를 하나의 조건부 블록으로 묶을 때 사용 (`<div>` 등으로 감싸지 않고 렌더링 결과에 포함되지 않는 래퍼 역할)

**Code Example:**

```html
<template v-if="name === 'Cathy'">
  <div>Cathy입니다</div>
  <div>나이는 30살입니다</div>
</template>
```

### **v-show**

  * 조건과 관계없이 항상 DOM에 렌더링 됨
  * CSS `display` 속성만 전환함 (none 속성으로 변환하여 숨김)

**Code Example:**

```javascript
const isShow = ref(false)
```

```html
<div v-show="isShow">v-show</div>
```

### **v-if vs v-show**

  * **v-if:** 초기 렌더링 비용이 낮음, 토글 비용이 높음 (자주 변경되지 않는 경우 적합)
  * **v-show:** 초기 렌더링 비용이 높음, 토글 비용이 낮음 (자주 토글되는 경우 적합)

-----

## 3\. List Rendering

### **v-for**

  * 배열 데이터를 기반으로 목록을 반복하여 렌더링
  * 형식: `item in items` (item: 반복되는 요소, items: 원본 데이터 배열)

**Code Example (배열):**

```javascript
const myArr = ref([
  { name: 'Alice', age: 20 },
  { name: 'Bella', age: 21 }
])
```

```html
<div v-for="(item, index) in myArr">
  {{ index }} / {{ item.name }}
</div>
```

*출력 결과:*
0 / Alice
1 / Bella

### **v-for with key**

  * **반드시 key를 사용해야 함**
  * Vue가 각 노드의 ID를 추적하고 기존 요소를 재사용하거나 순서를 변경하기 위해 필요
  * 데이터베이스의 고유 ID(UUID 등)를 사용하는 것을 권장 (index 사용 지양)

**Code Example:**

```html
<div v-for="item in items" :key="item.id">
  {{ item.name }}
</div>
```

### **v-for와 v-if**

  * **주의:** `v-if`가 `v-for`보다 우선순위가 높음. 따라서 동시에 사용할 경우 `v-if`에서 `v-for`의 변수에 접근할 수 없음.
  * **해결책:** `computed`를 활용하여 이미 필터링 된 목록을 반환하여 반복하도록 설정

**Code Example (Computed 활용 해결):**

```javascript
const completeTodos = computed(() => {
  return todos.value.filter((todo) => !todo.isComplete)
})
```

```html
<ul>
  <li v-for="todo in completeTodos" :key="todo.id">
    {{ todo.name }}
  </li>
</ul>
```

-----

## 4\. Watchers

### **watch()**

  * 반응형 데이터를 감시하고, 값이 바뀔 때마다 지정된 콜백 함수를 실행
  * 데이터 변경에 따른 비동기 작업이나 부수 효과(Side Effect)를 수행할 때 사용

**구조:**

```javascript
watch(source, (newValue, oldValue) => {
  // do something
})
```

**Code Example:**

```javascript
const message = ref('')
const messageLength = ref(0)

watch(message, (newValue, oldValue) => {
  messageLength.value = newValue.length
})
```

### **computed vs watch**

| 특징 | Computed | Watchers |
| :--- | :--- | :--- |
| **동작** | 의존하는 데이터 속성의 계산된 값을 반환 | 특정 데이터의 변화를 감지하고 작업 수행 (side-effects) |
| **사용 목적** | 계산된 값을 캐싱하여 재사용 | 데이터 변경에 따른 특정 작업을 수행 |
| **사용 예시** | 연산 된 길이, 필터링 된 목록 계산 등 | DOM 변경, 다른 비동기 작업 수행, 외부 API 연동 등 |

-----

## 5\. Lifecycle Hooks

### **개요**

  * Vue 컴포넌트 인스턴스가 생성, 마운트, 업데이트, 소멸되는 각 생애 주기 단계에서 실행되는 함수
  * 개발자는 특정 시점에 원하는 로직을 실행할 수 있음 (예: Mounting 시점에 API 요청)

### **주요 Hooks**

1.  **Mounting (onMounted):** 컴포넌트가 초기 렌더링 및 DOM 요소 생성이 완료된 후 실행
2.  **Updated (onUpdated):** 반응형 데이터 변경으로 컴포넌트의 DOM이 업데이트된 후 실행

**Code Example (onMounted):**

```javascript
onMounted(() => {
  console.log('mounted')
})
```

**Code Example (onUpdated):**

```javascript
onUpdated(() => {
  message.value = 'updated!'
})
```

### **주의사항**

  * Lifecycle Hooks는 동기적으로 정의되어야 함 (`setTimeout` 같은 비동기 함수 내부에 작성하면 안 됨)

**잘못된 예시:**

```javascript
setTimeout(() => {
  onMounted(() => { // 이 코드는 실행되지 않습니다!
    console.log('...')
  })
}, 100)
```

-----

## 6\. Vue Style Guide

### **우선순위 별 특징**

  * **A: 필수 (Essential):** 오류를 방지하는 데 도움이 되므로 예외 없이 준수 (예: v-for에 key 필수 사용)
  * **B: 적극 권장 (Strongly Recommended):** 가독성 및 개발자 경험 향상
  * **C: 권장 (Recommended):** 일관성을 보장
  * **D: 주의 필요 (Use with Caution):** 잠재적 위험 특성 고려

-----

## 7\. 참고 및 실습 (Todo App)

### **배열 변경 관련 메서드**

  * Vue는 반응형 배열의 변경 메서드가 호출되면 업데이트를 트리거함
  * `push()`, `pop()`, `shift()`, `unshift()`, `splice()`, `sort()`, `reverse()`

### **Todo 애플리케이션 구현 예제**

**Code Example:**

```javascript
const addTodo = function () {
  todos.value.push({
    id: id++,
    text: newTodo.value
  })
  newTodo.value = ''
}
```

### **Computed 주의사항**

1.  **Computed의 반환 값은 변경하지 말 것:** 계산된 값은 읽기 전용(Read-only)으로 취급되어야 함.
2.  **의존성 데이터 업데이트:** 대신 새 값을 얻기 위해선 의존하는 원본 데이터를 업데이트해야 함.