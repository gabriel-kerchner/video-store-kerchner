from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import UserForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
import json

# Create your views here.

def home(request):
    return render(request,'teste/home.html')

def movies(request):
    list_movie = Movie.objects.order_by('titulo')
    context = {'movies': list_movie}
    return render(request,'teste/movies.html', context)

def infoMovie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'teste/info.html', context)

def searchMovie(request):
    if request.method == "GET":
        titulo = request.GET.get('titulo', None)
    else:
        titulo = ''
    movies = Movie.objects.filter(titulo__startswith=titulo)   
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
        else:
            print(user_form.errors)
    else:
       user_form = UserForm() 

    return render(request, 'teste/register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):

    if request.method == 'POST':
     
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
        
            if user.is_active:
    
                login(request,user)
               
                return HttpResponseRedirect(reverse('teste:home'))
            else:
    
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'teste/login.html', {})
