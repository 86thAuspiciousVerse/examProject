from django.shortcuts import render
from django.shortcuts import HttpResponse
from examProject.models import Movie


def home(request):
    # 获取最新电影
    latest_movies = Movie.objects.order_by('-release_date')[:8]
    # 获取高评分电影
    top_rated = Movie.objects.order_by('-rating')[:8]
    
    context = {
        'latest_movies': latest_movies,
        'top_rated': top_rated,
    }
    return render(request, 'home/index.html', context)