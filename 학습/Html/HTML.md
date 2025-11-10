# HTML 정리

## 1. HTML 개념 및 역할
- HTML(HyperText Markup Language)은 웹 페이지의 구조와 의미를 정의하는 마크업 언어
- HyperText: 하이퍼링크로 문서 간 연결, 비선형적 탐색 가능
- Markup Language: 태그로 문서 구조와 의미를 명확히 표현

## 2. HTML 문서 기본 구조
- `<!DOCTYPE html>`: HTML5 표준 선언, 문서 맨 위에 위치
- `<html>`: 문서의 루트, lang 속성으로 언어 지정 가능
- `<head>`: 메타데이터(문서 정보, 문자 인코딩, 외부 리소스, 스타일, 스크립트 등)
- `<title>`: 브라우저 탭에 표시되는 문서 제목
- `<body>`: 실제 페이지에 표시되는 모든 콘텐츠(텍스트, 이미지, 영상 등)

## 3. HTML 요소와 속성
- 요소: 여는 태그, 닫는 태그, 콘텐츠로 구성
- 빈 요소: `<img>`, `<br>`, `<input>` 등(닫는 태그 없음)
- 속성(Attribute): 태그에 추가 정보 부여, 항상 따옴표로 감쌈
- 예시: `<img src="image.jpg" alt="설명">`
- 속성은 여러 개 지정 가능, 순서 무관

## 4. 주요 텍스트 구조 태그
- `<p>`: 문단, `<a href="url">`: 하이퍼링크, `<img src alt>`: 이미지
- 제목: `<h1>`~`<h6>`(중요도 순), 목록: `<ol>`, `<ul>`, `<li>`
- 강조: `<em>`(기울임), `<strong>`(굵게)
- 줄바꿈: `<br>`, 수평선: `<hr>`

## 5. 시맨틱 태그와 Semantic Web
- 시맨틱 태그: `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, `<footer>` 등
- 의미 중심 구조화, 검색엔진 최적화(SEO), 웹 접근성 향상
- 시맨틱 태그는 레이아웃뿐 아니라 정보의 목적/역할을 명확히 함

## 6. HTML5 특징 및 팁
- HTML5는 구조적 시맨틱 태그, 멀티미디어 태그(`<audio>`, `<video>`), 폼 입력 타입 등 다양한 기능 제공
- 템플릿 자동완성(`!`+Tab), 태그/속성 자동완성, 실시간 미리보기 등 에디터 활용
- W3C Validator(https://validator.w3.org/)로 문법 검사 가능

## 7. 실전 팁
- 들여쓰기, 주석(`<!-- 주석 -->`), 한글/영문 혼용 시 인코딩(UTF-8) 확인
- 접근성: alt 속성, label 연결, 시맨틱 태그 적극 활용
- 모바일 대응: `<meta name="viewport" content="width=device-width, initial-scale=1.0">` 추가
