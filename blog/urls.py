from django.urls import path
from .views import home_view, post_detail_view, post_create_view, post_update_view, post_delete_view

urlpatterns = [
    path("", home_view, name="home"),
    path("post/<int:pk>/", post_detail_view, name="post_detail"),
    path("post/new/", post_create_view, name="post_create"),
    path("post/<int:pk>/edit/", post_update_view, name="post_update"),
    path("post/<int:pk>/delete/", post_delete_view, name="post_delete"),
]
