from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from home.forms import ContactUsForm
from home.models import Slider, PopularItem, Special
from menu.models import MenuItem


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
        popular_items = PopularItem.objects.filter(is_active=True)

        specials_left = Special.objects.filter(is_active=True, position="left")
        specials_right = Special.objects.filter(is_active=True, position="right")

        menu_items = MenuItem.objects.filter(is_active=True)

        return render(
            request,
            "home/home.html",
            {
                "sliders": sliders,
                "popular_items": popular_items,
                "specials_left": specials_left,
                "specials_right": specials_right,
                "menu_items": menu_items,
            },
        )
