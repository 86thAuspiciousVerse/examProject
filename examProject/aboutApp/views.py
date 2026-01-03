from django.shortcuts import render
from django.shortcuts import HttpResponse

def introduction(request):
    return render(request, 'about/introduction.html', {})

def help_center(request):
    return render(request, 'about/help.html', {})