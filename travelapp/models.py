from django.db import models

# Create your models here.
class team(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
