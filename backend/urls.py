from django.urls import path, include

from backend.views import router

urlpatterns = [
    path('api/', include(router.urls)),
]