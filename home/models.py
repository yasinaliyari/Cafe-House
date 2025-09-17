from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="home/sliders/")
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slider Form"
        verbose_name_plural = "Slider Forms"


class PopularItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="home/popular_item/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Popular Item Form"
        verbose_name_plural = "Popular Item Forms"


class Special(models.Model):
    POSITION_CHOICES = (
        ("left", "Left"),
        ("right", "Right"),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="home/special/")
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, default="left")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Special Form"
        verbose_name_plural = "Special Forms"
