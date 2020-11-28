from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .Passwords import Passwords
from ..DAL.ContactsDAL import ContactsDAL as c
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, emailAddr, password=None):
        if not emailAddr:
            raise ValueError('Email must be set!')
        user = self.model(emailAddr=emailAddr)
        user.set_unusable_password()
        #user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emailAddr):
        user = self.create_user(emailAddr)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, emailAddr):
        return self.get(emailAddr=emailAddr)

class Users(AbstractBaseUser):
    #pass_ = Passwords()
    u_id = models.AutoField(primary_key=True)
    unq_id = models.CharField(max_length=255)
    contact_id = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    emailAddr = models.CharField(max_length=200, unique=True)
    password = None
    #password = models.CharField(max_length=200)
    #password = models.ForeignKey(Passwords,on_delete=models.CASCADE)
    isActive = models.CharField(max_length=200)
    updated_at = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    last_login = models.CharField(max_length=200)

    objects = UserAccountManager()

    USERNAME_FIELD = 'emailAddr'
#    created_at = models.DateTimeField('date published')

    def get_emailAddr(self):
        return self.emailAddr

    def get_username(self):
        return self.username

    def get_userId(self):
        return self.u_id

    def get_userUnqId(self):
        return self.unq_id

    def get_userContact(self):
        return c.selectUserContact(self.contact_id)