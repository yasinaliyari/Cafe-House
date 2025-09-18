from django.contrib import admin
from account.models import PasswordResetCode


@admin.register(PasswordResetCode)
class PasswordResetCodeAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "code")
