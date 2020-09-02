from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('tag', include('tag.urls')),
    path('', include('patent.urls')),
    path('', include('user.urls')),
]
