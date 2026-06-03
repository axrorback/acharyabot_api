from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_CHOICES = (
        ("superadmin", "Super Admin"),
        ("admission", "Admission Manager"),
        ("callcenter", "Call Center"),
        ("operator", "Operator"),
    )
    role = models.CharField(max_length=50,choices=ROLE_CHOICES,default="operator")

    def __str__(self):
        return self.username