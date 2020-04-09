from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from enum import Enum
from django.core.exceptions import ObjectDoesNotExist
import pytz


TOKEN_DURATION = 30         #in minutes
RESERVATION_TIME = 15       #in minutes
ALLOWED_ATTEMPS = 5         #allowed new token requests



class Status(Enum):
    TOKEN_EXPIRED = "TOKEN_EXPIRED"
    TOKEN_BURNED = "TOKEN_BURNED"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


# MANAGERS







class CartManager(models.Manager):
    def create_empty(self):
        cart            = self.create(expiration_time = 0, total=0)
        return cart

    def add(self, place_id, client_id):
        buyer = Client.objects.get(client_id=client_id)

        if buyer.authorized_action == True:
            cart = buyer.cart
            Place.objects.get(place_id=place_id)



    def RemoveFromBasket(self, place_id):
        place = self.objects.all().filter(place_id=place_id)
        place.in_basket = None
        place.save()

class PlaceManager(models.Manager):
    def CreatePlace(self, sector, row, number, price):
        place = self.create(place_id=Place.objects.all().count()+1, sector=sector, row=row,number=number, price=price, status='AV')
        place.save()

    def make_reservation(self, place_id, client_id):
        place = self.objects.get(place_id=place_id)
        buyer = Client.custom.get(client_id=client_id)
        basket = Cart.custom.get(buyer=buyer)

        if place.status == 'AV':
            place.status = 'RE'
            place.in_basket = basket
            place.save()
            return "SUCCESS"

        if place.status == 'RE' and place.in_basket == basket:
            pass



class Cart(models.Model):
    expiration_time = models.FloatField(default=0, verbose_name="Wygaśnięcie rezerwacji")
    total           = models.FloatField(default=0)
    object         = CartManager()


class Place(models.Model):
    AVAILABLE = 'AV'
    DISABLED = 'SL'
    SELECTED = 'SE'
    RESERVED = 'RE'

    STATUS = [
        (AVAILABLE, 'Available'),
        (DISABLED, 'Sold'),
        (SELECTED, 'Selected'),
        (RESERVED, 'Reserved'),
    ]

    place_id        = models.IntegerField(primary_key=True)
    sector          = models.CharField(max_length=2)
    row             = models.IntegerField(8)
    number          = models.IntegerField()
    price           = models.IntegerField()
    status          = models.CharField(
        max_length=2,
        choices=STATUS,
        default=AVAILABLE,
    )


    in_basket = models.ForeignKey(Cart, on_delete=models.DO_NOTHING, null=True, blank=True)
    objects = PlaceManager()

    def __str__(self):
        return str(self.place_id)



##MAIN CLIENT API

class AccessManager(models.Manager):
    def create_access(self):
        client_id           = abs(hash(str(datetime.now())))
        token               =  abs(hash(str(datetime.now()) + "token"))
        token_expires      = datetime.now() + timedelta(minutes=TOKEN_DURATION)

        auth    = Access.objects.create(client_id=client_id, token=token, token_expires=token_expires)
        auth.save()

        print("user/models.py: Pomyślnie utworzono AccessToken:")
        print("ID:", client_id)
        print("Token:", token)
        print("Wygasa:", token_expires)

        return auth

    def request_new_token(self, client_id, old_token):
        try:
            auth = Access.objects.get(client_id=client_id)
            print("user/models.py: Załadowano obiekt Access z ID:", client_id)
        except ObjectDoesNotExist:
            print("user/models.py: Nie znaleziono obiektu Access z ID:", client_id)
            return Status.FAILED

        if auth.invalid_attemps >= ALLOWED_ATTEMPS:
            print("Access dla ID:", client_id, "został zablokowany")
            auth.token_expires = 0
            return Status.TOKEN_BURNED
        print(auth.token)
        print(old_token)
        if str(auth.token) == str(old_token):

            auth.invalid_attemps    = 0
            auth.token = abs(hash(str(datetime.now()) + "token"))
            auth.token_expires = datetime.now() + timedelta(minutes=TOKEN_DURATION)

            print("Pomyślnie odświeżono token z ID", auth.client_id)
            print("Nowy token:", auth.token)
            print("Wygasa:", auth.token_expires)

            return Status.SUCCESS

        else:
            auth.invalid_attemps = auth.invalid_attemps + 1
            auth.save()
            print("Błędna autoryzacja ", auth.invalid_attemps, "/", ALLOWED_ATTEMPS, "tokenu z ID:", auth.client_id)
            return Status.FAILED

    def pass_token(self, client_id, token):
        try:
            auth = Access.objects.get(client_id=client_id)
            print("user/models.py: Załadowano obiekt Access z ID:", client_id)
        except ObjectDoesNotExist:
            print("user/models.py: Nie znaleziono obiektu Access z ID:", client_id)
            return Status.FAILED

        if auth.invalid_attemps >= ALLOWED_ATTEMPS:
            print("Access dla ID:", client_id, "został zablokowany")
            auth.token_expires = 0
            return Status.TOKEN_BURNED

        if str(auth.token) != str(token):
            auth.invalid_attemps = auth.invalid_attemps + 1
            print("Błędna autoryzacja ", auth.invalid_attemps, "/", ALLOWED_ATTEMPS, "tokenu z ID:", auth.client_id)
            return Status.FAILED

        utc = pytz.UTC
        if auth.token_expires < utc.localize(datetime.now()):
            print("Token:",auth.token,"uległ przedawnieniu.")
            return Status.TOKEN_EXPIRED

        if str(auth.token) == str(token):
            auth.client.authorized_action = True
            print("Token:",auth.token,"pomyślnie autoryzowany.")
            return Status.SUCCESS


class Access(models.Model):
    client_id        = models.CharField(max_length=100, default=0, null=True, verbose_name="ID kupującego")
    token           = models.CharField(max_length=32, default=0, null=True, verbose_name="Token autoryzujący")
    token_expires   = models.DateTimeField(default=datetime.now() + timedelta(minutes=TOKEN_DURATION), verbose_name="Czas wygaśnięcia tokenu")
    invalid_attemps = models.IntegerField(default=0, null=True, verbose_name="Błędne próby autoryzacji")

    objects         = models.Manager()
    custom          = AccessManager()

    def __str__(self):
        return self.client_id



class ShippingData(models.Model):
    city            = models.CharField(max_length=32, blank=True, verbose_name="Miasto")
    street          = models.CharField(max_length=32, blank=True, verbose_name="Ulica")
    house_number    = models.CharField(max_length=8, blank=True, verbose_name="Numer domu")
    flat_number     = models.CharField(max_length=8, blank=True, verbose_name="Numer mieszkania")
    post_code       = models.CharField(max_length=6, blank=True, verbose_name="Kod pocztowy")


class ClientData(models.Model):
    name            = models.CharField(max_length=32, default="", blank=True, verbose_name="Imie")
    surname         = models.CharField(max_length=32,default="", blank=True, verbose_name="Nazwisko")
    email           = models.EmailField(default="",blank=True, verbose_name="Adres email")
    phone_number    = models.CharField(default="",max_length=14, verbose_name="Numer telefonu")


class ClientManager(models.Manager):
    def create(self):
        auth            = Access.custom.create_access()
        buyer_data      = ClientData.objects.create()
        shipping_data   = ShippingData.objects.create()
        cart            = Cart.object.create_empty()
        print("NEW CLIENT CREATED")
        client = Client.objects.create(auth=auth, buyer_data=buyer_data, shipping_data=shipping_data, cart=cart)
        client.save()
        return client

class Client(models.Model):
    attached_to_user        = models.BooleanField(default=False, verbose_name="Podłączono do konta")
    authorized_action       = models.BooleanField(default=False, verbose_name="Autoryzowano dostęp")

    user                    = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    auth                    = models.OneToOneField(Access, on_delete=models.CASCADE, verbose_name="AccessToken")
    buyer_data              = models.OneToOneField(ClientData, on_delete=models.CASCADE, verbose_name="Dane personalne")
    shipping_data           = models.OneToOneField(ShippingData, on_delete=models.CASCADE, verbose_name="Dane adresowe")
    cart                    = models.OneToOneField(Cart, on_delete=models.CASCADE, verbose_name="Koszyk")

    objects                 = models.Manager()
    custom                 = ClientManager()
