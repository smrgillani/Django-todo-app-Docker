from django.db import models

# Create your models here.
class SharedTasks(models.Model):
    st_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=200)
    task_id = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)