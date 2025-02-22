from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
@login_required
def home_view(request):
    """
    Display a paginated list of all blog posts.

    Retrieves all blog posts, orders them by creation date (newest first),
    and paginates the results (4 posts per page).

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the home page with paginated blog posts.
    """
    posts_list = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 4)  # 4 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts})
@login_required
def post_detail_view(request, pk):
    """
    Display the details of a specific blog post.

    Fetches a blog post by primary key (`pk`) and renders the post detail page.
    If the post does not exist, returns a 404 error.

    Args:
        request (HttpRequest): The incoming HTTP request.
        pk (int): The primary key of the blog post.

    Returns:
        HttpResponse: Renders the post detail page.
    """
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

@login_required
def post_create_view(request):
    """
    Handle blog post creation.

    Displays a form to create a new blog post. If the request method is POST,
    validates and saves the form data, associates the post with the logged-in user,
    and redirects to the home page with a success message.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the post creation form or redirects to home after saving.
    """
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_at=datetime.now()
            post.save()
            messages.success(request, "Blog post saved successfully!")
            return redirect("home")
    else:
        form = BlogPostForm()
    return render(request, "blog/post_form.html", {"form": form})

@login_required
def post_update_view(request, pk):
    """
    Handle blog post updates.

    Allows the post's author to update their blog post. If the request method is POST,
    validates and saves the changes. If the user is not the author, redirects to home.

    Args:
        request (HttpRequest): The incoming HTTP request.
        pk (int): The primary key of the blog post to update.

    Returns:
        HttpResponse: Renders the post update form or redirects to home after saving.
    """
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user != post.author:
        return redirect("home")
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog post updated successfully!")
            return redirect("home")
    else:
        form = BlogPostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})

@login_required
def post_delete_view(request, pk):
    """
    Handle blog post deletion.

    Args:
        request (HttpRequest): The incoming HTTP request.
        pk (int): The primary key of the blog post to delete.

    Returns:
        HttpResponseRedirect: Redirects to home after deletion.
    """
    post = get_object_or_404(BlogPost, pk=pk)

    if request.method == "POST":
        if request.user == post.author:
            post.delete()
            messages.success(request, "Blog post deleted successfully!")
        return redirect("home")

    return render(request, "blog/post_delete.html", {"post": post})