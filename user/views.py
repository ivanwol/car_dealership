from django.shortcuts import render


def user(request):
    return render(request, 'user_templates/user.html')


def login(request):
    return render(request, 'user_templates/login.html')


def logout(request):
    return render(request, 'user_templates/logout.html')


def registration(request):
    return render(request, 'user_templates/registration.html')