from django.db import models

# Create your models here.
class Passwords(models.Model):
	p_id = models.AutoField(primary_key=True)
	user_id = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	auth_token = models.CharField(max_length=200)
	token_expiry = models.CharField(max_length=200)
	isActive = models.CharField(max_length=200)
	updated_at = models.CharField(max_length=200)
	created_at = models.CharField(max_length=200)