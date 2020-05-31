from rest_framework import serializers
from backend.models.restaurant import Restaurant
from backend.serializers.user import UserSerializer
from backend.serializers.review import SmallReviewSerializer

class RestaurantSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    reviews = SmallReviewSerializer(source='review_set', many=True)
    class Meta:
        model = Restaurant
        depth = 1
        fields = ('pk', 'name', 'content', 'location', 'longitude', 'latitude', 'created_by', 'created_at', 'reviews')

class RestaurantCreateSerializer(RestaurantSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'content', 'location', 'longitude', 'latitude')

class RestaurantUpdateSerializer(RestaurantSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'content', 'location', 'longitude', 'latitude')
