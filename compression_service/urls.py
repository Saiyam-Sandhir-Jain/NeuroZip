from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompressionViewSet, check_task_status

router = DefaultRouter()
router.register(r'compress', CompressionViewSet, basename='compress')

urlpatterns = [
    path("", include(router.urls)),
    path("compress/status/<str:task_id>/", check_task_status, name="check_task_status"),
]
