from rest_framework import routers
from . import api

router = routers.DefaultRouter()

router.register(prefix=r'restaurant', viewset=api.restaurant.RestaurantViewSet, basename='restaurant')

router.register(prefix=r'review', viewset=api.review.ReviewViewSet, basename='review')