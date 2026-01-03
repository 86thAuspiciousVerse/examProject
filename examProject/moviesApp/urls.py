from django.urls import path
from . import views

app_name = 'moviesApp'

urlpatterns = [
    path('', views.movie_home, name='movie_home'),
    path('category/', views.category, name='category'),
    path('search/', views.search, name='search'),
    path('details/<int:movie_id>/', views.details, name='details'),
]