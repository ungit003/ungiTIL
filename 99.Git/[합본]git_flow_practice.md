# 최초 설정

## 1. 깃랩 생성

## 2. 멤버 초대

## 3. 깃 이그노어 생성

- .gitignore.io 에서 생성 후 복 붙

# 작업 과정 1. 팀장

## 4. 파이썬 가상환경 생성 후 장고 설치

```shell
$ python -m venv venv
$ source venv/Script/activate
$ pip intall django
```

## 5. requirements.txt 생성

## 6. 브랜치 생성, 생성한 브랜치로 변경

```shell
$ git branch dev
$ git switch dev
```

## 7. git add , git commit

커밋 멘트 맘대로.

## 8. django project, app 생성

```shell
$ django-admin startproject pjt .
$ py manage.py startapp articles
```

## 9. 프로잭트에 앱 등록

```py
# pjt/settings.py

INSTALLED_APPS = [
    'accounts',
    ...,
]
```

## 10. 모델 생성, 마이그레이션

```py
class Article(models.Model):
    title = models.TextField()
```

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

## 11. 더미데이터 생성

### 추가 pip 설치, 저장

```shell
$ pip install django_extensions ipython
$ pip freeze > requirements.txt
```

### 쉘 플러스 창 진입

```shell
$ python manage.py shell_plus

$ article = Aritcle()
$ article.title = 'test'
$ article.save()

$ exit()
```

### 덤프데이터

```shell
$ python manage.py dumpdata --indent=4 articles > articles.json
```

### fixtures 폴더 만들기, 옮기기

```shell
$ mkdir articles/fixtures

$ mv articles.json articles/fixtures/
```

## 12. git add , git commit, git push

커밋 멘트는 마음대로.

```shell
$ git push -u origin dev
```

### -u ?

--set.upstream ? 등의 요청이 뜨는데 origin dev 를 다음에도 뜨게 해주는거

## 13. 본인 레포지토리, merge request

### but 아직 merge 할 이유가 없다.

팀장 할 일 끝.

# 작업 시작 2. 팀원

1. 팀장이 만든 dev 브랜치는 팀원에게 없음
2. 따라서 로컬에 dev 브랜치 만들기
3. 로컬 dev에 원격 dev 받기

### branch

- !! 팀원도 가상환경 설정하고 작업해야 함 !!
- 현재 `git branch` 해도 아무것도 없음
- `git branch dev` 브랜치 생성
- `git switch dev`
- `git pull origin dev` dev 브랜치의 내용들을 내 로컬 dev branch로

### branch 이동

- 작업물 pull받은 상태에서 새 브랜치 만듦
- `git branch accounts`
- `git switch accounts` 새 브랜치로 옮겨옴
- 가상환경, pip install

### 앱 생성

- `python manage.py startapp accounts` 앱 만듦

```py
# pjt/settings.py

  INSTALLED_APPS = [
    'articles',
    'accounts',
    ...,
]

AUTH_USER_MODEL = 'accounts.User`  # 유저모델도 추가
```

### models.py 모델 생성

- `from django.contrib.auth.models import AbstractUser` 임포트

```py
class User(AbstractUser):
  pass
```

- 이후 만들어진 model 바탕으로 makemigrations와 migrate 진행

### 계정 생성

- `python manage.py createsuperuser`
- `python manage.py dumpdata --indent=4 accounts > users.json`
- `mkdir accounts/fixtures`
- `mv users.json accounts/fixtures`

### git에 push

- 완성한 작업을 바탕으로 Git에 업로드
- add, commmit, push 순서대로 감
- `$ git push origin accounts`

# 작업 시작 3. 팀장

### git에 감

- gitlab 상단의 new merge request가 생성되었으면 그대로 가거나, 혹은 왼쪽 카테고리에서 merge request를 찾음
- 만약 branch가 master로 되어있으면 dev로 바꿈

### 동시에 작업하며 push&pull

- 현재 내가 작업중인 브랜치는 settings, 그러나 `git pull origin dev` 통하여 팀원의 작업물을 받아올 때가 있음
- 작업하던 중 상대방의 브랜치로 pull을 받게 되었을 때, vi로 이상한 창 뜨면 `:wq` 침 자동으로 머지됨

# 파일 합치기

- 홈페이지에서 작업하던 저장소에서 dev로 merge request하면 원격 저장소의 branch는 자동으로 사라짐
- 따라서 dev 브랜치(개발중인 주요 브랜치)는 로컬저장소와 원격저장소로 나누어짐을 알 수 있음
  - 로컬 저장소의 branch와 일치하는 원격 저장소 branch에 있는 것을 pull받음
- 이제 작업할 articles새 브랜치 생성 및 switch
- articles의 models.py에 다음 문구를 적음

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = models.TextField()
```

## ~ default 에러 생김

- 위 model 작업 완성하고 migration 하면 이상한 오류가 생길 수도 있음
- 이미 user와 관련된 정보 팀원이 만들어놨으므로 그에 대하여 이 관계에 대한 값을 설정한 적이 없다고 뜸

- 그러면 DB 삭제하고 다시 migrate
- 그럼 다시 select an option 뜸. 1 입력하고 그다음 적절한 문구를 입력하여 해결

### 2번 게시글 만들기

- loaddata하기 -`$ python manage.py loaddata users.json`
  - user id의 값이 없는 등 무결성 오류가 난다면,
  - 여러개의 앱 파일에 있는 여러 개의 json 파일을 한번에 loaddata하면 됨
  - > 그럼 매번 신경써야되는가? 그냥 같이 올리면 해결됨
  - 그래도 오류난다면 shell_plus 만든 다음 데이터 하나 더 만들고, .json 파일 덮어씀

# Git conflict가 난다면

### 홈페이지에서 merge할 때

- 주의, vsCode에서 branch에 `pull origin {branch명}` 한 다음 gitlab 홈페이지에 가면 홈페이지 가장 상단에 Create merge request라는 버튼이 뜸
  - 이 아이콘을 클릭하여 merge를 진행한다면 **pull 요청한 원격 저장소의 브랜치가 master 브랜치로 병합되는 상황이 발생할 수 있음** (경험담)
  - 따라서 홈페이지의 왼쪽 *merge request*로 들어간 다음, *New merge request*를 클릭하여 _Source branch_ 란과 *Target branch*란을 잘 확인하여야 함
  - Source branch : 내가 작업한 브랜치
  - Target branch : 합쳐서 올릴

### 진짜 터졌을 때 (정보가 정확하지 않을 수 있음)

- 홈페이지 에러 _Merge blocked_ 붉은색 동그란 그림과 함께 나타났다면 두 개의 아이콘 *Resolve locally*와 _Resolve conflicts_ 중 *Resolve locally*를 선택할 것
  - Resolve locally : vsCode에서 해결 (권장)
  - Resolve conflicts : 홈페이지에서
- vsCode
  - pull로 넣고자 하는 대상 브랜치에서 역으로 먼저 pull 받아옴
  - `$ git pull {pull 하고싶은 대상 브랜치}`
  - 브랜치 이름 뒤에 `|MERGE` 뜬다면 충돌이 난 파일에서 직접 충돌 코드를 고칠 수 있음
  - `=====`나 `<<<<<` 같은 잡다한 코드들을 지우고 저장한 다음 다시 add-commit-push 진행
  - 그다음 gitlab 홈페이지에 가서 한번 더 merge 시도한다면 잘 합쳐질 것임
