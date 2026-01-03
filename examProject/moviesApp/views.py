from django.shortcuts import render
from django.shortcuts import HttpResponse
from examProject.models import Movie, Category
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

def movie_home(request):
    movies = Movie.objects.all()[:12]
    return render(request, 'movies/index.html', {'movies': movies})

def category(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category', None)
    
    if category_id:
        movies = Movie.objects.filter(category_id=category_id)
    else:
        movies = Movie.objects.all()
    
    context = {
        'categories': categories,
        'movies': movies,
        'selected_category': category_id
    }
    return render(request, 'movies/category.html', context)

def search(request):
    query = request.GET.get('q', '')
    if query:
        movies = Movie.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(director__icontains=query) |
            Q(actors__icontains=query)
        )
    else:
        movies = []
    
    return render(request, 'movies/search.html', {'movies': movies, 'query': query})

def details(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/details.html', {'movie': movie})