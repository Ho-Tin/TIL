# CSS 정리

## 1. CSS 개념과 역할
- CSS(Cascading Style Sheets)는 웹 페이지의 디자인과 레이아웃을 담당하는 스타일링 언어
- HTML이 구조/내용, CSS는 시각적 표현(색상, 폰트, 여백, 위치 등) 담당

## 2. 스타일 적용 방법과 우선순위
- 인라인 스타일: `<p style="color:red;">` (권장X, 유지보수 어려움)
- 내부 스타일 시트: `<style>p { color: blue; }</style>` (문서 내 한정)
- 외부 스타일 시트: 별도 .css 파일, `<link rel="stylesheet" href="style.css">` (권장, 재사용성 높음)
- 우선순위: 인라인 > 내부 > 외부 > 브라우저 기본
- `!important`: 강제 적용(가급적 사용X)

## 3. CSS 기본 구조
- 선택자(Selector): 스타일 적용 대상 지정(태그, .class, #id, [attr=value], *)
- 선언(Declaration): `{속성: 값;}`
- 속성(Property)와 값(Value): 색상, 폰트, 여백, 크기, 위치 등
- 예시:
```css
.box {
  color: #333;
  background: #f0f0f0;
  padding: 10px 20px;
  border-radius: 8px;
}
```

## 4. 선택자 종류와 결합자
- 전체 선택자: `* {}`
- 태그 선택자: `p {}`
- 클래스 선택자: `.box {}`
- 아이디 선택자: `#header {}`
- 속성 선택자: `input[type="text"] {}`
- 자손 결합자: `div p {}` (div 내부 모든 p)
- 자식 결합자: `div > p {}` (div 바로 아래 p)
- 인접형제: `h1 + p {}` (h1 바로 뒤 p)
- 일반형제: `h1 ~ p {}` (h1 이후 모든 p)
- 가상클래스: `a:hover`, `li:first-child`, `input:focus`
- 가상요소: `p::before`, `p::after`

## 5. 단위와 색상
- px(절대), em/rem(상대, 폰트 기준), %, vw/vh(뷰포트 기준)
- 색상: 이름(red), 16진수(#fff), rgb(255,0,0), rgba(255,0,0,0.5), hsl(0,100%,50%)

## 6. 주요 속성
### 글꼴/텍스트
- `font-family`, `font-size`, `font-weight`, `font-style`, `color`, `text-align`, `text-decoration`, `line-height`, `letter-spacing`, `word-spacing`, `text-transform`
- 예시:
```css
h1 {
  font-family: 'Noto Sans', Arial, sans-serif;
  font-size: 2rem;
  font-weight: bold;
  color: #222;
  text-align: center;
}
```

### 배경
- `background-color`, `background-image`, `background-repeat`, `background-size`, `background-position`, `background-attachment`
- 예시:
```css
body {
  background: linear-gradient(90deg, #e66465, #9198e5);
}
```

### 여백/테두리
- `margin`, `padding`, `border`, `border-radius`, `box-shadow`
- 축약형: `margin: 10px 20px 30px 40px;` (상 우 하 좌)
- 예시:
```css
.box {
  margin: 20px auto;
  padding: 16px;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}
```

### 크기/위치
- `width`, `height`, `min-width`, `max-width`, `min-height`, `max-height`
- `top`, `left`, `right`, `bottom`, `z-index`

## 7. 박스 모델(Box Model)
- content(내용), padding(안쪽 여백), border(테두리), margin(바깥 여백)
- `box-sizing: content-box`(기본), `box-sizing: border-box`(전체 크기 지정)
- margin collapsing(마진 상쇄): 인접한 block 요소의 margin이 겹칠 때 큰 값만 적용
- 예시:
```css
.container {
  width: 400px;
  padding: 20px;
  border: 2px solid #333;
  margin: 30px auto;
  box-sizing: border-box;
}
```

## 8. Display/Position
### Display
- `block`: 새 줄에서 시작, 전체 가로폭 차지(`<div>`, `<p>`, `<h1>` 등)
- `inline`: 한 줄에 나란히, width/height 적용X(`<span>`, `<a>` 등)
- `inline-block`: 한 줄에 나란히, width/height 적용O(버튼 등)
- `none`: 화면에 표시X, 공간도 차지X

### Position
- `static`: 기본값, Normal Flow
- `relative`: 원래 위치 기준으로 이동, 공간 유지
- `absolute`: 가장 가까운 position 지정 부모 기준, 공간 차지X
- `fixed`: 뷰포트 기준, 스크롤해도 고정
- `sticky`: 스크롤 위치에 따라 relative→fixed로 변환
- `z-index`: 쌓임 순서 지정
- 예시:
```css
.fixed-btn {
  position: fixed;
  right: 20px;
  bottom: 20px;
  z-index: 100;
}
```

## 9. Flexbox
- 1D(가로나 세로 한 축) 레이아웃 시스템, 내부 요소 정렬 최적화
- 부모에 `display: flex;` 또는 `display: inline-flex;` 지정
- 주요 속성:
  - `flex-direction`: row, column, row-reverse, column-reverse
  - `flex-wrap`: wrap, nowrap
  - `justify-content`: flex-start, flex-end, center, space-between, space-around, space-evenly
  - `align-items`: stretch, flex-start, flex-end, center, baseline
  - `align-content`: 여러 줄 정렬
- 자식 속성:
  - `flex-grow`, `flex-shrink`, `flex-basis`, `align-self`
- 예시:
```css
.flex-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.flex-item {
  flex: 1 1 200px;
  margin: 8px;
}
```

## 10. Grid 레이아웃
- 2D(가로+세로) 레이아웃, 복잡한 배치에 적합
- 부모에 `display: grid;` 지정
- 주요 속성: `grid-template-columns`, `grid-template-rows`, `gap`, `grid-column`, `grid-row`, `justify-items`, `align-items`
- 예시:
```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 16px;
}
.grid-item {
  grid-column: span 2;
}
```

## 11. 미디어 쿼리(Media Query)
- 반응형 웹 구현, 화면 크기/기기별 스타일 지정
- 예시:
```css
@media (max-width: 600px) {
  .container {
    width: 100%;
    padding: 8px;
  }
}
```

## 12. 기타
- Shorthand(축약형) 속성: margin, padding, border 등
- 자동완성, 실시간 미리보기, 개발자 도구 활용
- transition, animation, transform 등 동적 효과
- 커스텀 속성(CSS 변수): `--main-color: #333; color: var(--main-color);`

## 13. 실전 팁
- 클래스명은 의미 중심으로 작성, 재사용성 높이기
- 커스텀 스타일은 별도 파일로 관리, 우선순위 충돌 주의
- 공식 문서(MDN, w3schools)와 개발자 도구 적극 활용
- 레이아웃 설계 시 Flexbox, Grid, 미디어쿼리 적극 활용
