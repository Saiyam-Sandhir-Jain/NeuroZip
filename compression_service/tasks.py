from celery import shared_task
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from .models import CompressedImage

@shared_task
def compress_image_task(image_path, original_id):
    try:
        original = CompressedImage.objects.get(id=original_id)
        img = Image.open(image_path)
        img = img.convert("RGB")

        buffer = BytesIO()
        img.save(buffer, format="JPEG", quality=50)
        compressed_image = ContentFile(buffer.getvalue(), name=f'compressed_{original.original_image.name}')

        original.compressed_image.save(compressed_image.name, compressed_image)
        original.save()
        return {"status": "completed", "compressed_image": original.compressed_image.url}

    except Exception as e:
        return {"status": "error", "message": str(e)}