from chats import views
from django.urls import path

urlpatterns = [
    path('',views.cover,name='cover'),
    path('home',views.home,name='home'),
    path('services',views.services,name='services'),
    path('about',views.about,name='about'),
    path('contact',views.contactview,name='contact'),
    path('chats',views.chatview,name='chats'),
    path('login',views.loginview,name='login'),
    path('register',views.registerview,name='register'),
    path('logout',views.logoutview,name='logout'),
    path('search',views.search,name='search'),
    path('lr',views.lr,name='lr')
]