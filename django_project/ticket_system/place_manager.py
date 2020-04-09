from django.core.serializers.json import DjangoJSONEncoder
from ticket_system.models import Place
from django.core import serializers
from django.http import HttpResponse




def createSector(name, rows):
    for r in range(len(rows)):
        for number in range(1,rows[r]+1):
            Place.objects.CreatePlace(name, r+1, number, 0)


