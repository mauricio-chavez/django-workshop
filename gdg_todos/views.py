"""GDG TODOs project views"""

from django.shortcuts import render


def index(request):
    """Shows main screen"""
    return render(request, 'index.html')
