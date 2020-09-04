from django.shortcuts import render
from django.utils import timezone

from .models import Post

def post_list(request):
    posts = Post.objects.filter(publiched_date__lte=timezone.now()).order_by('publiched_date')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

# Create your views here.
