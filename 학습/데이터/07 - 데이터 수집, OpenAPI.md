제공해주신 동영상(화면 녹화) 내용을 바탕으로 **삼성청년 SW·AI아카데미(SSAFY) - 데이터 수집(OpenAPI)** 강의 내용을 정리한 마크다운(MD) 파일입니다. 요청하신 대로 코드 내용은 요약하지 않고 화면에 나온 그대로 포함하였습니다.

---

# 데이터 수집 - OpenAPI (삼성청년 SW·AI아카데미)

## 1. OpenAPI 개요

### 1.1. OpenAPI란?

* **정의:** 누구나 사용할 수 있도록 공개된 API. 웹 사이트가 가진 기능을 모두가 이용할 수 있도록 공개한 프로그래밍 인터페이스.
* **활용 예시:** 네이버 지도, 구글 맵, 공공데이터 포털 등.
* **특징:**
* 많은 서비스 업체 및 공공 기관에서 데이터를 외부에서 사용할 수 있게 API를 제공.
* 대부분 HTTP 프로토콜의 GET, POST 등의 메서드를 사용해 자원이나 서비스를 요청.
* 일반적인 웹 페이지(Web Crawling)가 HTML 문서를 응답해주지만, OpenAPI는 요청을 보내면 데이터를 정제된 형식(XML, JSON 등)으로 응답해줌.



### 1.2. 웹 크롤링과 구조적 차이

* **웹 크롤링:** HTML 전체를 가져와서 필요한 데이터를 파싱해야 함.
* **OpenAPI:**
1. **요청 변수**를 포함하여 서버에 요청.
2. 서버는 **XML/JSON 형식의 데이터**로 응답.
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
    <employee id="34593">
        <firstName>Tina</firstName>
        </employee>
</EmployeeData>

```



### 2.2. JSON (JavaScript Object Notation)

* **구조:** 키(Key) : 값(Value) 페어로 데이터 표현.
* **예시:**
```json
{
    "FirstName"    : "Sam",
    "LastName"     : "Jackson",
    "employeeID"   : 5698523,
    "Designation"  : "Manager"
}

```



### 2.3. 기타 데이터 제공 유형

* **텍스트:** txt, vi 등 (이미지, 표 등을 미포함한 텍스트만 포함).
* **문서:** hwpx, docx 등 (이미지, 동영상 등 멀티미디어 포함 가능, XML 포맷 작성 문서는 포맷 편집, 열람 용이).
* **이미지:** jpg, png, svg 등 (래스터, 벡터 형식).
* **음성(음향):** mp3, acc 등 (소리, 음성 등을 재생하기 위한 디지털 오디오).
* **동영상:** mp4, mpg 등 (프레임을 활용하여 만들어진 움직이는 이미지와 음성).
* **공간 정보:** Shapefile (지리정보, 위치정보 등 공간 데이터를 포함).

---

## 3. HTTP 통신 및 Requests 라이브러리

### 3.1. HTTP 통신 개념

* **요청(Request):** "와인 있나요?" (클라이언트 -> 서버)
* **응답(Response):** "여기 보시면 됩니다." (서버 -> 클라이언트)

### 3.2. Requests 라이브러리 (Python)

* 접근할 웹 페이지의 데이터를 요청/응답 받기 위한 라이브러리.

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

* **GET 메소드:** 웹 서버에게 파라미터를 포함해 요청을 보내는 가장 쉬운 방법. URL에 파라미터 정보를 달아서 보냄.
* **구조 예시:** `https://youtube.com/results?search_query=bigdata`
* 페이지 URL: `https://youtube.com/results`
* 파라미터: `search_query = bigdata`



---

## 4. 공공 데이터 포털의 OpenAPI 활용

### 4.1. 사용 절차

1. **사용자:** 공공데이터 포털에 활용신청.
2. **공공데이터 포털:** API Key 발급.
3. **사용자:** 오픈 API 호출 (API Key 포함).
4. **제공기관:** 요청 처리 후 API 회신.
5. **사용자:** API 결과 응답 수신.

### 4.2. 상세 과정

* 활용목적 선택 및 신청 -> 승인 후 인증키(ServiceKey) 발급.
* **요청변수(Request Parameter):** 서비스키(필수), 페이지 번호, 한 페이지 결과 수, 데이터 생성일 시작/종료 범위 등.
* **응답 데이터:** XML 형태로 반환 (예: `<confCase>`, `<deathRate>` 등).

### 4.3. [실습 코드 1] OpenAPI 응답 데이터 이해 및 추출

*코로나19 감염현황 데이터를 가져오는 예제 코드*

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

*데이터프레임의 '구분' 컬럼 데이터를 정제하는 예제 (숫자와 '이상' 포함 처리)*

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

* 공공데이터는 정형/정적 데이터 위주인 반면, 기업 API는 실시간 서비스 중심 데이터를 다양하게 제공.
* 인증 방식: 로그인(OAuth) 등을 사용하는 서비스 주소 방식이 많음 (Client ID, Client Secret 필요).

### 5.2. Naver OpenAPI 사례

* 애플리케이션 등록 (API 이용신청).
* 비로그인 오픈 API (검색, 지도 등) vs 로그인 오픈 API (카페, 블로그 등).
* 일일 허용량(Quota) 존재.

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
