from rest_framework import serializers
from .models import Product
from skillhub.models import Artisan
from accounts.models import MyUser
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','username','password',)
        # make the password invisible to hackers
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        #create a user with the data sent
        def create(self, validated_data):
            user = MyUser.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user


class ProductSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    class Meta:
        model = Product
        fields = ('id','username','name','categories', 'contact_number', 'price', 'sold','date','image','image_two','image_three','descriptions')

    def get_username(self, Product):
        username = Product.user.username
        return username

class ArtisanSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    class Meta:
        model = Artisan
        fields = ('id','username','categories', 'contact_number','date','image','image_two','image_three','descriptions')

    def get_username(self, Artisan):
        username = Artisan.user.username
        return username