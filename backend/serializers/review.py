from rest_framework import serializers
from backend.models.review import Review
from backend.serializers.user import UserSerializer

class ReviewSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    class Meta:
        model = Review
        fields = '__all__'

class SmallReviewSerializer(serializers.ModelSerializer):
    writer = UserSerializer()
    class Meta:
        model = Review
        fields = ('content', 'star_rating', 'writer')

class ReviewCreateSerializer(ReviewSerializer):
    class Meta:
        model = Review
        fields = ('restaurant', 'content', 'star_rating')

class ReviewUpdateSerializer(ReviewSerializer):
    class Meta:
        model = Review
        fields = ('restaurant', 'content', 'star_rating')
