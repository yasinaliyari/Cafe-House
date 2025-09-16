from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from home.forms import ContactUsForm
from home.models import Slider


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, "home/contact.html", {"form": form})

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("contact")
        return render(request, "home/contact.html", {"form": form})


class HomePageView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_active=True).order_by("-created_at")
        return render(request, "home/home.html", {"sliders": sliders})
