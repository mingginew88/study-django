from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse
from django.views import generic
from .models import Post
from django.utils import timezone


def index(request):
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}

    return render(request, 'board/post_list.html', context)

'''
# Generic View 사용 예시
class IndexView(generic.ListView):
    def get_queryset(self):
        return Post.objects.order_by('-create_date')
'''

# 게시글 상세설명
def detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    # 404 에러페이지 처리
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}

    return render(request, 'board/post_detail.html', context)


# 댓글 작성
def create_comment(request, post_id):
    # post = Post.objects.get(id=post_id)
    # 404 에러페이지 처리
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(comment=request.POST.get('comment'), create_date=timezone.now())

    return redirect('post:detail', post_id=post.id)
