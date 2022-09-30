from django.shortcuts import render, redirect
from .models import Review
from multiprocessing import context

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def new(request):
    return render(request, 'movies/new.html')

def create(request):
    title = request.GET.get('title_')
    content = request.GET.get('content_')
    Review.objects.create(title=title, content=content)

    return redirect('movies:index')