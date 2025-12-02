영상 내용을 바탕으로 정리한 `Vue Basic Syntax 1` 학습 노트입니다. 요청하신 대로 코드 내용은 요약하지 않고 그대로 정리했습니다.

-----

# Vue Basic Syntax 1

## 1\. Template Syntax (템플릿 문법)

Vue는 DOM을 컴포넌트 인스턴스의 데이터에 **선언적으로 바인딩**할 수 있는 HTML 기반 템플릿 구문을 사용합니다.

### 1.1 Raw HTML

  * 콧수염 구문(`{{ }}`)은 데이터를 일반 텍스트로 해석합니다.
  * 실제 HTML을 출력하려면 `v-html` 디렉티브를 사용해야 합니다.

<!-- end list -->

```html
<p>Using text interpolation: {{ rawHtml }}</p>
<p>Using v-html directive: <span v-html="rawHtml"></span></p>
```

```javascript
const rawHtml = ref('<span style="color:red">This should be red.</span>')
```

### 1.2 Attribute Bindings (속성 바인딩)

  * Mustache(`{{ }}`) 구문은 HTML 속성 내에서 사용할 수 없습니다.
  * 대신 `v-bind` 디렉티브를 사용합니다.
  * 바인딩 값이 `null`이나 `undefined`인 경우, 해당 속성은 렌더링 요소에서 제거됩니다.

<!-- end list -->

```html
<div v-bind:id="dynamicId"></div>
```

```javascript
const dynamicId = ref('my-id')
```

### 1.3 JavaScript Expressions (자바스크립트 표현식)

  * Vue 템플릿 내에서 JavaScript 표현식의 모든 기능을 지원합니다.
  * 표현식은 하나의 값으로 평가될 수 있는 코드 조각이어야 합니다 (`return` 뒤에 사용할 수 있는 코드).

<!-- end list -->

```html
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div v-bind:id="`list-${id}`"></div>
```

-----

## 2\. Directive (디렉티브)

  * `v-` 접두사를 가진 특수 속성으로, DOM 요소에 반응형 동작을 적용합니다.

### 2.1 구성 요소

  * **Name**: `v-on` (디렉티브 이름)
  * **Argument**: `:submit` (콜론으로 구분, 일부 디렉티브에서 사용)
  * **Modifiers**: `.prevent` (점(.)으로 구분, 특별한 방식의 바인딩을 지시)
  * **Value**: `"onSubmit"` (JavaScript 표현식)

예시: `<form v-on:submit.prevent="onSubmit">...</form>`

### 2.2 Built-in Directives

  * `v-text`, `v-show`, `v-if`, `v-for`, `v-bind`, `v-on`, `v-model` 등

-----

## 3\. v-bind

HTML 태그의 속성, 클래스, 스타일을 데이터와 동적으로 연결합니다.

### 3.1 Dynamic Attribute Name

대괄호(`[]`)를 사용하여 인자를 동적으로 설정할 수 있습니다.

```html
<button :[key]="myValue"></button>
```

### 3.2 Class and Style Bindings

**Binding HTML Classes: Binding to Objects**
객체를 전달하여 클래스를 동적으로 전환할 수 있습니다.

```html
<div :class="{ active: isActive }"></div>
```

```html
<div class="static" :class="{ active: isActive, 'text-primary': hasInfo }"></div>
```

```javascript
const isActive = ref(true)
const hasInfo = ref(false)
```

**Binding HTML Classes: Binding to Arrays**
배열을 사용하여 여러 클래스를 적용할 수 있습니다.

```html
<div :class="[activeClass, errorClass]"></div>
```

```javascript
const activeClass = ref('active')
const errorClass = ref('text-danger')
```

**Binding Inline Styles**
JavaScript 객체나 배열을 사용하여 스타일을 적용할 수 있습니다.

```html
<div :style="{ color: activeColor, fontSize: fontSize + 'px' }"></div>
```

```javascript
const activeColor = ref('crimson')
const fontSize = ref(30)
```

```html
<div :style="[baseStyles, overridingStyles]"></div>
```

-----

## 4\. Event Handling (v-on)

DOM 이벤트를 수신하고 트리거 될 때 JavaScript 코드를 실행합니다.

  * **Shorthand (약어)**: `@` (예: `v-on:click` -\> `@click`)

### 4.1 Handler Types

**Inline Handlers**
이벤트가 트리거 될 때 실행될 인라인 JavaScript 코드입니다.

```html
<button @click="count++">Add 1</button>
<p>Count is: {{ count }}</p>
```

**Method Handlers**
컴포넌트에 정의된 메서드 이름을 전달합니다.

```html
<button @click="greet">Greet</button>
```

```javascript
const greet = function(event) {
  alert('Hello ' + name.value + '!')
  if (event) {
    alert(event.target.tagName)
  }
}
```

### 4.2 인자 전달 및 $event

**사용자 지정 인자 전달**

```html
<button @click="say('hello')">Say hello</button>
<button @click="say('bye')">Say bye</button>
```

\*\*이벤트 객체($event) 접근**
인라인 핸들러에서 원본 DOM 이벤트에 접근해야 할 때 `$event\`를 사용합니다.

```html
<button @click="warn('Form cannot be submitted yet.', $event)">
  Submit
</button>
```

```javascript
function warn(message, event) {
  if (event) {
    event.preventDefault()
  }
  alert(message)
}
```

### 4.3 Event Modifiers

이벤트 처리를 위한 수식어들입니다.

  * `.stop` (stopPropagation)
  * `.prevent` (preventDefault)
  * `.self`, `.capture`, `.once`, `.passive` 등

<!-- end list -->

```html
<a @click.stop="doThis"></a>

<form @submit.prevent="onSubmit"></form>

<a @click.stop.prevent="doThat"></a>
```

### 4.4 Key Modifiers

키보드 이벤트를 수신할 때 특정 키를 확인합니다.

```html
<input @keyup.enter="submit" />
```

-----

## 5\. Form Input Bindings (v-model)

폼 입력 요소(`input`, `textarea`, `select` 등)와 JavaScript 상태 간의 **양방향 바인딩**을 생성합니다.

  * 내부적으로 `v-bind:value`와 `v-on:input`을 조합하여 동작합니다.
  * IME(한국어, 중국어 등) 입력 시에는 글자가 완성되기 전까지 데이터가 업데이트되지 않을 수 있으므로, 실시간 반영이 필요하면 `v-bind`와 `v-on`을 사용해야 합니다.

### 5.1 활용 예시

**Checkbox (배열 바인딩)**

```html
<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
<label for="jack">Jack</label>

<input type="checkbox" id="john" value="John" v-model="checkedNames">
<label for="john">John</label>

<input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
<label for="mike">Mike</label>
```

```javascript
const checkedNames = ref([])
```

**Select (단일 선택)**

```html
<div>Selected: {{ selected }}</div>

<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>A</option>
  <option>B</option>
  <option>C</option>
</select>
```

```javascript
const selected = ref('')
```

-----

## 6\. 참고 사항 (Reference)

### 6.1 `$` 접두사가 붙은 변수

  * Vue 인스턴스 내에서 사용자가 정의한 반응형 변수나 메서드와 구분하기 위해 Vue가 제공하는 내부 공개 프로퍼티나 메서드에 사용됩니다 (예: `$event`, `$emit` 등).
  * 사용자가 변수를 만들 때 `$`나 `_`로 시작하는 것은 피하는 것이 좋습니다.

### 6.2 IME (Input Method Editor)

  * 한글과 같은 조합형 언어는 `v-model` 사용 시 한 글자가 완성(조합)되어야 데이터에 반영됩니다.
  * 입력 중인 상태를 실시간으로 반영하려면 `v-model` 대신 `v-bind:value`와 `v-on:input`을 직접 사용해야 합니다.