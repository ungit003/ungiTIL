# 깃랩 생성

# 멤버 초대

# 깃 이그노어 생성

- .gitignore.io 에서 생성 후 복 붙

# 파이썬 가상환경 생성 후 장고 설치

```shell
$ python -m venv venv
$ source venv/Script/activate
$ pip intall django
```

# requirements.txt 생성

# 브랜치 생성, 생성한 브랜치로 변경

```shell
$ git branch dew
$ git switch dew
```

# git add , git commit

# django project, app 생성

```shell
$ django-admin startproject pjt.
$ py manage.py startapp articles
```

# 프로잭트에 앱 등록

# 모델 생성, 메이크마이그레이션즈, 마이그레이트

# 더미데이터 생성

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

# git add , git commit, git push

커밋 멘트는 마음대로.

```shell
$ git push -u origin dev
```

### -u ?

--set.upstream ? 등의 요청이 뜨는데 origin dev 를 다음에도 뜨게 해주는거

# 본인 레포지토리, merge request

### but 아직 merge 할 이유가 없다.

팀장 할 일 끝.

<hr>
<hr>

# 팀원 start

팀장이 만든 dev 브랜치는 나한테 없음.

### 로컬에 dev 브랜치 만들기

### 로컬 dev에 원격 dev 받기

```shell
$ git pull origin dev
```

# accounts 브랜치 만들고 옮겨가기

# 가상환경, pip install

# accounts 어플리캐이션 만들기

# setting.py에 등록

```py
# pjt/settings.py
...,
INSTALLED_APPS = [
    'articles',
    'accounts',
    ...,
]

...,
AUTH_USER_MODEL = 'accounts.User'
```

# 팀장

# settings branch, base temlplate 만들기

BASE_DIR / 'templates'

# add, commit 까지만.

# git pull origin dev

### 둘 다 수정했는데 왜 conflict 안나는가?

둘이 다른 줄을 수정해서 상관없음.

# git push origin settings

# merge, branch 지우기

git switch dev

# articles branch 만들고 이동

# N:1 관계 만들기, 모델 생성

```py
article/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODER, on_delete=models.CASCADE)
    title = models.TextField()
```

# 마이그레이션

```shell
$ python manage.py makemigrations
```

### ~ default 에러 생김

sol : db.sqlite3 삭제하고 다시 마이그레이션 ㄱㄱ

그럼 빈칸 생겼는데 어떡하실? 물어봄 > 1

빈칸 뭐로 채울래? > 1

# 마이그레이트

# 유저 관계 포함한 게시글 정보 필요

```shell
$ python manage.py loaddata users.json
```

- > user id가 없어서 무결성 에러 발생
- > 팀원이 만든 아티클스 제이슨 먼저 하면 됨
- > 그럼 매번 신경써야되는가? 그냥 같이 올리면 해결됨

```shell
$ manage.py loaddata users.json articles.json
```

# 쉘플러스

```shell
user = User.objects.get(pk=1)
article = Article()
article.user = user
article.title = 'test'
article.save()
exit()
```

# 새 아티클 제이슨 만들기

```shell
python manage.py dumpdata --indent=4 articles > articles.json
```

# 기존의 제이슨에 덮어씌우기

# add, commit, push -> articles

# dev에 merge

<hr>
<hr>
 
 # if  confilct ?
그냥 깃풀 받아서 보면
 뭐 어케 고치실? 뜨면 원하는대로 하면됨

# 팀원이 pull
