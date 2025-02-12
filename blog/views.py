from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
@login_required
def home_view(request):
    posts_list = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts_list, 4)  # 4 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts})

def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})

@login_required
def post_create_view(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Blog post saved successfully!")
            return redirect("home")
    else:
        form = BlogPostForm()
    return render(request, "blog/post_form.html", {"form": form})

@login_required
def post_update_view(request, pk):
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
    post = get_object_or_404(BlogPost, pk=pk)
    if request.user == post.author:
        post.delete()
        messages.success(request, "Blog post deleted successfully!")
    return redirect("home")
