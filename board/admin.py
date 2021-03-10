from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post

# Post에서 검색 기능 추가
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']

# Post 등록
admin.site.register(Post, PostAdmin)


# 장고 내 기능[공식문서]
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/