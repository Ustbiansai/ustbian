from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Post

# Function based view
'''
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

'''

# Class based view
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post




def about(request):
    return render(request, 'blog/about.html')