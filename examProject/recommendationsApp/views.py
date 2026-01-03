from django.shortcuts import render
from django.shortcuts import HttpResponse
from examProject.models import Movie
from django.db.models import Avg

def score(request):
    # 基于评分推荐：评分前10的电影
    movies = Movie.objects.annotate(
        avg_rating=Avg('comment__rating')
    ).order_by('-avg_rating')[:10]
    return render(request, 'recommendations/score.html', {'movies': movies})

def type(request):
    # 基于类型偏好推荐
    # 这里简化实现：随机选择10部电影
    movies = Movie.objects.order_by('?')[:10]
    return render(request, 'recommendations/type.html', {'movies': movies})

