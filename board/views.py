from django.shortcuts import render

# Create your views here.
# ---------------------------------- [수정] ---------------------------------- #
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello! 연습 게시판에 오신것을 환영합니다.")
# ---------------------------------------------------------------------------- #