from rest_framework.response import Response
from rest_framework import status, viewsets
from django.db import transaction
from .models import CompressedImage
from .serializers import CompressedImageSerializer
from .tasks import compress_image_task  # Import the Celery task

class CompressionViewSet(viewsets.ModelViewSet):
    queryset = CompressedImage.objects.all()
    serializer_class = CompressedImageSerializer

    def create(self, request, *args, **kwargs):
        image = request.FILES.get("image")
        if not image:
            return Response({"error": "No image uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                original = CompressedImage(original_image=image)
                original.save()

                task = compress_image_task.delay(original.id)

            return Response(
                {
                    "message": "Image uploaded successfully. Compression in progress.",
                    "image_id": original.id,
                    "task_id": task.id,
                },
                status=status.HTTP_202_ACCEPTED,
            )

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)