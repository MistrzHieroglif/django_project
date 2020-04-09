from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
from django.contrib.contenttypes.fields import GenericRelation

class FighterManager(models.Manager):
    pass

class Fighter(models.Model):
    MALE = 1
    FEMALE = 2
    SEX = (
        (MALE, 'Mężczyzna'),
        (FEMALE, 'Kobieta'),
    )

    name = models.CharField(max_length=20, verbose_name='Imie')
    surname = models.CharField(max_length=20, verbose_name='Nazwisko')


    birth = models.DateField(verbose_name='Data urodzenia')
    weight = models.FloatField(verbose_name='Waga')
    height = models.FloatField(default=0, verbose_name='Wzrost')
    category = models.CharField(max_length=10,verbose_name='Kategoria wagowa')
    description = models.TextField(verbose_name='Opis')
    has_belt = models.BooleanField(default=False, verbose_name='Czy posiada pas mistrzowski?')
    priority = models.IntegerField(default=0, verbose_name='Priorytet')

    wins = models.IntegerField(verbose_name='Wygrane')
    losts = models.IntegerField(verbose_name='Przegrane')
    draws = models.IntegerField(verbose_name='Zremisowane', null=True, blank=True)

    sex = models.PositiveSmallIntegerField(
        choices=SEX,
        default=1,
        verbose_name='Płeć',
    )

    image = models.FileField(upload_to="fighters_img", blank=True, verbose_name='Zdjęcie zawodnika')

    published = models.BooleanField(default=True,verbose_name='Czy opublikować na stronie?')

    def fullname(self):
        return self.name + ' ' + self.surname

    def record(self):
        if self.draws == 0 or self.draws == None:
            return str(self.wins) + '-' + str(self.losts)
        return str(self.wins) + '-' + str(self.losts) + '-' + str(self.draws)

    def img_url(self):
        if self.image:
            return self.image.url
        return "no_image"

    def __str__(self):
        return self.name + ' ' + self.surname

class FighterLink(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nazwa')
    url = models.CharField(max_length=200, verbose_name='Adres linku')
    fighter = models.ForeignKey(Fighter, related_name='links', on_delete=models.DO_NOTHING)


class TeamMember(models.Model):
    name = models.CharField(max_length=20, verbose_name='Imie')
    surname = models.CharField(max_length=20, verbose_name='Nazwisko')
    role = models.CharField(max_length=30, verbose_name='Rola w zespole')
    description = models.TextField(verbose_name='Opis')
    priority = models.IntegerField(default=0, verbose_name='Priorytet')
    image = models.FileField(upload_to="team_img", blank=True, verbose_name='Zdjęcie')
    published = models.BooleanField(default=True, verbose_name='Czy opublikować na stronie?')

    def fullname(self):
        return self.name + ' ' + self.surname

    def img_url(self):
        if self.image:
            return self.image.url
        return "no_image"

    def __str__(self):
        return self.name + ' ' + self.surname


class TeamMemberLink(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nazwa')
    url = models.CharField(max_length=200, verbose_name='Adres linku')
    member = models.ForeignKey(TeamMember, related_name='links', on_delete=models.DO_NOTHING)

class FightCards(models.Model):
    image = models.FileField(upload_to="fighters_img", blank=True, verbose_name='Zdjęcie promujące pojedynek')
    category = models.CharField(max_length=10, verbose_name='Kategoria wagowa')
    main_event = models.BooleanField(default=False, verbose_name='Czy posiada pas mistrzowski?')
    description = models.TextField(verbose_name='Opis')


    priority = models.IntegerField(default=0, verbose_name='Priorytet')
    set_hidden = models.BooleanField(default=True, verbose_name='Czy opublikować jako ukrytą?')
    published = models.BooleanField(default=True, verbose_name='Czy opublikować na stronie?')


    product_object_id = models.IntegerField()
    product_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING,
    )
    product = GenericForeignKey(
        'product_content_type',
        'product_object_id',
    )


    def img_url(self):
        if self.image:
            return self.image.url
        return "no_image"

