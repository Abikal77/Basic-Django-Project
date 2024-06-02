from django.shortcuts import render

from .models import Blog

def Home(request):
    blogs= Blog. objects
    return render(request,'blog/blogpost.html',{'blogs':blogs})