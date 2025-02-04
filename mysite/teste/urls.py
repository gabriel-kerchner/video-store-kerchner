"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name = 'teste'

from django.urls import path, include
from teste import views


urlpatterns = [
    path('', views.home, name='home'),
    path('filmes', views.get_movies, name="movies"),
    path('info/<int:movie_id>', views.get_info_movie, name="info"),
    path('search/', views.search_movie, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('favoritos/', views.get_favorite_movies, name='my-movies'),
    path('meus-filmes/delete/<int:movie_id>', views.remove_favorite_movie, name="delete"),
    path('filmes/adicionar/<int:movie_id>/', views.add_favorite_movie, name='adicionar'),
    path('sobre/', views.about, name='about')
]
