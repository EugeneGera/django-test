# blog/views.py

from django.shortcuts import render
from datetime import date

def index(request):
    context = {'year': date.today().year}
    return render(request, 'blog/index.html', context)


def about(request):
    context = {'year': date.today().year}
    return render(request, 'blog/about.html', context)


def post(request):
    context = {
        'year': date.today().year,
        'title': 'test post',
        'author': 'Eugene Gerasimov',
        'date': date(2025, 11, 22),
        'content': 'test content',
    }
    return render(request, 'blog/post.html', context)
