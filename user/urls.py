from django.urls import path
from .views import LogIn

urlpatterns = [
    path('user/login', LogIn.as_view()),
]
