from rest_framework import serializers
from backend.models.restaurant import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class RestaurantCreateSerializer(RestaurantSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'content', 'location')

class RestaurantUpdateSerializer(RestaurantSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'content', 'location')
