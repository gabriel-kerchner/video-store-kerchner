from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Favorite
from .forms import UserForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.views import generic
import json
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'teste/home.html')

def get_movies(request):
    list_movie = Movie.objects.order_by('titulo')
    favorite_movies = Favorite.objects.filter(user=request.user)
    favorite_movies_ids = [favorite_movie.movie_id for favorite_movie in favorite_movies]
    
    context = {'movies': list_movie, 'favorite_movies_ids': favorite_movies_ids}
    return render(request,'teste/movies.html', context)

def get_info_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'teste/info.html', context)

def search_movie(request):
    if request.method == "GET":
        titulo = request.GET.get('titulo', None)
    else:
        titulo = ''
    movies = Movie.objects.filter(titulo__contains=titulo)   
    return render(request, 'teste/ajax-search.html', {'movies':movies})

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
            
            send_mail(
            'Cadastro realizado com sucesso!',
            'Obrigado por se cadastrar em nosso site!',
            'locadorakerchner@gmail.com',
            [user.email], fail_silently=False)
        else:
            print(user_form.errors)
    else:
       user_form = UserForm() 

    return render(request, 'teste/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
     
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
       

        if user:
        
            if user.is_active:
    
                login(request,user)
               
                return HttpResponseRedirect(reverse('teste:home'))
            else:
    
                return HttpResponse("Your account is not active.")
        else:
            print("Erro ao login.")
            print("Campos: username: {} e password: {}".format(username,password))
            return HttpResponse("Dados incorretos no login.")

    else:
        return render(request, 'teste/login.html', {})


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('teste:home'))

def get_favorite_movies(request):

    favorite_movies = Favorite.objects.filter(user=request.user)
    return render(request, 'teste/my-movies.html', {'favorite_movies': favorite_movies})

def remove_favorite_movie(request, movie_id):

    favorite = Favorite.objects.filter(user=request.user)
    movie = get_object_or_404(favorite, pk=movie_id)

    movie.delete()
    return HttpResponseRedirect(reverse('teste:my-movies'))

def add_favorite_movie(request, movie_id):

    favorite = Favorite(movie_id=movie_id, user_id=request.user.id)
    favorite.save()
    return HttpResponseRedirect(reverse('teste:movies'))


