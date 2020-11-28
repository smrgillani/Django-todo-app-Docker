from django.db import models

# Create your models here.
class Tasks(models.Model):
    t_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200)
    cate_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    dueDate = models.CharField(max_length=200)
    priority = models.CharField(max_length=200)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)