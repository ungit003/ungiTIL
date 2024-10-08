## PREVIEW :

### PUSH, PULL

Remote Repository : PULL or CLONE

롤백 하는 법

~~

---

## 원격 저장소 = remote repository

코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

### ex) 구글 클라우드, 원 드라이브, …

### 우리가 사용할 것 :  깃랩(삼성은 이거) 깃허브 빗버켓

썰 : 마소가 깃허브 사서 유료 툴을 무료로 다 풀었음. 마소가 깃허브 코드를 다 긁어가고 있다?

---

## 로컬, 원격 저장소

**유의 : 깃허브 이메일, 아이디는 깃에 등록한 것과 같도록. (로컬에 등록한 것과 같도록) **

레퍼지토리 메인→마스터

지금은 로컬만 있고  리모트 레퍼지토리에는 아무것도 없다.

### **1. git remote add origin remote_repo_url**

지금은 로컬만 있고  리모트 레퍼지토리에는 아무것도 없다.

#### first-repo로 이름설정.

- 첫 깃허브 레퍼지토리를 만듦.

#### 깃허브에 원격 레포 링크가 나옴. 이걸 복사해서 가져옴.

- 깃허브 레퍼지토리랑 로컬이랑 연결하려면 이렇게 해라~ !

여기서는 connect 와 같은 의미로 add를 씀.

origin = 추가하는 원격 저장소 별칭(개발자는 관행처럼 씀)

remote_repo_url 사이트 만들고 받은거(옮길 때 복사만 해와서 오른쪽 마우스 버튼을 쓸 것. ctrl+v는 오류가 자주남)

```
git remote add origin 복사한 링크
```
- 이러면 연결 된 것 !
```
git remote -v
```
origin  https://github.com/ungit003/first-repo.git (fetch)\
origin  https://github.com/ungit003/first-repo.git (push)

 : 내가 여기 주소로 push 하겠다

### **2. git push origin master**

원격 저장소에 commit 목록을 업로드

*git아. push해줘 origin 이라는 이름의 원격 저장소에 master 라는 이름의 브랜치를.

- 최초에는 로그인 창 나옴
```
touch a.txt
git add a.txt
git commit -m 'save'
git push origin master
```
- 로컬에서 원격으로 등록하는 과정
```
git log --oneline
```
- 체크하고 싶을 때

8ea7833 (HEAD -> master, origin/master) commit1_ver2\
→ HEAD는 최신 파일(최근에 수정한 것)에 붙는데, ‘로컬, 원격 둘 다 최신 파일이다.’라는 뜻. 두 개는 분리 될 수 있음.

### 깃허브 사이트에서.
- 중간이 커밋 버튼인데,
- 커밋 이력을 확인 할 수 있다.

---

## PULL & CLONE

**TIP : 원격 레퍼지토리에도 .git 폴더가 있다.**

### 1. git clone remote_repo_url

원격 저장소 전체를 복제(다운로드) : .git폴더가 포함되어 있음.

***clone으로 받은 프로젝트는 이미 git init이 되어있음.**

→깃으로 관리되는 곳에 넣지 말 것.

***상황 : 뉴비가 3년차의 파일을 받는 상황을 연습.**

git clone을 이용해서 내려받고 이후 이력을 확인함.

### 2. git pull remote_repo_url

파일을 내려받음.

.git이 있고, 업데이트 된 파일만 받고싶을 때 이용할 것.

***얘는 간단해서 헷갈릴 일 없을 듯.**

***TIP : mv -f 원래이름 바꿀이름 하면 이름 바뀜**

---

### 11:25 ~ 12:45

***실습 2에서 확인 할 점**

origin 이 아닌 다른 이름으로 원격 저장소를 추가함.

- **git remote -v**

fetch, push를 다 확인할 수 있음.

2인 1개조로 업도르 다운로드 하기.

### 14:00 ~

## gitignore

### = git에서 특정 파일이나 디렉토리를 추적하지 않도록 설정하는 데 사용되는 파일

프로그램은 환경설정, 시스템구동을 위한 것으로 나뉨.

→환경설정을 위한 것은 올릴 필요가 없다.

→추적 할 필요가 없으니 무시해라.

1. .gitignore 파일 생성 (파일명 앞에 ‘.’ 입력, 확장자 없음)
2. a.txt , b.txt 파일 생성
3. gitignore에 a.txt 작성
4. git init
5. git status

**git init 전에 만들어야 추적을 하지 않는다.**

→git rm cached 에서 명령어로 설정해야함.

https://www.toptal.com/developers/gitignore/

여기서 시스템 운영파일을 모아서 .gitignore에 넣어서 설정할 수 있다.

## github 활용하기

---

TIL을 통해 내가 학습하는 것을 기록.

- 개인, 팀 프로젝트 코드를 공유
    - 개발 면접 지원 시 본인의 github 주소를 공유해 어떤 프로젝트들을 진행했고, 어떤 코드를 작성했는지 공유하고 평가 받기 위해 사용
    
- 오픈 소스 프로젝트에 기여.
    - ex) 한국어로 번역

## TIL

---

### Today I Learned

매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것

→단순히 기록이 아닌 매일 무얼 했는가 기록하는 것.

→문서화는 신입 개발자에게 요구되는 가장 중요한 덕목

→https://d2.naver.com/news/3435170 참고. 레벨 2 이상의 개발자가 될 수 있도록 할 것.

**옛날 블로그 찾지 말고 최신 것으로 볼 것.(옛날 것 = 레거시 코드)레거시 코드로 된 것을 배우게 됨.

[README.md](http://README.md) 파일이란?

프로젝트에 대한 설명, 사용 방법, 문서화된 정보 등을 포함하는 역할

markdown형식으로 씀

github 대문에 표시됨.
### 기타명령어

- git remote -v
    - 현재 로컬 저장소에 등록된 원격 저장소 목록 보기
- git remote rm 원격_저장소_이름
    - 현재 로컬 저장소에 등록된 원격 저장소 삭제

# *이하 기능들은 필요하면 ‘구글링 ‘해서 익힐 것*

---

---

## github profile 꾸미기

---

검색해보기

## git revert

---

### 작동원리.

- 재설정
- 단일 commit을 실행 취소하는 것
- 프로젝트에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가함
    - https://www.atlassian.com/git/tutorials/undoing-changes/git-revert 참고.

### git revert 정리

---

- 변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업
- 커밋 기록에서 커밋을 삭제하거나 분리하는 대신 지정된 병경 사항을 반전시키는 새 커밋 생성
- 깃에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성을 높임

### git revert 추가명령어

---

공백을 사용해 여러 커밋을 한꺼번에 실행취소 가능

“..”을 사용해 범위를 지엉하여 어러 커밋을 한꺼번에 실행 취소 가능

커밋 메세지 작성을 위한 편집기를 열지 않음

자동으로 커밋하지 않고 스테이징 에어리어만 올림. 이후 직접 커밋해야함

## git reset

---

git reset [옵션] 해쉬

### git reset 작동원리

- 되돌리기
- 시계를 마치 과거로 돌리는 듯한 행위
- 특정 커밋으로 되돌아 갔을 때 되돌아간 커밋 이후의 커밋은 모두 삭제

** 팀별 과제 할 때 큰 재앙이 될 수 있음

### git reset 3가지 옵션

- --soft
    - 삭제된 커밋의 기록을 스테이징 에어리어에 남김
- --mixed
    - 삭제된 커밋의 기록을 워킹 디렉토리에 남김 (기본 옵션값)
- --hard
    - 삭제된 커밋의 기록을 남기지 않음

## git reflog

---

- 리셋의 하드 옵션을 통해 지워진 커밋도 리플로그로 조회하여 복구가능
- 커밋의 헤드가 가리켰던 모든 커밋을 보여줌

## git restore

---

워킹 디렉토리에서 파일을 수정한 뒤 파일의 수정사항을 취소하고 원래의 모습대로 되돌리는 작업. 모디파이드 상태의 파일 되돌리기.

## git rm --cached / git restore --staged

---

스테이징 에어리어에서 언스테이지 할 때 쓰는 것. (커밋안함)