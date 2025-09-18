from django.urls import path
from account.views import (
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
    PasswordResetRequestView,
    PasswordResetVerifyView,
    PasswordResetConfirmCustomView,
)

urlpatterns = [
    # Register / Login / Logout
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    # Password reset with 4-digit OTP
    path(
        "password_reset_request/",
        PasswordResetRequestView.as_view(),
        name="password_reset_request",
    ),
    path(
        "password_reset_verify/",
        PasswordResetVerifyView.as_view(),
        name="password_reset_verify",
    ),
    path(
        "password_reset_confirm/<int:user_id>/",
        PasswordResetConfirmCustomView.as_view(),
        name="password_reset_confirm_custom",
    ),
]
