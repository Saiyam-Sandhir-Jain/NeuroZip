from django.shortcuts import render

from django.core.files.base import ContentFile
from django.db import transaction
from PIL import Image
from io import BytesIO
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import CompressedImage
from .serializers import CompressedImageSerializer

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

                # Compress image
                img = Image.open(image)
                img = img.convert("RGB")
                buffer = BytesIO()
                img.save(buffer, format="JPEG", quality=50)
                compressed_image = ContentFile(buffer.getvalue(), name=f"compressed_{image.name}")

                original.compressed_image.save(compressed_image.name, compressed_image)
                original.save()
            
            return Response(CompressedImageSerializer(original).data, status=status.HTTP_201_CREATED)  
    
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)