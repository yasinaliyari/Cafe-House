from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}: {self.subject}"

    class Meta:
        verbose_name = "Contact Us Form"
        verbose_name_plural = "Contact Us Forms"


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


class MenuItem(models.Model):
    CATEGORY_CHOICES = (
        ("cold_drink", "Cold Drink"),
        ("hot_drink", "Hot Drink"),
        ("coffee_based", "Coffee Based"),
        ("food", "Food"),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="coffee_based"
    )
    image = models.ImageField(upload_to="home/menu_item/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.get_category_display()} - {self.price}"

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"
        ordering = ("category", "title")
