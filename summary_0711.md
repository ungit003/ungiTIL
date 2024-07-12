# <Markdown : 개발자의 언어>
---
## 장점
1. 코드를 서로 주고받기 좋다.
2. 쓰면서 동시에 서식을 만든다. (빠르게 !)
3. 문법이 간단하다. (30분 컷 가능)

## +a
-> 그렇다면 21세기, 24년도 개발자의 소통 방식은? = 깃허브
-> 깃허브에 올리는 방법 : markdown

* *마크다운 확장명 : .md
* 수업 목표 : 필요한 것 부터 배우고 필요하며 구글, gpt 이용.

# 기능

## 1. #의 갯수에 따라서 제목의 크기를 정렬할 수 있음
### 입력
```
# 제목1
## 제목2
### 제목3
#### 제목4
##### 제목5
###### 제목6
####### 제목7
```
### 출력
# 제목1
## 제목2
### 제목3
#### 제목4
##### 제목5
###### 제목6
####### 제목 7 <- 여섯개 까지만 가능 !

---
---
## 2. 순서가 있는 리스트
### 입력
```
1. 밥 
    1. 콩밥
    2. 팥밥
2. 국
    1. 미역국
    2. 소고기국
```

### 출력
1. 밥 
    1. 콩밥 (tab 누르면 한 칸 띄워서.)
    2. 팥밥
2. 국 (shift + tab 누르면 한칸 앞으로)
    1. 미역국
    2. 소고기국

## 3. 순서가 없는 리스트
### 입력
```
- 우산
- 의류
    - 윗도리
    - 아랫도리
```

### 출력
- 우산
- 의류
    - 윗도리
    - 아랫도리

## 4. 코드 블럭(Code Block)
### 역할
여러 줄의 코드를 그대로 넣고 싶을 때

### 입력
\```python <- 파이썬 문법을 쓰겠다. (색칠?도 해줌)

print("hello")

print("world")

\```

### 출력
```python
print("hello")
print("world")
```

### 4-2 만약에 짧게 쓰고 싶다면.

### 입력
제일 중요한 건 \`print(a)\` !

### 출력
제일 중요한 건 `print(a)` !

## 5. 링크 & 이미지

### 입력
```
[구글](https://www.google.com)

[naver](https://www.naver.com)

![언덕](https://picsum.photos/200/300)
```

### 출력
[구글](https://www.google.com)

[naver](https://www.naver.com)

![언덕](https://picsum.photos/200/300)

\* 크기바꾸기 : 마크다운으로는 조절할 수 없다. html로 조절.

\* 사진은 랜덤으로 바뀔 수 있다.

\* html = hyper text markup language.

## 6. 텍스트 관련 문법
### 입력
```
**굵게**

*기울임*

~~취소선~~

수평선

위
---
아래
```

### 출력
**굵게**

*기울임*

~~취소선~~

위
---
아래

### 참고
#### html 이랑 같은 결과를 만들 수 있다.
---
### 입력
```
<h1> 제목 1</h1>

# 제목 1
```
### 출력
<h1> 제목 1</h1>

# 제목 1

## *해보기* 

# 개발자로 성장하기
- 대체 어디서부터 시작해서 어디까지해야할까?
- Python과 Java를  배우면 개발자가 되는걸까?
제일 중요한 건 **꾸준한 학습**을 할 수 있는 사람인지를 보여줘야한다!

### \* 마크다운 에디터

typora, markytext 등등.

---
---
---

# <CLI : command line interface : 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식>

## 참고
<GUI : graphic user interface : 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식>

CLI가 불편해서 GUI로 변경 ( 스티브잡스 )

작업을 할 때 원래는 코드를 입력해 불러와야 했는데 그림을 마우스로 클릭해서 불러오는 방법을 만듦.

BUT, CLI : 서버용(여럿이 나눠쓰는 거), GUI : 개인용 으로 사용됨.

*CLI를 볼 수 있는 거 : GIT BASH(리눅스), cmd(도스)

여기서 깜빡이는거 : 커서, 프롬프트 입력기

### why CLI
---
키보드만, 저사양, ~

## CLI 기초 문법 실습.

git bash 로 실습.

- 여는 법 : 바탕화면 우클릭, git bash, vs code → view → terminal

- 폴더, 파일 이름 영어로 쓰기, 띄어쓰기 하지 않기.(인식을 다르게 함)
- 대신, 언더바 쓰기. 하이푼은 비추.

1. ls (list segments)\
    ls -a : 숨김파일까지 다 드러남.

2. cd (change directory)\
    디렉토리 (폴더랑 비슷한 개념)

    .  : 현재 디렉토리 \
    → cd . : 현재 디렉토리로 이동해라.

    ..  : 현재의 상위 디렉토리 \
    → cd .. : 현재의 상위 디렉토리로 이동해라.\
    → cd ../.. : 상위 x2

* 아래로 내려가고 싶으면?\
    → cd 폴더이름

    두번 내려가려면\
    → cd 폴더이름/폴더이름

* 옆폴더로 가기\
    → cd ../폴더이름

3. mkdir (make directory) : 폴더 만드는 거\
    ex) mkdir layer1

4. touch : 파일 만드는거\
    touch a.txt 라고 치니까 텍스트 파일 만들어짐

5. start : 파일을 엶\
    a.txt 는 메모장으로 열림

6. code :코딩 프로그램으로 엶.\
    a.txt 를 코딩 프로그램으로 열어줌

7. rm : 파일 제거\
    현재 디렉토리에 있는 파일 제거

8. -r : 디렉토리 제거\
    현재 디렉토리에서 하위에 있는 디렉토리 제거

### TIP : 현재 내 위치를 제대로 파악하는 것이 중요 ! 

## 절대경로 , 상대경로

### 절대 경로

root 디렉토리에서 목적지점까지 거치는 모든 경로 전부 작성.

\* pwd : 절대경로 불러옴.

### 상대경로

현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성.

### ex)

내가 SSAFY에 있을 때 Desktop 으로 가려고 함

절대경로 : cd c/Users/SSAFY/Desktop

상대경로 : cd SSAFY

### **TIP : 디렉토리 쓰다가 tab 누르면 자동완성됨. but 비슷한 것 있으면 겹치는 부분까지만 써줌.**

---
---
---

# <Git (리눅스 만든 사람이 만듦)>
## 특징
###  1. 분산 2. 버전 관리 시스템

#### *OS :  Operating System

전원이 꺼진 상태에서 켰을때 기계를 작동하게 하는 최저의 시스템\
ex) 윈도우, 맥, 리눅스~~

버전 관리 : 변화를 기록하고 추적하는 것\
→뭐가 바뀌었는지 다 알려준다. 

→원리 :  변경점을 기록하여 최종안에서 원하는 버전으로 되돌아 갈 수 있도록 만듦. (용량절감, 속도상승, 비용절감)

## 중앙 vs 분산

중앙 집중식 : 중앙서버에 버전 저장, 불러오기, 다시 업로드

분산식 : 여러개의 복제된 저장소에 저장, 관리

### 분산 장점

1. 중앙 의존 x 동시에 다양한 작업 : 개발자들 간의 충돌 x 생산성 향상

2. 서버 장애, 손실 대비 가능 백업 복구 좋음

3. 인터넷 연결 안돼도 작업 가능 → 중앙서버 동기화 필수

4. 변경이력 코드 로컬에 기록, 중앙에 동기화

*버전을 꼭 확인하면서 작업해야 문제가 발생하지 않음

## Git의 3가지 영역
### 1. working directoy(작업 디렉토리, 작업용 폴더)
    실제 작업 중인 영역
    
    
### 2. staging area
    1에서 변경된 파일 중 다음 버전에 포함시킬 파일들을 선택적으로 추가, 제외할 수 있는 중간 준비 영역

→why? 임시 공간으로서 중간에 조정이 가능.

### 3. repository(저장소)
    버전 이력, 파일들이 영구적으로 저장되는 영역, 모든 버전, 변경 이력 기록.

*commit = 버전을 찍는다. : 변경파일 저장하는 행위 (=snapshot)


## <명령어>


### 1. git init 로컬 저장소 설정(초기화)

    git 버전 관리를 시작할 디렉토리에서 진행
    이 때 파일 이름 옆에 U가 붙음(Untracked = 추적안함)

    * .git 폴더가 숨김폴더로 생김
    * 내가 관리하는 폴더는 (master) 라는 브랜치?로 표기됨
    * 추후 git branch 수업에서 계속.

(Untracked = 추적안함) : 매번 저장하지 않는다는 뜻인듯?

### 2. git add
    변경사항이 있는 파일을 staging area에 추가
    ex) git add a.txt 
        git add layer2-1
        git add a.txt, /layer2-1 (a 텍스트랑 layer2-1 동시에 올리기, 디렉토리는 /붙여야됨)
        git add *.txt( txt 확장자 전부 올리기)
        git add . (관리중인 모든 파일을 올리기)

    관리 폴더 안에서 파일 이름 옆에 A가 붙음. (Index Added = 인덱스 달고 추적 시작)

### 3. git rm —cached 파일이름
 add된 파일을 staging area에서 제거

### 4. git status

상태확인 시켜줌.

### 5. git commit

    staging area에 있는 파일을 저장소에 기록
    → 해당 시점의 버전을 생성, 변경 이력 남김.
    ex) git commit -m “메세지 내용”

## **commit 하기***
최초에. 등록을 하게되면, 내 정보를 몰라서 묻는 요청이 옴.
```
git commit -m 'first commit'
Author identity unknown

*** Please tell me who you are.

Run

git config --global user.email "[you@example.com](mailto:you@example.com)"
git config --global [user.name](http://user.name/) "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'SSAFY@DESKTOP-R2PNFNH.(none)')
```
요청에 맞게 답변 입력(개별적으로 git을 관리할 경우 global을 빼고 쓸 것)
```
git config --global user.email "[ungit003@gmail.com](mailto:ungit003@gmail.com)"
git config --global [user.name](http://user.name/) "ungit003"
```
이 후 commit -m "적고싶은 내용" 입력하면 정상작동 !
```
git commit -m 'first commit'
[master (root-commit) 843a816] first commit

1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 sample.txt
```
이까지 하면 sample.txt는 commit을 찍었고, working directory로 들어감. 
이후에는 파일 옆에 **알파벳 사라짐 !**

### 확인하고 싶다면. git status로 확인
```
git status
On branch master
Untracked files:
(use "git add <file>..." to include in what will be committed)
a.txt
sample2.txt
```
commit을 찍었기 때문에 staging area에 파일이 없음을 뜻함. 

### git에 등록된 정보를 알고싶으면. git log로 확인
```
git log
commit 843a81661a4d232f77fc4266d9dfe3cd0fce30c3 (HEAD -> master)
Author: ungit003 [ungit003@gmail.com](mailto:ungit003@gmail.com)
Date:   Thu Jul 11 14:22:34 2024 +0900
```
```
first commit

```
---
---
---
## sample.txt 에 내용을 변경해보기.
```
git status
On branch master
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   sample.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
a.txt
sample2.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
### 1. 만약에 바로 commit 한다면
```
$ git commit -m 'second commit'
On branch master
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git restore <file>..." to discard changes in working directory)
modified:   sample.txt

Untracked files:
(use "git add <file>..." to include in what will be committed)
a.txt
sample2.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
→ add 부터 하고 commit 할 것

### 2. commit 하기
```
$ git commit -m 'secont commit'
[master b0fcf41] secont commit
1 file changed, 1 insertion(+)
```
### → 확인해보기
```
$ git log
commit b0fcf41e0e049b32b6fa600e8f1cc91d407874c5 (HEAD -> master)
Author: ungit003 [ungit003@gmail.com](mailto:ungit003@gmail.com)
Date:   Thu Jul 11 14:32:59 2024 +0900


secont commit



commit 843a81661a4d232f77fc4266d9dfe3cd0fce30c3
Author: ungit003 [ungit003@gmail.com](mailto:ungit003@gmail.com)
Date:   Thu Jul 11 14:22:34 2024 +0900


first commit

```

### → 여기서.

commit 843a81661a4d232f77fc4266d9dfe3cd0fce30c3 : 커밋 해쉬(커밋 번호)

- 간단하게 요약해서 보는 방법
```
$ git log --oneline
b0fcf41 (HEAD -> master) secont commit
843a816 first commit
```
### HEAD -> master

헤드가 있는 것 = 깃발을 꽂는 것

제일 최근의 관심사? 정도로 이해하면 될 듯.

**\* git 은 로컬 저장소 내의 모든 파일의 변경을 감시한다( untracked 는 빼고)**


## 로컬.

git status

git log

git log --online

git config --global -l

### **** 절대로 git 로컬 저장소 안에 또다른 git 로컬 저장소를 만들지 말 것

상위 디렉토리에서 .git이 있고 하위 디렉토리에 또 .git이 생기면 commit이 수없이 꼬일 수 있음.

→하위의 .git 폴더를 지우면 됨

→rm -r .git 으로 해결 가능.

** 단 같은 레이어에서는 따로 만들어서 관리 가능.

## ?TIL 폴더?

(TODAY I LEARNED)

어떻게 만드는게 좋나? 구글링 해보고 참고.


## commit 수정하기

### git commit --amend

#### 1. commit 메세지 수정하기.
1. git commit -m “A 기능 구현 완료”
2. git log --oneline
3. git commit --amend
4. 편집모드(vm?뭐시기였던거 같은데) 진입
5. ‘ I ' 눌러서 (Insert) 편집 가능
6. 끝나면 ESC → shift + ; → wq 
#### 2. commit 전체 수정하기

1. git commit -m “A 기능 구현 완료”
2. git log --oneline
3. git commit --amend
4. 편집모드(vm?뭐시기였던거 같은데) 진입
5. ‘ I ' 눌러서 (Insert) 편집 가능
6. '기능 구현 완료 b-~~' 로 이름 변경
7. 끝나면 ESC → shift + ; → wq
8. git add로 빠진 파일 넣기

하면 들어가 있다! (?)