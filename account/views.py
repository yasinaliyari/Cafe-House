from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from account.forms import RegisterForm, PasswordResetRequestForm, PasswordResetCodeForm
from account.models import PasswordResetCode


class RegisterView(FormView):
    template_name = "account/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = "account/login.html"


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


class PasswordResetRequestView(FormView):
    template_name = "account/password_reset_request.html"
    form_class = PasswordResetRequestForm

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            reset_code = PasswordResetCode.objects.create(user=user)
            return render(
                self.request,
                "account/password_reset_show_code.html",
                {"code": reset_code.code, "user_id": user.id},
            )
        except User.DoesNotExist:
            messages.error(self.request, "No account found with this email.")
            return redirect("password_reset_request")


class PasswordResetVerifyView(FormView):
    template_name = "account/password_reset_verify.html"
    form_class = PasswordResetCodeForm

    def form_valid(self, form):
        code = form.cleaned_data["code"]
        user_id = self.request.POST.get("user_id")
        user = get_object_or_404(User, id=user_id)
        try:
            reset_obj = PasswordResetCode.objects.filter(user=user, code=code).latest(
                "created_at"
            )
            return redirect("password_reset_confirm_custom", user_id=user.id)
        except PasswordResetCode.DoesNotExist:
            messages.error(self.request, "Invalid code.")
            return redirect("password_reset_request")


class PasswordResetConfirmCustomView(View):
    template_name = "account/password_reset_confirm_custom.html"

    def get(self, request, user_id):
        return render(request, self.template_name, {"user_id": user_id})

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return render(request, self.template_name, {"user_id": user_id})

        user.set_password(password1)
        user.save()
        messages.success(
            request, "Your password has been reset successfully. You can now log in."
        )

        return redirect("password_reset_complete")
