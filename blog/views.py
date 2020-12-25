from django.shortcuts import render, get_object_or_404
from .models import Post
def blog(request):
    posts = Post.objects.all
    return render(request,'base.html',{'posts':posts})

def detail(request, post_id):
    detailpost = get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html', {'post':detailpost})