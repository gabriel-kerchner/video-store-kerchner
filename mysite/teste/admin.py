from django.contrib import admin
from .models import Movie, UserProfile, Favorite

# Register your models here.
admin.site.register(Movie)
admin.site.register(Favorite)
