from django.urls import path, include
from . import views

urlpatterns = [

    #REST

    path('', views.home, name='tickets-home'),
    path('api/fighters/', include('fight_service.api.urls', 'fight_service_api')),
    path('api/fights/', include('fight_service.api.urls', 'fight_service_api')),
    path('api/team/', include('fight_service.api.urls', 'fight_service_api')),



    path('api/places/', include('fight_service.api.urls', 'fight_service_api')),

    path('api/auth/', include('fight_service.api.urls', 'fight_service_api')),
    path('api/auth/guest/', include('fight_service.api.urls', 'fight_service_api')),
    path('api/auth/register/', include('fight_service.api.urls', 'fight_service_api')),
    path('api/auth/logout/', include('fight_service.api.urls', 'fight_service_api')),

    path('api/auth/logout/', include('fight_service.api.urls', 'fight_service_api')),

]
