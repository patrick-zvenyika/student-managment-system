from .views import *
from django.urls import path

urlpatterns = [
    path('', LandingPage, name='landing-page'),
    path('registration', RegisterPage, name='register'),
    path('login', LoginPage, name='login')
]
