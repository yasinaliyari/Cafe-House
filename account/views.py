from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from account.forms import RegisterForm, PasswordResetRequestForm
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
