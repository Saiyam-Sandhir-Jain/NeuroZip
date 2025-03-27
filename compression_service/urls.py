from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompressionViewSet

router = DefaultRouter()
router.register(r'compress', CompressionViewSet, basename='compress')

urlpatterns = [
    path('', include(router.urls)),
]
