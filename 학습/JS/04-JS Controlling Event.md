제공해주신 내용의 8번 항목 뒤에 **Lodash(로 대시)** 관련 내용을 추가하여 전체 문서를 완성해 드립니다.

-----

# JavaScript Controlling Event (완전 정복 + Lodash)

## 1\. 이벤트(Event)의 개념

### 1-1. 일상 속의 이벤트

프로그래밍의 이벤트는 우리의 일상생활과 매우 유사합니다.

  * **컴퓨터:** 키보드를 눌러 텍스트를 입력하는 것.
  * **전화기:** 전화벨이 울려 전화가 왔음을 알리는 것.
  * **제스처:** 손을 흔들어 인사하는 것.
  * **리모컨:** 버튼을 눌러 채널을 변경하는 것.

### 1-2. 웹 환경에서의 이벤트

  * **정의:** 웹 페이지에서 발생하는 모든 신호나 사건 (클릭, 입력, 드래그 등).
  * **DOM 요소:** HTML 문서는 브라우저 안에서 객체(DOM)로 변환되며, 이벤트는 이 **DOM 요소**에서 발생합니다.
  * **이벤트 객체 생성:** 이벤트가 발생하는 순간, 브라우저는 해당 이벤트에 대한 상세 정보를 담은 **Event Object**를 자동으로 생성합니다.

-----

## 2\. 이벤트 핸들러 (Event Handler)

이벤트가 발생했을 때, 시스템이 어떻게 반응할지를 정의하는 것입니다.

### 2-1. 바리스타 비유 (핵심)

  * **Event (주문):** 손님이 커피를 주문합니다.
  * **Event Handler (바리스타):** 주문을 받으면 커피를 만드는 **행동**을 합니다.
  * **역할:** 주문(이벤트)이 들어왔을 때, 바리스타(핸들러)가 연결되어 있어야 주문 처리가 가능합니다.

### 2-2. 정의

  * 특정 이벤트가 발생했을 때 실행되는 **콜백(Callback) 함수**입니다.
  * 사용자의 행동에 반응하여 로직을 수행하는 역할을 합니다.

-----

## 3\. 이벤트 등록 (`addEventListener`)

DOM 요소에 이벤트 핸들러를 연결하는 가장 권장되는 메서드입니다.

### 3-1. 기본 문법 구조

```javascript
element.addEventListener(type, handler)
```

1.  **element:** 이벤트를 감지할 대상 (DOM 요소).
2.  **type (이벤트 유형):** 수신할 이벤트의 이름 (**문자열**로 작성).
      * 예: `'click'`, `'mouseover'`, `'input'`, `'submit'` 등.
3.  **handler (핸들러):** 이벤트 발생 시 실행될 **함수**.
      * 함수 호출 `()` 형태가 아니라, **함수 이름**이나 **익명 함수** 자체를 전달해야 함.
      * **반환 값:** 없음.

### 3-2. 코드 예시

```javascript
const button = document.querySelector('#btn');

// 1. 핸들러 함수 정의
const handleClick = function(event) {
    alert('버튼 클릭됨!');
}

// 2. 이벤트 등록
button.addEventListener('click', handleClick);
```

-----

## 4\. 이벤트 객체와 `this` 주의사항 (중요)

### 4-1. 이벤트 객체 (`event`)

핸들러 함수는 호출될 때 브라우저로부터 **Event 객체**를 첫 번째 인자로 자동 전달받습니다.

  * `event.type`: 발생한 이벤트 종류.
  * `event.target`: 실제 이벤트가 발생한 요소.

### 4-2. 핸들러 내부의 `this` (Slide 54)

작성하는 함수 형태에 따라 `this`가 가리키는 대상이 달라지므로 주의가 필요합니다.

| 함수 형태 | `this`의 값 | 비고 |
| :--- | :--- | :--- |
| **일반 함수** (`function`) | **이벤트가 연결된 요소** (`currentTarget`) | 권장되는 방식 중 하나 |
| **화살표 함수** (`=>`) | **상위 스코프의 객체** (대부분 `window`) | **주의:** 핸들러 요소를 가리키지 않음 |

> **해결책:** 화살표 함수를 사용하거나 명확성을 위해서는 `this` 대신 항상 \*\*`event.currentTarget`\*\*을 사용하는 것이 좋습니다.

```javascript
// 일반 함수 (this === button)
button.addEventListener('click', function(event) {
    console.log(this); // <button>
});

// 화살표 함수 (this === window)
button.addEventListener('click', (event) => {
    console.log(this); // Window
    console.log(event.currentTarget); // <button> (이렇게 써야 함)
});
```

-----

## 5\. 이벤트 전파 (Event Propagation)

### 5-1. 버블링 (Bubbling)

  * **개념:** 한 요소에서 이벤트가 발생하면, 해당 요소의 핸들러가 동작한 후 **부모 요소 → 최상위 요소(Document)** 순으로 이벤트가 전파되는 현상.
  * **특징:** 마치 물속에서 거품이 위로 올라가는 것과 같습니다.
  * **예시:** `p` 태그를 클릭하면 `p` -\> `div` -\> `form` 순서로 클릭 이벤트가 모두 발생합니다.

### 5-2. 캡처링 (Capturing)

  * 이벤트가 최상위 요소에서 하위 요소로 전파되는 단계 (버블링의 반대).
  * 실제 개발에서는 잘 사용되지 않습니다.

-----

## 6\. `target`과 `currentTarget`

버블링 현상 때문에 핸들러 내에서 이 두 속성을 구분하는 것이 중요합니다.

  * **`event.target`**: 실제 이벤트를 **유발한(시작한) 가장 안쪽의 요소**. (변하지 않음)
  * **`event.currentTarget`**: 현재 이벤트 핸들러가 **등록된(연결된) 요소**. (이벤트가 전파되면서 바뀜)

**예시 상황:** `div` 안에 `button`이 있고, `div`에 핸들러를 단 경우.

  * 사용자가 `button` 클릭 시:
      * `target`: **button**
      * `currentTarget`: **div**

-----

## 7\. 기본 동작 방지 (`preventDefault`)

HTML 태그가 가진 고유의 동작을 막고 싶을 때 사용합니다.

### 7-1. 주요 사용 사례

  * **`<form>`:** `submit` 시 페이지 새로고침 방지.
  * **`<a>`:** 링크 이동 방지.
  * **`copy`:** 텍스트 복사 방지.

### 7-2. 복사 방지 코드

```javascript
const h1Tag = document.querySelector('h1');
h1Tag.addEventListener('copy', function(event) {
    event.preventDefault(); // 복사 기능 취소
    alert('복사 할 수 없습니다.');
});
```

-----

## 8\. 실습: 동적인 웹 만들기

영상에서 다룬 3가지 주요 실습 예제입니다.

### [실습 1] 입력 값 실시간 출력 (`input`)

사용자의 입력을 실시간으로 감지하여 화면에 보여줍니다.

```javascript
const inputTag = document.querySelector('#text-input');
const pTag = document.querySelector('p');

inputTag.addEventListener('input', function(event) {
    // 사용자가 입력한 값(value)을 p태그 텍스트로 넣음
    pTag.textContent = event.target.value;
});
```

### [실습 2] 클릭 & 스타일 토글 (`click`)

버튼 클릭 시 CSS 클래스를 껐다 켰다(Toggle) 합니다.

```javascript
const btn = document.querySelector('#btn');
const h1Tag = document.querySelector('h1');

// CSS: .blue { color: blue; }
btn.addEventListener('click', function() {
    h1Tag.classList.toggle('blue'); // 클래스 추가/제거 반복
});
```

### [실습 3] Todo List 구현 (종합)

`submit` 이벤트 제어, 빈 값 확인, 요소 생성 및 추가를 모두 활용합니다.

```javascript
const formTag = document.querySelector('.input-form');
const inputTag = document.querySelector('.input-data');
const ulTag = document.querySelector('.todo-list');

const addTodo = function(event) {
    event.preventDefault(); // 1. 새로고침 방지 (필수)

    const data = inputTag.value;

    // 2. 빈 문자열 입력 방지
    if (data.trim()) {
        const li = document.createElement('li'); // 요소 생성
        li.textContent = data;
        ulTag.appendChild(li); // 리스트에 추가
        inputTag.value = "";   // 입력창 초기화
    } else {
        alert('내용을 입력하세요.');
    }
}

formTag.addEventListener('submit', addTodo);
```

-----

## 9\. Lodash (로 대시)

영상 슬라이드 45페이지에 소개된 **JavaScript 유틸리티 라이브러리**입니다.

### 9-1. 개념 및 필요성

  * **정의:** 배열, 객체, 숫자, 문자열 등을 다룰 때 자주 쓰이는 필수 기능을 모아놓은 라이브러리입니다.
  * **특징:**
      * 순수 자바스크립트(Vanilla JS)로 짜면 길고 복잡해지는 코드를 **매우 간결하게** 만들어줍니다.
      * 데이터의 유효성 검사나 구조 변환이 쉽습니다.
  * **관례:** 라이브러리 이름처럼 보통 **`_` (underscore)** 라는 변수명으로 불러와 사용합니다.

### 9-2. 주요 함수 예시

라이브러리를 HTML에 로드(`<script src="...">`)한 후 사용 가능합니다.

```javascript
// 1. _.sample(array): 배열에서 요소 하나를 무작위로 추출
const fruits = ['Apple', 'Banana', 'Cherry'];
console.log(_.sample(fruits)); // 예: 'Banana'

// 2. _.sampleSize(array, n): 배열에서 n개의 요소를 무작위 추출
// 활용: 로또 번호 생성기 등
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log(_.sampleSize(numbers, 3)); // 예: [2, 9, 5]

// 3. _.range(start, end): 특정 범위의 숫자 배열 생성
const nums = _.range(1, 5); 
console.log(nums); // [1, 2, 3, 4] (종료값 5는 포함 안 됨)
```