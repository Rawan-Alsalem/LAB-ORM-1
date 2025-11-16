from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("posts/", views.posts_view, name="posts_view"),
    path("post/<int:post_id>/", views.post_detail_view, name="post_detail_view"),
    path("post/<int:post_id>/edit/", views.post_edit_view, name="post_edit_view"),
    path("post/<int:post_id>/delete/", views.post_delete_view, name="post_delete_view"),
]
