from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import (LoginRequiredMixin,
 UserPassesTestMixin)
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView,
        CreateView, UpdateView, DeleteView)


# Entire functionality of the site is performed here


def home(request):
    # making dictionary of all the posts records from the database
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home.html', context)

class PostListView(ListView):
    # this class makes list view of all the posts and is present on template named home.html
    # ordering is inbuilt feature of listview which orders based on date_posted
    # paginate_by denotes no of posts present on single page
    model = Post
    template_name = 'home.html' # <model>_<viewtype>.html
    context_object_name = 'posts'  
    ordering = ['-date_posted']  
    paginate_by = 5


class UserPostListView(ListView):
    # this class makes list view which shows the posts of particular user 
    model = Post
    template_name = 'user_post.html' # <model>_<viewtype>.html
    context_object_name = 'posts'  
    paginate_by = 5

    # This function takes the clicket username and returns all the posts of that user 
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    # this class is used when we have to see single post at a time 
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # this class creates new form so that user can make post new posts 
    # LoginRequiredMixin helps that user must be login when he wants to add or post
    # fields are used which allocates respective components required to make new post 
    # title will give textfield to enter short title
    # content will give textarea to enter large content 
    model = Post
    fields = ['title', 'content']

    # this function takes form to make new post and validate the form 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # this class is used to update present posts 
    # This functionality also requires login 
    # UserPassesTestMixin uses below mentioned test_func which allows the user to update 
    # which has made that post other wise throw error
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return(self.request.user == post.author)
           

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # Similar to update class 
    model = Post
    success_url = '/'

    # whenever successfull execution of function success url will be directed
    def test_func(self):
        post = self.get_object()
        return(self.request.user == post.author)

def about(request):
    return render(request, 'about.html', {'title': 'About'})

