from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from backend.models.review import Review
from backend.serializers.review import ReviewSerializer
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class ReviewViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = ((JSONWebTokenAuthentication,))  
    @action(detail=False, methods=['GET', 'POST'])
    def review(self, request):
        if request.method == 'GET':
            queryset = Review.objects.all()
            serializer = ReviewSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            pass
        