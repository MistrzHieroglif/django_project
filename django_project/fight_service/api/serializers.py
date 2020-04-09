from rest_framework import serializers
from fight_service.models import Fighter, FighterLink, TeamMember,TeamMemberLink
from ticket_system.models import Place
from ticket_system.models import Client, Cart

class FighterLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FighterLink
        fields = ['name', 'url']


class FighterSerializer(serializers.ModelSerializer):
    links = FighterLinkSerializer(many=True)
    class Meta:
        model = Fighter
        fields = ['fullname','weight','height', 'category','record','has_belt','description','img_url','priority','links']


class TeamMemberLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberLink
        fields = ['name', 'url']


class TeamMemberSerializer(serializers.ModelSerializer):
    links = TeamMemberLinkSerializer(many=True)
    class Meta:
        model = TeamMember
        fields = ['fullname','role','description','img_url','priority','links']




class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place_id','sector','row','number','status','price']



class PlaceReservation(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['place_id','']

class BasketAuthSerializer(serializers.ModelSerializer):
    places = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='place_id'
    )

    class Meta:
        model = Cart
        fields = ['exp_time','places']

class ClientAuthSerializer(serializers.ModelSerializer):
    basket = BasketAuthSerializer(required=True)
    class Meta:
        model = Client
        fields = ['last_result', 'buyer_id', 'key', 'name', 'surname', 'city', 'street','home_number','post_code','email','phone_number','basket']



class SmallFighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = ['fullname','weight','height', 'record','has_belt','img_url']


class FightsSerializer(serializers.ModelSerializer):
    fighter_left_name = serializers.SerializerMethodField(method_name='fighter_left')
    fighter_right_name = serializers.SerializerMethodField(method_name='fighter_right')
    class Meta:
        model = Fighter
        fields = ['fullname','weight','height', 'category','record','has_belt','description','img_url','priority','links']


    def fighter_left(self, instance):
        request = self.context.get('request')
        name = request.fullname
        print(name)
        return 'Hidden'

    def fighter_right(self, instance):
        request = self.context.get('request')
        name = request.fullname
        print(name)
        return 'Hidden'





