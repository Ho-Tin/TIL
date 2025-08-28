# 250825
# HTML과 CSS 상세 개념 정리

## HTML (HyperText Markup Language)

### 웹 의미와 구조 정의
HTML은 웹 페이지의 **의미와 구조**를 정의하는 언어입니다. 'HyperText'는 웹 문서들 간의 하이퍼링크 연결로, 비선형적 탐색과 상호연결성을 가능하게 하며 사용자가 주도적으로 웹을 탐색할 수 있게 합니다. 'Markup Language'는 태그를 활용해 문서 내 구조와 의미를 명시하는 역할을 합니다.

### HTML 문서 기본 구조
- `<!DOCTYPE html>`: 문서가 HTML5 표준임을 선언합니다. 반드시 문서 맨 위에 위치시킵니다.
- `<html>`: HTML 문서의 최상위 루트 태그입니다. 이 태그 내에 문서 전체가 포함됩니다.
- `<head>`: 문서에 대한 메타데이터를 담는 부분으로, 브라우저에 직접 표시되지 않습니다. 문자 인코딩, 문서 제목, 외부 스타일시트나 스크립트 연결 등이 포함됩니다.
- `<title>`: 웹 브라우저 탭의 제목으로 보여지는 문서 제목을 지정합니다.
- `<body>`: 실제 페이지에서 보여지는 모든 콘텐츠(텍스트, 이미지, 영상 등)를 포함합니다. 한 문서에는 오직 하나의 `<body>`만 존재해야 합니다.

### HTML 요소와 속성
- HTML 요소는 여는 태그 `<tag>`와 닫는 태그 `</tag>`로 구성되며, 그 사이에 콘텐츠를 넣습니다.
- 닫는 태그가 필요 없는 빈(empty) 요소도 있습니다. 예: `<img>`, `<br>`, `<input>` 등.
- 속성(Attribute)은 태그에 추가 정보를 부여하며, 요소의 동작이나 표현을 조절합니다.
  - 예: `<img src="image.jpg" alt="설명">`
  - 요소 이름과 속성 사이, 속성들 사이에는 공백이 필요하고 속성 값은 항상 따옴표로 감쌉니다.

### 주요 HTML 텍스트 구조 태그
- `<p>`: 문단(paragraph)을 표시하는 태그입니다.
- `<a href="url">`: 링크(anchor) 태그로 다른 페이지나 위치로 이동할 수 있게 합니다.
- `<img src="경로" alt="대체텍스트">`: 이미지 삽입 태그입니다.
- 제목 태그 `<h1>` ~ `<h6>`: 문서의 중요도 순서대로 제목을 나타냅니다. `<h1>`이 최상위 제목입니다.
- 목록 태그: 순서있는 목록 `<ol>`, 순서없는 목록 `<ul>`, 목록 항목 `<li>`.
- 강조 태그:
  - `<em>`: 기울임 강조 (emphasis)
  - `<strong>`: 굵게 강조 (strong importance)

### 보조 팁
- HTML5 템플릿은 `!` 입력 후 Tab 키로 자동 완성 가능합니다.
- 태그 및 속성 자동완성 기능이 많은 에디터에서 지원되어 편리합니다.

---

## CSS (Cascading Style Sheets)

### CSS란?
CSS는 웹 페이지의 디자인과 레이아웃을 설정하는 스타일링 언어입니다. HTML이 구조와 내용을 담당한다면, CSS는 색상, 폰트, 여백, 위치 등 시각적인 디자인 요소를 관리합니다.

### 스타일 적용 방법 및 우선순위
- **인라인 스타일**: 태그 내부에 `style` 속성으로 직접 작성 (`<p style="color:red;">`).
- **내부 스타일 시트**: `<style>` 태그 내부에 작성.
- **외부 스타일 시트**: 별도의 `.css` 파일을 만들고 `<link>` 태그로 연결합니다. 가장 권장되는 방법입니다.
- 우선순위: 인라인 > 내부 > 외부 스타일 순이며, 인라인 스타일은 유지보수가 어렵고 가독성을 떨어뜨리므로 가급적 피합니다.

### CSS 구조
- 선택자(Selector): 스타일을 적용할 HTML 요소 지정 (예: `p`, `.class`, `#id` 등).
- 선언(Declaration): `{속성: 값;}` 형식으로, 스타일 속성과 그 값을 정의합니다.
- 속성(Property) 및 값(Value): 글꼴 크기, 색상, 여백 등 변경할 스타일 항목과 해당 값을 의미합니다.

### CSS 선택자 종류
- 전체 선택자(`*`): 모든 요소를 선택합니다.
- 요소 선택자(태그 선택자): 특정 태그에 모두 적용 (`p {}`).
- 클래스 선택자(`.`): 같은 클래스를 가진 모든 요소 선택 (`.box {}`).
- 아이디 선택자(`#`): 특정 아이디를 가진 한 요소 선택 (`#header {}`).
- 속성 선택자(`[attr=value]`): 특정 속성이나 속성값을 가진 요소 선택 (`input[type="text"] {}`).

### CSS 결합자 (Combinators)
- 자손 결합자 (space): 특정 요소 내부에 있는 모든 자손 선택 (`div p`).
- 자식 결합자 (`>`): 특정 요소의 바로 아래 자식만 선택 (`div > p`).
- 인접 형제 결합자 (`+`): 바로 뒤에 오는 형제 요소 선택 (`h1 + p`).
- 일반 형제 결합자 (`~`): 같은 부모를 가진 이후 모든 형제 요소 선택 (`h1 ~ p`).

### CSS 단위
- 절대 단위: `px` (픽셀, 고정 크기)
- 상대 단위:
  - `em`: 부모 요소의 폰트 크기를 기준으로 크기 결정
  - `rem`: 최상위 `<html>` 요소 폰트 크기를 기준으로 결정, 중첩 시 문제 해결

### 명시도(Specificity)와 우선순위
- 스타일 충돌 시 우선 적용 기준:
  1. `!important` (사용 권장하지 않음)
  2. 인라인 스타일
  3. 아이디 선택자(`#id`)
  4. 클래스 선택자(`.class`)
  5. 요소 선택자 (태그)
- 같은 우선순위에서는 나중에 선언된 스타일이 적용됩니다.
- 클래스 선택자를 주로 사용해 재사용성과 유지보수를 효율적으로 합니다.

### 스타일 상속
- 텍스트 관련 속성(글꼴, 색상)은 부모에서 자식으로 상속됩니다.
- 레이아웃 관련 속성(마진, 패딩 등)은 상속되지 않습니다.

### CSS 박스 모델 (Box Model)
- 모든 요소는 사각형 박스 형태로, 다음 네 부분으로 구성됩니다:
  - 내용(content)
  - 안쪽 여백(padding)
  - 테두리(border)
  - 바깥 여백(margin)
- 기본 박스 모델은 `content-box`이며, `box-sizing: border-box;` 속성을 사용하면 padding과 border를 포함한 전체 크기를 지정할 수 있습니다.

---
# 250826
# 📘 CSS Layout 정리

## 1. CSS Box Model
요소를 하나의 박스로 보고, 내부와 외부 여백을 관리하는 개념

- **content** : 실제 콘텐츠(텍스트, 이미지 등)
- **padding** : 콘텐츠와 테두리(border) 사이의 여백
- **border** : 박스를 둘러싼 테두리
- **margin** : 박스와 다른 요소 사이의 간격

---

## 2. Display 속성과 박스 타입

### (1) Block 타입
- 문단, 레이아웃 같은 큰 구조에 사용
- 항상 **새 줄에서 시작**, 가로 폭 전체(100%)를 차지
- `width`, `height`, `margin`, `padding` 모두 적용 가능
- 다른 요소 옆에 나란히 배치 ❌
- 대표 요소: `<div>`, `<h1>~<h6>`, `<p>`, `<header>`, `<footer>`

### (2) Inline 타입
- 텍스트처럼 **한 줄 안에 자연스럽게 배치**
- 콘텐츠 크기만큼만 영역 차지
- `width`, `height` 지정 불가  
- 수평 여백(`padding`, `margin-left/right`)은 적용 가능하지만, 수직 여백은 레이아웃에 영향을 거의 주지 못함
- 대표 요소: `<span>`, `<a>`, `<strong>`, `<em>`

### (3) Inline-block 타입
- **inline + block의 특징**을 동시에 가짐
- 한 줄(인라인 흐름) 안에 배치되지만 `width`/`height` 지정 가능
- 버튼이나 내비게이션 메뉴 UI 구성에 자주 사용

### (4) none
- 해당 요소가 표시되지 않고, **공간도 차지하지 않음**

---

## 3. Normal Flow (기본 배치 흐름)
- 특별히 `position`, `float` 등으로 조정하지 않은 상태에서의 **기본 배치 규칙**
- 박스 타입에 따라 block은 세로로 쌓이고, inline은 가로로 이어짐

---

## 4. CSS Position 속성
요소의 위치를 제어하는 방법  

1. **static** (기본값)  
   - Normal Flow에 따라 배치  
   - 좌표 속성(`top`, `left`) 적용 불가

2. **relative** (상대 위치)  
   - 원래 static 위치를 기준으로 이동  
   - 공간은 유지 → 다른 요소 레이아웃에 영향 X

3. **absolute** (절대 위치)  
   - Normal Flow에서 제거됨(공간 차지 X)  
   - 가장 가까운 `position: relative` 부모를 기준으로 이동  
   - 없으면 `body` 기준

4. **fixed** (고정 위치)  
   - 뷰포트(Viewport)를 기준으로 위치  
   - 스크롤해도 자리 고정

5. **sticky** (상황에 따라 relative/fixed)  
   - 지정된 스크롤 위치까지는 relative처럼 작동  
   - 임계점에 도달하면 fixed처럼 화면에 고정  
   - 뉴스 사이트의 헤더 메뉴 등에 활용됨

6. **z-index**  
   - 요소가 겹쳤을 때 쌓이는 순서 제어  
   - 값이 클수록 위에 표시  
   - 같은 부모 안에서만 비교, 부모보다 위로는 못 올라감

---

## 5. CSS Flexbox
일차원(1D) 레이아웃 시스템 → 가로나 세로 한 축을 기준으로 정렬 최적화  

### Flexbox 기본 용어
- **flex container** : `display:flex;` 또는 `display:inline-flex;` 설정된 부모
- **flex item** : 컨테이너 안의 자식 요소
- **main axis** : 아이템이 배치되는 기본 축 (row → 가로, column → 세로)
- **cross axis** : 보조 축 (main axis의 수직 방향)

---

### Flex Container 속성
- **flex-direction** : 배치 방향
  - `row`, `row-reverse`, `column`, `column-reverse`
- **flex-wrap** : 줄바꿈 여부
  - `nowrap`(기본) / `wrap` / `wrap-reverse`
- **justify-content** : 메인 축 정렬
  - `flex-start`, `flex-end`, `center`, `space-between`, `space-around`, `space-evenly`
- **align-items** : 교차 축 정렬
  - `stretch`, `flex-start`, `flex-end`, `center`, `baseline`
- **align-content** : 여러 줄이 있을 때 교차 축에서 줄 간격 정렬 (wrap일 때만 적용)

---

### Flex Item 속성
- **flex-grow** : 남는 공간 분배 비율
- **flex-shrink** : 공간이 부족할 때 줄어드는 비율
- **flex-basis** : 아이템의 기본 크기 (width 대신 자주 사용됨)
- **align-self** : 개별 아이템의 교차 축 정렬

---

## 6. 추가 개념 (보강 포인트)

- **Margin Collapsing (마진 상쇄)**  
  두 block 요소의 `margin(top/bottom)`이 만나면 겹쳐져서 큰 값만 반영됨

- **Shorthand 속성 (축약형)**  
  - `margin: 10px;` → 네 방향 모두 10px  
  - `margin: 10px 20px;` → 상하 10px, 좌우 20px  
  - `margin: 10px 20px 30px;` → 상 10px, 좌우 20px, 하 30px  
  - `flex: 1;` → `flex-grow:1, flex-shrink:1, flex-basis:0`

---

# ✅ 요약
- Display는 **외부 배치 방식(Block/Inline) 제어**
- Position은 **Normal Flow에서 벗어나 배치 위치 제어**
- Flexbox는 **내부 요소(자식) 정렬 최적화**
- Box Model은 여백과 테두리를 계산하는 기본 단위

# 250827
# Bootstrap 정리

## 1. Bootstrap 개요
- **CSS 프론트엔드 프레임워크 (Toolkit)**
  - 미리 만들어진 다양한 디자인 요소(스타일, 레이아웃, 컴포넌트)를 제공  
  - 개발자가 복잡한 CSS를 직접 작성하지 않고도 빠르게 UI 구현 가능  

- **CDN(Content Delivery Network)**
  - 서버와 사용자 사이의 물리적 거리를 줄여 **로딩 속도를 향상**
  - 지리적으로 가까운 서버에서 리소스를 제공하여 사용자 경험 개선  

---

## 2. Bootstrap 기본 사용법
- Bootstrap은 **규칙적인 클래스 이름**을 사용해 스타일과 레이아웃을 제공  
- 주요 클래스 규칙:
  - **Spacing (여백)**
    - `m` : margin  
    - `p` : padding  
  - **방향 (sides)**  
    - `t` : top  
    - `b` : bottom  
    - `s` : start(=left)  
    - `e` : end(=right)  
    - `x` : 좌우  
    - `y` : 상하  
    - (blank) : 전체  
  - **크기 (0 ~ 5)**  
    - `0` = 0  
    - `1` = 0.25rem  
    - `2` = 0.5rem  
    - `3` = 1rem  
    - `4` = 1.5rem  
    - `5` = 3rem  

📌 예시  
```html
<div class="mt-3 p-2">내용</div>
```
- `mt-3` : 위쪽 margin 1rem  
- `p-2` : padding 0.5rem  

---

## 3. Reset CSS
- **Reset CSS의 목적**
  - HTML 요소의 스타일을 브라우저마다 동일하게 맞추기 위함  
  - 모든 브라우저는 `user agent stylesheet`(기본 CSS)를 가지고 있으며, 서로 차이가 있음  

- **방법**
  - 모든 스타일을 초기화 → 개발자가 원하는 스타일을 직접 정의  
  - 대표적인 기법: **Normalize CSS**
    - 브라우저 간 차이가 발생하는 부분만 최소한으로 수정하여 표준에 맞게 정리  

---

## 4. Bootstrap 활용
- **Typography**
  - 제목, 본문, 텍스트, 목록 등을 통일된 스타일로 제공  

- **Color**
  - 의미론적(semantic) 색상 제공 → `primary`, `success`, `danger`, `warning`, `info`, `dark`, `light` 등  

---

## 5. Component (컴포넌트)
- **UI 관련 요소**들을 미리 제공  
- 주요 예시:
  - **Alerts** : 알림 메시지  
  - **Badges** : 상태 표시용 작은 라벨  
  - **Cards** : 콘텐츠 박스  
  - **Navbar** : 네비게이션 바  

- **Carousel**
  - 이미지나 콘텐츠를 자동/수동으로 넘기는 기능  
  - `id`와 `data-bs-target` 속성 값이 일치해야 동작  

- **Modal**
  - 팝업창 형태 (예: 로그인 실패 알림)  
  - `data-bs-target` 속성과 modal의 `id` 값이 일치해야 실행  
  - 보통 **body 태그 닫히기 직전**에 작성하는 것을 권장 (다른 요소에 가려지는 문제 방지)  

---

## 6. Semantic Web
- **정의**
  - 웹을 "시각적 디자인"이 아니라 **목적과 역할** 중심으로 구조화하는 방식  
  - 데이터를 의미론적으로 표현 → 검색, 접근성, 유지보수에 유리  

---

## 7. Semantic in HTML
- HTML 요소 자체가 **의미(semantic)를 가지는 것**  
- 예시:
  - `<header>` : 문서나 섹션의 머리글  
  - `<nav>` : 내비게이션 링크 모음  
  - `<section>` : 주제별 콘텐츠 구역  
  - `<article>` : 독립적인 콘텐츠  
  - `<footer>` : 문서나 섹션의 바닥글  

✅ 시맨틱 태그를 활용하면 **SEO(검색엔진 최적화)**와 **웹 접근성**을 향상시킬 수 있음  

---
# 250828
***

# Responsive Web & Bootstrap Grid System

## Bootstrap Grid System

### 1. 12-Column System  
- 부트스트랩의 그리드 시스템은 웹 페이지의 레이아웃을 조정하기 위해 **12개의 컬럼**으로 구성되어 있습니다.  
- **12개인 이유**  
  - 12는 약수가 많아(1,2,3,4,6,12) 다양한 조합으로 칸을 나누기에 매우 편리합니다.
  - 예: 4컬럼(3+3+3+3), 3컬럼(4+4+4), 2컬럼(6+6) 등 유연한 레이아웃이 가능합니다.

### 2. Grid System 구조  
- **Container**  
  - 전체 그리드 시스템, 컬럼들을 담는 상위 공간입니다.
- **Row**  
  - 한 줄을 형성하며, 컬럼들이 포함됩니다.
- **Column**  
  - 실제 컨텐츠가 들어가는 영역입니다.
- **Gutter**  
  - 컬럼 사이의 수평(padding) 및 수직(margin) 여백
  - 다양한 클래스(`gx-0`, `g-5`, `gy-5` 등)로 x, y축 방향의 여백을 조절
- **Nesting(중첩)**  
  - `col` 안에 `row`를 추가하여 복잡한 레이아웃 구성도 가능합니다.
  - 예:  
    ```html
    <div class="row">
      <div class="col-8">
        <div class="row">
          <div class="col-6">Nested 1</div>
          <div class="col-6">Nested 2</div>
        </div>
      </div>
      <div class="col-4">Single column</div>
    </div>
    ```
- **Offset(상쇄)**  
  - 칸 띄우기, 특정 컬럼을 오른쪽으로 이동  
  - 예: `offset-4`, `offset-sm-3` 등 사용  
    ```html
    <div class="row">
      <div class="col-4 offset-4">This column is centered</div>
    </div>
    ```

## Grid System for Responsive Web

### 반응형 웹 디자인(Responsive Web Design)
- 디바이스 종류와 해상도 상관없이 어디서나 일관된 레이아웃과 사용자 경험을 제공하는 디자인 기술입니다.
- 웹 브라우저, 태블릿, 모바일 등 다양한 기기에서 자동으로 레이아웃이 조정됩니다.

### Grid System Breakpoints
- 다양한 화면 크기에 맞춰 적절한 레이아웃 배치를 위한 **6개의 분기점(breakpoints)**이 존재합니다.
- **분기점 종류 및 기본 너비(px)**
  - `xs`: Extra small (`<576px`)
  - `sm`: Small (`≥576px`)
  - `md`: Medium (`≥768px`)
  - `lg`: Large (`≥992px`)
  - `xl`: Extra large (`≥1200px`)
  - `xxl`: Extra extra large (`≥1400px`)

- **클래스 예시**
  - `.col-sm-6`, `.col-md-4`
  - `.offset-sm-1`, `.offset-md-2`

## UX & UI

### UX (User Experience : 사용자 경험)
- 사용자의 웹사이트/앱 사용 과정에서 느끼는 만족도를 높이기 위한 설계 철학
- 여러 요소의 통합적 설계 필요
  - 유저 리서치 (User Research)
  - 데이터 설계 및 정제 (Data Design & Refinement)
  - 유저 시나리오 및 플로우 작성 (User Scenario)
  - 프로토타입 설계 (Prototype Design)

### UI (User Interface : 사용자 인터페이스)
- 사용자와 서비스를 연결하는 **시각적/기능적 디자인** 영역
- 버튼, 네비게이션, 컬러, 폰트, 아이콘 등 실제 사용자가 조작할 수 있는 요소의 디자인

***

## 추가: 예시 코드

```html
<!-- Responsive Grid 예시 -->
<div class="container">
  <div class="row gx-3 gy-4">
    <div class="col-12 col-md-6 col-lg-4">Column 1</div>
    <div class="col-12 col-md-6 col-lg-4">Column 2</div>
    <div class="col-12 col-md-12 col-lg-4">Column 3</div>
  </div>
</div>
```
- 위 예시에서는 화면 크기에 따라 컬럼의 개수와 배치가 유동적으로 변합니다.

***

## 그리드 시스템 요약

- **유연하고 반응형**인 레이아웃 설계를 가능하게 해줌
- **다양한 화면**에서도 일관된 UX&UI 경험 제공
- **코드 재사용성** 및 개발 편의성 향상

***
