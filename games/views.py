from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.select_related('author')[:10]
    template = 'games/index.html'
    context = {
        'games': posts,
    }
    return render(request, template, context)


def group_list(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:10]
    template = 'games/group_list.html'
    context = {
        'text': slug,
        'group': group,
        'games': posts,
    }
    return render(request, template, context)
