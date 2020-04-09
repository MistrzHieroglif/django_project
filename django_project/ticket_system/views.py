from django.shortcuts import render
from django.http import HttpResponse
from ticket_system.models import *
from ticket_system.serializers import *
from django.core import serializers


def home(request):
    return render(request, 'ticket_system/home.html')



def arena_map(request):
    return HttpResponse('arena')

def basket(request):
    return HttpResponse('basket')

def summary(request):
    return HttpResponse('summary')




def card(request):
    return HttpResponse('card')

def fighters(request):
    return HttpResponse('fighters')

def news(request):
    return HttpResponse('news')

def team(request):
    return HttpResponse('team')


def contact(request):
    return HttpResponse('contact')

def login(request):
    return HttpResponse('login')

def about1(request):
    return HttpResponse('about')


def about(request):
   return getPlacesList(request)


def makeReservation(request):
    pass


def getPlacesList(request):
    places = Place.objects.all()
    place_list = serializers.serialize('json', places)
    return GetAllPlacesJSON()

