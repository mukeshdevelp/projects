from django.shortcuts import render
from .models import Posts
#3--creating views.index
# Create your views here.
def index(request):
  posts = Posts.objects.all()
  return render(request, 'index.html',{'posts' : posts})

def Post(request,pk):
  posts = Posts.objects.get(id=pk)
  return render(request, 'post.html', {'posts': posts})