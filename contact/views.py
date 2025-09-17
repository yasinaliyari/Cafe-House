from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from contact.forms import ContactUsForm


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, "contact/contact.html", {"form": form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        return render(
            request,
            "contact/contact.html",
            {"form": form},
        )
