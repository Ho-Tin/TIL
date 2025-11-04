
# 💻 SQL Statements 기초 학습

## 1. SQL 문 유형

SQL 문은 기능에 따라 4가지 유형으로 분류됩니다.

* **DDL (Data Definition Language):** 데이터 정의어
    * 데이터의 구조와 형식을 정의합니다.
    * 키워드: `CREATE`, `DROP`, `ALTER`
* **DQL (Data Query Language):** 데이터 질의어
    * 데이터를 검색(조회)합니다.
    * 키워드: `SELECT`
* **DML (Data Manipulation Language):** 데이터 조작어
    * 데이터를 추가, 수정, 삭제합니다.
    * 키워드: `INSERT`, `UPDATE`, `DELETE`
* **DCL (Data Control Language):** 데이터 제어어
    * 사용자 및 작업에 대한 권한을 제어합니다.
    * 키워드: `COMMIT`, `ROLLBACK`, `GRANT`, `REVOKE`

---

## 2. DDL (데이터 정의어)

테이블이나 스키마의 구조를 정의하는 명령어입니다.

### 1) CREATE TABLE
새로운 테이블을 생성합니다.

**주요 제약 조건:**
* **`PRIMARY KEY`**: 테이블의 고유 식별자(기본 키)로 설정합니다.
* **`AUTOINCREMENT`**: (SQLite 등) 정수형 기본 키에 사용 시, 값이 자동으로 1씩 증가합니다.
* **`NOT NULL`**: 해당 필드에 NULL 값을 허용하지 않습니다.

**예시 코드:**
```sql
CREATE TABLE examples (
    ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);
````

### 2\) ALTER TABLE

기존 테이블의 구조를 수정합니다.

  * **`ADD COLUMN` (열 추가)**
    ```sql
    ALTER TABLE examples
    ADD COLUMN Country VARCHAR(100) NOT NULL DEFAULT 'default value';
    ```
  * **`DROP COLUMN` (열 삭제)**
    ```sql
    ALTER TABLE examples
    DROP COLUMN PostCode;
    ```
  * **`RENAME TO` (테이블 이름 변경)**
    ```sql
    ALTER TABLE examples
    RENAME TO new_examples;
    ```

### 3\) DROP TABLE

테이블을 삭제합니다.

```sql
DROP TABLE new_examples;
```

-----

## 3\. DML (데이터 조작어)

테이블 내의 데이터를 조작(추가, 수정, 삭제)하는 명령어입니다.

### 1\) INSERT

테이블에 새 데이터(행)를 추가합니다.

  * **단일 행 추가:**
    ```sql
    INSERT INTO articles (title, content, createdAt)
    VALUES ('hello', 'world', '2000-01-01');
    ```
  * **다중 행 추가:**
    ```sql
    INSERT INTO articles (title, content, createdAt)
    VALUES
        ('title1', 'content1', '1900-01-01'),
        ('title2', 'content2', '1800-01-01'),
        ('title3', 'content3', '1700-01-01');
    ```

### 2\) UPDATE

기존 데이터를 수정합니다. **`WHERE` 절을 사용하지 않으면 모든 행이 변경되므로 주의해야 합니다.**

```sql
UPDATE articles
SET title = 'Update Title', content = 'Update Content'
WHERE id = 2;
```

### 3\) DELETE

데이터(행)를 삭제합니다. **`WHERE` 절을 사용하지 않으면 모든 행이 삭제됩니다.**

```sql
DELETE FROM articles
WHERE id = 1;
```

-----

## 4\. JOIN (테이블 조인)

두 개 이상의 테이블을 특정 조건(일반적으로 외래 키)을 기준으로 결합하여 데이터를 조회합니다.

### 1\) INNER JOIN (내부 조인)

두 테이블에서 `ON` 절의 조건이 일치하는 행만 결합합니다. (교집합)

[Image of INNER JOIN Venn diagram]

**예시 구조:**

```sql
SELECT *
FROM articles
INNER JOIN users
    ON articles.userId = users.id;
```

### 2\) LEFT JOIN (왼쪽 외부 조인)

왼쪽 테이블(먼저 `FROM`에 선언된 테이블)의 모든 데이터를 기준으로, 오른쪽 테이블에서 `ON` 절의 조건이 일치하는 데이터를 결합합니다. 일치하는 데이터가 없으면 `NULL`로 표시됩니다.

**예시 구조:**

```sql
SELECT *
FROM users  -- (Left Table)
LEFT JOIN articles -- (Right Table)
    ON users.id = articles.userId;
```

-----

## 5\. 기타 참고 사항

  * **SQLite Type Affinity**: SQLite에서 데이터 타입을 추론하는 방식입니다. (예: `INTEGER`, `TEXT`, `BLOB`, `REAL`, `NUMERIC`)
  * **`NOT NULL` 제약 조건**: `NULL` 값을 허용하지 않음을 명시합니다.
  * **날짜와 시간**: `DATE()` 함수 등을 사용해 날짜 데이터를 입력할 수 있습니다.
