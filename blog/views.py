from django.shortcuts import render
from django.utils import timezone  # 쿼리셋 필터를 위한 import
from .models import Post  # 우리가 생성한 모델을 가져옴
from django.shortcuts import render, get_object_or_404


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')  # 쿼리셋
    # 매개변수 posts를 추가하여 보낸다.
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
