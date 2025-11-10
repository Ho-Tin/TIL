# Bootstrap & Grid System 정리

## 1. Bootstrap 개요
- Bootstrap은 트위터에서 개발된 대표적인 CSS 프론트엔드 프레임워크입니다.
- 미리 만들어진 다양한 디자인 요소(버튼, 폼, 네비게이션, 모달 등)와 레이아웃 시스템을 제공해 빠르고 일관된 UI 구현이 가능합니다.
- CDN(Content Delivery Network)으로 빠르게 적용할 수 있고, 커스텀 CSS 없이도 반응형 웹을 쉽게 만들 수 있습니다.

## 2. Bootstrap 기본 사용법
- Bootstrap 공식 CDN을 `<head>`에 추가하거나, npm/yarn 등으로 설치해 사용합니다.
- 클래스 기반 스타일링: HTML 요소에 미리 정의된 클래스를 부여해 스타일 적용
- 주요 클래스 규칙:
  - Spacing(여백): `m`(margin), `p`(padding)
  - 방향: `t`(top), `b`(bottom), `s`(start/left), `e`(end/right), `x`(좌우), `y`(상하), (blank: 전체)
  - 크기: 0~5 (0=0, 1=0.25rem, 2=0.5rem, 3=1rem, 4=1.5rem, 5=3rem)
- 예시:
```html
<div class="mt-3 p-2">내용</div>
```
- `mt-3`: 위쪽 margin 1rem, `p-2`: padding 0.5rem

## 3. Reset CSS
- 브라우저마다 기본 스타일이 달라서, Reset CSS(초기화) 또는 Normalize CSS를 적용해 일관성 확보
- Bootstrap은 자체적으로 Reset/Normalize가 적용되어 있음

## 4. 주요 컴포넌트
- Typography: 제목, 본문, 목록 등 텍스트 스타일 제공
- Color: 의미론적 색상(primary, success, danger, warning, info, dark, light 등)
- Alerts: 알림 메시지, Badges: 상태 표시 라벨, Cards: 콘텐츠 박스, Navbar: 네비게이션 바
- Carousel: 이미지 슬라이드, Modal: 팝업창(로그인, 알림 등)
- 각 컴포넌트는 공식 문서 예제와 함께 다양한 옵션/클래스 제공

## 5. Semantic Web & Tag
- 시맨틱 태그(`<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`)를 활용해 의미 중심 구조화
- SEO(검색엔진 최적화), 웹 접근성 향상에 도움

## 6. Grid System
- 12-Column System: 한 줄(row)을 12칸으로 나누어 다양한 레이아웃 구현
- Container: 전체 그리드의 상위 공간, Row: 한 줄, Column: 실제 콘텐츠 영역
- Gutter: 컬럼 사이 여백, Nesting: 컬럼 안에 row를 중첩해 복잡한 레이아웃 구현
- Offset: 특정 컬럼을 오른쪽으로 이동(`offset-4` 등)
- 예시:
```html
<div class="container">
  <div class="row">
    <div class="col-8">
      <div class="row">
        <div class="col-6">Nested 1</div>
        <div class="col-6">Nested 2</div>
      </div>
    </div>
    <div class="col-4">Single column</div>
  </div>
</div>
```
- Offset 예시:
```html
<div class="row">
  <div class="col-4 offset-4">중앙</div>
</div>
```

## 7. 반응형 웹 & Breakpoints
- 다양한 기기/해상도에 맞춰 자동으로 레이아웃 조정
- 6개 분기점: xs(<576px), sm(≥576px), md(≥768px), lg(≥992px), xl(≥1200px), xxl(≥1400px)
- 클래스 예시: `.col-sm-6`, `.col-md-4`, `.offset-sm-1`, `.offset-md-2`
- 예시:
```html
<div class="container">
  <div class="row gx-3 gy-4">
    <div class="col-12 col-md-6 col-lg-4">Column 1</div>
    <div class="col-12 col-md-6 col-lg-4">Column 2</div>
    <div class="col-12 col-md-12 col-lg-4">Column 3</div>
  </div>
</div>
```
- 화면 크기에 따라 컬럼 개수/배치가 유동적으로 변함

## 8. UX & UI
- UX(User Experience): 사용자의 웹/앱 사용 과정에서 느끼는 만족도, 편의성, 효율성 등
- UI(User Interface): 버튼, 네비게이션, 컬러, 폰트, 아이콘 등 실제 조작 가능한 시각적/기능적 디자인
- Bootstrap은 일관된 UI와 빠른 프로토타이핑, 반응형 UX 구현에 매우 유리

## 9. 실전 팁
- 공식 문서(https://getbootstrap.com/)에서 컴포넌트별 예제와 옵션을 꼭 참고
- 커스텀 스타일은 별도 CSS로 관리, Bootstrap 클래스와 혼용 시 명시도/우선순위 주의
- 그리드 시스템은 레이아웃 설계의 기본, 반응형 디자인은 모바일 우선(mobile first) 원칙 활용

## 10. 요약
- Bootstrap은 빠르고 일관된 UI/UX, 반응형 웹, 코드 재사용성, 개발 편의성을 모두 제공하는 강력한 프레임워크
