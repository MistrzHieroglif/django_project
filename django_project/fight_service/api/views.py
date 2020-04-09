from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import Http404

from fight_service.models import Fighter, TeamMember, FightCards
from fight_service.api.serializers import FighterSerializer, PlaceSerializer, TeamMemberSerializer, FightsSerializer
from ticket_system.models import Place, Client


# main class
class EstablishConnection(APIView):
    def post(self, request, format=None):
        again       = request.data['again']
        client_id   = request.data['client_id']
        token       = request.data['token']

        if again == False:
            new_client = Client.custom.create()
            new_client_id = new_client.auth.client_id
            new_client_token = new_client.auth.token

        queryset = Client.objects.filter(client_id = new_client_id)
        serializer = FighterSerializer(queryset, many=False)
        print(serializer.data)
        return Response(serializer.data)





class Login(APIView):
    def post(self, request, format=None):
        pass



class FighterCardList(APIView):
    def get(self, request, format=None):
        queryset = Fighter.objects.filter(published=True)
        serializer = FighterSerializer(queryset, many=True)
        return Response(serializer.data)

class TeamList(APIView):
    def get(self, request, format=None):
        queryset = TeamMember.objects.filter(published=True)
        serializer = TeamMemberSerializer(queryset, many=True)
        return Response(serializer.data)

class FightsList(APIView):
    def get(self, request, format=None):
        queryset = FightCards.objects.filter(published=True)
        serializer = FightsSerializer(queryset, many=True)
        return Response(serializer.data)


class AllPlacesList(APIView):
    def get(self, request, format=None):
        queryset = Place.objects.all()
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        place_id = request.data['place_id']
        user_id = request.data['user_id']

        place = Place.objects.get(place_id=place_id)

        result = Place.objects.make_reservation(place_id, user_id)

        return Response({"place_id": place_id, "success":result})


class SinglePlace(APIView):
    def get(self, request, id, format=None):
        try:
            queryset = Place.objects.get(place_id=id)
        except Place.DoesNotExist:
            raise Http404

        serializer = PlaceSerializer(queryset)
        return Response(serializer.data)







