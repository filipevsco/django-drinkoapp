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
        
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser needs to be True")
            

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email
        
        