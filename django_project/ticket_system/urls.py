from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='tickets-home'),

    path('buy', views.arena_map, name='buy'),
    path('basket', views.basket, name='basket'),
    path('summary', views.summary, name='summary'),

    path('card', views.card, name='card'),
    path('fighters', views.fighters, name='fighters'),
    path('team', views.team, name='team'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
]
