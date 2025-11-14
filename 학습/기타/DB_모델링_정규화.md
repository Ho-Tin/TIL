
-----


## 목차

  * **데이터베이스 모델링 실습**
      * 레시피 관리 프로젝트
      * 정규화 및 모델 정의
      * 사전 준비 및 프로젝트 코드 확인
      * 레시피 생성
      * 레시피 조회
  * **관통 프로젝트 안내**

-----

## 1\. 데이터베이스 모델링

### 📊 Database Modeling의 중요성

  * **효율성**: 데이터베이스 구조를 잘 설계하면 쿼리 성능과 저장 효율이 향상됩니다.
  * **일관성**: 중복과 이상 현상을 최소화하여, 데이터가 서로 모순되거나 충돌하지 않도록 합니다.
  * **무결성 보장**: 무결성 제약 조건을 모델링 단계에서 설정하여, 부적절한 데이터를 방지합니다.

### 🛡️ 무결성 (Integrity)

  * 데이터베이스가 잘못된 데이터의 삽입·수정·삭제로부터 보호되어, 데이터의 **일관성과 신뢰성을 유지**하는 것을 의미합니다.

### 🔑 1. 개체 무결성 (Entity Integrity)

  * \*\*기본키(Primary Key)\*\*가 중복을 불가하고 'NULL' 값을 허용하지 않는 제약입니다.
  * **핵심 원칙**:
    1.  레코드는 유일한 식별자(PK)를 가져야 합니다. (PK 중복 불가)
    2.  기본 키는 NULL 값을 가질 수 없습니다. (필수 값)
  * **예시 코드**:
    ```sql
    CREATE TABLE Student (
        student_id INT PRIMARY KEY,    -- NULL 불가, 중복 불가
        name VARCHAR(50) NOT NULL
    );
    ```

### 🔢 3. 도메인 무결성 (Domain Integrity)

  * 속성(컬럼)이 \*\*정의된 도메인(값의 범위, 형식)\*\*을 벗어나지 않도록 하는 제약입니다.
  * **핵심 원칙**:
    1.  속성별로 데이터 타입, 길이, 범위 등을 정의해야 합니다.
    2.  값이 해당 도메인을 벗어나면 삽입·수정이 제한되거나 오류가 발생합니다.
  * **예시 코드**:
    ```sql
    CREATE TABLE Product (
        product_id INT PRIMARY KEY,
        price DECIMAL(10,2) CHECK (price > 0),      -- 가격은 0보다 커야 함
        category VARCHAR(20) CHECK (category IN ('전자제품', '의류', '도서')) -- 특정 값만 허용
    );
    ```

### 📋 그 외 무결성 제약 조건

  * **4. 고유성 (UNIQUE)**: 특정 컬럼의 값이 테이블 내에서 중복되지 않도록 하는 제약 (예: 이메일)
  * **5. NULL 무결성 (NOT NULL)**: 특정 컬럼이 NULL 값을 가질 수 없도록 하는 제약
  * **6. 일반 무결성 (General Integrity)**: 특정 은행 계좌 잔액이 0 미만이 될 수 없게 하는 등, 비즈니스 로직에 따라 추가로 정의하는 무결성 규칙

### 🔄 데이터베이스 모델링 진행 순서

  * 요구사항 수집 및 분석 ➔ 개념적 설계 ➔ **논리적 설계** ➔ 물리적 설계

### 📝 1. 요구 (Requirements)

  * 여러 종류의 데이터를 정리
  * **개체 (Entity)**: 업무에 필요한 유용한 정보 (예: 고객, 상품)
  * **속성 (Attribute)**: 관리하고자 하는 정보 (예: 고객명, 고객전화)
  * **관계 (Relationship)**: 개체 사이의 논리적 관계 (예: 고객은 상품을 구매)

### diagrams 1. ERD 표기 방법 (Crow's Foot Model)

  * `|-||` : 1개의 관계 (반드시 필요)
  * `|-|o` : 0개 또는 1개의 관계 (선택적 필요)
  * `|-<` : 1개 이상의 관계 (N개의 관계)
  * `o-<` : 0개 이상의 관계 (N개의 관계, 0개 이상 필요)

### 🏛️ 3. 논리적 설계

  * 개념적 설계를 기반으로 데이터베이스의 논리적 구조를 설계합니다.
  * 테이블, 컬럼(속성), 제약 조건 등 구체적인 데이터베이스 개체를 정의합니다.
  * 정규화를 수행하여 데이터의 중복을 최소화하고 일관성을 유지합니다.

-----

## 2\. 정규화 (Normalization)

### 🎯 정규화 목적

1.  **중복 최소화**: 불필요한 중복 데이터를 제거해 데이터 일관성을 유지합니다.
2.  **이상 현상 방지**: 삽입, 갱신, 삭제 작업 시 발생할 수 있는 불일치 문제를 예방합니다.
3.  **유연성 향상**: 데이터베이스 구조 변경 시 영향을 최소화하여 유지보수성을 높입니다.

### 🐛 이상 현상 (Anomaly)

  * 데이터베이스를 비정상적으로 설계했을 때, 중복된 데이터가 많아져 삽입, 갱신, 삭제 등의 연산에서 비일관성이 생기는 문제입니다.
  * **삽입 이상**: 새로운 데이터를 삽입하기 위해 불필요한 데이터도 함께 삽입해야 하는 문제
  * **갱신 이상**: 데이터가 여러 행에 분산되어 있어, 수정 시 모두 변경해야 하며 누락 시 데이터 모순이 발생합니다. (예: '뽀모도로' 레시피의 설명을 바꾸려 할 때)
  * **삭제 이상**: 특정 레시피를 지울 때, 그 안에만 있던 재료 정보까지 같이 사라지는 문제입니다. (예: '명란 파스타'를 지우면 '명란젓' 재료 정보가 사라짐)

### 💡 해결 방법 (정규화)

1.  **재료(Ingredient) 테이블**을 별도로 분리합니다.
2.  **레시피(Recipe) 테이블**과 **재료(Ingredient) 테이블** 간 **N:M (ManyToMany)** 구조를 설정합니다.
      * 중개 테이블 `Recipe_Ingredient(recipe_id, ingredient_id)` 사용
3.  **결과**:
      * **삽입 이상 해결**: "마늘" 재료만 등록할 수 있습니다.
      * **갱신 이상 해결**: "파스타"를 "스파게티"로 Ingredient 테이블에서 한 번만 수정하면 모든 레시피에 반영됩니다.
      * **삭제 이상 해결**: 레시피에서 "명란젓"을 삭제해도 Ingredient 테이블에는 남아있습니다.

### 📚 정규화 종류

  * 일반적으로 **1NF(제1정규형) ➔ 2NF ➔ 3NF** 순서로 진행합니다.
  * 필요에 따라 BCNF (또는 4NF, 5NF, 6NF)까지 고려하기도 합니다.
  * 실무에서는 보통 **3NF** 또는 **BCNF**까지 정규화가 이루어졌다고 표현합니다.

### 1️⃣ 제 1 정규형 (1NF)

  * **문제**: 한 고객이 2개를 초과하는 전화번호를 저장할 수 없습니다. (예: `전화번호1`, `전화번호2` 컬럼)
  * **해결**: 컬럼을 추가하면 불필요한 NULL이 발생합니다. (별도 테이블로 분리 필요)

### 2️⃣ 제 2 정규형 (2NF)

  * **부분 함수적 종속**을 제거합니다. (기본 키의 일부에만 종속되는 속성을 분리)
  * **예시**: {상품명, 생산자}가 기본 키일 때, `상품가격`은 {상품명, 생산자}에 종속되지만 `생산지`는 `생산자`에만 종속됩니다. (부분 종속) ➔ `생산자` 테이블 분리

### 3️⃣ 제 3 정규형 (3NF)

  * **이행 함수적 종속**을 제거합니다. (기본 키가 아닌 속성 간의 종속 제거)
  * **예시**: `학생번호` ➔ `학과`, `학과` ➔ `학과장`. (즉, `학생번호` ➔ `학과장`이 성립)
  * **해결**: `학과` 테이블(학과, 학과장)과 `학생` 테이블(학생번호, 학생이름, 학과)로 분리합니다.

### BCNF (Boyce-Codd Normal Form)

  * **후보 키**: 기본 키가 될 수 있는 속성들의 집합 (유일성, 최소성 만족)
      * (예: 학생번호, 주민등록번호)
  * **BCNF 진행**: 3NF보다 엄격한 규칙. **모든 결정자가 후보 키여야 합니다.**
  * **예시**: {학생번호, 과목명}이 후보 키일 때, `담당교수` ➔ `과목명` 관계가 성립한다면 (교수 1명이 1과목만 가르칠 시), `담당교수`가 후보 키가 아니므로 BCNF 위반입니다.
  * **해결**: `Course`(담당교수, 과목명)와 `Takes`(학생번호, 과목명, 학점)로 테이블을 분해합니다.

### 📝 정규화 정리

  * **정의**: 중복과 이상 현상을 줄이기 위한 데이터베이스 설계 기법
  * **목표**: 데이터 무결성과 일관성을 확보하고, 유지보수 시 구조 변경 부담을 최소화

-----

## 3\. 레시피 관리 프로젝트 (실습)

### 🥘 Recipe Model class 정의

  * `Ingredient`와 `Recipe`를 N:M (ManyToMany) 관계로 설정합니다.
    ```python
    class Recipe(models.Model):
        name = models.CharField(max_length=200)
        description = models.TextField(blank=True)
        # N:M 관계 설정
        ingredients = models.ManyToManyField('Ingredient', ...) 
        ...
    ```

### 📄 Recipe 데이터 생성 화면

  * (HTML Form 예시: Name, Description 입력, Ingredients 체크박스)

### 🍴 제 1 정규화 (실습 적용)

  * 식재료를 저장하는 **`Ingredient` 테이블**과 레시피를 저장하는 **`Recipe` 테이블**을 분리합니다.

### ⚙️ 사전 준비 (Migrations)

  * 정의한 Model을 DB에 반영합니다.
    ```bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    ```

### ✍️ Form 수정

  * 재료를 다중 선택할 수 있도록 `MultipleChoiceField`로 변경합니다.
    ```python
    # forms.py
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    ```

### 🔍 [참고] queryset 속성

  * `queryset=get_filtered_ingredients()`처럼 별도의 메소드를 정의하여 동적으로 목록을 가져올 수도 있습니다.

### 🖥️ 생성 view와 template

  * `ModelMultipleChoiceField`를 사용하면 선택한 데이터 처리에 별도 전처리 과정이 불필요하며, `save` 과정 수정도 (기본적으로는) 필요 없습니다.

### ✅ 레시피 생성 결과 확인

  * `foods_recipe` 테이블 (레시피)과 `foods_recipe_ingredients` (중간 테이블)에 데이터가 생성된 것을 확인합니다.

### 🧾 레시피 조회 (Template)

  * Django M:N 관계의 **역참조 매니저**(`recipe.ingredients.all`)를 활용하여 렌더링합니다.
    ```html
    <ul>
      {% for ingredient in recipe.ingredients.all %}
        <li>{{ ingredient.name }}</li>
      {% endfor %}
    </ul>
    ```

### ⚠️ [주의사항] Model 정의 시 MTM

  * `Recipe`는 `ingredients`를 직접 필드로 가지지 않습니다. (중간 테이블을 통해 참조)
  * 따라서 `ModelForm`은 이 필드를 감지하지 못하고, **`form.save()`는 ManyToMany 관계를 무시**합니다.
  * **해결**: `form.save()` 이후, `cleaned_data`에서 재료 목록을 가져와 수동으로 `add` 해주는 별도 전처리 과정이 필요합니다.
    ```python
    # foods/views.py
    recipe_form = RecipeForm(request.POST)
    if recipe_form.is_valid():
        recipe = recipe_form.save()
        ingredients = form.cleaned_data.get('ingredients')
        # 수동으로 M:M 관계 추가
        recipe.ingredients.add(recipe) # (슬라이드에 recipe.ingredients.add(recipe)로 표기되어 있으나, add(*ingredients)가 일반적입니다)
    ```

-----

