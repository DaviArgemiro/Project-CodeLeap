from django.db import models
from datetime import date

# Create your models here.
    
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    create_datetime = models.DateField(default=date.today)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)