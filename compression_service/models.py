from django.db import models

class CompressedImage(models.Model):
    original_image= models.ImageField(upload_to='originals/')
    compressed_image=models.ImageField(upload_to='compressed/',null=True, blank=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)



