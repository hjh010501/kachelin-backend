from rest_framework import serializers
from backend.models.restaurant import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'content', 'positive_count', 'negative_count']