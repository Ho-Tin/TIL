업로드해주신 영상은 SQL에 대한 교육용 프레젠테이션을 녹화한 것입니다.

영상 내용을 바탕으로 요청하신 대로 자세한 내용을 정리하여 마크다운(MD) 파일 형식으로 작성했습니다.

````md
# SQL DDL, DML, JOIN - 테이블 정의 및 데이터 조작

이 문서는 제공된 영상을 바탕으로 SQL의 주요 개념과 명령어를 정리한 요약본입니다.

---

## 1. SQL Statements 유형

SQL 명령어는 기능에 따라 크게 4가지로 분류됩니다.

* **DDL (Data Definition Language)**: 데이터 정의어
    * 역할: 데이터의 기본 구조 및 형식을 정의합니다.
    * 주요 키워드: `CREATE`, `DROP`, `ALTER`
* **DQL (Data Query Language)**: 데이터 질의어
    * 역할: 데이터를 검색합니다.
    * 주요 키워드: `SELECT`
* **DML (Data Manipulation Language)**: 데이터 조작어
    * 역할: 데이터를 추가, 수정, 삭제합니다.
    * 주요 키워드: `INSERT`, `UPDATE`, `DELETE`
* **DCL (Data Control Language)**: 데이터 제어어
    * 역할: 데이터 및 작업에 대한 사용자 권한을 제어합니다.
    * 주요 키워드: `COMMIT`, `ROLLBACK`, `GRANT`, `REVOKE`

---

## 2. DDL (Data Definition Language)

### 🔹 CREATE TABLE (테이블 생성)

데이터베이스에 새 테이블을 생성합니다.

**주요 제약 조건 3가지:**

1.  **PRIMARY KEY (기본 키)**
    * 테이블의 고유 식별자(ID)로 사용됩니다.
    * `AUTOINCREMENT`: INTEGER 타입과 함께 사용 시, 데이터가 추가될 때마다 값이 자동으로 1씩 증가합니다.
    * `BIGINT` 등 다른 정수 유형은 `AUTOINCREMENT`를 적용할 수 없습니다.
2.  **NOT NULL**
    * 해당 필드(column)에 `NULL` 값(빈 값)을 허용하지 않도록 지정합니다.
3.  **FOREIGN KEY (외래 키)**
    * 다른 테이블과의 관계를 정의합니다.

**예시 구문:**

```sql
CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);
````

**TIP:** `PRAGMA table_info('테이블명');` 명령어를 사용하면 해당 테이블의 스키마(구조) 정보를 확인할 수 있습니다.

-----

### 🔹 ALTER TABLE (테이블 수정)

기존에 생성된 테이블의 구조를 변경합니다.

  * **ADD COLUMN**: 테이블에 새 필드(column)를 추가합니다.
      * `NOT NULL` 제약 조건과 함께 추가할 경우, `DEFAULT` 값을 지정해야 SQLite에서 오류가 발생하지 않습니다.
    <!-- end list -->
    ```sql
    ALTER TABLE examples
    ADD COLUMN Country VARCHAR(100) NOT NULL DEFAULT 'default value';
    ```
  * **RENAME COLUMN**: 필드(column)의 이름을 변경합니다. (영상에서는 PostCode가 추가되는 장면만 나오고 RENAME은 제목으로만 언급되었습니다.)
  * **DROP COLUMN**: 필드(column)를 삭제합니다.
    ```sql
    ALTER TABLE examples
    DROP COLUMN PostCode;
    ```
  * **RENAME TO**: 테이블의 이름을 변경합니다.
    ```sql
    ALTER TABLE examples
    RENAME TO new_examples;
    ```

-----

### 🔹 DROP TABLE (테이블 삭제)

테이블을 데이터베이스에서 완전히 삭제합니다.

**예시 구문:**

```sql
DROP TABLE new_examples;
```

-----

## 3\. DML (Data Manipulation Language)

### 🔹 INSERT (데이터 삽입)

테이블에 새로운 레코드(row)를 추가합니다.

**예시 구문:**

```sql
-- 단일 데이터 삽입
INSERT INTO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');

-- 다중 데이터 삽입
INSERT INTO articles (title, content, createdAt)
VALUES
    ('title1', 'content1', '1900-01-01'),
    ('title2', 'content2', '1800-01-01'),
    ('title3', 'content3', '1700-01-01');

-- 함수를 사용한 삽입 (예: 현재 날짜)
INSERT INTO articles (title, content, createdAt)
VALUES ('mytitle', 'mycontent', DATE());
```

-----

### 🔹 UPDATE (데이터 수정)

테이블의 기존 레코드(row)를 수정합니다.

  * **`WHERE` 절이 매우 중요합니다.** `WHERE`를 생략하면 **테이블의 모든 레코드**가 변경됩니다.

**예시 구문:**

```sql
-- 특정 레코드의 단일 필드 수정
UPDATE articles
SET title = 'Update Title'
WHERE id = 1;

-- 특정 레코드의 여러 필드 수정
UPDATE articles
SET
    title = 'Update Title',
    content = 'Update Content'
WHERE id = 2;
```

-----

### 🔹 DELETE (데이터 삭제)

테이블의 레코드(row)를 삭제합니다.

  * **`WHERE` 절이 매우 중요합니다.** `WHERE`를 생략하면 **테이블의 모든 레코드**가 삭제됩니다.

**예시 구문:**

```sql
-- 특정 레코드 삭제
DELETE FROM articles
WHERE id = 1;

-- 정렬 후 상위 N개 레코드 삭제 (예: 가장 오래된 2개 삭제)
DELETE FROM articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createdAt
    LIMIT 2
);
```

-----

## 4\. JOIN (테이블 조인)

두 개 이상의 테이블을 특정 조건(공통된 값)을 기준으로 연결하여 데이터를 조회합니다.

**예시 테이블:** `articles` (게시글), `users` (작성자), `roles` (권한)

### 🔹 INNER JOIN

  * 두 테이블(A, B) 간의 **교집합**에 해당하는 레코드만 반환합니다.
  * 조인 조건(예: `users.id = articles.userId`)이 일치하는 데이터만 결과에 포함됩니다.

**예시 구문:**

```sql
-- 'articles'와 'users' 테이블을 조인하여 게시글 제목과 작성자 이름을 함께 조회
SELECT
    articles.title,
    users.name
FROM articles
INNER JOIN users
    ON users.id = articles.userId;
```

### 🔹 LEFT JOIN (LEFT OUTER JOIN)

  * 왼쪽 테이블(A)의 **모든 레코드**를 반환하고, 오른쪽 테이블(B)에서는 조인 조건을 만족하는 레코드만 반환합니다.
  * 오른쪽 테이블에 일치하는 데이터가 없으면 해당 필드는 `NULL` 값으로 채워집니다.

**예시 구문:**

```sql
-- 'users' 테이블을 기준으로 'articles' 테이블을 조인
-- (작성한 게시글이 없는 회원도 조회 결과에 포함됨)
SELECT *
FROM users
LEFT JOIN articles
    ON users.id = articles.userId;
```

-----

## 5\. 기타 참고 사항

  * **SQLite 데이터 타입 (Type Affinity)**
      * SQLite는 데이터 타입을 엄격하게 강제하지 않고 '유사성(Affinity)'을 가집니다.
      * 예: `VARCHAR(255)`로 선언해도 255자가 넘는 텍스트를 저장할 수 있습니다.
  * **NOT NULL**
      * 필드가 `NULL` 값을 가질 수 없도록 하는 제약 조건입니다.
  * **날짜 및 시간**
      * `DATE()`와 같은 내장 함수를 사용하여 날짜 및 시간 데이터를 관리할 수 있습니다.

-----

## 6\. 학습 요약

  * **`CREATE TABLE`**: 새 테이블 생성 및 `PRIMARY KEY`, `NOT NULL` 등 제약 조건 설정.
  * **`ALTER TABLE`**: `ADD/DROP COLUMN`, `RENAME`을 통한 테이블 구조 변경.
  * **`DROP TABLE`**: 테이블 삭제.
  * **`JOIN`**: `INNER JOIN` (교집합)과 `LEFT JOIN` (왼쪽 기준)을 사용한 다중 테이블 데이터 조회.
  * **SQLite Type Affinity**: 데이터 타입을 엄격하게 강제하지 않는 SQLite의 특징.

<!-- end list -->

```

혹시 이 내용 중에서 특정 SQL 명령어의 사용법이나 예시에 대해 더 궁금한 점이 있으신가요?
```