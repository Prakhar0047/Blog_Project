from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app.models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from basic_app.forms import PostForm
from django.urls import reverse

class About_us(TemplateView):
    template_name = "basic_app/about_us.html"


class PostList(ListView):
    queryset = Post.objects.all().filter(status=1).order_by('-created_on')
    template_name = "basic_app/post_list.html"


class PostDetail(DetailView):
    model = Post
    template_name = 'basic_app/post_detail.html'


class DraftListView(ListView):
    queryset = Post.objects.all().filter(status=0).order_by('-created_on')
    template_name = "basic_app/post_draft_list.html"


class CreatePostView(CreateView):
    form_class = PostForm
    model = Post


def logout_request(request):
    logout(request)
    return redirect("home")