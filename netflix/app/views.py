from django.shortcuts import render
from django.http import HttpResponse
#from .models import Genre, Video
from .models import Video

# Create your views here.

def index(request):
    #return HttpResponse('welcome to beta netflix')
    #genres =Genre.objects.all()
    video= Video.objects.first()

    return render(request,'index.html',{'video': video })
#return render(request,'index.html',{'video': video ; 'genres':genres })