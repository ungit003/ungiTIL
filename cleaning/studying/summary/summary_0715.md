### 9 : 00 ~ 9 : 50

- 월요일은 평가가 있어서 라이브 강의 시간이 변동 될 수 있음

(https://file.notion.so/f/f/9b719315-a3f7-4877-b15e-e2efe24e1986/6f86a676-ac73-4cac-9b0c-64424f1db902/df3751e9-d9fb-4a94-a9af-eda557391e55.png?id=a6508bb9-b7c3-4c62-af0a-406e72ca94d0&table=block&spaceId=9b719315-a3f7-4877-b15e-e2efe24e1986&expirationTimestamp=1721174400000&signature=XsGFjIl6ZtlpzdCwQu9bosPJ68QdvSz1preSh3LM2Eg&downloadName=Untitled.png)

- 금요일은 일주일 동안 배운 것 프로젝트 or 심화 강의 (저 사람 아님)
- 금요일은 시험 범위 아님

- lab.ssafy.com/s12/python
- 교제는 에듀싸피
- 파일을 깃랩에서 받아서 쓸 것(뭔가 오류가 생겨서 실패, 다운로드함)
- 안에서 주피터 파일 안에 필기해야 할 내용 제공. 여기다 바로 편집하는 게 제일 빠를 듯.
- ppt랑 주피터랑 내용 순서가 좀 다르고 피피티 기준으로 수업
- 필기가 필요하면 피피티를 보면서 (수업내용) 해야함.

```markdown
### 변수와 메모리 "값이 저장되는 법"

#### 변수(variable)
- 값을 저장하기 위한 이름
- -> 값을 참조하기 위한 이름

#### 변수 할당
- 표현식을 통해 변수에 값을 저장
```

값을 저장하는 상자 → 곤란

- 할당 / 재할당 ( ‘=’ 이걸 기호로 사용)

노트북 1번 파일 끝

### 10 : 00 ~ 11 : 00

2번 데이터 타입 시작

str까지 함.

style guide 

- 스네이크 케이스 ?
- 변수 명 짓는 걸 자주 고민해보기.

### * pep 8 *

https://peps.python.org/pep-0008/

파이썬 작성 양식 같은 것.

### 마무리.

https://file.notion.so/f/f/9b719315-a3f7-4877-b15e-e2efe24e1986/e89d5e06-09b7-4dab-81f2-e41cdbbf94c1/Untitled.png?id=f330dfd0-864d-4d1c-ab50-212b31f5d6b8&table=block&spaceId=9b719315-a3f7-4877-b15e-e2efe24e1986&expirationTimestamp=1721174400000&signature=NZBrj6VlBN877uTP6QB2I4_rwkbzd-mEmi-w1E98qt8&downloadName=Untitled.png

https://file.notion.so/f/f/9b719315-a3f7-4877-b15e-e2efe24e1986/b2b9bc04-7b36-4196-84b2-0bc8be55f4f5/Untitled.png?id=c0f32ce2-15ed-4e81-abd9-93be46601d95&table=block&spaceId=9b719315-a3f7-4877-b15e-e2efe24e1986&expirationTimestamp=1721174400000&signature=SjVnat08llgL_1nwAc-r3qwXYKNZdEz87idMYHGE9ls&downloadName=Untitled.png

### 11 : 10 ~ 12 : 50

- 프로젝트 싸피를 통해서 오프라인 수업을 한다.
- pull_only는 깃랩에서 받기만 할 것.
    - 별도 폴더 만들어서 여기 copy 후 사용.
- 수업내용 보충
    - shell에서 파이썬 작동 시킬 때 파일이 있는 폴더까지 이동하기

- ipynb = py + nb
- new 자기소개

## 하늘쌤 summary

---

1. **변수 값 할당**
    - a = 3 : 수학 용어(같다) 코딩용어 (할당 : assignment)
    
    - 옛날의 입력방법
        1. tape 돌돌 말아서 통에 담아서 쌓아둠
        2. card(omr, punch)
        3. keyboard-(이런건 없었지만 typewriter 는 존재)
            
            ⇒ typewriter에서 데이터로 보낼 때 화살표 ← 로 보냄 ⇒ 화살표가 = 으로 바뀜
            
            (a ←3  ⇒ a = 3)
            

1. **문자열 데이터 타입 이해**
    - 컴퓨터는 숫자열 베이스라 문자열을 쓰기 위해서 사람의 노력이 많이 필요함.
    - c  : machine dependent
    - python : human ~?
    - 문자열  ‘  ‘ ( “   “ 는 정의는 아니고 같은 취급만)
    - ‘a’ ‘apple’ ‘hello_world’ : 문자열 “1”개
    
2. **문자열의 인덱싱, 슬라이싱**
    - 인덱싱 : 번호매기기
        - 타자기에 있는 모든 기호, 문자에 번호를 매김(아스키코드 : 정보교환표준부호)
    - 양의 인덱스, 음의 인덱스, 슬라이싱
        - * 띄어쓰기, 기호 모두 인덱스 번호를 받음.
        - * 음의 인덱스는 -1 스타트인 이유 : 0번으로 스타트하면 양의 인덱스랑 겹친다.
        - 슬라이싱 : 문자열의 일부를 ‘copy’ (i= 자르기)
    
3. **f-string**
    - {place_holder} 안에 변수. 식 다 넣을 수 있음.
    
4. **변수 이름 컨벤션(숫자, 스네이크 케이스)**
    - 변수에 한글 쓰지 말기, 대문자 쓰지 말기, 언더바 쓰기
    
5. **들여쓰기 컨벤션**
    - *들여쓰기 중요. 파이썬의 구분 방식.
6. **여러 줄  주석** - “”” “””
7. **제발 에러 메시지 읽기 .!**

### 14 : 00 ~

1. **파이썬 튜터**
    - 사이트 들어가면 코딩 과정을 가시적으로 보여줌
2. **영어로 검색 - 에러 메시지 복붙**

## project ssafy

---

- 실습 : lv별로 2 2 2 1 1 / lv3까지는 책에 있고, 4, 5는 research
- 과제 : lv2 1 lv4 1 최소 1개 이상.

- **첫 실습, 과제 소감**
    - 난이도가 쉬워서 금방 풀고 개인 공부를 할 수 있었다.
    - 하지만 진도가 빠른 만큼 공부 내용에 대한 확실한 요약, 복습 필요해 보였다.
    - 공부를 미리 해서 진도보다 항상 여유로울 수 있도록 할 것.