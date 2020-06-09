from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app.models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from basic_app.forms import PostForm, NewUserForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

class About_us(TemplateView):
    template_name = "basic_app/about_us.html"


# Post List View (Home Page)

class PostList(ListView):
    queryset = Post.objects.all().filter(status=1).order_by('-created_on')
    template_name = "basic_app/post_list.html"


# Detailed Version Of Post

class PostDetail(DetailView):
    model = Post
    template_name = 'basic_app/post_detail.html'


# View For drafts

class DraftListView(ListView):
    queryset = Post.objects.all().filter(status=0).order_by('-created_on')
    template_name = "basic_app/post_draft_list.html"


# View For Creating Post
class CreatePostView(CreateView):
    form_class = PostForm
    model = Post


# Login View 
def login_request(request):
    if request.method == 'POST': # Means User Is Giving Some Input
        form = AuthenticationForm(request=request, data=request.POST) # Checks All Details
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "basic_app/login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    return redirect("home")