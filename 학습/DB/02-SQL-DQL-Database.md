# SQL DQL - 관계형 데이터베이스 개념 및 데이터 조회

이 문서는 동영상 강의 내용을 바탕으로 데이터베이스, 관계형 데이터베이스(RDBMS), 그리고 SQL의 기본 개념을 정리합니다.

## **1\. 데이터베이스란?**

### **데이터 (Data)**

저장이나 처리를 위해 구조화된 형태로 변환된 정보를 의미합니다.

### **데이터베이스 (Database)**

데이터를 효율적으로 저장하고 관리할 수 있게 하는 기술 및 저장소입니다.

### **스프레드시트의 한계**

엑셀과 같은 스프레드시트는 데이터 관리에 유용하지만, 다음과 같은 한계가 있습니다.

* **크기 (Size):** 처리할 수 있는 데이터의 양(예: 약 100만 행)에 제한이 있습니다.  
* **보안 (Security):** 단순한 파일 소유권 기반의 접근 제어만 제공합니다.  
* **정확성 및 일관성 (Accuracy & Consistency):** 데이터가 여러 곳에 분산되어 있을 때, 하나를 수정해도 다른 곳에 반영되지 않아 데이터 불일치 문제가 발생할 수 있습니다.

## **2\. 관계형 데이터베이스 (Relational Database)**

### **정의**

데이터 항목 간에 미리 정의된 \*\*관계(Relationship)\*\*를 기반으로 데이터를 구성하는 데이터베이스입니다. 데이터는 정해진 구조(테이블)에 저장되며, 이 테이블들은 서로 논리적으로 연결될 수 있습니다.

### **DBMS (Database Management System)**

데이터베이스를 효율적으로 관리하고 운영하기 위한 소프트웨어 프로그램입니다.

* **RDBMS (관계형 DBMS):** 관계형 데이터베이스를 관리하는 시스템입니다.  
* **예시:** SQLite, MySQL, PostgreSQL, Oracle Database 등

### **핵심 키워드**

* **Table (혹은 Relation):** 데이터가 실질적으로 저장되는 행(Row)과 열(Column)의 2차원 구조입니다.  
* **Field (혹은 Column, Attribute):** 테이블의 '열'에 해당하며, 데이터의 특정 속성을 나타냅니다.  
* **Record (혹은 Row, Tuple):** 테이블의 '행'에 해당하며, 관련된 데이터 값의 집합입니다.  
* **Primary Key (PK, 기본 키):** 테이블의 각 레코드(행)를 고유하게 식별할 수 있는 값입니다. (예: 고객 ID)  
* **Foreign Key (FK, 외래 키):** 한 테이블의 필드(열)가 다른 테이블의 기본 키(PK)를 참조하여, 두 테이블 간의 관계를 맺어주는 키입니다. (예: '주문' 테이블의 '고객 ID')

## **3\. SQL (Structured Query Language)**

### **정의**

관계형 데이터베이스(RDBMS)에서 데이터를 정의, 조작, 제어하고 쿼리(조회)하기 위해 사용하는 표준 언어입니다.

### **기본 문법**

* 일반적으로 SELECT column\_name FROM table\_name;과 같은 형식을 가집니다.  
* SQL 키워드는 대소문자를 구분하지 않습니다. (관례적으로 대문자 사용)  
* 각 SQL 문장(Statement)은 세미콜론(;)으로 끝납니다.

### **SQL 문 유형**

1. **DQL (Data Query Language):** 데이터 조회  
   * SELECT: 데이터를 검색합니다.  
2. **DML (Data Manipulation Language):** 데이터 조작  
   * INSERT: 데이터를 삽입합니다.  
   * UPDATE: 데이터를 수정합니다.  
   * DELETE: 데이터를 삭제합니다.  
3. **DDL (Data Definition Language):** 데이터 정의  
   * CREATE: 데이터베이스 객체(테이블 등)를 생성합니다.  
   * DROP: 객체를 삭제합니다.  
   * ALTER: 객체의 구조를 변경합니다.  
4. **DCL (Data Control Language):** 데이터 제어  
   * GRANT: 사용자에게 권한을 부여합니다.  
   * REVOKE: 사용자의 권한을 취소합니다.  
   * COMMIT: 트랜잭션을 확정합니다.  
   * ROLLBACK: 트랜잭션을 되돌립니다.

## **4\. 데이터 조회 (Querying Data)**

### **SELECT**

테이블에서 데이터를 조회합니다.

* SELECT \* FROM table\_name;: table\_name의 **모든 열**을 조회합니다.  
* SELECT col1, col2 FROM table\_name;: table\_name의 col1, col2 **특정 열**을 조회합니다.  
* SELECT col1 AS "별칭" FROM table\_name;: col1 열의 이름을 '별칭'으로 변경하여 조회합니다.

### **DISTINCT**

조회 결과에서 중복된 값을 제거하고 고유한 값만 반환합니다.

* SELECT DISTINCT country FROM customers;

### **WHERE**

특정 조건을 충족하는 레코드(행)만 필터링합니다.

* **비교 연산자:** \=, \!= (또는 \<\>), \>, \<, \>=, \<=  
* **논리 연산자:** AND, OR, NOT  
* **기타 유용한 연산자:**  
  * BETWEEN a AND b: a와 b 사이의 값 (양 끝 포함)  
  * IN (val1, val2, ...): 목록 안의 값 중 하나와 일치  
  * LIKE: 문자열 패턴 매칭  
    * %: 0개 이상의 문자를 의미 (예: son% \- 'son'으로 시작하는 문자열)  
    * \_: 1개의 단일 문자를 의미 (예: \_\_a\_ \- 3번째 글자가 'a'인 4자리 문자열)  
  * IS NULL / IS NOT NULL: NULL 값인지 아닌지 확인

### **LIMIT**

조회 결과로 반환되는 레코드(행)의 수를 제한합니다.

* LIMIT 10;: 상위 10개의 결과만 반환합니다.  
* LIMIT 5 OFFSET 3;: 3개의 레코드를 건너뛰고, 그 다음부터 5개의 결과를 반환합니다.

## **5\. 데이터 정렬 및 그룹화**

### **ORDER BY**

조회 결과를 특정 열을 기준으로 정렬합니다.

* ORDER BY col1 ASC;: col1을 기준으로 **오름차순** 정렬 (기본값)  
* ORDER BY col1 DESC;: col1을 기준으로 **내림차순** 정렬  
* ORDER BY col1, col2 DESC;: col1로 먼저 오름차순 정렬 후, col1이 같은 값 내에서 col2로 내림차순 정렬

### **GROUP BY**

특정 열을 기준으로 레코드를 그룹화하여, 각 그룹에 대한 집계 함수를 적용할 때 사용합니다.

* **집계 함수 (Aggregate Functions):**  
  * COUNT(): 그룹의 레코드 수  
  * SUM(): 합계  
  * AVG(): 평균  
  * MAX(): 최댓값  
  * MIN(): 최솟값  
* 예시: SELECT country, COUNT(\*) FROM customers GROUP BY country;  
  (고객 테이블을 국가별로 그룹화하고, 각 국가의 고객 수를 계산)

### **HAVING**

GROUP BY로 그룹화된 결과에 대한 조건을 지정합니다. (WHERE는 그룹화 전 개별 행에 대한 조건)

* 예시: ... GROUP BY country HAVING COUNT(\*) \> 10;  
  (고객 수가 10명 초과인 국가만 조회)

## **6\. SQL 실행 순서**

SQL 문은 작성된 순서와 다르게 내부적으로 다음과 같은 순서로 실행됩니다.

1. **FROM**: 대상 테이블을 지정합니다.  
2. **WHERE**: 개별 행을 필터링합니다.  
3. **GROUP BY**: 행을 그룹화합니다.  
4. **HAVING**: 그룹을 필터링합니다.  
5. **SELECT**: 조회할 열을 선택합니다.  
6. **ORDER BY**: 결과를 정렬합니다.  
7. **LIMIT**: 반환할 행의 수를 제한합니다.

## **7\. 중요 개념**

* **NULL 값:** '값이 없음'을 의미하는 특별한 값입니다. 숫자 0이나 빈 문자열('')과는 다릅니다.  
  * NULL 값과 비교할 때는 \= 연산자가 아닌 IS NULL 또는 IS NOT NULL을 사용해야 합니다.  
* **SQL 표준 (ANSI/ISO):** SQL은 표준이 있지만, 각 RDBMS(MySQL, PostgreSQL 등)마다 표준을 벗어나는 고유의 문법이나 함수(방언, Dialect)를 가질 수 있습니다.