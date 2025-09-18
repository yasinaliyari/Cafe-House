import random
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = str(random.randint(1000, 9999))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.code}"
