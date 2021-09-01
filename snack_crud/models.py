from django.db import models

# Create your models here.
class Snack(models.Model):
    title= models.CharField(max_length=256)
    purchaser= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    description=models.TextField()