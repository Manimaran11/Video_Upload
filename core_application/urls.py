from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url  # For django versions before 2.0
from django.urls import include, path  # For django versions from 2.0 and up
from video_application.views import HomeView, NewVideo, CommentView, LoginView, RegisterView, VideoView, VideoFileView,LogoutView
 
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
     path('', include('video_application.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
 
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns