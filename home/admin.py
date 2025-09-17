from django.contrib import admin
from home.models import Slider, PopularItem, Special


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
