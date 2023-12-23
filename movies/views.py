from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from .models import Movie

# Create your views here.


class MoviesView(ListView):
    #Spisok filmov
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movies.html'

class MovieDetailView(View):#polnoe opisanie filma
    model = Movie
    slug_field = 'url'
