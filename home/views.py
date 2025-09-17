from django.views.generic import TemplateView
from home.models import Slider, PopularItem, Special
from menu.models import MenuItem


class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sliders"] = Slider.objects.filter(is_active=True).order_by(
            "-created_at"
        )
        context["popular_items"] = PopularItem.objects.filter(is_active=True)

        context["specials_left"] = Special.objects.filter(
            is_active=True, position="left"
        )
        context["specials_right"] = Special.objects.filter(
            is_active=True, position="right"
        )

        context["menu_items"] = MenuItem.objects.filter(is_active=True)[:6]

        return context
