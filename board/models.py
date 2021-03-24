from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.

# python manage.py migrate 명령어를 이용하여 SQLite에 데이터베이스 구성하고,
# 클래스 생성이후, python manage.py makemigrations 명령어를 이용하여 model 등록을 해주어야함.
# python manage.py migrate 명령어를 이용하여 데이터베이스에 추가한 model 업데이트

# 게시글
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 게시글 등록
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        # labels = {
        #     'title': '제목',
        #     'content': '내용',
        # }

# 댓글
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    create_date = models.DateTimeField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

