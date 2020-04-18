"""Users app views"""

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login(request):
    """Authenticates a user"""
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('todos:list')
        else:
            context['error'] = 'El usuario no pudo ser autenticado'

    return render(request, 'users/login.html', context)


def logout(request):
    """Logs out a user"""
    auth.logout(request)
    return redirect('index')
