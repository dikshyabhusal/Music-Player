from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/images/')
    audio_file = models.FileField(upload_to='static/audio/')
    audio_link = models.URLField(max_length=200 ,blank=True,null=True)
    lyrics = models.TextField(blank=True,null=True)
    duration = models.CharField(max_length=20)
    paginate_by =2
    
    def __str__(self):
        return self.title

