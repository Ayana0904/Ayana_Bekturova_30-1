from django.shortcuts import render, redirect

from posts.models import Post, Hashtag
from posts.forms import PostCreateForm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context_data = {
            'posts': posts
        }

        return render(request, 'posts/posts.html', context=context_data)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()
        context_data = {
            'hashtags': hashtags
        }
        return render(request, 'posts/hashtags/hashtags.html', context=context_data)


def post_detail_view(request, id):
    if request.method == 'GET':
        post = Post.objects.get(id=id)
        print(post)

        context_data = {
            'post': post
        }

        return render(request, 'posts/detail.html', context=context_data)


def post_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': PostCreateForm
        }

        return render(request, 'posts/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = PostCreateForm(data, files)

        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
            )
            return redirect('/posts/')

        return render(request, 'posts/create.html', context={
            'form': form
        })
