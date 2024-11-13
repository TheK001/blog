from django.shortcuts import render
from blog_app.models import Blog

def index(request):
    blogs = Blog.objects.all()
    context = {
        "blogs" : blogs,
    }

    return render(request, 'index.html', context )
