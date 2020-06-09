# Import Required Files Here

from django.contrib import admin
from django.urls import path, include
from basic_app import views

# These Are Just Like Path For Webpages.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('basic_app.urls')),
    path('draft',views.DraftListView.as_view(), name='draft'),
    path('logout', views.logout_request, name='logout'),
    path('', views.PostList.as_view(), name='home'),
    path("login", views.login_request, name="login"),
]
