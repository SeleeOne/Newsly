from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cookies', views.cookies, name='cookies'),
    path('privacypolicy', views.privacypolicy, name='privacy_policy'),
    path('register', views.registerPage, name='register'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutUser, name='logout')
]
