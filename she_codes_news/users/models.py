from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    about = models.TextField(blank=True)
    user_img = models.URLField(blank=True)

    def __str__(self):
        return self.username
