from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
import random
from faker import Faker

def seed_data(request):

    users = []

    for _ in range(15):
        username = fake.user_name()

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=fake.email(),
                password="password123"
            )
            users.append(user)

    for _ in range(40):
        Post.objects.create(
            title=fake.sentence(nb_words=6),
            content="\n\n".join(fake.paragraphs(nb=6)),
            author=random.choice(users)
        )

    return HttpResponse("Fake users and posts created!")


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_app/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog_app/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
        

class UserPostListView(ListView):
    model = Post
    template_name = 'blog_app/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model= Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'



def about(request):
    return render(request, 'blog_app/about.html')

