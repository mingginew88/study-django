# study-django 개요
Using Python Django Web Framework, Create Sample Board.

"''"

## 1. config 설정

### urls.py
 - view 경로 설정
 - include('board.urls') 메서드 사용하여 전체 url 중 패키지별 url 관리 
 
### settings.py
 - INSTALLED_APPS 설정 (앱등록)
 - DATABASES 체크 (sqlite3 사용) : 서비스내의 소규모 데이터베이스
 - LANGUAGE_CODE 설정 : 한국어 'ko-kr'로 변경
 - TIME_ZONE 설정 : 'Asia/Seoul'로 변경
 
## 2. board 패키지 설정
### urls.py
  - urlpatterns에서 index 페이지 설정
  
### views.py
  - index 페이지 설정
 
### SQLite 설치
  - https://sqlitebrowser.org/dl/
  
### models.py
 - python manage.py migrate 명령어를 이용하여 SQLite에 데이터베이스 구성하고,
 - 클래스 생성이후, python manage.py makemigrations 명령어를 이용하여 model 등록을 해주어야함.
 - python manage.py migrate 명령어를 이용하여 데이터베이스에 추가한 model 업데이트
 - migrations 패키지 내에 0001_initial.py 생성
 
### admin 계정 생성
 - python manage.py createsuperuser 명령어 이용하여 admin 계정 생성
 - 계정 확인을 위한 python manage.py runserver 명령어 사용후
 - http://127.0.0.1:8000/admin URL로 접속 후 계정 정보 입력

### admin.py
 - admin.site.register(Post) 입력