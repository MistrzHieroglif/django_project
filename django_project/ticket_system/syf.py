











class Arena(models.Model):
    places_counter = models.IntegerField(default=1)
    id = models.IntegerField(primary_key=True)




class ArenaManager(models.Manager):
    def check_arena(self):
        pass

    def GetNewPlaceID(self):
        arena = Arena.object.get(id=1).places_counter

    def CreatePlace(self, sector, row, number, price):
        place = Place(place_id = 1 )

    def GetAllPlacesList(self):
        pass

    def UpdatePlacesStatus(self):
        pass

    def ReservatePlace(self, id):
        pass




class User(models.Model):
    user_id = models.CharField(max_length=50)
    ticket_arena = models.ForeignKey(Arena, on_delete=models.DO_NOTHING)


    def SelectPlace(self, id):
        pass

    def UnselectPlace(self, id):
        pass


class Basket(models.Model):
    total_value = models.IntegerField()
    user = models.OneToOneField(User,
        primary_key=True,
        on_delete=models.DO_NOTHING
    )


class DeliveryData(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.CharField(max_length=50)
    flat_number = models.CharField(max_length=50)
    post_code = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

class Transaction():
    transaction_id = models.IntegerField()
    creation_time = models.DateTimeField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_ip = models.CharField(max_length=20) #do validacji
    is_paid = models.BooleanField(default=False)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=3) ##do poprawy
    sold_basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
    delivery_data = models.OneToOneField(DeliveryData, on_delete=models.DO_NOTHING)



