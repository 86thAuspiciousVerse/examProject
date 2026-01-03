from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from examProject.models import UserCollection

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def data(request):
    return render(request, 'user/data.html', {'user': request.user})

@login_required
def collect(request):
    collections = UserCollection.objects.filter(user=request.user)
    return render(request, 'user/collect.html', {'collections': collections})