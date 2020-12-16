from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Users



def create(response):
    if response.method == "POST":
        form = UserForm(response.POST)
        if form.is_valid:
            form.save() 
            form = UserForm()
            return redirect('/home')
    else:
        form = UserForm()
    return render(response,'userApp/index.html', {"form":form})

def update(response, pk):
    user = Users.objects.get(id=pk)
    form = UserForm(instance=user)
    if response.method == "POST":
        form = UserForm(response.POST, instance=user)
        if form.is_valid:
            form.save()
            form = UserForm()
            return redirect('/home')
    return render(response, 'userApp/update.html', {"form":form})

def delete(response, pk):
    user = Users.objects.get(id=pk)
    if response.method == 'POST':
        user.delete()
        return redirect('/home')
    return render(response, 'userApp/delete.html', {'user':user})


def showUser(response):
    all_users = Users.objects.all()
    return render(response, 'userApp/home.html', {"all_users": all_users})


