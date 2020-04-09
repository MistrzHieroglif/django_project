from django.core.serializers.json import DjangoJSONEncoder
from ticket_system.models import Place
from django.core import serializers
from django.http import HttpResponse



def SerializePlace(place):
    t_place_id = '\n\t"place_id":' + str(place.place_id) + ', '
    t_sector = '\n\t"sector":"'+ str(place.sector) + '", '
    t_row = '\n\t"row":' + str(place.row) + ','
    t_number = '\n\t"number":' + str(place.number) + ', '
    t_status = '\n\t"status":"' + str(place.status) + '", '
    t_price = '\n\t"price":"' + str(place.price) + '", '
    return "\n{" + t_place_id + t_sector + t_row + t_number + t_status + t_price + "\n}"



def GetAllPlacesJSON():
    places = Place.objects.all()
    JSON_response = "{ places_list:["
    for pl in places:
        JSON_response += SerializePlace(pl) + ","
    JSON_response += "] }"
    return HttpResponse(JSON_response, content_type='text/plain')



