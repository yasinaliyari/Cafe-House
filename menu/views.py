from django.views.generic import TemplateView
from menu.models import MenuItem


class MenuPageView(TemplateView):
    template_name = "menu/menu.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cold_drinks"] = MenuItem.objects.filter(
            category="cold_drink", is_active=True
        )
        context["hot_drinks"] = MenuItem.objects.filter(
            category="hot_drink", is_active=True
        )
        context["coffee_based"] = MenuItem.objects.filter(
            category="coffee_based", is_active=True
        )
        context["foods"] = MenuItem.objects.filter(category="food", is_active=True)

        return context
