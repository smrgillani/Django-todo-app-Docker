from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class CustomUserAuthentication(ModelBackend):
    # supports_object_permissions = True
    # supports_anonymous_user = False
    # supports_inactive_user = False


    def get_user(self, user_id):
      usermodel = get_user_model()
      try:
        return usermodel.objects.get(pk=user_id)
      except usermodel.DoesNotExist:
        return None

#this method will work if you have password field in your user table
    def authenticate(self, request, username, password):
        usermodel = get_user_model()
        try:
          user = usermodel.objects.get(Q(username=username) | Q(emailAddr=username))
        except usermodel.DoesNotExist:
          return None
        return user if user.check_password(password) else None

    def authenticate(self, request, username):
        usermodel = get_user_model()
        try:
          user = usermodel.objects.get(Q(username=username) | Q(emailAddr=username))
        except usermodel.DoesNotExist:
          return None
        #return user if user.check_password(password) else None
        return user if user is not None else None