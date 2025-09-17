from django.db import models


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
