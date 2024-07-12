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

112312