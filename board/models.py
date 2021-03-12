from django.db import models

# Create your models here.

# python manage.py migrate 명령어를 이용하여 SQLite에 데이터베이스 구성하고,
# 클래스 생성이후, python manage.py makemigrations 명령어를 이용하여 model 등록을 해주어야함.
# python manage.py migrate 명령어를 이용하여 데이터베이스에 추가한 model 업데이트

# 게시글
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.title

# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField()



