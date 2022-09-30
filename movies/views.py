from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    movies = Review.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def new(request):

    return render(request, 'movies/new.html')

def create(request):
    title = request.GET.get('title_')
    content = request.GET.get('content_')
    Review.objects.create(title=title, content=content)

    return redirect('movies:index')

def detail(request, pk):
    movie_click = Review.objects.get(id=pk)

    context = {
        'title': movie_click.title,
        'content': movie_click.content,
    }
    return render(request, 'movies/detail.html', context)