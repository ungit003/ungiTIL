## 9 : 00 ~ 11 : 00

### 강의 핵심

- 함수의 정의와 호출
- 매개변수와 인자
- 함수와 스코프
- 글로벌
- map() zip()

# 함수

---

**특정 작업을 수행하기 위한 재사용 가능한 코드 묶음**

---

- **사용하는 이유**
    - 두 수의 합을 구하는 함수 정의, 사용 → 코드 중복 방지
    - 재사용성 증가, 가독성, 유지보수성(함수 하나만 고치면 되니까) 향상

- 함수 구조
    - input ( parameter)
        
        → a, b, pram ~~~
        
    - body = function
        - (docstring = document string : 함수 설명서)
    - output (return value)
        
        → return a + b, ~~~
        

- input : 함수 정의(정의)
    - def 함수_이름 (매개변수)

- body
    - 콜론( : ) 다음 ‘들여쓰기’ 된 코드블록
        - + docstring

- output
    - 결과 반환”할 수 있음”
    - return 반환할_값
        - 실행종료, 결과를 호출 부분으로 변환
        - 없으면 None 나옴.
        - **프린트는 출력은 있고 리턴은 없다.**
    - 함수 호출
        - 사용 하려면 호출
        - 이름, 소괄호로 호출
        - 필요하면 인자 전잘
        - 호출 부분에서 인자는 함수 정의 시 작성한 매개변수에 대입

```markdown
# *교제에 없음*
def my_func():
    print('hello world')
    
result = my_func()
print(result)

hello world
None
```

# 매개변수와 인자

---

## 매개변수 : parameter

---

**함수를 정의할 때 함수가 받을 값을 나타내는 변수**

## 인자 : argument

---

**함수를 호출할 때 전달되는 값**

```markdown
def add_numbers(x, y): # x와 y는 매개변수(parameter)
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b) # a와 b는 인자(argument)
print(sum_result)
```

### 다양한 인자의 종류

- 위치 인자
    - 함수 호출 시 인자의 위치에 따라 전달되는 인자
    - **위치 인자는 함수 호출 시 반드시 값을 전달해야 함**
- 기본 인자 값
    - 함수 정의에서 매개변수에 기본 값을 할당하는 것
    - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
- 키워드 인자
    - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
    - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당할 수 있음
    - 인자의 순서는 중요하지 않으며, 인자의 이름을 명시하여 전달
    - **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**
- 임의의 인자 목록
    - 정해지지 않은 개수의 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 `‘*’`를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
- 임의의 키워드 인자 목록
    - 정해지지 않은 개수의 키워드 인자를 처리하는 인자
    - 함수 정의 시 매개변수 앞에 `‘**’`를 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어 처리

### 함수 인자 권장 작성순서

- **위치 -> 기본 -> 가변 -> 가변 키워드**

```markdown
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)

func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')

"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""
```

# 재귀 함수

---

**함수 내부에서 자기 자신을 호출하는 함수**

---

```markdown
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)
# 팩토리얼 계산 예시
print(factorial(5))  # 120
```

### 재귀 함수 특징

- 특정 알고리즘, 변수사용 감소, 코드가독성 증가
- 1개 이상의 base case 존재, 수렴하도록.

### 재귀 함수를 사용하는 이유

### 재귀 함수 활용 시 기억해야 하는 것

# 내장 함수

---

**파이썬이 기본적으로 제공하는 함수**

---

***반댓말로 외장 함수 라는 건 없음**

- python document 치면 공식 문서에 내장함수가 어떤게 있는지 나옴.

```markdown
# 자주 사용되는 내장 함수 예시
numbers = [1, 2, 3, 4, 5]

print(len(numbers))  # 5
print(max(numbers))  # 5
print(min(numbers))  # 1
print(sum(numbers))  # 15
print(sorted(numbers, reverse=True))  # [5, 4, 3, 2, 1]
```

## 유용한 내장함수 map & zip

---

## map(function, iterable)

**순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환**

→iterable : 반복 가능한 개체 = collection

- function이 iterable에 하나하나 다 적용됨
- **function을 내가 정의한 것으로도 할 수 있음.**

### map() 활용

- SWEA 문제의 input 처럼 문자열 `'1 2 3'`이 입력 되었을 때 활용 예시

```markdown
numbers1 = input().split()
# input : 입력 받고
# split : ()기준으로 나눔
print(numbers1)  # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]
```

## **zip(*iterable)**

**임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환**

- 2차원 리스트 사용할 때 행, 열로 묶어내기 좋은 방법.

# 함수와 Scope(범위)

---

**함수는 코드 내부에 `local scope`를 생성하며, 그 외의 공간인 `global scope`로 구분**

---

### 범위와 변수의 관계

- scope
    - global scope : 코드 어디에서든 참조할 수 있는 공간
    - local scope : 함수가 만든 scope (함수 내부에서만 참조 가능)

### scope 예시

### 변수 수명주기(lifecycle)

- bulit-in scope
- global scope
- local scope

### 이름 검색 규칙(Name Resolution) : LEGB Rule

### `global`  키워드

- 변수의 스코프를 전역 범위로 지정하기 위해 사용
- 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용

### **‘global’ 키워드 주의사항**

- global 키워드 선언 전에 참조 불가
- 매개변수에는 global 키워드 사용 불가

# Packing & Unpacking

---

## Packing

---

**여러 개의 값을 하나의 변수에 묶어서 담는 것**

### 패킹 예시

---

**‘*’을 활용한 패킹**

## Unpacking

---

# 람다 함수

---

**1회성으로 함수를 쓸 때**

## 11 : 20 ~

### 오늘 핵심

- 변수명과 객체
    - OS, 변수, 메모리, 할당 검색해보기
- copy, deepcopy
    - a = 3, b = a 라하면 3을 새로 만들어서 b에 할당(기본적으로 deepcopy)
    - a = [1, 2, 3],  b= a 라 하면 b를 a 리스트에 갖다 붙임
        
        → why? 메모리 절약(리스트가 얼마나 클지 모름), 계산 속도 등 향상
        
- 함수 정의와 호출
    - def
    - 함수는 코드를 재사용하려고 만든 것
        
        → 파이썬 튜터로 보면서 하면 도움됨
        
        → 리턴을 쓰고 안쓰고?
        
        **→ 모르면 시험 나옴**
        
    
    매개변수와 인자 _ 가변 인자를 쓰는 이유
    
    ```markdown
    def save_new_customer(id, pw, *args):
    		print(f'{id} = '}
    		print(f'{pw} = '}
    		print(args
    		
    save_new_customer('sky', '1234') # tel, age
    save_new_customer('', '1234')
    ```
    
    → 보통 *args는 입력을 지맘대로 한걸 걸러내는 용도로 사용하는 듯
    
    함수와 스코프
    
    - 글로벌
- lambda
    
    map(), 
    
    함수를 람다로 써도 되고 포 문으로 써도 됨
    
    zip()
    
    짝이 안맞으면 어떻게 되는가?