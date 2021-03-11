from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index),
    path('', views.IndexView.as_view()),  # Generic View 사용 예시
    path('<int:post_id>/', views.detail),
]