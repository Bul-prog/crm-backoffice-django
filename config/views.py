from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout


@login_required
def home(request):
    return render(request, 'users/index.html')


def logout_get(request):
    logout(request)
    return redirect('/accounts/login/')
