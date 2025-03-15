from django.db import models

class Music(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='music_images/',null=True)  # Added upload_to for images
    artist = models.CharField(max_length=255)
    file = models.FileField(upload_to='music/')
    uploaded_date = models.DateTimeField(auto_now_add=True)  # Automatically sets the upload date

    def __str__(self):
        return self.title
