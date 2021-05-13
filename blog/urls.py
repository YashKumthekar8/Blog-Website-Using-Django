from django.urls import path
from . import views
from .views import (PostDeleteView, PostListView,
        PostDetailView, PostCreateView, PostUpdateView, UserPostListView)


# when '' url comes PostListView from views.py invoked
# user/<str:username> denotes link like user/YashK where as <inside this denotes variable value>
# <int:pk> denotes integer value of pk where pk is primary key
# similarly create all the links required and name here denotes that whenever without
# link we have to call function using name can be called

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]



