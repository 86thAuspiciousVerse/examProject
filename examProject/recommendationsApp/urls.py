from django.urls import path
from . import views

app_name = 'recommendationsApp'

urlpatterns = [
    path('score/', views.score, name='score'),
    path('type/', views.type, name='type'),
]