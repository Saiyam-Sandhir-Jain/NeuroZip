from rest_framework import serializers
from .models import CompressedImage

class CompressedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model= CompressedImage
        fields= '__all__'