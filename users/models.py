from django.db import models
from diango.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    
    user_in_mogrations = True
    
    def _create_user(self, email, passwor, **extra_fields):
        if not email:
            raise ValueError("email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email
        
        