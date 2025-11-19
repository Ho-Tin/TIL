
-----

# JavaScript Basic Syntax 02: 객체, 배열, 클래스 완전 정복

## 1\. 객체 (Object)

### 1.1 객체의 정의와 기본 조작

객체는 \*\*키(Key)와 값(Value)\*\*으로 구성된 속성(Property)들의 집합입니다. 데이터들의 묶음을 저장할 때 사용합니다.

  * **속성 접근:** `.` (점 표기법) 또는 `[]` (대괄호 표기법) 사용.
  * **대괄호 표기법 사용 시점:** 키에 공백이 있거나, 변수를 키로 사용할 때.

**[예시 코드: 조회, 추가, 수정, 삭제]**

```javascript
const user = {
  name: 'Alice',
  age: 30,
  'key with space': true, // 공백이 포함된 키
}

// 1. 조회
console.log(user.name) // Alice (점 표기법)
console.log(user['key with space']) // true (대괄호 표기법)

// 2. 추가
user.address = 'korea'
console.log(user) // { name: 'Alice', ..., address: 'korea' }

// 3. 수정
user.name = 'Bella'
console.log(user.name) // Bella

// 4. 삭제
delete user.name
console.log(user) // { age: 30, 'key with space': true, address: 'korea' }
```

### 1.2 메서드(Method)와 `this`

메서드는 객체의 속성으로 정의된 함수입니다. 메서드 내부의 `this` 키워드는 **호출하는 방식**에 따라 가리키는 대상이 달라집니다.

  * **메서드 호출:** `this`는 해당 메서드를 호출한 객체.
  * **일반 함수 호출:** `this`는 전역 객체(`window`).

**[예시 코드: `this`의 동작]**

```javascript
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      // forEach의 콜백 함수는 '일반 함수'로 호출됨 -> this가 전역 객체(window)를 가리킴
      console.log(this) // window 출력
    })
  }
}
myObj2.myFunc()
```

### 1.3 ES6+ 추가 문법 (유용한 기능)

#### A. 계산된 속성 (Computed Property Name)

대괄호 `[]` 안에 표현식(변수 등)을 넣어 동적으로 키 이름을 결정할 수 있습니다.

**[예시 코드]**

```javascript
const product = prompt('물건 이름을 입력해주세요') // 예: bag 입력
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,             // 입력받은 'bag'이 키가 됨
  [prefix + suffix]: 'value', // 'myproperty'가 키가 됨
}

console.log(bag) // { bag: 5, myproperty: 'value' }
```

#### B. 구조 분해 할당 (Destructuring Assignment)

객체나 배열의 속성을 분해하여 개별 변수에 담을 수 있습니다. 함수의 매개변수로 받을 때 매우 유용합니다.

**[예시 코드]**

```javascript
const person = {
  name: 'Bob',
  age: 35,
  city: 'London',
}

// 객체 전체를 받아서 내부에서 분해하는 대신, 매개변수 단계에서 분해
function printInfo({ name, age, city }) {
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}

printInfo(person) // 이름: Bob, 나이: 35, 도시: London
```

#### C. Optional Chaining (`?.`)

중첩된 객체에서 속성이 존재하는지 확인하지 않고 접근하면 에러가 발생합니다. `?.`를 사용하면 속성이 없을 때 에러 대신 `undefined`를 반환합니다.

**[예시 코드]**

```javascript
const user = {
  name: 'Alice',
  greeting: function () { return 'hello' }
}

// user.address가 없으므로 .street 접근 시 에러 발생
// console.log(user.address.street) // Uncaught TypeError

// ?. 사용 시 안전하게 접근 가능
console.log(user.address?.street) // undefined

// 존재하지 않는 메서드 호출 시에도 사용 가능
console.log(user.nonMethod?.()) // undefined
```

### 1.4 객체 도우미 메서드

객체의 키, 값, 쌍을 배열로 반환해주는 메서드입니다.

**[예시 코드]**

```javascript
const profile = { name: 'Alice', age: 30 }

console.log(Object.keys(profile))   // ['name', 'age']
console.log(Object.values(profile)) // ['Alice', 30]
console.log(Object.entries(profile)) // [['name', 'Alice'], ['age', 30]]
```

-----

## 2\. JSON (JavaScript Object Notation)

자바스크립트 객체와 유사하게 생겼으나, 실제로는 **문자열(String)** 형식입니다. 서버와 데이터를 주고받을 때 주로 사용합니다.

  * `JSON.stringify()`: 객체 → JSON 문자열
  * `JSON.parse()`: JSON 문자열 → 객체

**[예시 코드]**

```javascript
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}

// 1. Object -> JSON String 변환
const objToJson = JSON.stringify(jsObject)
console.log(objToJson) // '{"coffee":"Americano","iceCream":"Cookie and cream"}' (문자열임)

// 2. JSON String -> Object 변환
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj.coffee) // Americano (다시 객체로 사용 가능)
```

-----

## 3\. 배열 (Array)

### 3.1 기본 수정 메서드

배열의 앞이나 뒤에 요소를 추가하거나 삭제합니다. 원본 배열이 변경됩니다.

**[예시 코드]**

```javascript
const names = ['Alice', 'Bella', 'Cathy']

// pop: 뒤에서 제거
console.log(names.pop()) // 'Cathy'

// unshift: 앞에서 추가
names.unshift('Eric')
console.log(names) // ['Eric', 'Alice', 'Bella']

// shift: 앞에서 제거
console.log(names.shift()) // 'Eric'
```

### 3.2 Array Helper Methods (순회 메서드)

반복문(`for`) 대신 콜백 함수를 사용하여 배열을 효율적으로 다룹니다.

#### A. `forEach`

배열의 요소를 단순히 순회합니다. **반환값(return)이 없습니다.**

**[예시 코드]**

```javascript
const names = ['Alice', 'Bella', 'Cathy']

names.forEach((item, index, array) => {
  console.log(`${item} / ${index}`)
})
// 출력:
// Alice / 0
// Bella / 1
// Cathy / 2
```

#### B. `map`

배열의 모든 요소에 콜백 함수를 적용하고, 그 결과를 모아 **새로운 배열을 반환**합니다.

**[예시 코드]**

```javascript
const numbers = [1, 2, 3]

// 각 요소를 2배로 만드는 함수
const doubleNum = numbers.map((number) => {
  return number * 2
})

console.log(doubleNum) // [2, 4, 6] (새로운 배열)
console.log(numbers)   // [1, 2, 3] (원본 유지)
```

요청하신 대로 **3.2 Array Helper Methods** 항목에 `reduce` 설명을 추가하여 정리해 드립니다. 기존 양식인 \*\*[핵심 설명]\*\*과 **[예시 코드]** 형식을 유지했습니다.

이 내용을 기존 노트의 **B. `map`** 바로 아래에 추가하시면 됩니다.

-----

#### C. `reduce`

배열의 각 요소를 순회하며 콜백 함수를 실행하고, **최종적으로 하나의 결과값**을 반환합니다. 주로 합계, 평균 등 누적 계산이 필요할 때 사용합니다.

  * **콜백 함수 인자:** `(accumulator, currentValue)`
      * `accumulator` (acc): 이전 순회에서 반환된 누적값
      * `currentValue` (cur): 현재 처리 중인 배열의 요소
  * **초기값:** `reduce` 함수의 두 번째 인자로 전달 (생략 시 첫 번째 요소가 초기값이 됨)

**[예시 코드]**

```javascript
const scores = [90, 80, 70, 100]

// total: 누적값, score: 현재 요소, 0: 초기값
const sum = scores.reduce((total, score) => {
  // 리턴된 값이 다음 순회의 total로 전달됨
  return total + score
}, 0)

console.log(sum) // 340

// (활용) 평균 구하기
const average = sum / scores.length
console.log(average) // 85
```

-----

### 📝 요약: `map` vs `reduce` 차이점

  * **`map`**: 배열의 길이만큼 새로운 값을 생성하여 **새로운 배열**을 만듦 (1:1 변환).
  * **`reduce`**: 배열의 요소들을 합쳐서 **단 하나의 값**(숫자, 문자열, 객체 등)을 만듦 (N:1 요약).


### 3.3 전개 구문 (Spread Syntax)

`...`을 사용하여 배열의 요소를 개별적으로 펼칩니다. 배열 합치기나 복사에 유용합니다.

**[예시 코드]**

```javascript
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발'] 
// parts 배열이 펼쳐져서 들어감

console.log(lyrics) // ['머리', '어깨', '무릎', '발']
```

-----

## 4\. 클래스 (Class)

ES6부터 도입된 문법으로, 객체를 생성하기 위한 설계도 역할을 합니다. `constructor`를 통해 초기값을 설정합니다.

**[예시 코드]**

```javascript
class Member {
  // 생성자: new Member() 호출 시 실행됨
  constructor(name, age) {
    this.name = name
    this.age = age
  }

  // 메서드 정의
  sayHi() {
    console.log(`Hi, I am ${this.name}`)
  }
}

// 클래스 사용 (인스턴스 생성)
const member1 = new Member('Alice', 30)
member1.sayHi() // "Hi, I am Alice"
```