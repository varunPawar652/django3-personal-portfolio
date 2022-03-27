from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    Projects = Project.objects.all()
    return render(request,"home.html",{'projects':Projects})

