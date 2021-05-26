
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

    context = {
        'posts': posts,

    }
    return render(request, 'index.html', context)

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

@csrf_exempt
def occupiedSeats(request):
    data=json.loads(request.body)

    movie=Movie.objects.get(title=data["movie_title"])
    occupied=Movie.booked_seats.all()
    occupied_seat=list(map(lambda seat : seat.seat_no - 1,occupied))

    return JsonResponse({
        "occupied_seats":occupied_seat,
        "movie":str(movie)
    })






