

-----

# 관통 프로젝트 07: DOM 조작과 Event

## 1\. 개요

  * **목표:** 웹 페이지를 단순한 정적인 문서가 아닌, 사용자와 끊임없이 대화하고 반응하는 **살아있는 인터페이스**로 구현.
  * **Event란?** 웹 페이지 내에서 발생하는 모든 사건(클릭, 스크롤, 입력 등)을 말하며, JavaScript가 이를 감지하여 특정 동작을 수행하게 함.

-----

## 2\. Input Event (입력 이벤트)

### 2.1 개념

  * **Input Event:** 요소의 `value`(값)이 변경될 때마다 발생. 복사/붙여넣기에도 반응하므로 실시간 유효성 검사에 적합.
  * **Keyup Event:** 키보드 키를 눌렀다 뗄 때 발생. (예: Enter 키 감지 등 특정 키 조작 시 사용)

### 2.2 실습: 입력 유효성 확인 (글자 수 제한)

사용자가 입력한 텍스트가 지정된 길이(20자)를 넘으면 입력을 차단하고 시각적 알림을 줍니다.

**HTML 구조**

```html
<h1>텍스트 입력 제한 (20자)</h1>
<input type="text" class="text-input" id="textInput" placeholder="최대 20자">
<div class="counter" id="counter">0 / 20</div>
```

**JavaScript 로직**

```javascript
const textInput = document.querySelector('#textInput');
const counter = document.querySelector('#counter');
const maxLength = 20;

textInput.addEventListener('input', function (e) {
  const currentLength = e.target.value.length;

  // 글자 수 초과 시 처리
  if (currentLength > maxLength) {
    // 1. 초과된 뒷부분 잘라내기
    e.target.value = e.target.value.substring(0, maxLength); 
    
    // 2. 에러 효과 (CSS 클래스 추가)
    e.target.classList.add('error');

    // 3. 0.5초 뒤 에러 효과 제거 (애니메이션 재실행을 위함)
    setTimeout(() => {
      e.target.classList.remove('error');
    }, 500);
    return; 
  }

  // 정상 입력 시 카운터 업데이트    
  counter.textContent = `${currentLength} / ${maxLength}`;
});
```

-----

## 3\. Drag Event (드래그 이벤트)

### 3.1 핵심 조건

  * **`draggable="true"`**: 드래그하려는 HTML 요소에 반드시 이 속성이 있어야 합니다.
  * **`e.preventDefault()`**: `dragover` 이벤트에서 브라우저의 기본 동작(드래그 금지 등)을 막아야 `drop` 이벤트가 발생할 수 있습니다.

### 3.2 실습: 드래그를 통한 카드 순서 변경

드래그 중인 마우스 위치를 기준으로 다른 카드들과의 거리를 계산하여, 카드가 들어갈 위치를 동적으로 변경합니다.

**위치 계산 알고리즘 (JavaScript)**

```javascript
const container = document.querySelector('.container');

// 1. 드래그 중인 요소가 컨테이너 위에 있을 때 (필수 처리)
container.addEventListener('dragover', (e) => {
  e.preventDefault(); // 드래그 허용을 위해 기본 동작 취소
  
  // 현재 마우스 위치(y)를 기준으로 가장 가까운 뒷 요소 찾기
  const afterElement = getDragAfterElement(container, e.clientY);
  
  // 드래그 중인 요소(.dragging)를 DOM에서 이동시킴
  const draggable = document.querySelector('.dragging');
  
  if (afterElement == null) {
    container.appendChild(draggable); // 맨 뒤로 이동
  } else {
    container.insertBefore(draggable, afterElement); // 특정 요소 앞으로 이동
  }
});

// 2. 가장 가까운 카드를 찾는 함수
function getDragAfterElement(container, y) {
  // 드래그 중이 아닌 나머지 카드들만 선택
  const draggableElements = [...container.querySelectorAll('.draggable:not(.dragging)')];

  return draggableElements.reduce((closest, child) => {
    const box = child.getBoundingClientRect(); // 요소의 위치/크기 정보
    
    // offset = 마우스 위치 - 카드 수직 중심점
    const offset = y - (box.top + box.height / 2);

    // 마우스가 카드 중심보다 위에 있으면서(음수), 가장 가까운(최대값) 요소 찾기
    if (offset < 0 && offset > closest.offset) {
      return { offset: offset, element: child };
    } else {
      return closest;
    }
  }, { offset: Number.NEGATIVE_INFINITY }).element;
}
```

-----

## 4\. Scroll Event (스크롤 이벤트)

### 4.1 주요 속성

  * `window.scrollY`: 현재 스크롤된 수직 위치.
  * `element.scrollHeight`: 요소의 전체 콘텐츠 높이 (보이지 않는 영역 포함).
  * `window.innerHeight`: 현재 브라우저 화면(Viewport)의 높이.

### 4.2 실습: 스크롤 진행률 표시 (Progress Bar)

스크롤 위치에 따라 상단 바의 길이를 조절합니다.

**JavaScript 로직**

```javascript
function updateProgress() {
  const scrollTop = window.scrollY; // 현재 위치
  
  // 전체 스크롤 가능 범위 = 전체 높이 - 화면 높이
  const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;

  // 진행률 (0.0 ~ 1.0)
  const progress = scrollTop / scrollHeight;

  // CSS transform으로 너비 조절 (scaleX 활용이 성능상 유리)
  const progressBar = document.querySelector('.progress-bar');
  progressBar.style.transform = `scaleX(${progress})`;
}

window.addEventListener('scroll', updateProgress);
```

-----

## 5\. Parallax Scroll (패럴랙스 스크롤)

### 5.1 개념

스크롤 할 때 배경과 전경(앞의 요소)이 **서로 다른 속도**로 움직여 입체감(3D 효과)을 주는 기법입니다.

### 5.2 실습: 레이어별 속도 차이 구현

**JavaScript 로직**

```javascript
// 각 레이어별 속도 계수 설정
const speeds = {
  mountain: 0.05, // 멀리 있는 산 (천천히)
  cloud: 0.1,
  bird: 0.4       // 가까이 있는 새 (빠르게)
};

window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;

  // 요소별 이동 거리 계산: 스크롤 값 * 속도 계수
  const layerMountain = document.querySelector('.mountain');
  layerMountain.style.transform = `translateY(${scrolled * speeds.mountain}px)`;

  // 새는 대각선으로 이동 (X축 이동 추가)
  const layerBird = document.querySelector('.bird');
  layerBird.style.transform = `translate(${scrolled * speeds.bird * 0.1}px, ${scrolled * speeds.bird}px)`;
});
```

-----

## 6\. 심화 실습 (참고)

### 6.1 스크롤에 따른 배경색 변경 (해와 달)

스크롤 진행도에 따라 시간의 흐름(새벽→낮→밤)을 표현하기 위해 구간별 정규화를 수행합니다.

**로직 예시 (달의 이동)**

```javascript
// 전체 진행률(progress)이 60% ~ 100%일 때만 달이 움직이도록 설정
if (progress > 0.6) {
  // 0.6 ~ 1.0 사이의 값을 0 ~ 1 사이의 값으로 변환 (정규화)
  // 공식: (현재값 - 시작값) / (종료값 - 시작값)
  const normalizedProgress = (progress - 0.6) / 0.4; 
  
  // 화면 너비만큼 이동
  const moveX = normalizedProgress * (window.innerWidth - moonSize);
  moon.style.transform = `translateX(${moveX}px)`;
}
```

### 6.2 가로, 세로 스크롤 혼합

사용자는 마우스를 아래로 내리지만(세로 스크롤), 화면의 특정 컨텐츠는 옆으로 흐르는(가로 스크롤) 효과입니다.

**원리 및 코드**

1.  **Sticky:** 부모 컨테이너(`height: 500vh` 등) 내에서 보여질 요소를 `position: sticky`로 고정합니다.
2.  **Transform:** 스크롤 된 만큼 요소를 `translateX`로 왼쪽으로 밀어냅니다.

<!-- end list -->

```javascript
const container = document.querySelector('.horizontal-container');
const track = document.querySelector('.horizontal-track');

function stickyScroll() {
  const rect = container.getBoundingClientRect();
  
  // 컨테이너가 화면에 닿아있는 동안 (Sticky 구간)
  if (rect.top <= 0 && rect.bottom >= window.innerHeight) {
    // 스크롤 된 양(절댓값)
    const scrolled = Math.abs(rect.top); 
    
    // 가로 이동 거리 계산 및 적용
    // (트랙 전체 길이 - 화면 너비) 비율에 맞춰 이동
    track.style.transform = `translateX(-${scrolled}px)`;
  }
}
window.addEventListener('scroll', stickyScroll);
```