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
        extra_fields.setdefault("is_staff", True)
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser needs to be is_superuser=True")
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser needs to be staff=True")
        
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField("E-mail", unique=True)
    is_staff = models.BooleanField("Menbro da Equipe", default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
        
