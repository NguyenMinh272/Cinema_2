
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def HomeView(request):
    posts = MoviePost.objects.all().order_by("-id")
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def MovieList(request):
    posts = MoviePost.objects.all().order_by("-id")
    first_movie = MoviePost.objects.first()
    three_movie = MoviePost.objects.all()[1:3]
    two_categories = Category.objects.all()[0:3]
    context = {
        'posts': posts,
        'first_movie': first_movie,
        'three_movie': three_movie,
        'two_categories': two_categories

    }
    return render(request, 'movie_list.html', context)

def MovieDetail(request,id):
    movie_detail = MoviePost.objects.get(id=id)

    context = {
        'movie_detail': movie_detail,
    }

    return render(request, 'movie-detail.html', context)

def booksite(request):
    movies = Movie.objects.all()
    return render(request, 'booksite.html',{
        "movies":movies
    })








