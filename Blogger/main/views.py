from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from .models import Post

def index_view(request: HttpRequest):
    posts = Post.objects.filter(is_published=True).order_by("-published_at")
    return render(request, "main/index.html", {"posts": posts})


def posts_view(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        is_published = True if request.POST.get("is_published") == "on" else False
        image = request.FILES.get("image")

        Post.objects.create(
            title=title,
            content=content,
            is_published=is_published,
            image=image
        )

        return redirect("main:index_view")

    return render(request, "main/posts.html")


def post_detail_view(request: HttpRequest, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "main/post_detail.html", {"post": post})


def post_edit_view(request: HttpRequest, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.is_published = True if request.POST.get("is_published") == "on" else False

        if request.FILES.get("image"):  
            post.image = request.FILES.get("image")

        post.save()
        return redirect("main:post_detail_view", post_id=post.id)

    return render(request, "main/edit_post.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("main:index_view")
