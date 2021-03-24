from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.http import HttpResponse
from django.views import generic
from .models import Post, PostForm
from django.utils import timezone
from django.core.paginator import Paginator

def index(request):

    page = request.GET.get('page', '1')
    post_list = Post.objects.order_by('-create_date')

    paginator = Paginator(post_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj}

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
@login_required(login_url='common:login')
def create_comment(request, post_id):
    # post = Post.objects.get(id=post_id)
    # 404 에러페이지 처리
    post = get_object_or_404(Post, pk=post_id)
    post.comment_set.create(comment=request.POST.get('comment'), writer=request.user, create_date=timezone.now())

    return redirect('post:detail', post_id=post.id)


# 게시글 작성
@login_required(login_url='common:login')
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.create_date = timezone.now()
            post.save()
            return redirect('post:index')
    else:
        form = PostForm()

    context = {'form': form}
    return render(request, 'board/create_post.html', context)


