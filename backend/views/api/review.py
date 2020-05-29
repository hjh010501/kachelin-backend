from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from backend.models.review import Review
from backend.serializers.review import ReviewSerializer, ReviewCreateSerializer
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class ReviewViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = ((JSONWebTokenAuthentication,)) 
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewCreateSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)


    def update(self, request, pk):
        instance = self.get_object()
        if instance.user == request.user:
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        