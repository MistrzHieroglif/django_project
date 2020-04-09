from django.urls import path
from fight_service.api import views


app_name = 'fight_service'

urlpatterns = [
    path('fighters/', views.FighterCardList.as_view(), name='fighter-cards'),
    path('fights/', views.FightsList.as_view(), name='fights'),
    path('team/', views.TeamList.as_view(), name='members'),


    path('places/', views.AllPlacesList.as_view(), name='get-all-places'),
    path('places/<int:id>/', views.SinglePlace.as_view(), name='get-place'),

    path('auth/', views.EstablishConnection.as_view(), name='establish-connection')

]