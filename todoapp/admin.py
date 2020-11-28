from django.contrib import admin
from .Entities.Users import Users
from .Entities.Contacts import Contacts
from .Entities.Passwords import Passwords

# Register your models here.
admin.site.register(Users)
admin.site.register(Contacts)
admin.site.register(Passwords)