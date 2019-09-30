

from django.urls import path
from . import views
app_name='video_application'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('login', views.LoginView.as_view(),name='login'),
    path('register', views.RegisterView.as_view(),name='register'),
    path('new_video', views.NewVideo.as_view(),name='newVideo'),
    path('video/<int:id>', views.VideoView.as_view(),name='Video'),
    path('comment',views.CommentView.as_view(),name='comment'),
    path('get_video/<file_name>', views.VideoFileView.as_view(),name='getVideo'),
    path('logout', views.LogoutView.as_view(),name='logout')
]