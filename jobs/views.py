from django.shortcuts import render

from jobs.models import Jobs

def Home(request):
    jobs=Jobs.objects
    return render(request,'jobs/home.html',{'jobs':jobs})