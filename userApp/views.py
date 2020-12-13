from django.shortcuts import render, redirect
from .forms import UserFrom

# Create your views here.


def home(response):
    if response.method == "POST":
        form = UserFrom(response.POST)
        if form.is_valid:
            form.save()
            form = UserFrom()
    else:
        form = UserFrom()
    return render(response,'userApp/home.html', {"form":form})
