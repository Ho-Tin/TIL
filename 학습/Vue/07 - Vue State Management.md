
-----

# State Management (Pinia)

## 1\. 개요 (State Management)

### 학습 목표

  * Props와 Emit 방식의 상태 관리 문제점을 설명할 수 있다.
  * Pinia의 state, getters, actions의 역할을 이해한다.
  * `defineStore` 함수를 사용해 중앙 저장소(store)를 정의한다.
  * 컴포넌트에서 Pinia store를 호출하여 상태를 사용할 수 있다.
  * store의 `getters`를 활용하여 계산된 값을 얻을 수 있다.
  * Pinia 플러그인을 사용해 상태를 Local Storage에 저장한다.

### 상태 관리의 필요성

  * **기존 방식 (Props & Emit):**
      * 상태(State), 뷰(View), 기능(Actions)은 "단방향 데이터 흐름"으로 상호작용.
      * **문제점:** 컴포넌트 구조가 깊어질 경우, 데이터를 전달하기 위해 거쳐야 하는 중간 컴포넌트가 많아짐 (Prop Drilling).
      * 유지보수가 어렵고 코드가 복잡해짐.
  * **해결 방법 (Pinia):**
      * 각 컴포넌트의 공유 상태를 추출하여, \*\*전역에서 참조할 수 있는 중앙 저장소(Store)\*\*에서 관리.
      * 컴포넌트 트리에 구애받지 않고 상태에 접근 및 수정 가능.

-----

## 2\. Pinia 구성 요소

Pinia는 Vue의 공식 상태 관리 라이브러리입니다.

### 구성 요소 (Composition API 기준)

1.  **store:** 중앙 저장소. `defineStore`로 정의.
2.  **state:** 반응형 데이터 (Vue의 `ref`).
3.  **getters:** 계산된 값 (Vue의 `computed`).
4.  **actions:** 상태를 변경하는 메서드 (Vue의 `function`).
5.  **plugin:** 추가 기능 (예: Local Storage 저장).

### 기본 구조 코드 (`stores/counter.js`)

```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

// 'counter'는 애플리케이션 전체에서 사용하는 store의 고유 ID
export const useCounterStore = defineStore('counter', () => {
  
  // 1. State (상태)
  const count = ref(0)

  // 2. Getters (계산된 값)
  const doubleCount = computed(() => count.value * 2)

  // 3. Actions (기능/메서드)
  function increment() {
    count.value++
  }

  // 반환: 컴포넌트에서 사용하려면 반드시 반환해야 함
  return { count, doubleCount, increment }
})
```

### 컴포넌트에서 활용 (`App.vue`)

```javascript
<script setup>
import { useCounterStore } from '@/stores/counter'

// store 인스턴스 생성
const store = useCounterStore()

// state 및 action 접근
console.log(store.count) 
store.increment()
</script>

<template>
  <div>
    <p>Count: {{ store.count }}</p>
    <p>Double Count: {{ store.doubleCount }}</p>
    <button @click="store.increment">증가</button>
  </div>
</template>
```

-----

## 3\. 실습: Todo Project 구현

### 3-1. 사전 준비 & Todo 조회 (Read)

**Store 정의 (`stores/counter.js`)**

```javascript
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  let id = 0
  
  // State 정의
  const todos = ref([
    { id: id++, text: '할 일 1', isDone: false },
    { id: id++, text: '할 일 2', isDone: false }
  ])

  return { todos }
})
```

**TodoList 컴포넌트 (`TodoList.vue`)**

```javascript
<script setup>
import { useCounterStore } from '@/stores/counter'
import TodoListItem from '@/components/TodoListItem.vue'

const store = useCounterStore()
</script>

<template>
  <div>
    <TodoListItem 
      v-for="todo in store.todos" 
      :key="todo.id" 
      :todo="todo" 
    />
  </div>
</template>
```

### 3-2. Todo 생성 (Create)

**Store에 Action 추가 (`stores/counter.js`)**

```javascript
// ... 기존 코드
const addTodo = function (todoText) {
  todos.value.push({
    id: id++,
    text: todoText,
    isDone: false
  })
}

return { todos, addTodo }
```

**TodoForm 컴포넌트 (`TodoForm.vue`)**

```javascript
<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const todoText = ref('')
const store = useCounterStore()
const formElem = ref(null)

const createTodo = function (todoText) {
  store.addTodo(todoText)
  formElem.value.reset() // 입력 후 초기화
  todoText.value = ''
}
</script>

<template>
  <form @submit.prevent="createTodo(todoText)" ref="formElem">
    <input type="text" v-model="todoText">
    <input type="submit">
  </form>
</template>
```

### 3-3. Todo 삭제 (Delete)

**Store에 Action 추가 (`stores/counter.js`)**

```javascript
// 방법 1: findIndex와 splice 사용
const deleteTodo = function (selectedId) {
  const index = todos.value.findIndex((todo) => todo.id === selectedId)
  if (index > -1) {
    todos.value.splice(index, 1)
  }
}

// 방법 2: filter 사용 (참고)
// const deleteTodo = function (selectedId) {
//   todos.value = todos.value.filter((todo) => todo.id !== selectedId)
// }

return { todos, addTodo, deleteTodo }
```

**TodoListItem 컴포넌트 (`TodoListItem.vue`)**

```javascript
<script setup>
import { useCounterStore } from '@/stores/counter'

const props = defineProps({
  todo: Object
})

const store = useCounterStore()
</script>

<template>
  <div>
    <span>{{ todo.text }}</span>
    <button @click="store.deleteTodo(todo.id)">삭제</button>
  </div>
</template>
```

### 3-4. Todo 수정 (Update)

**Store에 Action 추가 (`stores/counter.js`)**

```javascript
const updateTodo = function (selectedId) {
  todos.value = todos.value.map((todo) => {
    if (todo.id === selectedId) {
      todo.isDone = !todo.isDone
    }
    return todo
  })
}

return { todos, addTodo, deleteTodo, updateTodo }
```

**TodoListItem 컴포넌트 적용 (`TodoListItem.vue`)**

```javascript
<template>
  <div>
    <span 
      @click="store.updateTodo(todo.id)" 
      :class="{ 'is-done': todo.isDone }"
    >
      {{ todo.text }}
    </span>
    <button @click="store.deleteTodo(todo.id)">삭제</button>
  </div>
</template>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>
```

### 3-5. 완료된 Todo 개수 계산 (Getters)

**Store에 Getter 추가 (`stores/counter.js`)**

```javascript
const doneTodosCount = computed(() => {
  return todos.value.filter((todo) => todo.isDone).length
})

return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
```

**App.vue에서 사용**

```javascript
<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo: {{ store.doneTodosCount }}</h2>
    </div>
</template>
```

-----

## 4\. Local Storage (상태 유지)

브라우저를 새로고침해도 데이터가 사라지지 않도록 플러그인을 사용합니다.

### 설정 방법

1.  **설치:**

    ```bash
    $ npm i pinia-plugin-persistedstate
    ```

2.  **플러그인 등록 (`main.js`):**

    ```javascript
    import { createApp } from 'vue'
    import { createPinia } from 'pinia'
    import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
    import App from './App.vue'

    const app = createApp(App)
    const pinia = createPinia()

    pinia.use(piniaPluginPersistedstate) // 플러그인 사용 설정

    app.use(pinia)
    app.mount('#app')
    ```

3.  **Store에서 활성화 (`stores/counter.js`):**

    ```javascript
    export const useCounterStore = defineStore('counter', () => {
      // ... state, actions, getters 정의 ...

      return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }
    }, { persist: true }) // persist 옵션 추가
    ```

-----

## 5\. 핵심 요약

| 개념 | 설명 | 예시 (Composition API) |
| :--- | :--- | :--- |
| **Pinia** | Vue의 공식 상태 관리 라이브러리 | `createPinia()` |
| **defineStore** | 중앙 저장소(Store)를 정의하는 함수 | `defineStore('id', () => {})` |
| **state** | 중앙 저장소의 반응형 데이터 | `ref()` |
| **getters** | state를 기반으로 계산된 속성 | `computed()` |
| **actions** | state를 변경하는 메서드 | `function()` |
| **상태 유지** | Pinia 상태를 Local Storage에 저장 | `{ persist: true }` |

### Pinia 사용 시점

  * **사용 권장:**
      * 여러 컴포넌트가 동일한 상태를 공유해야 할 때.
      * 컴포넌트 깊이가 깊어서 Props 전달이 복잡할 때.
  * **주의:**
      * 애플리케이션이 단순하다면 Pinia 없이 Props/Emit만으로도 충분할 수 있음.
      * 상황에 맞게 적절히 활용하여 효율성을 극대화해야 함.