from django.urls import path
from . import views




urlpatterns=[
    

    path('', views.index, name='index'),  # Home page
    path('register.html/', views.register, name='register'),  # Register 
    path('login.html/', views.login, name='login'), #Login

    #path('posts.html/', views.posts, name='posts'),
    path('posts/<str:pk>/', views.dynamic_posts, name='posts'), # Dynamic post

    #path('post/', views.index),  # Redirect to index view

]
