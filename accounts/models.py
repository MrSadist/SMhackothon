from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.utils import timezone
import random
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('user', 'User'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    otp_code = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def generate_otp(self):
        code = f"{random.randint(100000, 999999)}"
        self.otp_code = code
        self.otp_created_at = timezone.now()
        self.save()
        return code
    
