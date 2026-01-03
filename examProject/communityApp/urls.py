from django.urls import path
from . import views

app_name = 'communityApp'

urlpatterns = [
    path('comment/', views.comment, name='comment'),
    path('share/', views.share, name='share'),
]