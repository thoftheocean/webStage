from django.db import models

# Create your models here.
class Poem(models.Model):
    author = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
