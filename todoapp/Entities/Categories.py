from django.db import models

# Create your models here.
class Categories(models.Model):
    c_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)