

-----

# Vue.js Component Data Flow (Props & Emit)

## 1\. 개요 및 학습 목표

  * **Props:** 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달하는 방법.
  * **Emit:** 자식 컴포넌트에서 부모 컴포넌트로 이벤트를(메시지를) 전달하는 방법.
  * **One-Way Data Flow (단방향 데이터 흐름):** 모든 props는 부모에서 자식으로 향하는 **단방향 바인딩**을 형성함.

-----

## 2\. Props (Parent -\> Child)

### 2.1. Props 특징

  * 부모의 데이터가 업데이트되면 자식에게 전달되지만, **반대는 불가능**함.
  * 자식 컴포넌트 내부에서 **props를 직접 변경하려고 시도해서는 안 됨** (읽기 전용).
  * 데이터 흐름의 '일관성' 및 '예측 가능성'을 높이기 위함.

### 2.2. Props 선언 및 사용 (기본)

**사전 준비 (ParentChild 컴포넌트 관계 작성)**

```html
<script setup>
import Parent from '@/components/Parent.vue'
</script>

<template>
  <div>
    <Parent />
  </div>
</template>
```

**부모 컴포넌트에서 데이터 전달 (Parent.vue)**

  * HTML 속성처럼 `prop-name="value"` 형태로 전달.

<!-- end list -->

```html
<script setup>
import ParentChild from '@/components/ParentChild.vue'
</script>

<template>
  <div>
    <ParentChild my-msg="message" />
  </div>
</template>
```

**자식 컴포넌트에서 Props 선언 (ParentChild.vue)**

  * `defineProps()` 매크로를 사용하여 선언.
  * 문자열 배열을 사용한 선언 방식.

<!-- end list -->

```html
<script setup>
// 문자열 배열로 props 선언
const props = defineProps(['myMsg'])

// js에서 접근 시
console.log(props.myMsg) 
</script>

<template>
  <div>
    <p>{{ myMsg }}</p>
  </div>
</template>
```

### 2.3. Props Naming Convention (네이밍 컨벤션)

  * **HTML (부모 템플릿):** kebab-case 권장 (`my-msg`)
  * **JS (자식 스크립트):** camelCase 권장 (`myMsg`)

<!-- end list -->

```html
<ParentChild my-msg="message" />

<script setup>
defineProps({
  myMsg: String 
})
</script>
<template>
  <p>{{ myMsg }}</p>
</template>
```

### 2.4. Static Props & Dynamic Props

  * **Static:** 고정된 값 전달.
  * **Dynamic:** `v-bind`(`:`)를 사용하여 변수나 표현식 전달.

<!-- end list -->

```html
<script setup>
import { ref } from 'vue'
const name = ref('Alice')
</script>

<template>
  <ParentChild my-msg="message" />

  <ParentChild :dynamic-props="name" />
</template>
```

```html
<script setup>
defineProps({
  myMsg: String,
  dynamicProps: String
})
</script>
```

### 2.5. v-for와 함께 사용

반복되는 요소를 props로 전달할 때 사용.

```html
<script setup>
import { ref } from 'vue'
import ParentItem from '@/components/ParentItem.vue'

const items = ref([
  { id: 1, name: '사과' },
  { id: 2, name: '바나나' },
  { id: 3, name: '딸기' }
])
</script>

<template>
  <ParentItem 
    v-for="item in items"
    :key="item.id"
    :my-prop="item"
  />
</template>
```

```html
<script setup>
defineProps({
  myProp: Object
})
</script>

<template>
  <div>
    <p>{{ myProp.id }} : {{ myProp.name }}</p>
  </div>
</template>
```

-----

## 3\. Component Events / Emit (Child -\> Parent)

### 3.1. Emit 개요

  * 자식 컴포넌트가 이벤트를 발생시켜 부모에게 메시지를 보내는 기능.
  * **$emit(event, ...args):** 이벤트를 발생시키는 내장 메서드.

### 3.2. 이벤트 발신 및 수신 (기본)

**자식 컴포넌트: 이벤트 발신 (ParentChild.vue)**

  * 템플릿에서 `$emit` 사용.

<!-- end list -->

```html
<template>
  <button @click="$emit('someEvent')">클릭</button>
</template>
```

**부모 컴포넌트: 이벤트 수신 (Parent.vue)**

  * `v-on`(`@`)을 사용하여 수신.

<!-- end list -->

```html
<script setup>
const someCallback = () => {
  console.log('ParentChild가 이벤트를 발신함!')
}
</script>

<template>
  <ParentChild @some-event="someCallback" />
</template>
```

### 3.3. emit 이벤트 선언 (defineEmits)

  * `defineEmits()` 매크로를 사용하여 발신할 이벤트를 명시적으로 선언 (코드 가독성 및 유지보수 향상).
  * `<script setup>` 내에서 사용 시 `emit` 함수를 반환받아 사용.

<!-- end list -->

```html
<script setup>
// 1. 발신할 이벤트 선언
const emit = defineEmits(['someEvent', 'myFocus'])

const buttonClick = () => {
  // 2. emit 함수 호출하여 이벤트 발신
  emit('someEvent')
}
</script>

<template>
  <button @click="buttonClick">클릭</button>
</template>
```

### 3.4. 이벤트 인자 전달 (Arguments)

이벤트 발생 시 데이터를 함께 전달할 수 있음.

**자식 컴포넌트 (ParentChild.vue)**

```html
<script setup>
const emit = defineEmits(['emitArgs'])

const emitArgs = () => {
  // 이벤트 이름, 전달할 추가 데이터들
  emit('emitArgs', 1, 2, 3)
}
</script>

<template>
  <button @click="emitArgs">추가 인자 전달</button>
</template>
```

**부모 컴포넌트 (Parent.vue)**

```html
<script setup>
// 전달받은 인자들을 매개변수로 사용 가능
const getNumbers = (...args) => {
  console.log(args) // [1, 2, 3]
  console.log(`ParentChild가 전달한 추가 인자 ${args}를 수신했어요.`)
}
</script>

<template>
  <ParentChild @emit-args="getNumbers" />
</template>
```

### 3.5. Emit 활용 (데이터 갱신 예시)

자식이 요청하고 부모가 데이터를 변경하는 흐름.

**부모 컴포넌트**

```html
<script setup>
import { ref } from 'vue'
// ... (ParentChild import)

const name = ref('Alice')

// 자식이 보낸 새로운 이름으로 업데이트하는 함수
const updateName = (newName) => {
  name.value = newName
}
</script>

<template>
  <ParentChild 
    :my-msg="name" 
    @update-name="updateName" 
  />
</template>
```

**자식 컴포넌트**

```html
<script setup>
defineProps({ myMsg: String })
const emit = defineEmits(['updateName'])

const onNameChange = () => {
  // 'Bella'라는 데이터와 함께 updateName 이벤트 발신
  emit('updateName', 'Bella')
}
</script>

<template>
  <div>
    <p>{{ myMsg }}</p>
    <button @click="onNameChange">이름 변경</button>
  </div>
</template>
```

-----

## 4\. 참고: Props 선언 시 객체 문법 권장

### 객체 선언 문법 (Object Syntax)

단순 배열보다 객체 형태의 선언을 권장함.

  * 데이터 타입 유효성 검사 가능.
  * `default` 값 설정 가능.
  * `required` 여부 설정 가능.
  * 다른 개발자에게 명확한 문서화 효과 제공.

<!-- end list -->

```javascript
// 권장되는 방식
defineProps({
  // 기본 타입 체크
  propA: Number,
  
  // 여러 타입 허용
  propB: [String, Number],
  
  // 필수 문자열
  propC: {
    type: String,
    required: true
  },
  
  // 기본값이 있는 숫자
  propD: {
    type: Number,
    default: 100
  },
  
  // 객체 타입의 기본값 (팩토리 함수 반환 필요)
  propE: {
    type: Object,
    default(rawProps) {
      return { message: 'hello' }
    }
  },
  
  // 커스텀 유효성 검사 함수
  propF: {
    validator(value) {
      return ['success', 'warning', 'danger'].includes(value)
    }
  }
})
```

-----

## 5\. 정리 (Summary)

  * **Props:**
      * 부모 -\> 자식 데이터 전달.
      * **단방향 데이터 흐름** (자식에서 수정 금지).
      * HTML에서는 kebab-case, JS에서는 camelCase 사용.
  * **Emit:**
      * 자식 -\> 부모 이벤트(데이터) 전달.
      * `$emit` 또는 `defineEmits`를 사용.
      * 데이터의 흐름: 부모(Props) -\> 자식 -\> (Emit) -\> 부모 update.