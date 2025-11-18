네, 알겠습니다. 코드 외에 동영상에서 다룬 주요 이론적인 내용들을 추가하여 마크다운 파일을 다시 구성했습니다.

-----

# Javascript DOM & 기초 문법/이론 정리

## 목차

1.  **JavaScript의 역사와 이론**
      * 웹의 탄생 (1990)
      * 웹 브라우저의 대중화 (1993)
      * 1차 브라우저 전쟁 (1996)
      * 2차 브라우저 전쟁 (2004-2017)
      * ECMAScript (표준 명세)
2.  **변수 (Variables)**
      * 변수 선언 키워드 (`let`, `const`, `var`)
      * 스코프 (Scope)
      * 호이스팅 (Hoisting)
      * 변수 명명 규칙 (Naming Convention)
3.  **DOM (Document Object Model)**
      * 문서 구조 (Document structure)
      * DOM 이란?
      * DOM Tree
4.  **DOM 선택 (DOM Selection)**
      * `document.querySelector()`
      * `document.querySelectorAll()`
5.  **DOM 조작 (DOM Manipulation)**
      * HTML 콘텐츠 조작 (`textContent`)
      * 속성 조작 (`setAttribute`, `getAttribute`)
      * 클래스 속성 조작 (`classList`)
      * Style 조작 (`style`)
      * DOM 요소 생성 및 제거 (`createElement`, `appendChild`)
6.  **주요 용어 정리**
      * Parsing (파싱)
      * `NodeList`

-----

## 1\. JavaScript의 역사와 이론

### 웹의 탄생 (1990)

  * \*\*팀 버너스리(Tim Berners-Lee)\*\*가 하이퍼텍스트 시스템인 \*\*WWW (World Wide Web)\*\*를 고안했습니다.
  * 웹 페이지를 찾기 위한 **URL**, 웹과 서버 간 통신 규약인 **HTTP**, 웹 페이지를 만드는 **HTML**의 초기 버전을 설계하고 구현했습니다.

### 웹 브라우저의 대중화 (1993)

  * 최초의 상용 웹 브라우저인 **Netscape Navigator**가 출시되었습니다.
  * 당시 90% 이상의 시장 점유율을 가졌으며, 웹의 동적인 기능을 위해 프로젝트(JavaScript)를 시작했습니다.

### 1차 브라우저 전쟁 (1996)

  * Microsoft가 **Internet Explorer(IE) 3.0**에 JavaScript와 유사한 'JScript'를 도입했습니다.
  * 이로 인해 회사마다 독자적인 브라우저 규격을 변경하기 시작했고, **웹 표준**의 필요성이 대두되었습니다. (크로스 브라우징 이슈 발생)

### 2차 브라우저 전쟁 (2004-2017)

  * IE가 표준을 정의했지만, 가장 높은 점유율을 가진 IE는 표준을 지키지 않았습니다.
  * **Firefox**가 IE에 대항하기 시작했으며, 2008년 **Chrome**이 등장했습니다.
  * Chrome은 **V8 JavaScript 엔진**을 필두로 한 빠른 속도와 **웹 표준 준수**를 내세워 웹 시장을 주도하게 되었습니다.

### ECMAScript (표준 명세)

  * JavaScript의 표준화된 스크립트 언어 명세를 의미합니다. (ECMA International이 정의)
  * `ECMAScript 5 (ES5)` (2009): 안정성과 생산성을 크게 높였습니다.
  * `ECMAScript 2015 (ES6)` (2015): 획기적인 발전을 이룬 버전으로, `let`, `const`, 화살표 함수 등 많은 중요 문법이 추가되었습니다.

[Image of ECMAScript version evolution timeline]

-----

## 2\. 변수 (Variables)

### 변수 선언 키워드 (`let`, `const`, `var`)

ES6 이후로는 `let`과 `const`를 주로 사용합니다.

  * **`let`**: 재할당이 필요한 변수를 선언할 때 사용합니다. (블록 스코프)
  * **`const`**: 재할당이 불가능한 상수(constant)를 선언할 때 사용합니다. 선언 시 반드시 값을 초기화해야 합니다. (블록 스코프)
    ```javascript
    const number = 10;
    // number = 20; // TypeError: Assignment to constant variable.

    // const name; // SyntaxError: Missing initializer in const declaration.
    ```
  * **`var`**: ES6 이전에 사용되던 키워드. 재선언 및 재할당이 모두 가능하며, 함수 스코프를 가집니다. 호이스팅 문제가 있어 현재는 사용을 권장하지 않습니다.

### 스코프 (Scope)

  * **블록 스코프 (Block scope)**: `let`, `const`는 ` {}  `(중괄호)로 둘러싸인 블록 내에서만 유효합니다.
    ```javascript
    let x = 1;
    if (x === 1) {
      let x = 2;
      console.log(x); // 2
    }
    console.log(x); // 1
    ```
  * **함수 스코프 (Function scope)**: `var`는 함수 내에서 선언되면 함수 전체에서 유효합니다.
    ```javascript
    function foo() {
      var x = 1;
      console.log(x); // 1
    }
    foo();
    // console.log(x); // ReferenceError: x is not defined
    ```

### 호이스팅 (Hoisting)

  * `var`로 선언된 변수나 함수 선언문이 해당 스코프의 최상단으로 끌어 올려지는 것처럼 동작하는 현상입니다.
  * `var`로 선언된 변수는 선언부는 끌어 올려지지만, 할당부는 제자리에 남아있어 `undefined`가 출력될 수 있습니다.
    ```javascript
    // 실제 코드
    console.log(name); // undefined
    var name = '홍길동';

    // 자바스크립트 해석 (호이스팅 발생)
    var name; // 선언부가 호이스팅됨
    console.log(name);
    name = '홍길동'; // 할당부는 제자리에 있음
    ```

### 변수 명명 규칙 (Naming Convention)

  * **카멜 케이스 (camelCase)**: 변수, 함수명에 사용. (예: `myVariable`)
  * **파스칼 케이스 (PascalCase)**: 클래스, 생성자명에 사용. (예: `MyClass`)
  * **스네이크 케이스 (SNAKE\_CASE)**: 상수(constants)명에 사용. (예: `MAX_NUMBER`)

-----

## 3\. DOM (Document Object Model)

### 문서 구조 (Document structure)

  * 브라우저가 텍스트(HTML)를 표현하기 위해 사용하는 데이터 구조입니다.
  * 우측 이미지와 같은 문서의 모양(구조)을 객체(Object)로 표현합니다.

### DOM 이란?

  * \*\*Document Object Model (문서 객체 모델)\*\*의 약자입니다.
  * 웹 페이지(HTML 문서)를 객체로 표현한 모델이며, 자바스크립트와 같은 프로그래밍 언어가 웹 페이지에 접근하고 조작할 수 있도록 해주는 \*\*API (인터페이스)\*\*입니다.
  * 자바스크립트는 이 DOM을 통해 HTML의 구조, 콘텐츠, 스타일을 동적으로 변경할 수 있습니다.

### DOM Tree

  * HTML 태그를 나타내는 elements의 문서는 구조를 결정합니다.
  * DOM은 문서를 **트리(Tree) 구조**로 표현하며, `document` 객체는 이 트리의 최상위 진입점이 됩니다.
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Document</title>
    </head>
    <body>
      <h1>Heading</h1>
      <p>Hello, <a href="https://www.google.com/">google</a></p>
    </body>
    </html>
    ```

-----

## 4\. DOM 선택 (DOM Selection)

CSS 선택자를 사용하여 HTML 요소를 선택합니다.

### `document.querySelector(selector)`

  * 제공된 CSS 선택자와 일치하는 **첫 번째** 요소를 반환합니다.
  * 일치하는 요소가 없으면 `null`을 반환합니다.

### `document.querySelectorAll(selector)`

  * 제공된 CSS 선택자와 일치하는 **모든** 요소를 `NodeList` (유사 배열 객체) 형태로 반환합니다.

-----

## 5\. DOM 조작 (DOM Manipulation)

### HTML 콘텐츠 조작 (`textContent`)

  * `Element.textContent` 속성은 요소 내부의 텍스트 콘텐츠를 가져오거나 설정합니다.
    ```javascript
    <script>
      const h1Tag = document.querySelector('.heading');

      // 텍스트 내용 변경
      h1Tag.textContent = '내용 수정';

      // 텍스트 내용 확인
      console.log(h1Tag.textContent); // '내용 수정'
    </script>
    ```

### 속성 조작 (`setAttribute`, `getAttribute`)

  * `Element.getAttribute(name)`: 요소의 지정된 속성 값을 반환합니다.
  * `Element.setAttribute(name, value)`: 요소에 지정된 속성 값을 설정합니다.
  * `Element.removeAttribute(name)`: 요소에서 지정된 속성을 제거합니다.

### 클래스 속성 조작 (`classList`)

  * `Element.classList` 속성은 요소의 클래스 목록을 `DOMTokenList` 형태로 반환합니다.
  * `Element.classList.add('className')`: 클래스를 추가합니다.
  * `Element.classList.remove('className')`: 클래스를 제거합니다.
    ```css
    /* style.css */
    .red {
      color: crimson;
    }
    ```
    ```javascript
    // <p>요소에 'red' 클래스 추가하기
    const pTag = document.querySelector('p');
    pTag.classList.add('red');
    ```

### Style 조작 (`style`)

  * `Element.style` 속성을 통해 요소의 인라인 스타일을 직접 조작할 수 있습니다.
  * CSS 속성명이 하이픈(-)을 포함하는 경우 (예: `font-size`), camelCase(예: `fontSize`)로 변환하여 사용해야 합니다.
    ```javascript
    const pTag = document.querySelector('p');

    pTag.style.color = 'crimson';
    pTag.style.fontSize = '2rem'; // 'font-size' 아님

    console.log(pTag.style); // CSSStyleDeclaration 객체
    ```

### DOM 요소 생성 및 제거

  * `document.createElement(tagName)`: 지정된 태그명의 새로운 HTML 요소를 생성합니다.
  * `Node.appendChild(childNode)`: 특정 부모 노드의 자식 노드 리스트 중 마지막 자식으로 노드를 추가합니다.
  * `Node.removeChild(childNode)`: DOM에서 자식 노드를 제거합니다.

-----

## 6\. 주요 용어 정리

  * **Parsing (파싱)**: 브라우저가 문자열(HTML, CSS 등)을 해석하여 **DOM Tree**와 같은 의미 있는 구조로 변환하는 과정을 의미합니다.
  * **`NodeList`**: `querySelectorAll` 메서드 등을 통해 반환되는 노드(element)의 컬렉션(집합)입니다. 배열과 유사하게 인덱스로 각 항목에 접근할 수 있지만, 배열의 모든 메서드를 지원하지는 않는 **유사 배열**입니다. (단, `forEach` 등은 사용 가능)