from django.shortcuts import render
from django.http import HttpRequest

from .models import Comment, Post
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request: HttpRequest, pk):
    post = Post.objects.get(pk=pk)

    if request.POST:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)


def blog_tag(request, tag):
    posts = Post.objects.filter(
        tags__name=tag
    ).order_by('-created_on')

    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog_tag.html', context)
