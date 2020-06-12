from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def registerPage(request):
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, "Account was created for " + user)
        form = CreateUserForm()
    context = {'form' : form}
    return render(request,'auth/signUp.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged in as " + username)
            # redirect('')
        else:
            messages.info(request, 'Username OR Password is incorrect!')
    context = {}
    return render(request,'auth/login.html',context)