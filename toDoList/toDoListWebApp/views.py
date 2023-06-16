from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from .forms import SignUpForm, TaskFrom
from .models import Tasks

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        form = TaskFrom(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                task = form.save(commit=False)
                task.userId = request.user
                task.save()
                return redirect("home")

        tasks = Tasks.objects.filter(userId=request.user).order_by("-created_at")
        return render(request, "toDoListWebApp/home.html", {"tasks": tasks, "form": form})
    else:
        return render(request, "toDoListWebApp/home.html")

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect("home")

    return render(request, "toDoListWebApp/register.html", {"form": form})


def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")

    return render(request, "toDoListWebApp/login.html", {})

def logout_user(request):
    logout(request)
    return redirect("home")

def delete_task(request, id):
    task = get_object_or_404(Tasks, pk=id)
    task.delete()
    return redirect("home")