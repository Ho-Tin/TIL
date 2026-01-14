죄송합니다. 확인해보니 **1. XML**과 **3. JSON** 사이에 **2. CSV** 내용이 있었는데, 해당 부분이 누락되었습니다.

말씀하신 내용을 바탕으로 **2. CSV** 내용을 포함하여 전체 내용을 다시 정리해 드립니다.

---

# 데이터 수집 - OpenAPI (삼성청년 SW·AI아카데미)

## 1. OpenAPI 개요

### 1.1. OpenAPI란?

* **정의:** 누구나 사용할 수 있도록 공개된 API. 웹 사이트가 가진 기능을 모두가 이용할 수 있도록 공개한 프로그래밍 인터페이스.
* **활용 예시:** 네이버 지도, 구글 맵, 공공데이터 포털 등.
* **특징:**
* 많은 서비스 업체 및 공공 기관에서 데이터를 외부에서 사용할 수 있게 API를 제공.
* 대부분 HTTP 프로토콜의 GET, POST 등의 메서드를 사용해 자원이나 서비스를 요청.
* 일반적인 웹 페이지(Web Crawling)가 HTML 문서를 응답해주지만, OpenAPI는 요청을 보내면 데이터를 정제된 형식(XML, JSON, CSV 등)으로 응답해줌.



### 1.2. 웹 크롤링과 구조적 차이

* **웹 크롤링:** HTML 전체를 가져와서 필요한 데이터를 파싱해야 함.
* **OpenAPI:**
1. **요청 변수**를 포함하여 서버에 요청.
2. 서버는 **XML/JSON/CSV 형식의 데이터**로 응답.
3. 데이터 가공 후 분석, 시각화, 자동화 등에 활용.



---

## 2. OpenAPI의 데이터 유형

### 2.1. XML (eXtensible Markup Language)

* **구조:** 트리(Tree) 형태의 구조.
* **예시:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<EmployeeData>
    <employee id="34594">
        <firstName>Heather</firstName>
        <lastName>Banks</lastName>
        <hireDate>1/19/1998</hireDate>
        <deptCode>BB001</deptCode>
        <salary>72000</salary>
    </employee>
</EmployeeData>

```



### 2.2. CSV (Comma Separated Values)

* **정의:** 몇 가지 필드를 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일.
* **특징:**
* 엑셀, 메모장 등 다양한 프로그램에서 쉽게 읽고 쓸 수 있어 호환성이 높음.
* 구조가 단순하고 불필요한 태그가 없어 용량이 작음.
* 주로 표(Table) 형태의 데이터를 표현할 때 사용.


* **예시:**
```csv
FirstName,LastName,employeeID,Designation
Sam,Jackson,5698523,Manager

```



### 2.3. JSON (JavaScript Object Notation)

* **구조:** 키(Key) : 값(Value) 페어로 데이터 표현.
* **특징:** 자바스크립트 객체 표기법을 따르며, 가독성이 좋고 용량이 가벼워 웹/앱 통신에서 가장 많이 사용됨.
* **예시:**
```json
{
    "FirstName"    : "Sam",
    "LastName"     : "Jackson",
    "employeeID"   : 5698523,
    "Designation"  : "Manager"
}

```



### 2.4. 기타 데이터 제공 유형

* **텍스트:** txt, vi 등 (이미지, 표 등을 미포함한 텍스트만 포함).
* **문서:** hwpx, docx 등 (이미지, 동영상 등 멀티미디어 포함 가능).
* **이미지:** jpg, png, svg 등 (래스터, 벡터 형식).
* **음성(음향):** mp3, acc 등.
* **동영상:** mp4, mpg 등.
* **공간 정보:** Shapefile (지리정보, 위치정보 등 공간 데이터).

---

## 3. HTTP 통신 및 Requests 라이브러리

### 3.1. HTTP 통신 개념

* **요청(Request):** 클라이언트가 서버에게 데이터를 달라고 요구 ("와인 있나요?").
* **응답(Response):** 서버가 클라이언트에게 결과를 전달 ("여기 보시면 됩니다.").

### 3.2. Requests 라이브러리 (Python)

* 접근할 웹 페이지의 데이터를 요청/응답 받기 위한 파이썬 라이브러리.

**[코드 예시: Requests 기본 사용]**

```python
# requests 라이브러리 불러오기
import requests as req

# 김싸피: request야 네이버 메인페이지 정보 좀 알아줘~
# request: 네. 근데 네이버가 어디예요?
# 김싸피: www.naver.com

res = req.get('http://www.naver.com')

# <Response [200]> = 데이터를 잘 가지고왔습니다~, 통신에 성공했습니다!
# 김싸피: res변수에서 내용만 보고싶어~

res
# <Response [200]>

```

### 3.3. GET 메소드와 URL

* **GET 메소드:** 웹 서버에게 파라미터를 포함해 요청을 보내는 가장 쉬운 방법. URL 뒤에 파라미터 정보를 붙여서 보냄.
* **구조 예시:** `https://youtube.com/results?search_query=bigdata`
* 페이지 URL: `https://youtube.com/results`
* 파라미터: `search_query = bigdata` (서버가 요청에 대한 대답을 찾을 때 사용하는 힌트)



---

## 4. 공공 데이터 포털의 OpenAPI 활용

### 4.1. 사용 절차

1. **사용자:** 공공데이터 포털(data.go.kr)에 접속하여 활용신청.
2. **공공데이터 포털:** 승인 후 API Key 발급.
3. **사용자:** 오픈 API 호출 (API Key 포함).
4. **제공기관:** 요청 처리 후 API 회신.
5. **사용자:** API 결과 응답 수신.

### 4.2. 상세 과정

* **요청변수(Request Parameter):** 서비스키(ServiceKey - 필수), 페이지 번호(pageNo), 한 페이지 결과 수(numOfRows), 데이터 생성일 시작/종료 범위(startCreateDt, endCreateDt) 등.
* **응답 데이터:** 주로 XML 형태로 반환되며, `<item>` 태그 안에 `<confCase>`, `<deathRate>` 등의 데이터가 포함됨.

### 4.3. [실습 코드 1] OpenAPI 응답 데이터 이해 및 추출

*코로나19 감염현황 데이터를 XML로 받아와 파싱하는 예제*

```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('API_KEY')

base_url = "http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid09Api"

# 날짜 범위 설정
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 10)

date_list = [
    (start_date + timedelta(days=i)).strftime("%Y%m%d")
    for i in range((end_date - start_date).days + 1)
]

rows = []
for date in date_list:
    url = (
        f"{base_url}?"
        f"serviceKey={key}&"
        f"pageNo=1&"
        f"numOfRows=10&"
        f"apiType=xml&"
        f"create_dt={date}"
    )
    
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'xml')
    items = bs.select('item')
    
    for item in items:
        gubun = item.select_one("gubun").text
        confCase = item.select_one("confCase").text
        
        rows.append({
            "date": date,
            "gubun": gubun,
            "confCase": int(confCase)
        })

```

### 4.4. [실습 코드 2] OpenAPI 응답 데이터 전처리

*수집한 데이터프레임의 '구분' 컬럼 데이터를 정제하는 예제 (숫자와 '이상' 처리)*

```python
# 연령대 데이터만 남기기 ('숫자-숫자' or '이상' 포함)
age_df = df[df['구분'].str.contains(r'\d')].copy()

def extract_age(group):
    if '이상' in group:
        return int(group.replace(' 이상', ''))
    else:
        return int(group.split('-')[0])

age_df['연령대'] = age_df['구분'].apply(extract_age)

```

---

## 5. 기업 OpenAPI 활용

### 5.1. 특징

* **공공데이터:** 정형·정적 데이터 위주.
* **기업 API:** 실시간 서비스, 사용자 중심 데이터를 다양하게 제공 (소셜 로그인, 지도, 검색 등).
* **인증 방식:** 단순히 Key만 보내는 것이 아니라, 로그인(OAuth) 인증을 사용하는 경우가 많음 (Client ID, Client Secret).

### 5.2. Naver OpenAPI 사례

* **등록:** 애플리케이션 등록 (API 이용신청) 필요.
* **종류:**
* 비로그인 오픈 API: 검색, 지도, 번역 등 (HTTP 헤더에 ID/Secret 포함).
* 로그인 오픈 API: 카페, 블로그, 캘린더 등 (사용자 동의 및 로그인 필요).


* **제한:** 일일 허용량(Quota)이 존재하므로 확인 필요.

### 5.3. [실습 코드 3] Naver OpenAPI를 활용한 뉴스 검색 및 전처리

*뉴스 검색 결과를 가져와 HTML 태그를 제거하고 정리하는 예제*

```python
import pandas as pd
import html

# <b>, &quot; 같은 태그 제거
def clean_html(text):
    text = html.unescape(text) # HTML 엔티티 변환
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# ... (API 호출 후 items 리스트를 받았다고 가정) ...
# in items:
    # ...
    # "title": clean_html(it.get("title")),
    # "description": clean_html(it.get("description")),
    # "link": it.get("link"),
    # "pubDate": it.get("pubDate"),
    # "originallink": it.get("originallink"),
    # ...

# .DataFrame(rows)

```
