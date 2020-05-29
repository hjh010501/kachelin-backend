from rest_framework import serializers
from backend.models.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['restaurant', 'content', 'star_rating', 'user']