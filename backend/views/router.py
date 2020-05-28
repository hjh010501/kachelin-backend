from rest_framework import routers
from . import api

router = routers.DefaultRouter()
router.register(r'restaurant', api.restaurant.RestaurantViewSet, basename='restaurant')