
-----

# JavaScript Basic Syntax 02 - 예시 코드 모음

## 1\. 객체 (Object)

### 1.1 속성 접근 및 수정 (Property Access)

객체의 속성을 조회, 추가, 수정, 삭제하는 방법입니다.

```javascript
const user = {
  name: 'Alice',
  age: 30,
  'key with space': true, // 공백이 있는 키
}

// 조회
console.log(user.name) // Alice
console.log(user['key with space']) // true

// 추가
user.address = 'korea'
console.log(user) // { name: 'Alice', ..., address: 'korea' }

// 수정
user.name = 'Bella'
console.log(user.name) // Bella

// 삭제
delete user.name
console.log(user) // { age: 30, 'key with space': true, address: 'korea' }
```

### 1.2 메서드와 `this` (Method)

메서드 내부의 `this`는 호출 방식에 따라 달라집니다.

```javascript
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      // 일반 함수로 호출된 콜백 함수 내부의 this는 전역 객체(window)를 가리킴
      console.log(this) // window
    })
  }
}
console.log(myObj2.myFunc())
```

### 1.3 계산된 속성 (Computed Property Name)

변수 값을 키 이름으로 동적으로 사용할 수 있습니다.

```javascript
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
  [product]: 5,
  [prefix + suffix]: 'value',
}

console.log(bag) // { [입력값]: 5, myproperty: 'value' }
```

### 1.4 구조 분해 할당 (Destructuring Assignment)

객체나 배열의 속성을 분해하여 변수에 할당합니다.

```javascript
const person = {
  name: 'Bob',
  age: 35,
  city: 'London',
}

// 함수의 매개변수로 구조 분해 할당 사용
function printInfo({ name, age, city }) {
  console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
}

printInfo(person) // 이름: Bob, 나이: 35, 도시: London
```

### 1.5 유용한 객체 메서드 (Object Helper Methods)

`keys`, `values`, `entries`를 통해 객체의 정보를 배열로 반환합니다.

```javascript
const profile = {
  name: 'Alice',
  age: 30,
}

console.log(Object.keys(profile))   // ['name', 'age']
console.log(Object.values(profile)) // ['Alice', 30]
console.log(Object.entries(profile)) // [['name', 'Alice'], ['age', 30]]
```

### 1.6 Optional Chaining (`?.`)

존재하지 않을 수 있는 속성에 안전하게 접근합니다.

```javascript
const user = {
  name: 'Alice',
  greeting: function () {
    return 'hello'
  }
}

// console.log(user.address.street) // Uncaught TypeError (에러 발생)
console.log(user.address?.street) // undefined (에러 없이 undefined 반환)

// console.log(user.nonMethod()) // Uncaught TypeError
console.log(user.nonMethod?.()) // undefined
```

-----

## 2\. JSON 변환

객체를 JSON 문자열로 변환하거나 그 반대로 변환합니다.

```javascript
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
}

// Object -> JSON String
const objToJson = JSON.stringify(jsObject)
console.log(objToJson) // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson) // string

// JSON String -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'Cookie and cream' }
console.log(typeof jsonToObj) // object
```

-----

## 3\. 배열 (Array)

### 3.1 기본 조작 메서드

`pop`, `unshift`, `shift` 등을 이용해 배열 요소를 직접 수정합니다.

```javascript
const names = ['Alice', 'Bella', 'Cathy']

// pop(): 마지막 요소 제거 및 반환
console.log(names.pop()) // Cathy
console.log(names) // ['Alice', 'Bella']

// unshift(): 앞에 요소 추가 (배열의 길이 반환)
names.unshift('Eric')
console.log(names) // ['Eric', 'Alice', 'Bella']

// shift(): 앞의 요소 제거 및 반환
console.log(names.shift()) // Eric
console.log(names) // ['Alice', 'Bella']
```

### 3.2 Array Helper Methods - `forEach`

반환값 없이 배열을 순회합니다.

```javascript
const names = ['Alice', 'Bella', 'Cathy']

names.forEach(function (item, index, array) {
  console.log(`${item} / ${index} / ${array}`)
})

// 화살표 함수 사용 예시
names.forEach((item, index, array) => {
  console.log(`${item} / ${index} / ${array}`)
})
```

### 3.3 Array Helper Methods - `map`

배열을 순회하며 각 요소에 콜백 함수를 적용한 결과를 모아 **새로운 배열**을 반환합니다.

```javascript
// 기본 사용법
const arr = [1, 2, 3]
// const newArr = arr.map(function (item, index, array) { ... })

// 활용 예시 (커스텀 콜백 함수 사용)
const numbers = [1, 2, 3]

const myCallbackFunc = function (number) {
  return number * 2
}

const doubleNumber = numbers.map(myCallbackFunc)
console.log(doubleNumber) // [2, 4, 6]
```

### 3.4 전개 구문 (Spread Syntax)

배열을 합치거나 중간에 삽입할 때 유용합니다.

```javascript
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']

console.log(lyrics) // ['머리', '어깨', '무릎', '발']
```

-----

## 4\. 클래스 (Class)

ES6부터 도입된 클래스 문법입니다.

```javascript
class Member {
  // 생성자 함수: 객체 생성 시 초기화 담당
  constructor(name, age) {
    this.name = name
    this.age = age
  }

  // 메서드 정의
  sayHi() {
    console.log(`Hi, I am ${this.name}`)
  }
}

// 인스턴스 생성
const member1 = new Member('Alice', 30)
member1.sayHi() // Hi, I am Alice
```