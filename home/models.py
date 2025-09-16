from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}: {self.subject}"

    class Meta:
        verbose_name = "Contact Us Form"
        verbose_name_plural = "Contact Us Forms"
