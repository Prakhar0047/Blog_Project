from django.urls import path
from basic_app import views

# Define App Name For More Open URL Mapping and Generalization
app_name = 'blog'

urlpatterns = [
    path('about',views.About_us.as_view(),name='about_us'),
    path('<slug:slug>', views.PostDetail.as_view(),name='post_detail'),
    path('new/',views.CreatePostView.as_view(),name='new_post'),
]