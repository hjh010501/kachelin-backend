from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from backend.models.restaurant import Restaurant
from backend.serializers.restaurant import RestaurantSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class RestaurantViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = ((JSONWebTokenAuthentication,))
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer   

restaurant_list = RestaurantViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

restaurantt_detail = RestaurantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})