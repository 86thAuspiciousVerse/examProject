from django.shortcuts import render
from django.shortcuts import HttpResponse
from examProject.models import Comment, Share

def comment(request):
    comments = Comment.objects.order_by('-created_at')[:20]
    return render(request, 'community/comment.html', {'comments': comments})

def share(request):
    shares = Share.objects.order_by('-created_at')[:20]
    return render(request, 'community/share.html', {'shares': shares})