요청하신 강의 영상의 내용을 바탕으로 마크다운(.md) 파일을 작성했습니다.

```md
# SSAFY 강의 노트: JavaScript & DOM

---

## 📜 JavaScript 역사

### 1. 웹의 탄생 (1990)
* **Tim Berners-Lee**가 WWW (World Wide Web), 하이퍼텍스트 시스템을 개발했습니다.
* URL, HTTP, 초기 웹 브라우저를 설계하고 구현했습니다.

### 2. 1-2차 브라우저 전쟁
* **1차 (1996):** Netscape (JavaScript) vs Microsoft (JScript)
    * 두 회사가 독자적인 규격을 사용하면서 브라우저 간 호환성 문제가 심각해졌습니다. (웹 표준의 부재)
* **2차 (2004-2017):** IE vs Firefox, Chrome
    * Firefox의 등장으로 IE가 웹 표준을 준수하려는 노력을 시작했습니다.
    * Chrome (2008)이 등장하며, **V8 엔진**의 빠른 속도와 **웹 표준 준수**를 기반으로 시장을 주도하게 되었습니다.

### 3. ECMAScript
* ECMA International이 정의한 "표준화된 스크립트 언어 명세"입니다.
* **ES5 (2009):** 안정성과 생산성이 향상되었습니다.
* **ES6 (2015):** 언어의 큰 발전을 이룬 버전으로, 가장 중요한 버전 중 하나로 평가됩니다.

---

## 💻 JavaScript 기본: 변수와 스코프

### 1. 변수 선언 키워드 3가지
* **`let`**: 재할당이 필요한 변수 선언 시 사용합니다. (블록 스코프)
* **`const`**: 재할당이 불가능한 상수 선언 시 사용하며, **반드시 선언과 동시에 초기화**해야 합니다. (블록 스코프)
* **`var`**: 재선언 및 재할당이 가능합니다. (함수 스코프)
    > **[!] 주의:** `var`는 **호이스팅(Hoisting)** 문제를 유발하고 블록 스코프를 따르지 않아, 현재는 사용을 권장하지 않습니다.

### 2. 스코프 (Scope)
* **블록 스코프 (Block scope):** `if`, `for` 등 중괄호(`{ }`) 내부를 의미합니다. `let`, `const`는 블록 스코프를 따릅니다.
* **함수 스코프 (Function scope):** 함수 내부를 의미합니다. `var`는 함수 스코프를 따릅니다.

### 3. 호이스팅 (Hoisting) 이란?
* 변수 선언문이 코드의 최상단으로 "끌어올려지는" 현상을 의  미합니다.
* `var`로 선언된 변수는 선언되기 전에 `undefined`로 접근 가능합니다. (에러가 발생하지 않음)

---

## 🌳 DOM (Document Object Model)

### 1. DOM 이란?
* HTML 문서를 표현하는 **문서 구조 (Document structure)**입니다.
* 웹 페이지의 요소(태그)들을 **객체(Object)**로 표현한 모델입니다.
* JavaScript가 이 객체 모델(DOM)에 접근하여 페이지의 구조, 스타일, 콘텐츠를 조작할 수 있게 하는 **API**입니다.
* `document` 객체는 DOM 트리의 최상위 객체이자 모든 조작의 진입점입니다.

### 2. DOM 선택 (Selection)
* **`document.querySelector(selector)`**
    * 제공된 CSS 선택자와 일치하는 **첫 번째 요소** 하나를 반환합니다.
    * 일치하는 요소가 없으면 `null`을 반환합니다.
* **`document.querySelectorAll(selector)`**
    * 제공된 CSS 선택자와 일치하는 **모든 요소**를 `NodeList` (유사 배열) 형태로 반환합니다.

---

## 🛠️ DOM 조작 (Manipulation)

### 1. HTML 콘텐츠 조작
* **`element.textContent`**: 요소의 텍스트 내용을 가져오거나 설정합니다.

### 2. Style 조작
* **`element.style`** 속성을 사용합니다.
* 예: `pTag.style.color = 'crimson'`, `pTag.style.fontSize = '2rem'`
* **[!] 주의:** CSS 속성명에 하이픈(-)이 있는 경우(예: `font-size`), JavaScript에서는 카멜 케이스(camelCase) (예: `fontSize`)로 변환하여 사용해야 합니다.

### 3. 속성 (Attribute) 조작
* **클래스(Class) 조작: `element.classList`**
    * `element.classList.add('className')`: 클래스 추가
    * `element.classList.remove('className')`: 클래스 제거
* **일반 속성 조작**
    * `element.getAttribute('name')`: 속성 값 조회
    * `element.setAttribute('name', 'value')`: 속성 값 설정
    * `element.removeAttribute('name')`: 속성 제거

### 4. DOM 요소 조작
* **`document.createElement(tagName)`**: 새 HTML 요소를 **메모리에** 생성합니다.
* **`Node.appendChild(childNode)`**: 부모 노드의 마지막 자식으로 노드를 **삽입**합니다. (이때 화면에 보이게 됩니다.)
* **`Node.removeChild(childNode)`**: 자식 노드를 DOM에서 **제거**합니다.

---

## 📚 참고: 용어 정리

* **NodeList**:
    * `querySelectorAll` 등으로 반환되는 노드(요소)의 목록입니다.
    * 배열과 유사하게 인덱스로 접근 가능합니다.
    * `querySelectorAll`이 반환하는 `NodeList`는 **정적(static)**이며, DOM 변경 사항이 실시간으로 반영되지 않습니다.
* **Parsing (파싱)**:
    * 브라우저가 문자열(HTML 코드)을 해석하여 DOM Tree로 만드는 과정입니다.
```