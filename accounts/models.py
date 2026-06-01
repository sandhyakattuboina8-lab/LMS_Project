from django.contrib.auth.models import AbstractUser
from django.db import models
#http://127.0.0.1:8000/api/auth/register/
#POST http://127.0.0.1:8000/api/auth/login/


class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('INSTRUCTOR', 'Instructor'),
        ('STUDENT', 'Student'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='STUDENT')
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # IMPORTANT FIX
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.username