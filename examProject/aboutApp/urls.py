from django.urls import path
from . import views

app_name = 'aboutApp'

urlpatterns = [
    path('introduction/', views.introduction, name='introduction'),
    path('help/', views.help_center, name='help'),
]