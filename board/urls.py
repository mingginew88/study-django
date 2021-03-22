from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view()),  # Generic View 사용 예시
    path('<int:post_id>/', views.detail, name='detail'),
    path('post/create/<int:post_id>/', views.create_comment, name='create_comment'),
    path('create_post/', views.create_post, name='create_post'),
]