from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='photography/photos')
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-likes',]