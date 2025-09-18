from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView
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


class PasswordRestRequestView(FormView):
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


class PasswordRestVerifyView(FormView):
    template_name = "account/password_reset_verify.html"
    form_class = PasswordResetCodeForm

    def form_valid(self, form):
        code = form.cleaned_data["code"]
        user_id = self.request.POST.get("user_id")
        user = get_object_or_404(User, id=user_id)
        try:
            reset_obj = PasswordResetCode.objects.filter(user=user, code=code).lastest(
                "created_at"
            )
            return redirect("password_reset_confirm_custom", user_id=user.id)
        except PasswordResetCode.DoesNotExist:
            messages.error(self.request, "Invalid code.")
            return redirect("password_reset_request")
