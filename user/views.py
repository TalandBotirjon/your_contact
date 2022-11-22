from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def user_login(request):
    username = password = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"{user.username} siz saytga muvaffaqiyatli kirdingiz.")
            return redirect('/')
        else:
            messages.error(request, "Hatolik bor.")
    context = {'username': username, 'password': password}
    return render(request, 'user/login.html', context)


def signupview(request):
    if request.method == "POST":
        print(request.POST.get('username'))
        print(request.POST.get('email'))
        print(request.POST.get('password1'))
        print(request.POST.get('password2'))
    return render(request, 'user/signup.html')