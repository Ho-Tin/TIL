
-----

# JavaScript: AJAX & Asynchronous Programming

## 1\. 동기(Synchronous) vs 비동기(Asynchronous)

### 1.1. 동기 (Synchronous)

  * **정의**: 프로그램의 실행 흐름이 순차적으로 진행되는 방식.
  * **특징**: 하나의 작업이 완료된 후에야 다음 작업이 실행됩니다. 앞선 작업이 길어지면 뒤의 작업은 계속 대기해야 합니다(Blocking).

**[동기 코드 예시]**

```javascript
console.log('작업 1 시작')

const syncTask = function () {
  for (let i = 0; i < 1000000000; i++) {
    // 반복 실행 동안 잠시 대기
  }
  return '작업 완료'
}

const result = syncTask()
console.log(result)

console.log('작업 2 시작')

/* 출력 결과 */
// 작업 1 시작
// (반복 실행 동안 잠시 대기)
// 작업 완료
// 작업 2 시작
```

### 1.2. 비동기 (Asynchronous)

  * **정의**: 특정 작업의 완료를 기다리지 않고 다음 작업을 즉시 실행하는 방식.
  * **특징**: 병렬적으로 작업을 처리하며, 시간이 오래 걸리는 작업(예: 데이터 로딩, API 호출)을 백그라운드에서 실행하여 사용자 경험(UX)을 향상시킵니다(Non-blocking).

**[비동기 코드 예시]**

```javascript
console.log('작업 1 시작')

const asyncTask = function (callBack) {
  setTimeout(() => {
    callBack('작업 완료')
  }, 3000) // 3초를 기다렸다가 콜백 함수를 호출하는 함수
}

asyncTask((result) => {
  console.log(result)
})

console.log('작업 2 시작')

/* 출력 결과 */
// 작업 1 시작
// 작업 2 시작
// (3초 후)
// 작업 완료
```

-----

## 2\. JavaScript Runtime (동작 원리)

자바스크립트는 기본적으로 **Single Thread** 언어이지만, 브라우저 환경을 통해 비동기 처리가 가능합니다.

### 구성 요소

1.  **JavaScript Engine (Call Stack)**
      * 코드가 실행되면 함수 호출이 순서대로 쌓이는 작업 공간.
      * Single Thread이므로 한 번에 하나의 작업만 처리 가능.
2.  **Web API**
      * 브라우저에서 제공하는 런타임 환경.
      * 시간이 걸리거나 언제 실행될지 모르는 비동기 작업들(DOM Events, AJAX, setTimeout 등)을 처리.
3.  **Task Queue**
      * Web API에서 처리가 완료된 작업(콜백 함수)들이 순서대로 줄을 서서 기다리는 대기열.
4.  **Event Loop**
      * Call Stack이 비어 있는지 계속해서 확인.
      * Call Stack이 비어 있다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보냄.

### 동작 순서 시각화 (`setTimeout` 예시)

1.  `console.log('Hi')` → Call Stack에서 즉시 실행.
2.  `setTimeout` 호출 → Call Stack에서 실행되지만, 처리는 **Web API**로 위임(타이머 시작).
3.  `console.log('Bye')` → Call Stack에서 즉시 실행.
4.  타이머 종료(3초 경과) → 콜백 함수가 **Task Queue**로 이동.
5.  **Event Loop**가 Call Stack이 비어있음을 확인하고, Task Queue의 콜백 함수를 Call Stack으로 이동.
6.  콜백 함수(`console.log('Work')`) 실행.

-----

## 3\. AJAX (Asynchronous JavaScript And XML)

  * **정의**: 비동기적인 웹 애플리케이션을 제작하기 위한 웹 개발 기법.
  * **특징**:
      * 브라우저와 서버 간의 데이터를 비동기적으로 교환.
      * 페이지 전체를 새로고침하지 않고도 **일부분만 업데이트** 가능 (Single Page Application의 기반).
      * 과거엔 XML을 썼으나 현재는 **JSON** 형식을 주로 사용.
  * **XHR (XMLHttpRequest)**: 자바스크립트를 사용하여 서버에 HTTP 요청을 할 수 있는 객체.

-----

## 4\. Axios

브라우저와 Node.js 환경에서 모두 사용할 수 있는 **Promise 기반의 HTTP 클라이언트 라이브러리**입니다.

  * XMLHttpRequest보다 사용이 간편하고 편리한 기능을 제공합니다.
  * **설치/사용**: CDN 등을 통해 로드하여 사용 (`<script src="..."></script>`).

### 4.1. Axios 기본 구조

```javascript
axios({
  method: 'post',
  url: '/user/12345',
  data: {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }
})
.then((콜백함수) => {
    // 성공 처리
    // 서버로부터 받은 응답 데이터를 처리
    // then 메서드를 사용해서 "성공했을 때 수행할 로직"을 작성
})
.catch((콜백함수) => {
    // 실패 처리
    // 네트워크 오류나 서버 오류 등의 예외 상황을 처리
    // catch 메서드를 사용해서 "실패했을 때 수행할 로직"을 작성
})
```

### 4.2. 실습: 고양이 사진 가져오기

버튼을 클릭하면 고양이 이미지를 요청하고, 응답받은 이미지 URL을 `img` 태그에 넣어 화면에 출력하는 예제입니다.

```javascript
const URL = 'https://api.thecatapi.com/v1/images/search'
const btn = document.querySelector('button')

const getCats = function () {
  axios({
    method: 'get',
    url: URL,
  })
    .then((response) => {
      console.log(response)
      console.log(response.data)
      
      // 응답 데이터에서 이미지 url 추출 (구조에 따라 다를 수 있음, 예시는 배열의 첫 번째 요소)
      const imgUrl = response.data[0].url
      
      // 이미지 태그 생성 및 속성 설정 (화면 추가 로직은 생략됨, 예: body에 append)
      const img = document.createElement('img')
      img.setAttribute('src', imgUrl)
      document.body.appendChild(img) 
    })
    .catch((error) => {
      console.log(error)
      console.log('실패했다옹')
    })
    
  console.log('야옹야옹') // 비동기이므로 응답보다 먼저 출력될 수 있음
}

btn.addEventListener('click', getCats)
```

-----

## 5\. Callback과 Promise

### 5.1. 비동기 콜백의 문제점 (Callback Hell)

비동기 작업의 결과를 받아 순차적으로 다음 작업을 수행하기 위해 콜백 함수를 계속 중첩하면, 코드의 가독성이 떨어지고 유지보수가 어려워지는 \*\*"콜백 지옥(Callback Hell)"\*\*이 발생합니다.

### 5.2. Promise

  * **정의**: 자바스크립트에서 비동기 작업의 최종 완료 또는 실패를 나타내는 객체.
  * **목적**: 콜백 지옥 문제를 해결하고 비동기 처리를 명확하게 표현하기 위해 등장.
  * **특징**: "작업이 끝나면 실행 시켜 줄게"라는 약속(Promise).

### 5.3. Promise Chaining (체이닝)

Axios와 같은 라이브러리는 Promise 객체를 반환하므로 `then`과 `catch`를 이어서 작성할 수 있습니다.

```javascript
axios({...}) // Promise 객체 return
  .then(성공하면 수행할 1번 콜백함수) // 성공하면 수행할 1번 콜백함수
  .then(1번 콜백함수가 성공하면 수행할 2번 콜백함수) 
  .then(2번 콜백함수가 성공하면 수행할 3번 콜백함수)
  .catch(실패하면 수행할 콜백함수) // 위 과정 중 하나라도 실패하면 실행
```

### 5.4. Promise(Chaining)의 장점

1.  **가독성**: 비동기 작업의 순서와 의존 관계를 명확히 표현 가능.
2.  **에러 처리**: `catch` 메서드를 통해 전체 체인의 에러를 한 곳에서 통합 처리 가능.
3.  **유연성**: 각 단계마다 데이터를 가공하거나 다른 작업을 수행하기 용이.
4.  **코드 관리**: 비동기 작업을 분리하여 구성하므로 관리가 쉬움.

-----

## 핵심 요약

  * **비동기(Asynchronous)**: 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 실행하는 방식.
  * **JavaScript Runtime**: Call Stack, Web API, Task Queue, Event Loop의 상호작용으로 비동기 코드를 처리.
  * **Axios**: Promise 기반의 HTTP 클라이언트 라이브러리로, AJAX 요청을 쉽게 보낼 수 있음.
  * **Promise**: 비동기 작업의 성공/실패를 처리하고, `then` 체이닝을 통해 순차적인 비동기 로직을 가독성 있게 작성 가능.