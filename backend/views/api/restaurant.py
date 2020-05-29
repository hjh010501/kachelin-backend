from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from backend.models.restaurant import Restaurant
from backend.serializers.restaurant import RestaurantSerializer, RestaurantCreateSerializer
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class RestaurantViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = ((JSONWebTokenAuthentication,)) 
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    def get_serializer_class(self):
        if self.action == 'create':
            return RestaurantCreateSerializer
        return RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)