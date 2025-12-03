
-----

# Vue.js 심화 학습 노트: SFC, Build Tools, & Project Structure

## 1\. Single-File Components (SFC) 심화

### 1.1 SFC의 등장 배경과 개념

  * **기존 방식의 문제점**: 과거 웹 개발은 HTML(구조), CSS(스타일), JavaScript(로직) 파일을 각각 별도로 분리하여 관리했습니다. 앱의 규모가 커질수록 서로 관련된 파일들을 찾고 관리하는 것이 복잡해졌습니다 (`관심사의 분리`가 파일 종류별로 되어 있어 비효율적).
  * **SFC의 해결책 (`.vue`)**: Vue는 \*\*'화면의 특정 영역(컴포넌트)'\*\*을 기준으로 HTML, CSS, JS를 하나의 파일에 묶어서 관리하는 방식을 제안합니다. 이는 물리적으로 파일을 합친 것이 아니라, **논리적으로 연관된 코드들을 한곳에 모은 것**입니다.
  * **건축 비유**:
      * **애플리케이션**: 하나의 집.
      * **컴포넌트**: 집을 구성하는 각 방(거실, 부엌, 침실 등).
      * **SFC 방식**: 각 방의 구조, 인테리어, 기능을 완벽하게 분리하여 설계함으로써, 거실을 수리해도 부엌에 영향을 주지 않게 만듭니다.

### 1.2 SFC 파일 구조 (`*.vue`) 상세 분석

`.vue` 파일은 브라우저가 바로 해석할 수 없으며, 컴파일러를 통해 표준 HTML/CSS/JS로 변환됩니다.

```html
<template>
  <div class="greeting-container">
    <p class="message">{{ msg }}</p>
    <button @click="changeMessage">메시지 변경</button>
  </div>
</template>

<script setup>
import { ref } from 'vue' // Vue의 반응형 API 가져오기

// 반응형 상태(State) 선언: 값이 바뀌면 화면도 자동으로 갱신됨
const msg = ref('Hello Vue World!')

// 함수 정의
function changeMessage() {
  msg.value = '반갑습니다!'
}
</script>

<style scoped>
.greeting-container {
  text-align: center;
  margin-top: 20px;
}

.message {
  color: #42b883; /* Vue의 공식 초록색 */
  font-weight: bold;
}
</style>
```

-----

## 2\. 개발 환경과 빌드 도구 (Build Tools)

### 2.1 Node.js와 NPM의 역할

브라우저는 HTML/CSS/JS만 이해할 수 있습니다. 하지만 현대적인 개발을 위해서는 `.vue` 파일 변환, 코드 최적화, 라이브러리 관리가 필요하며, 이를 수행하는 도구들이 **Node.js** 환경 위에서 돌아갑니다.

  * **Node.js**: 자바스크립트를 브라우저가 아닌 컴퓨터(서버/로컬)에서 실행시켜 주는 런타임 환경입니다.
  * **NPM (Node Package Manager)**:
      * 전 세계 개발자들이 만든 오픈소스 패키지(라이브러리)들이 모여 있는 거대한 창고입니다.
      * `npm install` 명령어를 통해 내 프로젝트에 필요한 도구들을 손쉽게 설치하고 관리합니다.

### 2.2 모듈(Module)과 번들러(Bundler)

  * **모듈의 한계**: 자바스크립트 파일을 기능별로 잘게 쪼개면(모듈화), 브라우저가 수많은 파일을 각각 다운로드해야 하므로 네트워크 부하가 심해지고 속도가 느려집니다. 또한 파일 간 변수 이름 충돌이나 의존성 순서 문제가 발생할 수 있습니다.
  * **번들러의 역할**: 수십, 수백 개의 모듈 파일과 `.vue` 파일들을 의존성 관계에 따라 엮어서(Bundling) \*\*최적화된 소수의 파일(정적 파일)\*\*로 만들어줍니다.
  * **의존성(Dependency) 시각화**: 강의에서는 '블랙홀' 이미지를 통해 `node_modules`의 깊고 복잡한 의존성 관계를 설명했습니다. 번들러는 이 복잡한 관계를 정리해줍니다.

### 2.3 Vite (차세대 빌드 도구)

  * **기존 도구(Webpack)와의 차이**: 기존 번들러는 모든 소스 코드를 한 번에 빌드한 후 서버를 시작했기 때문에 프로젝트가 커질수록 시작 속도가 느려졌습니다.
  * **Vite의 장점**:
      * **빠른 서버 구동**: 브라우저의 기본 기능(Native ES Modules)을 활용하여 필요한 부분만 즉시 로딩합니다.
      * **HMR (Hot Module Replacement)**: 코드 수정 시 전체를 새로고침하지 않고, 변경된 컴포넌트만 즉시 교체하여 개발 생산성을 극대화합니다.

-----

## 3\. Vue Project 구조 및 패키지 관리

### 3.1 프로젝트 생성 (Scaffolding)

스캐폴딩(Scaffolding)은 건물을 지을 때 임시로 세우는 비계처럼, 프로젝트 시작 시 필요한 기본 폴더 구조와 설정 파일들을 자동으로 생성해주는 과정입니다.

```bash
# 최신 버전의 Vue 프로젝트 생성 명령
$ npm create vue@latest

# 이후 나타나는 선택지에서 필요한 기능(TypeScript, Router 등)을 Space바로 선택
```

### 3.2 핵심 파일 상세 설명

  * **`package.json` (설계도)**:
      * 프로젝트의 이름, 버전, 실행 스크립트 등을 정의.
      * **dependencies**: 실제 배포 시 필요한 라이브러리 목록.
      * **devDependencies**: 개발 과정에서만 필요한 도구 목록.
      * 버전 범위(예: `^3.2.0`)로 명시되어 있어, 설치 시점에 따라 버전이 미세하게 다를 수 있음.
  * **`package-lock.json` (스냅샷)**:
      * `package.json`을 기반으로 실제 설치된 패키지들의 **정확한 버전**과 의존성 트리를 기록.
      * **중요**: 협업 시 이 파일이 있어야 팀원 모두가 완전히 동일한 개발 환경을 가질 수 있습니다.
  * **`node_modules/` (자재 창고)**:
      * 설치된 패키지들의 실제 소스 코드가 저장되는 곳.
      * 용량이 매우 크고, `package.json`만 있으면 언제든 다시 설치(`npm install`)할 수 있으므로 **Git 저장소에는 절대 올리지 않습니다.**

### 3.3 SRC 디렉토리 구조

  * **`main.js`**: Vue 앱의 진입점. `createApp` 함수로 앱 인스턴스를 생성하고, HTML의 `#app` 요소에 마운트(연결)합니다.
  * **`App.vue`**: 최상위 루트 컴포넌트. 모든 하위 컴포넌트들이 이 안에 포함됩니다.
  * **`assets/`**: Webpack/Vite가 처리하는 정적 자산. 이곳의 이미지는 빌드 시 최적화되거나 base64로 변환될 수 있습니다.

-----

## 4\. Virtual DOM (가상 DOM) 동작 원리

### 4.1 직접 DOM 조작의 문제점

JavaScript로 `document.getElementById` 등을 사용해 실제 DOM을 직접 자주 조작하면, 브라우저는 그때마다 화면의 레이아웃을 다시 계산하고 그리는 과정(Reflow/Repaint)을 거쳐야 합니다. 이는 성능 저하의 주원인입니다.

### 4.2 Vue의 해결책: 가상 DOM

Vue는 메모리 상에 실제 DOM 구조를 본뜬 가벼운 자바스크립트 객체(가상 DOM)를 둡니다.

1.  **데이터 변경 감지**: Vue의 데이터가 변경됩니다.
2.  **가상 DOM 비교 (Diffing)**: 변경 전의 가상 DOM과 변경 후의 가상 DOM을 비교하여 정확히 **어떤 부분이 바뀌었는지 계산**합니다.
3.  **실제 DOM 패치 (Patch)**: 변경이 필요한 **최소한의 부분**만 실제 DOM에 반영합니다.

**주의사항**: Vue를 사용할 때는 `querySelector` 등으로 실제 DOM을 직접 건드리는 것을 피해야 합니다. Vue가 관리하는 가상 DOM과 실제 DOM 사이의 동기화가 깨져 예측 불가능한 버그가 발생할 수 있습니다.

-----

## 5\. Composition API vs Option API

Vue 3에서 도입된 Composition API는 코드의 재사용성과 관리 용이성을 획기적으로 개선했습니다.

### 5.1 Option API (Vue 2 스타일)

코드가 데이터, 메서드, 라이프사이클 등의 **옵션별로 분리**됩니다. 기능이 단순할 때는 직관적이지만, 컴포넌트가 커지면 하나의 기능을 구현하기 위해 코드가 여기저기 흩어지게 됩니다.

```javascript
// Option API 예시
export default {
  data() { return { count: 0 } }, // 상태는 data에
  methods: {                      // 로직은 methods에
    increment() { this.count++ }
  },
  mounted() { console.log('Mounted') } // 시점은 mounted에
}
```

### 5.2 Composition API (Vue 3 권장)

관련된 코드(상태, 로직, 라이프사이클)를 **기능 단위로 묶어서** 작성할 수 있습니다. `<script setup>`을 사용하면 문법이 훨씬 간결해집니다.

```javascript
// Composition API 예시
<script setup>
import { ref, onMounted } from 'vue'

// 1. 카운터 관련 기능이 한곳에 모임
const count = ref(0)
const increment = () => count.value++

onMounted(() => console.log('Mounted'))
</script>
```

-----

## 6\. 스타일 가이드 및 추가 주제

### 6.1 Scoped CSS의 작동 원리

`<style scoped>`를 사용하면 Vue는 빌드 시 해당 컴포넌트의 HTML 요소들에 고유한 데이터 속성(예: `data-v-f3f3eg9`)을 자동으로 부여합니다. 그리고 CSS 선택자를 `div[data-v-f3f3eg9]` 형태로 변환하여 스타일이 외부로 새어나가는 것을 막습니다.

  * **예외 (Root Element)**: 자식 컴포넌트의 최상위(루트) 요소는 부모 컴포넌트의 스타일 영향도 받고, 자식 컴포넌트의 스타일 영향도 받습니다. 이는 부모가 자식 컴포넌트의 레이아웃(위치 잡기 등)을 제어할 수 있게 하기 위함입니다.

### 6.2 Single Root Element

Vue 2에서는 템플릿 태그 바로 아래에 반드시 하나의 태그만 있어야 했습니다. Vue 3에서는 여러 태그(Fragments)가 있어도 되지만, 스타일링과 트랜지션 효과 적용 시의 명확성을 위해 여전히 **하나의 루트 엘리먼트로 감싸는 것이 권장**됩니다.