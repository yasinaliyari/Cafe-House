from django.contrib import admin
from home.models import ContactUs, Slider, PopularItem, Special


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "is_read", "created_at"]
    list_filter = ["is_read", "created_at"]
    search_fields = ["name", "email", "subject", "message"]


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ["is_active", "created_at"]
    search_fields = ["title", "subtitle"]


@admin.register(PopularItem)
class PopularItemAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ["title", "description"]


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ["title", "description"]
