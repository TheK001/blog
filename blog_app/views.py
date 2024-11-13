from django.shortcuts import render, redirect
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.all()
    context = {
        "blogs" : blogs
    }
    return render(request, "blogs.html", context)

def add_blogs(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        Blog.objects.create(title=title, description=description)
        return redirect('all_blogs')
    
    return render(request, "add_blog.html")

def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        "blog" : blog
    }

    if request.method =="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        blog.title = title
        blog.description = description
        blog.save()

    return render(request, "update_blog.html", context)

def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()

    return redirect('all_blogs')