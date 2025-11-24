from django.shortcuts import render, redirect
from datetime import date

from .models import Review
from .forms import ReviewForm


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

def reviews_view(request):
    reviews = Review.objects.filter(checked=True).order_by('-created_at')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:reviews')
    else:
        form = ReviewForm()

    context = {
        'year': date.today().year,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'blog/reviews.html', context)
