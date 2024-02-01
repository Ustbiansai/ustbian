from django.urls import path
from . import views
from . views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'), # if the records for id 1,2 are deleted then the pk will start from 3 for new entries
    path('post/new/', PostCreateView.as_view(), name='create'), 
    path('about/', views.about, name='about'),
]