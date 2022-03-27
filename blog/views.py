from django.shortcuts import render
from .models import Blog
# Create your views here.

def all_blogs (request):
    all_blog = Blog.objects.order_by("-date")[:3]
    return render(request, "all_blog.html",{"Blogs":all_blog})