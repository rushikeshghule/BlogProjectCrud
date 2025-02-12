from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm
from django.contrib import messages

def signup_view(request):
    """
    Handle user signup.

    If the request method is POST, validates the submitted form, creates a new user,
    logs them in automatically, and redirects to the login page with a success message.
    
    If the request method is GET, displays an empty signup form.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the signup page with the form.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User created successfully!")
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

def login_view(request):
    """
    Handle user login.

    If the request method is POST, validates the login credentials and logs in the user.
    On successful login, redirects to the home page.
    
    If the request method is GET, displays an empty login form.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Renders the login page with the form.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password. Please try again.")  # ✅ Error message
            request.session.pop('_messages', None)
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def logout_view(request):
    """
    Handle user logout.

    Logs out the current user, displays a success message using Django's messages framework,
    and redirects to the login page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponseRedirect: Redirects to the login page.
    """
    logout(request)
    messages.success(request, "User logged out successfully!")  # ✅ Triggers toast
    return redirect("login")
